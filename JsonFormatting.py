import json

people_string = '''
{
  "people": 
  [
    {
      "name": "John Smith",
      "ph.": "1234123"
    },
    {
      "name": "Jane Doe",
      "ph.": "1234234524634576"
    }
  ]
}
'''

data = json.loads(people_string)
print(data)