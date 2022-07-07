import json

# Reads the given file, returns the entire contents as a single string.
def readFile(theFilename):
  inHandle = open(theFilename)
  result = inHandle.read()
  inHandle.close()
  return result

jsonData = json.loads(readFile("secrets.json"))
print("https://api.tfl.gov.uk/Line/northern/Arrivals?app_id=" + jsonData["tfl"]["app_id"] + "&app_key=" + jsonData["tfl"]["app_key"])
