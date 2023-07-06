import json

# Read JSON file
"""
    {
        "actions": "Action-1",
        "cout_par_action": 20,
        "benefice": 5
    },
"""
with open("./action.json") as f:
    actions: list = json.load(f)

# variables
valid_combinations: list = []


# Function to generate combinations
def generate_combinations(actions: list, r, combination=[]) -> None:
    """
    Generate all combinations of actions
    """
    if r == 0:
        total_cost: int = sum(
            [action["cout_par_action"] for action in combination]
        )
        if total_cost == 500:
            valid_combinations.append(combination)
        return

    for i in range(len(actions)):
        new_combination = combination + [actions[i]]
        generate_combinations(actions[i + 1 :], r - 1, new_combination)


# Script
for r in range(1, len(actions) + 1):
    generate_combinations(actions, r)


"""
    Ajoute les combinaisons valides dans un fichier JSON
"""
# Creer une structure de donnees
results = {"combinations": []}

# Ajoute les combinaisons valides au resultat
for combination in valid_combinations:
    combination_data = [
        {
            "action": action["actions"],
            "cost": action["cout_par_action"],
            "benefit": action["benefice"],
        }
        for action in combination
    ]

    # benefice total
    total_benefit: int = sum([action["benefice"] for action in combination])
    combination_data.append({"total_benefit": total_benefit})

    results["combinations"].append(combination_data)

# Recupere la combinaison avec le benefice le plus eleve
best_combination = max(
    results["combinations"],
    key=lambda combination: combination[-1]["total_benefit"],
)

# Ajoute la combinaison avec le benefice le plus eleve dans un fichier JSON
with open("./best_combination.json", "w") as f:
    json.dump(best_combination, f, indent=4)

# Ecrit le resultat dans un fichier JSON
with open("./result.json", "w") as f:
    json.dump(results, f, indent=4)


print("Fin du script !")