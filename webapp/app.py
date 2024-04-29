from flask import Flask, session, render_template, request

import os
import swimclub


app = Flask(__name__)
app.secret_key = "12345"
#Landing page for webapp
@app.get("/")
def index():
    return render_template(
        "index.html",
        title="Welcome to Flipper",
        )
#Creates a glob instace session for swimmers dictionary
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

#Shows names for all swimmers in club
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
#Shows swim html files associated with name 
@app.post("/showfiles")
def display_swimmer_files():
    populate_data()
    name= request.form['swimmer']
    return render_template(
        "select.html",
        title="Pick an event",
        url="/showbarchart",
        select_id="file",
        data=session["swimmers"][name],
    )
#Creates a barchart by fetching it from create module
@app.post("/showbarchart")
def show_bar_chart():
    file_id = request.form["file"]
    location = swimclub.produce_bar_charts(file_id, "templates/")
    return render_template(location.split("/")[-1])

if __name__ == "__main__":
    app.run(debug=True)