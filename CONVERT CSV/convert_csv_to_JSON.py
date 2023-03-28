# how to convert csv to python
import json
import csv

with open ("coba_.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"firstname":row[0],
        "age": row[1]})
        
with open("names.json", "w") as f:
    json.dump(data, f, indent=4)