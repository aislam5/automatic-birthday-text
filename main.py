"""
1. Store Data in .csv file
2. Use Python to get date (the date in the file and the date in python should be of the same format)
3. OPen csv file and see if todays Date Matches the date in the csv file
4. Send Message then (using package such as pywhatkit)
5. Run the Script daily somehow (schedule python package)
"""

#make a csv file with the name, date(mm/dd), number, message
#so that you can use this for yourself

import csv
import datetime

date = datetime.datetime.now()
date_formatted = date.strftime("%m/%d")
with open('birthdays.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0 
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            if row[1].strip() == date_formatted:
                print(f"HBD {row[0]}")
            line_count += 1
    print(f'Processes {line_count} lines.')
