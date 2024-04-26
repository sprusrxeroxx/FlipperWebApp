from flask import Flask, session

import os
import swimclub


app = Flask(__name__)
app.secret_key = "12345"

@app.get("/")
def index():
    return "This is a placeholder for your webapp's index page"

@app.get("/swimmers")
def display_swimmers():
    swim_files = os.listdir(swimclub.FOLDER)
    swim_files.remove(".DS_Store")

    session["swimmers"]={}

    for file in swim_files:
        name, *_ = swimclub.read_swim_data(file)
        if name not in session["swimmers"]:
            session["swimmers"][name] = []
        session["swimmers"][name].append(file)
    
    return str(sorted(session["swimmers"]))

@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    return str(session["swimmers"][swimmer])

if __name__ == "__main__":
    app.run(debug=True)