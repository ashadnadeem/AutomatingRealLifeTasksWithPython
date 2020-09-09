__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/2/2020"

import json

#Example 1
json_object1 = {
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002
}

#Example2
json_object2 = {
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002,
  "phone": {
    "office": "802-867-5309",
    "cell": "802-867-5310"
  }
}

#Example3
people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

#Writing to json file
with open('people.json', 'w') as people_json:
    # Write in Single Line, difficult to Understand
    json.dump(people, people_json)
    # Write in Multi Line, Easy to read and understand
    json.dump(people, people_json, indent=2)

#Just to display use dumps()
people_json = json.dumps(people)
print(people_json)

#Reading from json file
with open('people.json', 'r') as people_json:
    people = json.load(people_json)
    print(people)