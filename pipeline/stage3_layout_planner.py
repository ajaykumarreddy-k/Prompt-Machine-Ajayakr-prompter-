"""stage3_layout_planner.py — Deterministically assigns layout primitives to the ontology components."""

# Allowed Layout Primitives - strictly semantic only, no wrappers
PRIMITIVES = {"Page", "Component"}

from pipeline.stage5_blueprint_validator import FORBIDDEN_PRIMITIVES

# Component Responsibility Mappings for LLM Guidance
COMPONENT_RESPONSIBILITIES = {
    "Navbar": ["Renders top navigation bar", "Handles mobile menu toggle", "Displays logo and links"],
    "Footer": ["Renders site footer", "Displays copyright and social links", "Groups legal and site-map links"],
    "Sidebar": ["Renders side navigation panel", "Handles collapsable state", "Displays user-specific shortcuts"],
    "Hero": ["Renders main headline and CTA", "Displays hero image or animation", "Sets the visual tone of the page"],
    "HeroSection": ["Renders full-width hero impact area", "Handles primary call to action", "Displays background media"],
    "FeatureGrid": ["Renders grid of feature cards", "Displays icons and descriptions", "Highlights key product selling points"],
    "FeaturesSection": ["Renders structured feature overview", "Groups multiple feature highlights", "Handles 'Learn More' routing"],
    "PricingTable": ["Renders tiered pricing options", "Displays feature comparisons", "Handles subscription tier selection"],
    "PricingSection": ["Renders pricing plans area", "Displays billing cycle toggles", "Showcases value propositions"],
    "TestimonialSlider": ["Renders rotating customer reviews", "Displays user avatars and names", "Handles manual/auto-sliding"],
    "TestimonialsSection": ["Renders social proof area", "Groups multiple user success stories", "Highlights key quotes"],
    "NewsletterSignup": ["Renders email subscription form", "Handles submission validation", "Displays success/error feedback"],
    "CTASection": ["Renders final conversion block", "Displays secondary call to action", "Provides urgency-driven copy"],
    "ProductShowcase": ["Renders detailed product screenshots", "Displays feature-specific callouts", "Handles interactive product demos"],
    "BenefitsSection": ["Renders value-driven outcome list", "Displays benefits vs features", "Highlights ROI for the user"],
    "StatCard": ["Renders key performance indicator", "Displays numerical data and labels", "Shows trend indicators"],
    "ChartWidget": ["Renders data visualization", "Displays line/bar/pie charts", "Handles time-range filtering"],
    "DataGrid": ["Renders sortable data table", "Handles pagination and search", "Displays rows of structured info"],
    "ActivityFeed": ["Renders chronological event list", "Displays user actions and timestamps", "Supports real-time updates"],
    "UserMenu": ["Renders user profile dropdown", "Handles logout and account links", "Displays user avatar and name"],
    "QuizList": ["Renders available quiz categories", "Displays quiz duration and difficulty", "Handles quiz selection"],
    "QuizCard": ["Renders single quiz preview", "Displays teaser image and title", "Links to the quiz player"],
    "QuizPlayer": ["Renders the main quiz interface", "Handles state management for questions", "Displays progress and current score"],
    "QuestionCard": ["Renders interactive question area", "Displays prompt and multi-choice options", "Handles answer selection state"],
    "OptionButton": ["Renders clickable answer choice", "Displays hover and selected states", "Provides visual feedback on click"],
    "Timer": ["Renders countdown for questions", "Displays remaining time visually", "Triggers timeout events"],
    "ProgressBar": ["Renders current quiz progress", "Displays percentage/step completion", "Animates on step transition"],
    "FlashcardComponent": ["Renders flippable study card", "Handles front/back state toggle", "Displays term and definition"],
    "ResultsSummary": ["Renders final score overview", "Displays correct/incorrect breakdown", "Provides personalized performance tips"],
    "ScoreSummary": ["Renders live score during session", "Displays current points or streak", "Provides immediate feedback"],
    "ProductGrid": ["Renders e-commerce product list", "Handles filtering and sorting", "Displays price and availability"],
    "ProductCard": ["Renders product preview", "Displays price, rating, and image", "Handles 'Add to Cart' action"],
    "ShoppingCart": ["Renders current items summary", "Handles quantity updates", "Calculates totals and taxes"],
    "CheckoutForm": ["Renders multi-step payment form", "Handles shipping and billing info", "Processes data for payment gateway"],
    "CategoryFilter": ["Renders sidebar/top filters", "Handles attribute selection", "Triggers product list updates"],
    "PromoBanner": ["Renders time-sensitive offer", "Displays discount codes", "Handles urgency countdown"],
    "Contact": ["Renders contact message form", "Displays map/office location", "Handles support ticket submission"],
    "Projects": ["Renders portfolio gallery", "Displays project tech stack", "Links to live demos or case studies"],
    "Skills": ["Renders competency grid", "Displays skill levels/badges", "Groups skills by category"],
    "Experience": ["Renders career timeline", "Displays job roles and achievements", "Highlights key career growth"],
    "About": ["Renders mission and vision info", "Displays team member profiles", "Tells the company story"]
}

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

