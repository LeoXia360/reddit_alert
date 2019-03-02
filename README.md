# Quickstart
## Pushbullet installation
  1. Install PushBullet for iOS or Android
  2. Go here: https://www.pushbullet.com/#settings/account
  3. Click 'Create Access Token'
  4. Copy and paste into the python file
  5. ```pip install pushbullet.py```

## Reddit installation
1. go here: https://www.reddit.com/prefs/apps/
2. Scroll down and 'create new application'
3. for redirect uri you can just put http://localhost:8080
4. Copy the random generated string beneath 'personal use script': that's the client_id and paste in python script
5. Copy the 'secret' which is the client_secret and paste in python script
6. Change the subreddit in the python to whatever you want
7. Do the same with search terms
8. ```pip install praw```
