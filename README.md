
#  Introduction
This is a simple proof-of-concept for managing restricted (single/limited channel) 
guest users in Slack. 

* Slack channel that guest users are invited, will host GIT artifact

* Every time a new artifact is produced, subscribed users will be notified to download the new version of the artifact


#  Prerequisites

###  Create Git Repostiory For Storing Artifact
1. Create a GitHub account https://help.github.com
2. create a repository called ATG-Artifact
3. Add artifact file to the repository
    1. Clone git repository 
    2. git add  artifact 
    3. commit artifact 
    4. push the artifact to remote repository
    

###  Create Slack Account & Channel For Feed
1. Create a slack account https://slack.com/
2. Create a channel by name "atg-artifact"
3. On Slack go to browse apps -> gitHub Notifications
4. Click on New Configuration
5. In "Post to Channel" option select "atg-artifact"
6. Click Add GitHub Integration
7. Copy the payload URL and follow the instruction as per slack documentation on gitHub or follow below steps
   1. In your GitHub account, go to the repository that you'd like to monitor (ATG-Artifact). Click on the Settings tab in the top navigation.
   2. Click on Webhooks in the left navigation, and then press the Add webhook button.
   3. Enter the payload URL
   4. In the Content Type: select application/json

###  Token Generator    
* https://api.slack.com/custom-integrations/legacy-tokens
#### This GitHub is a community version, hence it is a public repository. "Git Guardian" script will make sure the token gets disabled, when ever the "GG" script runs and finds out that a slack token is publicly available on git repository.

### Python
* To install python on linux: https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux-python.html
* To install python on windows: https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html

#  Python Script: "guest_invite.py" 

##  Purpose Of This Script Is To: 
* Read configuration file for attributes and its value for slack API REST call
* Attribute email, which is a comma separated value, for which generate a slack guest invite request

 guest_invite.py takes *.ini file as input argument.

```
example:
   python guest_invite.py singleChannelOnly.ini	
   python guest_invite.py multiChannel.ini
```
#  Configuration File Is Used To Manage Guest Users & Channels

* Each configuration file can have multiple channels as a section and API attributes as options.
* email attribute can take list of email id's with comma separated 
* configuration file "singleChannelOnly.ini" for adding  guest users restricted to single channel
* configuration file  "multiChannel.ini" for adding guest users, who can access more than one channel

* For more about supported attributes, please refer to the following link:
* https://github.com/ErikKalkoken/slackApiDoc/blob/master/users.admin.invite.md
```	
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
```


