import json

person ={"name": "John" , "age":30 , "city": "NewYork" , "hasChildren": False , "titles":["engineer", "programmer"]}


personJson = json.dumps(person , indent=4 , sort_keys=True)
print(personJson)

with open('person.json', 'w') as file:
    json.dump(person,file ,indent=4)