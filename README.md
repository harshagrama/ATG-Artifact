
***********ATG Assignment*********************

##############################################################################
  Create Git Repostiory For Storing Artifact
##############################################################################
1. Create a GitHub account https://help.github.com
2. create a repository called ATG-Artifact
3. Add artifact file to the repository
    a. Clone git repository 
    b. git add the artifact 
    c. commit artifact 
    d. push the artifact to remote repository
    

##############################################################################
 Create Slack Account & Channel for feed
##############################################################################
1. Create a slack account https://slack.com/
2. Create a channel by name "atg-artifact"
3. On Slack go to browse apps -> gitHub Notifications
4. Click on New Configuration
5. Post to Channel select "atg-artifact"
6. click Add GitHub Integration
7. Copy the payload URL and follow the instruction as per slack documentation on gitHub Or follow below steps
    a. In your GitHub account, go to the repository that you'd like to monitor (ATG-Artifact). Click on the Settings tab in the top navigation.
    b. Click on Webhooks in the left navigation, and then press the Add webhook button.
    c. Enter the payload URL
    d. Content Type: select application/json

##############################################################################
Token Generator    
##############################################################################
https://api.slack.com/custom-integrations/legacy-tokens
Since git is a public repository slack good guy will make sure the token gets expired every 24hours are so or when ever the good guy script runs and finds out that a slack tocken is publicly available on git repository.


##############################################################################
python script guest_invite.py 
##############################################################################
guest_invite.py takes *.ini file as input argument.

example:
guest_invite.py singleChannelOnly.ini	
guest_invite.py multiChannel.ini
##############################################################################
*.ini file, section & options
##############################################################################
[Channel Name]
token:<value>
channels:<value>
ultimate_restricted:<value>
.
.
.
.
email:<value>,<value>,<value>.......

Example:
[atg-artifact]
token: xoxp-461571340768-461571341648-465944437334-3d0d32a21acdfda2d235b6cfb783b5e4    
channels: GDKM90001
ultimate_restricted: 1
email: abc@gmail.com, abc@slkconsult.com, abc@rediffmail.com




