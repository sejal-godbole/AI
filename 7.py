def forward_chaining():
    print("--- Start Forward Chaining ---")
    
    rules = [
        {"if": ["P", "Q"], "then": "R"},
        {"if": ["R", "S"], "then": "T"},
        {"if": ["T"],      "then": "U"}
    ]

    facts = ["P", "Q", "S"]
    goal = "U"

    print(f"Initial facts: {facts}")

    while True:
        new_fact_added = False
        
        for rule in rules:
            if rule["then"] in facts:
                continue
            
            can_fire = True
            for condition in rule["if"]:
                if condition not in facts:
                    can_fire = False
                    break
            
            if can_fire:
                new_fact = rule["then"]
                print(f"Rule Fired: {rule['if']} -> Adds '{new_fact}'")
                facts.append(new_fact)
                new_fact_added = True
                
                if new_fact == goal:
                    print("SUCCESS: Goal found!")
                    print(f"Final Facts: {facts}")
                    return

        if not new_fact_added:
            break
            
    print("FAIL: Goal could not be derived.")

forward_chaining()