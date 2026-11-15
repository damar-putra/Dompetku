import json
import os
from config.settings import DATA_DIR

def pastikan_folder_ada():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def baca_json(file_path):
    pastikan_folder_ada()
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_json(file_path, data):
    pastikan_folder_ada()
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)