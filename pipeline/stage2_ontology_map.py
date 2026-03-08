"""stage2_ontology_map.py — Maps PRD intent to exact domain components via a 3-layer strategy."""

from vector_kb import get_model
import numpy as np
import re

from pipeline.stage5_blueprint_validator import FORBIDDEN_PRIMITIVES

# ── 4. COMPONENT ONTOLOGY OUTPUT ──────────────────────────────────────────────
# Core component mappings per domain. These lists strictly forbid incorrect injections.
DOMAIN_MAPS = {
    "quiz": [
        "Navbar", "QuizList", "QuizCard", "QuizPlayer", "QuestionCard", 
        "OptionButton", "Timer", "ProgressBar", "FlashcardComponent", 
        "ResultsSummary", "ScoreSummary", "Footer"
    ],
    "ecommerce": [
        "Navbar", "ProductGrid", "ProductCard", "ShoppingCart", 
        "CheckoutForm", "CategoryFilter", "PromoBanner", "Footer"
    ],
    "dashboard": [
        "Sidebar", "Navbar", "StatCard", "DataGrid", 
        "ChartWidget", "UserMenu", "ActivityFeed"
    ],
    "marketing": [
        "Navbar", "Hero", "FeatureGrid", "PricingTable", "TestimonialSlider", 
        "NewsletterSignup", "Footer"
    ]
}

# ── 1. HARD DOMAIN ANCHORS (Rule Layer) ───────────────────────────────────────
DOMAIN_ANCHORS = {
    "quiz": {
        "quiz": 3, "exam": 3, "question": 2, "flashcard": 2,
        "answer": 1, "score": 1, "timer": 1, "mock test": 3, "practice test": 3
    },
    "ecommerce": {
        "cart": 3, "checkout": 3, "buy": 2, "shop": 2,
        "inventory": 2, "price": 1, "add to cart": 3, "store": 2
    },
    "dashboard": {
        "dashboard": 3, "admin": 3, "metrics": 2, "analytics": 2,
        "chart": 1, "graph": 1, "statistics": 2, "portal": 2,
        "board": 2, "task": 2, "kanban": 3
    },
    "marketing": {
        "landing page": 3, "waitlist": 3, "newsletter": 2,
        "pricing": 2, "testimonials": 2, "hero": 1, "saas": 2
    }
}

# ── 2. EMBEDDING DESCRIPTIONS ─────────────────────────────────────────────────
DOMAIN_DESCRIPTIONS = {
    "quiz": "application for quizzes exams questions answers scoring flashcards practice tests",
    "dashboard": "analytics dashboard charts metrics monitoring statistics internal tool portal",
    "ecommerce": "online store products shopping cart checkout commerce buy items payments",
    "marketing": "landing page hero features pricing testimonials marketing newsletter signup"
}

# ── 3. FEATURE OVERRIDES ──────────────────────────────────────────────────────
FEATURE_SIGNALS = {
    "quiz": ["timer", "question", "flashcard", "score", "progress", "quiz"],
    "ecommerce": ["cart", "checkout", "product", "payment", "buy"],
    "dashboard": ["chart", "metric", "graph", "analytics", "admin"],
    "marketing": ["hero", "pricing", "testimonial", "newsletter"]
}

def map_ontology_by_embedding(intent: dict) -> dict:
    """Takes parsed PRD intent, uses a 3-layer detection strategy to find domain, returns strict component list."""
    print("\n\033[36m  Executing 3-Layer Ontology Detection...\033[0m")
    
    # Text corpus block combining all PRD intent strings
    text_corpus = " ".join([
        intent.get("product_name", ""),
        intent.get("product_type", ""),
        intent.get("industry", ""),
        " ".join(intent.get("key_features", [])),
        " ".join(intent.get("ui_interactions", [])),
        " ".join(intent.get("custom_components", []))
    ]).lower()

    detected_domain = None
    decision_path = []

    # ---------------------------------------------------------
    # LAYER 1: HARD DOMAIN ANCHORS (Domain Lock)
    # ---------------------------------------------------------
    for domain, anchors in DOMAIN_ANCHORS.items():
        score = 0
        matches = []
        for word, weight in anchors.items():
            if re.search(r'\b' + re.escape(word) + r'\b', text_corpus):
                score += weight
                matches.append(word)
                
        if score >= 4:
            detected_domain = domain
            decision_path.append(f"Detected {domain} anchors: {', '.join(matches)}")
            decision_path.append(f"Anchor score: {score}")
            decision_path.append(f"Domain lock activated -> {domain}")
            break

    # ---------------------------------------------------------
    # LAYER 2: EMBEDDING DOMAIN CLASSIFIER (Fallback)
    # ---------------------------------------------------------
    if not detected_domain:
        decision_path.append("No anchor rules triggered")
        model = get_model()
        query_emb = model.encode(text_corpus, normalize_embeddings=True)
        
        best_score = -1.0
        scores = {}
        for domain, desc in DOMAIN_DESCRIPTIONS.items():
            anchor_emb = model.encode(desc, normalize_embeddings=True)
            sim = float(np.dot(query_emb, anchor_emb))
            scores[domain] = sim
            if sim > best_score:
                best_score = sim
                detected_domain = domain
                
        decision_path.append("Embedding similarity scores:")
        for d, s in scores.items():
            decision_path.append(f"  {d} -> {s:.2f}")
        decision_path.append(f"Selected domain -> {detected_domain}")
    
    # ---------------------------------------------------------
    # LAYER 3: FEATURE SIGNAL DETECTION (Override)
    # ---------------------------------------------------------
    features_list = " ".join(
        intent.get("key_features", []) + 
        intent.get("ui_interactions", []) + 
        intent.get("custom_components", [])
    ).lower()
    
    override_domain = None
    override_signals = []
    
    for sig_domain, signals in FEATURE_SIGNALS.items():
        matches = [word for word in signals if re.search(r'\b' + re.escape(word) + r'\b', features_list)]
        if len(matches) >= 2:
            override_domain = sig_domain
            override_signals = matches
            break
            
    if override_domain and override_domain != detected_domain:
        decision_path.append(f"Feature signals detected: {', '.join(override_signals)}")
        decision_path.append(f"Feature override triggered -> {override_domain}")
        detected_domain = override_domain

    # ---------------------------------------------------------
    # 5. DEBUG OUTPUT 
    # ---------------------------------------------------------
    for log in decision_path:
        print(f"\033[90m    {log}\033[0m")

    # ---------------------------------------------------------
    # GENERATE ONTOLOGY COMPONENTS 
    # ---------------------------------------------------------
    required_comps = set(DOMAIN_MAPS.get(detected_domain, []))
    
    # Explicitly add requested custom components
    for comp in intent.get("custom_components", []):
        if comp not in FORBIDDEN_PRIMITIVES:
            required_comps.add(comp)
        else:
            print(f"\033[90m    Skipping forbidden primitive: {comp}\033[0m")
        
    extracted = list(required_comps)
    print(f"\033[90m  Ontology Components: {', '.join(extracted)}\033[0m")
    
    return {
        "domain": detected_domain,
        "required_components": extracted
    }
