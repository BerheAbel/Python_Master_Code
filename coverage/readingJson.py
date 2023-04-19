import json
with open('/home/aberhe/pythonMasterClass/coverage/states.json') as r:
    data = json.load(r)
    # print(data)

for state in data['states']:
    print(state['name'])

with open('/home/aberhe/pythonMasterClass/coverage/new_states.json', mode='w') as r:
    json.dump(data, r, indent=2)