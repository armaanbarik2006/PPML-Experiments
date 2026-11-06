"""
Read CSV and JSON files using Pandas

Python lab experiment.
Run: python 03_read_csv_json.py
"""
import pandas as pd


# Place sample.csv and sample.json in this script's working directory.
try:
    csv_data = pd.read_csv("sample.csv")
    print("DataFrame from CSV:")
    print(csv_data)
except FileNotFoundError:
    print("sample.csv not found. Add the file to this folder to test CSV reading.")

try:
    json_data = pd.read_json("sample.json")
    print("\nDataFrame from JSON:")
    print(json_data)
except FileNotFoundError:
    print("sample.json not found. Add the file to this folder to test JSON reading.")
