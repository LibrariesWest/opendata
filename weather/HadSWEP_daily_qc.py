## Date: 15th December 2016
## Author: Dave Rowe
## Description: This is a script to take HadUKP (UK precicipation data) as published by the Met Office, and transform it into CSV form
## What is does:    a) Loads in the text file.  
#                   b) Ignores first few lines. 
#                   c) For each other line (a month), constructs a line for each day.

import csv
import datetime

hadukpfile = open('weather\HadSWEP_daily_qc.txt', 'r')
mindate = datetime.datetime(2016,6,7)

with open('weather\HadSWEP.csv', 'w', newline='') as output:
    precipitationwriter = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i, line in enumerate(hadukpfile):
        if (i > 2):
            values = line.split()
            year = values[0]
            month = values[1]
            for x, prec in enumerate(values):
                if (x > 1 and prec != '-99.99'):
                    date = datetime.datetime(int(year),int(month),x-1)
                    if (date >= mindate):
                        precipitationwriter.writerow([date.strftime("%Y-%m-%d"), str(prec)])
