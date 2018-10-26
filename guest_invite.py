import sys
import requests 
import ConfigParser

####################################################################
# Guest Invite Class
####################################################################
class InviteGuest:
  
    def __init__(self):
        self.URL = "https://slack.com/api/users.admin.invite"

    ####################################################################
    # Process the *.ini file and prepare the data
    ####################################################################
    def getItDone(self,fileName):
        data = {}
        colData = []
        emails = []
        config = ConfigParser.ConfigParser()
        config.read(fileName)
        sec = config.sections()
        for section in sec:
            options = config.options(section)
            for option in options:
		data[option] = config.get(section, option)
                if option=='email':
                   emails = data[option].split(',')
            for email in emails:
                data['email'] = email
                self.sendRequest(data)              
               
    ####################################################################
    # Slack API Call
    ####################################################################
    def sendRequest(self,data):
        result = requests.post(url=self.URL, data=data)
        print ("REQUEST:{} --> RESPONSE:{}".format(data,result.text))

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
