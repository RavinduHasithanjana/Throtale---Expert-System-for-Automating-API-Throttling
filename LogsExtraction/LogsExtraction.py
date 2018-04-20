# copyright reserver for Throtale system
# Authour Ravindu Perera
import re
import datetime
import time
import numpy


def main():
    LogsExtraction()


def LogsExtraction():
    strptime = datetime.datetime.strptime
    arrayone = []
    f = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/test.txt", "rb")  # orginal set of log files
    fo = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/logs.csv", "w")  # new data which is created from the log set

    for line in f:
     match = re.search(r'((\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}))', line.decode('utf-8'))
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




if __name__ == '__main__': main()
