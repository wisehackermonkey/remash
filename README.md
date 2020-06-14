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



# NOT WORKING ANYMORE due to flask_socketio bug
### bug is descripbed here 
[stackoverflow.com](https://stackoverflow.com/questions/53522052/flask-app-valueerror-signal-only-works-in-main-thread)


# Install 
```
pip install -r requirements.txt
```

### run app in windows (CMD)
```bash
set FLASK_APP=main.py
set FLASK_ENV=development

flask run
```

### run app in windows (POWERSHELL)
```bash
$env:FLASK_APP="main.py"
$env:FLASK_ENV="development"
flask run
```
## Run app
```bash
>python main.py
```

# Links:
- [docs for flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)

- [tutorial for use of flask and socket.io together](https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d)
