import json;
import csv

panCardDataDict = {}



with open('Csv_To_Json_Converter/panToBeRead.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
      panCardData = {"input":{"consent":"Y"},"output":{"result":{},"request_id":"65d45b5a-659c-11e9-9128-cf9a3b317d19","status-code":"101"}}
      panCardData["input"]["pan"]=row[1]
      panCardData["output"]["result"]["name"]=row[0]
      panCardDataDict[row[1]] = panCardData 

with open('Csv_To_Json_Converter/panCards.json', 'w') as json_file:
    json.dump(panCardDataDict, json_file, indent=4)
