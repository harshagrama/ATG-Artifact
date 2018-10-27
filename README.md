
##############################################################################
  Introduction
##############################################################################
This is a simple proof-of-concept for managing restricted (single/limited channel) 
guest users in Slack, Slack channel that guest users are invited to will host 
GIT artifact.

Every time a new artifact is produced, subscribed users will be notified to 
download the new version of the artifact

##############################################################################
  Create Git Repostiory For Storing Artifact
##############################################################################
1. Create a GitHub account https://help.github.com
2. create a repository called ATG-Artifact
3. Add artifact file to the repository
    a. Clone git repository 
    b. git add  artifact 
    c. commit artifact 
    d. push the artifact to remote repository
    

##############################################################################
  Create Slack Account & Channel for feed
##############################################################################
1. Create a slack account https://slack.com/
2. Create a channel by name "atg-artifact"
3. On Slack go to browse apps -> gitHub Notifications
4. Click on New Configuration
5. In "Post to Channel" option select "atg-artifact"
6. click Add GitHub Integration
7. Copy the payload URL and follow the instruction as per slack documentation on gitHub or follow below steps
    a. In your GitHub account, go to the repository that you'd like to monitor (ATG-Artifact). 
       Click on the Settings tab in the top navigation.
    b. Click on Webhooks in the left navigation, and then press the Add webhook button.
    c. Enter the payload URL
    d. In the Content Type: select application/json

##############################################################################
  Token Generator    
##############################################################################
https://api.slack.com/custom-integrations/legacy-tokens
Since I am, using git as public repository "Git Guardian" script will make sure the token gets disabled,
when ever the "GG" script runs and finds out that a slack token is publicly available on git repository.

##############################################################################
python script guest_invite.py 
##############################################################################
Purpose of this script is to 
     * Read configuration file for Slack REST API's  attributes and its value
     * For attribute email, which is a coma separated value generate a slack 
	   guest invite request

"guest_invite.py" takes *.ini file as input argument.

example:
python guest_invite.py singleChannelOnly.ini	
python guest_invite.py multiChannel.ini

##############################################################################
Configuration file is used to manage guest users & channels
##############################################################################
* Each configuration file can have multiple channels as a section and
    API attributes as an options.
* email attribute can take list of email id's with coma separated 
* configuration file "singleChannelOnly.ini" here we add guest users restricted to single channel
* configuration file  "multiChannel.ini" here we add guest users, who can access more than 
    one channel

For more about supported attributes, please refer to the following link:
https://github.com/ErikKalkoken/slackApiDoc/blob/master/users.admin.invite.md
	
[Channel Name]
<attribute>:<value>
<attribute>:<value>
<attribute>:<value>
<attribute>:<value>
email:<value>,<value>,<value>

Example:

[atg-artifact]
token: xoxp-461571340768-461571341648-465944437334-3d0d32a21acdfda2d235b6cfb783b5e4    
channels: GDKM90001
ultimate_restricted: 1
email: abc@gmail.com, abc@slkconsult.com, abc@rediffmail.com



*******************************END**********************************
