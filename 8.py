rules = [
    {"if": ["Fever", "Cough"],             "then": "ViralInfection"},
    {"if": ["ViralInfection", "BodyAche"], "then": "FluSymptoms"},
    {"if": ["FluSymptoms"],                "then": "Flu"}
]

facts = ["Fever", "Cough", "BodyAche"]

def backward_chain(goal):
    print(f"Attempting to prove: {goal}")

    if goal in facts:
        print(f"  -> Success: '{goal}' is already a known fact.")
        return True

    matching_rules = []
    for r in rules:
        if r["then"] == goal:
            matching_rules.append(r)
    
    if not matching_rules:
        print(f"  -> Fail: No rules found that produce '{goal}'")
        return False

    for rule in matching_rules:
        print(f"  -> Checking rule: IF {rule['if']} THEN {rule['then']}")
        
        all_conditions_met = True
        
        for condition in rule["if"]:
            if not backward_chain(condition):
                all_conditions_met = False
                break
        
        if all_conditions_met:
            print(f"  -> Rule Succeeded! Added '{goal}' to facts.")
            facts.append(goal) 
            return True

    return False

print("\n--- Start Backward Chaining ---")
print(f"Initial Facts: {facts}")
print(f"Target Goal: Flu\n")

if backward_chain("Flu"):
    print("\nFINAL RESULT: PROVED! The patient has Flu.")
else:
    print("\nFINAL RESULT: FAILED. Could not prove Flu.")