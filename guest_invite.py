import sys
import requests 
import ConfigParser

####################################################################
# Guest invite class
#   Purpose of this class is to read configuration file for the following:
#     * Slack REST API attributes and its value
#     * Every email coma seperated value generate a slack 
#	  guest invite request
####################################################################
class InviteGuest:
  
    def __init__(self):
        self.URL = "https://slack.com/api/users.admin.invite"

    # Process the *.ini file and prepare the data
    def getItDone(self,fileName):
        data = {}
        emails = []
        config = ConfigParser.ConfigParser()
        try:
            with open (fileName) as f:
                config.readfp(f)
        except IOError:
            print ("Error: Unable to open file: %s" %fileName)
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
               
    # Slack API Call
    def sendRequest(self,data):
        result = requests.post(url=self.URL, data=data)
        print ("REQUEST:{} --> RESPONSE:{}".format(data,result.text))

# Usage Function
def usage():
    print 'Usage: invite_guest.py <Config YML file>'
    print 'eg: python guest_invite.py config.ini'
    sys.exit(2)

# Main
argv=sys.argv[1:]
if len(argv) != 1:
     usage()
input_file = argv[0]

proc = InviteGuest()
proc.getItDone(input_file)
