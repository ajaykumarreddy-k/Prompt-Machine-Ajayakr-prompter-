"""stage3_layout_planner.py — Deterministically assigns layout primitives to the ontology components."""
# Allowed Layout Primitives - strictly semantic only, no wrappers
PRIMITIVES = {"Page", "Component"}

from pipeline.stage5_blueprint_validator import FORBIDDEN_PRIMITIVES

# Deterministic Page Rules per Domain
PAGE_RULES = {
    "quiz": [
        {"name": "Home", "route": "/"},
        {"name": "QuizSelection", "route": "/quiz-selection"},
        {"name": "QuizPlayer", "route": "/quiz-player"},
        {"name": "Results", "route": "/results"},
        {"name": "FlashcardStudy", "route": "/flashcards"}
    ],
    "dashboard": [
        {"name": "Overview", "route": "/"},
        {"name": "Analytics", "route": "/analytics"},
        {"name": "Settings", "route": "/settings"}
    ],
    "ecommerce": [
        {"name": "Storefront", "route": "/"},
        {"name": "ProductDisplay", "route": "/product"},
        {"name": "Cart", "route": "/cart"},
        {"name": "Checkout", "route": "/checkout"}
    ],
    "marketing": [
        {"name": "Landing", "route": "/"},
        {"name": "Pricing", "route": "/pricing"},
        {"name": "About", "route": "/about"}
    ]
}

# Mandatory sequence for Marketing SaaS landing pages
MARKETING_SEQUENCE = [
    "HeroSection", "FeaturesSection", "ProductShowcase",
    "BenefitsSection", "TestimonialsSection", "PricingSection",
    "CTASection", "Footer"
]

def generate_page_layout(domain: str, page_name: str, available_components: list, discarded_reasons: dict) -> dict:
    """Builds a flat semantic AST for a single page. Max depth 2 (Page -> Components)."""

    stack_children = []

    # helper
    def add_if_available(comp_name):
        nonlocal stack_children
        # Allow mapped names (e.g. Hero -> HeroSection)
        mapping = {
            "Hero": "HeroSection",
            "Features": "FeaturesSection",
            "Benefits": "BenefitsSection",
            "Testimonials": "TestimonialsSection",
            "Pricing": "PricingSection",
            "CTA": "CTASection",
            "FeatureGrid": "FeaturesSection",
            "TestimonialSlider": "TestimonialsSection",
            "PricingTable": "PricingSection"
        }
        target = mapping.get(comp_name, comp_name)

        # Prevent self-duplicates (target type already in stack)
        if any(c["type"] == target for c in stack_children):
            if comp_name != target:
                discarded_reasons[comp_name] = f"replaced by {target}"
            return True # Target exists, but we return True to show it's "handled"

        if target in available_components or comp_name in available_components:
            stack_children.append({"type": target, "original_name": comp_name})
            if comp_name != target:
                discarded_reasons[comp_name] = f"replaced by {target}"
            return True
        return False

    # Always include Navbar if available
    add_if_available("Navbar")

    if domain == "marketing" and page_name == "Landing":
        # Rule 9: Strict sequence for Landing
        for comp in MARKETING_SEQUENCE:
            add_if_available(comp)
    elif domain == "quiz":
        if page_name == "Home":
            add_if_available("QuizList")
        elif page_name == "QuizPlayer":
            add_if_available("ProgressBar")
            add_if_available("Timer")
            add_if_available("QuestionCard")
            add_if_available("OptionButton")
        elif page_name == "Results":
            add_if_available("ScoreSummary")
            add_if_available("ResultsSummary")
    elif domain == "dashboard":
        if page_name == "Overview":
            add_if_available("StatCard")
            add_if_available("ActivityFeed")
        elif page_name == "Analytics":
            add_if_available("ChartWidget")
            add_if_available("DataGrid")
    else:
        # Fallback for other pages/domains
        for comp in available_components:
            if comp not in ["Navbar", "Footer"] and "Section" in comp:
                add_if_available(comp)

    # Rule 8: Ensure Ontology -> Layout Consistency (Greedy placement on Home/Landing)
    if page_name in ["Home", "Landing", "Overview"]:
        placed_types = {c["type"] for c in stack_children}
        for comp in available_components:
            if comp not in placed_types and comp not in ["Navbar", "Footer", "Sidebar"] and comp not in FORBIDDEN_PRIMITIVES:
                # Try to map and add
                add_if_available(comp)

    # Always include Footer if available and not already added
    if "Footer" not in [c["type"] for c in stack_children]:
        add_if_available("Footer")

    # Assemble AST
    return {
        "type": "PageLayout",
        "children": stack_children
    }

def plan_layout(intent: dict, ontology: dict) -> dict:
    """Deterministically structures the frontend page layouts as an AST."""
    print("\n\033[36mLayout Planner Stage\033[0m")

    domain = ontology.get("domain", "marketing")
    components = ontology.get("required_components", [])

    print(f"\033[90m  Domain detected -> {domain}\033[0m")

    pages = PAGE_RULES.get(domain, PAGE_RULES["marketing"])
    page_names = [p["name"] for p in pages]

    print(f"\033[90m  Generating pages -> {', '.join(page_names)}\033[0m")
    print(f"\033[90m  Applying layout rules\033[0m")

    ast = []
    discarded_reasons = {}
    for page in pages:
        layout_tree = generate_page_layout(domain, page["name"], components, discarded_reasons)
        ast.append({
            "name": page["name"],
            "route": page["route"],
            "layout": layout_tree
        })

    print(f"\033[90m  Layout AST generated\033[0m")

    # Calculate discarded components
    used_components = set()
    for page in ast:
        for comp in page["layout"]["children"]:
            used_components.add(comp["type"])
            if comp.get("original_name"):
                used_components.add(comp["original_name"])

    discarded_components = []
    for comp in components:
        if comp not in used_components:
            reason = discarded_reasons.get(comp, "Not used in layout")
            discarded_components.append({"component": comp, "discard_reason": reason})

    return {"pages": ast, "discarded_components": discarded_components}
