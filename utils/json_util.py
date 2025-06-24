
import json
import os.path


# Read json

def read_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File is missing,{file_path}")
    with open(file_path) as file:
        return json.load(file)

# file writing

def write_json(file_path,data):
    with open(file_path,'w',indent=4):
        json.dump(data)
        

