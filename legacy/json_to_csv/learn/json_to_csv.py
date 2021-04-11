import json
import csv

# open JSON file and load its data
with open('data.json') as json_file:
    data = json.load(json_file)

employee_data = data['emp_details']

# open file for writing
data_file = open('data_file.csv', 'w')

# create csv writer object
csv_writer = csv.writer(data_file)

count = 0
for emp in employee_data:
    if count == 0:
        # write headers of csv file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
    # write data of csv file
    csv_writer.writerow(emp.values())

data_file.close()

