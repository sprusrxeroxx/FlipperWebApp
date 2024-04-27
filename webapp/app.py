from flask import Flask, session, render_template, request

import os
import swimclub


app = Flask(__name__)
app.secret_key = "12345"

@app.get("/")
def index():
    return render_template(
        "index.html",
        title="Welcome to the Flipper swimclub system",
        )

def populate_data():
    if "swimmers" not in session:
        swim_files = os.listdir(swimclub.FOLDER)
        swim_files.remove(".DS_Store")
        session["swimmers"] = {}

        for file in swim_files:
            name, *_ = swimclub.read_swim_data(file)
            if name not in session["swimmers"]:
                session["swimmers"][name] = []
            session["swimmers"][name].append(file)

@app.get("/swimmers")
def display_swimmers():
    populate_data()
    return render_template(
        "select.html",
        title="Pick a swimmer",
        url="/showfiles",
        select_id="swimmer",
        data=sorted(session["swimmers"]), #returns list of all swimmer names 
        )
@app.post("/showfiles")
def display_swimmer_files():
    populate_data()
    name= request.form['swimmer']
    return render_template(
        "select.html",
        title="select an event",
        url="/showbarchart",
        select_id="file",
        data=session["swimmers"][name],
    )

@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    populate_data()
    return str(session["swimmers"][swimmer]) #returns swimmer's files associated with name via hashmap

if __name__ == "__main__":
    app.run(debug=True)