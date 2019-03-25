import json
from pprint import pprint

file='test.json'

with open(file, 'r') as f:
    data=json.load(f)

sorted_data=sorted(data.items(), key=lambda k: k[0])

print sorted_data

with open('output.txt','w+') as output:
    output_json = json.dumps(sorted_data, output, indent=4)