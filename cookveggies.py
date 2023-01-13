#1. Read output/vegetables.csv (see previous section) into a variable called vegetables.
import csv
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#2. Print the variable vegetables.
print(vegetables)

#3. Write vegetables as a JSON file called output/vegetables.json. It should look like this:
import json 
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)

##### Super hero example #####

#1. Reads superheroes.json (in this folder)
with open('superheroes.json', 'r') as f:
    data = json.load(f)
#2. Creates an empty array called powers
    powers = []
#3. Loop thorough the members of the squad, and append the powers of each to the powers array.
    for item in data["members"]:
        powers.append(item["powers"])
#4. Prints those powers to the terminal
        print(item["powers"])

##### Try it #####

#1. Read superheroes.json
with open('superheroes.json', 'r') as f:
    data = json.load(f)
#2. Write a header to the CSV file
    with open('heroes.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "secretidentity", "powers", 
            "squadname", "hometown", "formed", "secretbase", "active"])
#3. Loop over the members, and for each member write a row to the csv file
        for i in data["members"]: 
            writer.writerow([i["name"], i["age"],i["secretIdentity"],i["powers"],
            data["squadName"], data["homeTown"],data["formed"],data["secretBase"],data["active"]])