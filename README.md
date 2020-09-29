# Remash
### live book editor
```
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20190106 updated 20200613
```

# Project:
```
The idea for this project is to let reddit collaboratively write a book in a 24 hours. 
It works similar to collaborative editing on google docs.
This project uses docker to host the web server, that I manage maintain, 
To test it out open two tabs and type something, and see it replicate over to the other tab.
```

# (Easiest) Run using docker 
# If you just want to try it out id recommend using play-with-docker.com 
### [play-with-docker.com](https://labs.play-with-docker.com/)


# Run using docker for everyone else
```bash
docker login
>docker run -it --rm -p 80:8080 wisehackermonkey/remash
```
# Docker Run/Install
```bash
docker run -it --rm -p 80:8080 wisehackermonkey/remash
```

# Deploy
```bash
docker run -d --restart=always --name remash -p 80:8080 wisehackermonkey/remash
```


# The (hardway)
#### Install   
```
pip install -r requirements.txt
```

##### run app in windows (CMD)
```bash
set FLASK_APP=main.py
set FLASK_ENV=development

flask run
```

##### run app in windows (POWERSHELL)
```bash
$env:FLASK_APP="main.py"
$env:FLASK_ENV="development"
flask run
```
#### Run app
```bash
>python main.py
```


### in browser go to 
```
in browser go to 
http://localhost:80
Type something into the text box
open another browser tab to 
http://localhost:80
and type something else you will see the stuff replicated across the browser tabs!
```

## Bugs due to flask_socketio bug
#### bug is descripbed here 
[stackoverflow.com](https://stackoverflow.com/questions/53522052/flask-app-valueerror-signal-only-works-in-main-thread)


# TODO
- capcha per character
- improve character syncing useing the same algorithm that google docs uses that was created by microsoft

# Links:
- [docs for flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)

- [tutorial for use of flask and socket.io together](https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d)
