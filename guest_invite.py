import requests 
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")
channels=config.sections()
print ("Channels ->>%s" %channels) 

#api-endpoint
URL = "https://slack.com/api/users.admin.invite"

#data to be sent to
data = {'token': 'xoxp-461571340768-461571341648-465944437334-3d0d32a21acdfda2d235b6cfb783b5e4',
        'email': 'harshag@slkconsult.com',
        'channels': 'GDKM90001',
        'ultimate_restricted': '1'}

result = requests.post(url=URL, data=data)

print("Output is:%s" %result.text)
