"""

"""
import statistics
import hfpy_utils
import os
import webbrowser


FOLDER= "swimdata/"
CHARTS = "charts/"

def read_swim_data(filename):

    """ This is a function that returns the swim data from a CSV file
    
    
        Given the name of a swimmer's file, it extracts all the required data, then returns a tuple to the caller
    """

    Name, Age, Distance, Stroke = filename.removesuffix(".txt").split("-")

    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(",")

    converts = []
    for t in times:
        # The minute value is verified to be below or above zero, this prevents ValueError due to mismatching list assignment
        if ":" in t :
            minutes, mixed_seconds = t.split(":")
            seconds, nano_seconds = mixed_seconds.split(".")
        else:
            minutes = 0
            seconds, nano_seconds = t.split(".")


        converts.append(int(minutes)*60*100 + int(seconds)*100 + int(nano_seconds))

    averageTime = statistics.mean(converts)
    min_secs, nano_seconds = f"{(averageTime / 100):.2f}".split(".") # conversion
    min_secs = int(min_secs)
    minutes = min_secs // 60
    seconds = min_secs - minutes*60

    averageTime = f"{minutes}:{seconds:0>2}.{nano_seconds}"

    return (Name, Age, Distance, Stroke, times, averageTime, converts) #A tuple containing all the values 

def produce_bar_charts(fn, location=CHARTS):
    """
        Given the name of a swimmer's file, produces the HTML/SVG-based bar chart for the stats.
    
        Saves the chart to the CHARTS folder, Returns the path to the bar chart file
    """
    *_, times, average, converts = read_swim_data(fn)

    from_max = max(converts)
    times.reverse()
    converts.reverse()

    (swimmer, age, distance, stroke, *_) = read_swim_data(fn)  # Extracting the name, age, distance and stroke for each swimmer

    title = f"{swimmer} (Under {age}) {distance} {stroke}"  # string variable for the title of the html code


    # string variable for the header tag of the html page

    header = f"""
                <!DOCTYPE html>
                    <html>
                        <head>
                            <title>{title}</title>
                            <link rel="stylesheet" href="/static/webapp.css"/>
                        </head>
                        <body>
                            <h2>{title}</h2>
            """
    
    body = ""

    #Enumarator to number all the swim times for swimmer 

    for n, t in enumerate(times):
        bar_width = hfpy_utils.convert2range(converts[n], 0, from_max, 0, 350) # function to scale all the converted swim times to svg bar range
        body = body + f"""
                            <svg height= "30" width="400">
                                <rect height="30" width="{bar_width}" style="fill:rgb(0, 0, 255);" />
                            </svg>{t}<br />
                        """

    # string for the footer of the html content 

    footer = f""""
                            <p>Average Time: {average}</p>
                        </body>
                    </html>
                """

    # HTML code components 

    page = header + body + footer

    save_to = f"{location}{fn.removesuffix('.txt')}.html"

    # save html stats code to charts folder
    with open(save_to, "w") as sf:
        print(page, file=sf)

    return save_to