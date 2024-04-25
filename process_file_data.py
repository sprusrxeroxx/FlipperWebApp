# i have to find a way to extract the swim data from inside the file for each student.
import statistics


FN = "Darius-13-100m-Fly.txt"
FOLDER= "swimdata/"
Name, Age, Distance, Stroke = FN.removesuffix(".txt").split("-")

with open(FOLDER + FN) as file:
    lines = file.readlines()

times = lines[0].strip().split(",")

converts = []
for t in times:
    minutes, mixed_seconds = t.split(":")
    seconds, nano_seconds = mixed_seconds.split(".")

    converts.append(int(minutes)*60*100 + int(seconds)*100 + int(nano_seconds))

    print(t, "->", int(minutes)*60*100 + int(seconds)*100 + int(nano_seconds))

averageTime = statistics.mean(converts)
min_secs, nano_seconds = str(round(averageTime/100, 2)).split(".") #conversion

min_secs = int(min_secs)
minutes = min_secs // 60
seconds = min_secs - minutes*60

averageTime = str(minutes) + ":" + str(seconds) + ":" + nano_seconds

print(Name)
print(Age)
print(Stroke)
print ("averageTime -> " + averageTime)
