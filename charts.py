import swimclub
import hfpy_utils
import os
import webbrowser

swim_files = os.listdir(swimclub.FOLDER)
fn = "Darius-13-100m-Fly.txt"
FN = "Darius-13-100m-Fly.txt"


# Open html code in browser
webbrowser.open("file://" + os.path.realpath(save_to))