import json
filename = "user_settings.txt"
myfile = open(filename, 'w', encoding='Latin-1')
player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}
myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ---------------- SAVE by JSON -------------------
json.dump(myplayers, myfile)
myfile.close()
# ---------------- LOAD by JSON -------------------
myfile = open('user_settings.txt', 'r', encoding='Latin-1')
json_data = json.load(myfile)
print(json_data)
for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: "+ str(user['Score']))
    print("Player Awards № 1: " + str(user['awards'][0]))
    print("Player Awards № 1: " + str(user['awards'][1]))
    print("Player Awards № 1: " + str(user['awards'][2]))
    print("---------------------------------------------")