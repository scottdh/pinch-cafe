import json

# Reads the given file, returns the entire contents as a single string.
def readFile(theFilename):
  inHandle = open(theFilename)
  result = inHandle.read()
  inHandle.close()
  return result

jsonData = json.loads(readFile("secrets.json"))
curlCommand = "curl https://api.tfl.gov.uk/Line/northern/Arrivals?app_id=" + jsonData["tfl"]["app_id"] + "\&app_key=" + jsonData["tfl"]["app_key"] + " --output /etc/webconsole/tasks/hy6a5ak6b1lmnpl1/www/TFLData.json 2>&1"
print(curlCommand)
os.system(curlCommand)
