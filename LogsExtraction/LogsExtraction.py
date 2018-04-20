# copyright reserver for Throtale system
# Authour Ravindu Perera
import re
import datetime
import platform
import csv
import time
import pandas
import numpy


def main():
    LogsExtraction()


def LogsExtraction():
    # match_record = re.compile(b"[A-Za-z]").match
    strptime = datetime.datetime.strptime
    arrayone = []
    f = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/test.txt", "rb")  # orginal set of log files
    fo = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/logs.csv", "w")  # new data which is created from the log set

    for line in f:
     match = re.search(r'((\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}))', line.decode('utf-8'))
     #print(match.group())
     str_time = match.group()
     t1 = strptime(str_time, "%d/%b/%Y:%H:%M:%S")
     ls = float(time.mktime(t1.timetuple()))
     # val = float(ls)
     secondval = time.mktime(t1.timetuple())

     print(ls)
     arrayone.append(ls)
     # fo.write(ls)

    # logMessage()
    print(arrayone)
    print(arrayone)
    numpy.savetxt("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv", arrayone, delimiter=",")
     #print(time.year + time.month) # create and csv format with the following way
     # logMessage(time)




# def logMessage():
#     print("work")
#     with open('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/logs.txt', 'r') as in_file:
#         stripped = (line.strip() for line in in_file)
#
#         print(stripped)
#         lines = (line.split() for line in stripped if line)
#         with open('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/logs.csv', 'w') as out_file:
#             writer = csv.writer(out_file)
#             writer.writerow(('title'))
#             writer.writerows(lines)

def counting():
    print()

if __name__ == '__main__': main()