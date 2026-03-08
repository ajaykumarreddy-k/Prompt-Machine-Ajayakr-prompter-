import sys

FORBIDDEN_PRIMITIVES = {
    "Container", "Section", "Wrapper", "Layout", 
    "PageContainer", "SectionWrapper", "Stack", "Grid", "FlexRow",
    "ModalWrapper", "AppLayout"
}

def validate_blueprint(blueprint: dict, required_components: list) -> dict:
    """Strictly validates the blueprint AST. Stops pipeline on failure."""
    print("  Validating Blueprint AST...")
    
    errors = []
    ontology_used = set()
    
    if not blueprint.get("pages"):
        errors.append("Blueprint has no pages.")

    # Get discarded components for consistency check
    discarded_set = {item["component"] for item in blueprint.get("discarded_components", [])}

    for page in blueprint.get("pages", []):
        name = page.get("name")
        route = page.get("route")
        
        if not name or not route:
            errors.append(f"Page missing name or route: {page}")
            
        layout = page.get("layout", {})
        children = layout.get("children", [])
        
        # Rule 4: Duplicate Component Prevention
        seen_components = set()
        
        for child in children:
            c_type = child.get("type")
            
            # Rule 1: Forbidden layout primitives
            if c_type in FORBIDDEN_PRIMITIVES:
                errors.append(f"INVALID_LAYOUT_PRIMITIVE_DETECTED: Forbidden layout primitive '{c_type}' found in page '{name}'")
            
            # Rule 9: Duplicate Component Prevention
            if c_type in seen_components:
                errors.append(f"DUPLICATE_COMPONENT_IN_LAYOUT: Duplicate component '{c_type}' on page '{name}'")
            seen_components.add(c_type)
            
            # Track used components for ontology check
            ontology_used.add(c_type)
            if child.get("original_name"):
                ontology_used.add(child["original_name"])
            
            # Rule 7: Component Responsibilities
            resp = child.get("responsibilities")
            if not resp or not isinstance(resp, list) or len(resp) == 0:
                errors.append(f"Component '{c_type}' on page '{name}' is missing mandatory 'responsibilities' array")

            # Depth check (simplified: no nested children allowed in this shallow model)
            if child.get("children"):
                errors.append(f"Layout depth too deep for component '{c_type}' on page '{name}'. Max depth is Page -> Component.")

    # Rule 2: Ontology -> Layout Consistency
    missing_ontology = [c for c in required_components if c not in ontology_used and c not in ["Navbar", "Footer"]]
    
    for comp in missing_ontology:
        if comp not in discarded_set:
            errors.append(f"ONTOLOGY_CONSISTENCY_ERROR: Component '{comp}' was detected but not placed in the layout or explicitly discarded.")

    if errors:
        print("\033[31m\033[1m[VALIDATION FAILED]\033[0m")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
        
    print("\033[32m  ✓ Blueprint Validated.\033[0m")
    return blueprint
