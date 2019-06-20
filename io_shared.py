import os, json

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensure_file(filename):
    ensure_dir(filename)
    # create file is not exist
    with open(filename,"w") as f:
        f.write("")

def save_as_json(filename,data,verbose): 
    ensure_file(filename)
    if verbose:
        print('Write json file to output %s'%filename)

    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f)