MARKETING_SEQUENCE = [
    "HeroSection",
    "AboutSection",
    "SkillsSection",
    "ExperienceSection",
    "ProjectsSection",
    "FeaturesSection",
    "BenefitsSection",
    "ProductShowcase",
    "TestimonialsSection",
    "PricingSection",
    "NewsletterSignup",
    "CTASection",
    "ContactSection",
    "Footer"
]

def generate_page_layout(domain: str, page_name: str, available_components: list, discarded_reasons: dict) -> dict:
    """Builds a flat semantic AST for a single page. Max depth 2 (Page -> Components)."""

    stack_children = []

    # helper
    def add_if_available(comp_name):
        nonlocal stack_children
        # Allow mapped names (e.g. Hero -> HeroSection)
        mapping = {
            "Hero":               "HeroSection",
            "About":              "AboutSection",
            "Skills":             "SkillsSection",
            "Experience":         "ExperienceSection",
            "Projects":           "ProjectsSection",
            "Contact":            "ContactSection",
            "Features":           "FeaturesSection",
            "FeatureGrid":        "FeaturesSection",
            "Benefits":           "BenefitsSection",
            "Testimonials":       "TestimonialsSection",
            "TestimonialSlider":  "TestimonialsSection",
            "Pricing":            "PricingSection",
            "PricingTable":       "PricingSection",
            "CTA":                "CTASection",
            "Newsletter":         "NewsletterSignup",
            "NewsletterSignup":   "NewsletterSignup",
        }
        target = mapping.get(comp_name, comp_name)

        # FIX (correct order):
        if any(c["type"] == target for c in stack_children):
            if comp_name != target:
                discarded_reasons[comp_name] = f"mapped to {target} (already placed)"
            return True

        if target in available_components or comp_name in available_components:
            responsibilities = COMPONENT_RESPONSIBILITIES.get(target, 
                               COMPONENT_RESPONSIBILITIES.get(comp_name, 
                               ["Renders UI component"]))
            
            stack_children.append({
                "type": target, 
                "original_name": comp_name,
                "responsibilities": responsibilities
            })
            if comp_name != target:
                discarded_reasons[comp_name] = f"mapped to {target}"
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

    # REPLACE the final discarded_components block with this:
    all_placed = set()
    all_mapped_originals = set()

    for page in ast:
        for comp in page["layout"]["children"]:
            all_placed.add(comp["type"])
            if comp.get("original_name"):
                all_placed.add(comp["original_name"])
                all_mapped_originals.add(comp["original_name"])

    # Also collect from discarded_reasons (aliases that hit the duplicate guard)
    for original, reason in discarded_reasons.items():
        all_mapped_originals.add(original)

    discarded_components = []
    for comp in components:
        if comp not in all_placed:
            if comp in all_mapped_originals or comp in discarded_reasons:
                reason = discarded_reasons.get(comp, "mapped to layout equivalent")
            else:
                reason = "Not placed in any page layout"
            discarded_components.append({"component": comp, "discard_reason": reason})

    return {"pages": ast, "discarded_components": discarded_components}
