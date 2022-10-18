# Import json
import json

database_address = {
  "host": "10.0.0.5",
  "port": 8456
}

#dump the dictionary into json file 
# Open if file doesn't exits it creates itthe configuration file in writable mode
with open("database_config.json", "w") as fh:
  """
  Serialize the object in this file handle
  the file is the second parameter of json.dump and in this program the file is open as fh, 
  therefore fp as to equal to the file that will be
  written into
  """
  json.dump(obj=database_address, fp=fh) 