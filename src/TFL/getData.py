import os
import json

# Reads the given file, returns the entire contents as a single string.
def readFile(theFilename):
  inHandle = open(theFilename)
  result = inHandle.read()
  inHandle.close()
  return result

def printCommand(theCommand):
  print(theCommand)
  os.system(theCommand + " 2>&1")

jsonData = json.loads(readFile("secrets.json"))
printCommand("curl https://tfl.gov.uk/tfl/syndication/feeds/serviceboard-fullscreen.htm --output www/index.html")
printCommand("curl https://api.tfl.gov.uk/Line/northern/Arrivals?app_id=" + jsonData["tfl"]["app_id"] + "\&app_key=" + jsonData["tfl"]["app_key"] + " --output www/northernArrivals.json"
