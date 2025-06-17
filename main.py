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

with open('birthdays.csv') as csv_file:
    csv.reader = csv.reader(csv_file, delimiter = ',')
