import sys
import requests 
import ConfigParser

class InviteGuest:
  
    def __init__(self):
        self.URL = "https://slack.com/api/users.admin.invite"
   
    def getItDone(self,fileName):
        data = {}
        colData = []
        config = ConfigParser.ConfigParser()
        config.read("config.ini")
        sec = config.sections()
        
        for section in sec:
            options = config.options(section)
            for option in options:
		data[option] = config.get(section, option)
                if option=='email':
                   emails = data[option].split(',')
                   for email in emails:
			data[option] = email
   			self.sendRequest(data)              
               
  
    def sendRequest(self,data):
        result = requests.post(url=self.URL, data=data)
        print ("%s" %data)
        print ("Output is:%s" %result.text)

########################################################################
# Usage Function
########################################################################
def usage():
    print 'Usage: invite_guest.py <Config YML file>'
    print 'eg: python guest_invite.py config.ini'
    sys.exit(2)
#############################
# Main
############################
argv=sys.argv[1:]
if len(argv) != 1:
     usage()
input_file = argv[0]

proc = InviteGuest()
proc.getItDone(input_file)
