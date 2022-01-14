import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    sum = 0
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    print('Count:', len(info))
    for item in info['comments']:
        sum = sum + int(item['count'])
    print('sum:',sum)
    break
