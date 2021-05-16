import requests
import json

r = requests.get('https://api.kanye.rest')
print('Status code is ' + str(r.status_code))
a = r.json()
print('The date that this operation was requested\t' + r.headers['Date'] )
f = open('kanye.json', 'w')
json.dump(a, f)
print('Kanye West said:\t' + a['quote'])