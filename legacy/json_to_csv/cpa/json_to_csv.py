import json
# import csv
import pandas as pd
import os

cpa_json_data = os.path.abspath('/Users/lukemcevoy/Develop/stevens/s21/CPA/cs546-data-endpoint/JSON_samples')
files = os.listdir(cpa_json_data)

for file in files:
    curr_file = os.path.abspath(cpa_json_data + "/" + file)
    df = pd.read_json(curr_file)
    # df.to_csv(file[:4]+ '.csv', index=False)
    print(df)


