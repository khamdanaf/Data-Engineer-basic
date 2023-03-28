# how to convert csv to python
import json
import csv

with open ("coba_csv.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"Year":row[0],
                     "Industry_aggregation_NZSIOC": row[1],
                     "Industry_code_NZSIOC": row[2],
                     "Industry_name_NZSIOC": row[3],
                     "Units": row[4],
                     "Variable_code": row[5],
                     "Variable_name": row[6],
                     "Variable_category": row[7],
                     "Value": row[8],
                     "Industry_code_ANZSIC06": row[9]
                     })
        
with open("hasil_coba.json", "w") as f:
    json.dump(data, f, indent=4)