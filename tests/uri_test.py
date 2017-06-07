import requests

valid_uri = ['/restaurants/',
             '/restaurant/1/',
             '/restaurant/new/',
             '/restaurant/1/edit/',
             '/restaurant/1/delete/']

host = "http://localhost:5000{}"

for uri in valid_uri:
    r = requests.get(host.format(uri))
    if r:
        print("{}{}".format(uri, ' 200 OK!'))
    else:
        print("{}{}".format(uri, ' 404 BAD'))