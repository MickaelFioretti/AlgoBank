import json

# Variables
"""
    {
        "actions": "Action-1",
        "cout_par_action": 20,
        "benefice": 5
    },
"""

data: list = []
action_list: list = []
investissement: list = []

# Read JSON file
with open("./action.json") as f:
    data: list = json.load(f)


# Brute force
def brute_force() -> None:
    for i in range(len(data)):
        action_list.append(data[i])
        # aditionner tous les couts par action de la liste
        cout: int = sum([action["cout_par_action"] for action in action_list])
        # aditionner tous les benefices de la liste
        benefice: int = sum([action["benefice"] for action in action_list])
        # si le cout est inferieur ou egal a 500
        if cout <= 500:
            # afficher le cout et le benefice
            # print(f"cout: {cout} benefice: {benefice}")
            # faire une variable avec les actions et le benefice
            print(action_list)
            investissement.append(
                [
                    "essai n°: " + str(i + 1),
                    "actions: " + str(action_list),
                    "benefice: " + str(benefice),
                ]
            )
    print(investissement[0])


brute_force()
