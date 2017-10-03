import xolphin
client = xolphin.Client('youremail@domain.com', 'YourPassword')

request = client.request().get(123456789)
#print(request.id)

for vald in request.validations:
    print(vald)