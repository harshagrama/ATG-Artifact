import requests 
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")
channels=config.sections()
print ("Channels ->>%s" %channels) 

#api-endpoint
URL = "https://slack.com/api/users.admin.invite"

#data to be sent to
data = {'token': xoxp-461571340768-461571341648-461953215104-1233114e019a59bf594243e69a7052b9,
        'email': harshag@slkconsult.com
        'channels':GDKM90001}

result = requests.post(url=URL, data=data)

print("Output is:%s" %result)
