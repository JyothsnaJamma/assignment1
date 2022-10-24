"""
import csv
f=open("people.csv","a",newline="")
tup1= ("bob",19,"b")
writer = csv.writer(f)
writer.writerow(tup1)
f.close()
"""

import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_names.csv','w') as new_file:
        fieldnames=['first_name','last_name','email']
        
        csv_writer = csv.writer(new_file,delimiter=',')
        
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
            