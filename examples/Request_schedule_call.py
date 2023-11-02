import xolphin
import json

client = xolphin.Client('youremail@domain.com', 'YourPassword', True);

order_id = 964178685
date = "2024-01-26"
time = "11:00"
timezone = "Europe Amsterdam"

#scheduling automated callback
try:
	vc = client.request().configure_validation_call(order_id)
	vc.date = date
	vc.time = time
	vc.timezone = timezone
	vc.phoneNumber = "132456789"
	#vc.action = "ScheduledCallback" #not mandatory, this is the default action
	request = client.request().send_validation_call(vc)
	print(vars(request))
except Exception as ex:
	print("------- ERROR -------")
	print(ex)

#scheduling manual callback
try:
	vc = client.request().configure_validation_call(order_id)
	vc.date = date
	vc.time = time
	vc.timezone = timezone
	vc.phoneNumber = "132456789"
	vc.extensionNumber = "123"
	vc.action = "ManualCallback"
	vc.commet = "Please ask for Joe"
	request = client.request().send_validation_call(vc)
	print(vars(request))
except Exception as ex:
	print("------- ERROR -------")
	print(ex)


#changing callback phone number
try:
	vc = client.request().configure_validation_call(order_id)
	vc.date = date
	vc.time = time
	vc.timezone = timezone
	vc.phoneNumber = "987654321"
	vc.action = "ReplacePhone"
	request = client.request().send_validation_call(vc)
except Exception as ex:
	print("------- ERROR -------")
	print(ex)	

#changing callback method from Telephone to Email
try:
	vc = client.request().configure_validation_call(order_id)
	vc.date = date
	vc.time = time
	vc.timezone = timezone	
	vc.action = "replaceEmailAddress"
	vc.emailAddress = "youremail@domain.com"	
	request = client.request().send_validation_call(vc)
	print(vars(request))
except Exception as ex:
	print("------- ERROR -------")
	print(ex)	

#request re-sending callback email to customer
try:
	vc = client.request().configure_validation_call(order_id)
	vc.date = date
	vc.time = time
	vc.action = "sendCallbackEmail"	
	request = client.request().send_validation_call(vc)
	print(vars(request))
except Exception as ex:
	print("------- ERROR -------")
	print(ex)	

