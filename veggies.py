vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

import csv

# 1. Loops through each vegetable

for veg in vegetables: 
    print(veg)

# 2. In the loop, write the name of each vegetable and the color 
#    into a CSV called vegetables.csv
# 3. Bonus: add the length of the name of the vegtable as separate column 

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "color", "length"])
    for veg in vegetables: 
        writer.writerow([veg["name"], veg["color"],len(veg["name"])])




