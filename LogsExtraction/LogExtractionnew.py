# copyright reserver for Throtale system
# Authour Ravindu Perera
import csv
import re
import datetime
import time
import numpy


def main():
    LogsExtraction()


def LogsExtraction():
    strptime = datetime.datetime.strptime
    arrayone = []
    arrayYear = []
    arrayMonth = []
    arrayDay = []
    arrayHour = []
    arrayMin = []
    arraySec = []
    f = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/test.txt", "rb")  # orginal set of log files
    fo = open("/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/logs.csv", "w")  # new data which is created from the log set

    for line in f:
     match = re.search(r'((\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}))', line.decode('utf-8'))
     # print(match)
     str_time = match.group()
     t1 = strptime(str_time, "%d/%b/%Y:%H:%M:%S")
     # print(t1.minute)
     arrayYear.append(t1.year)
     arrayMonth.append(t1.month)
     arrayDay.append(t1.day)
     arrayHour.append(t1.hour)
     arrayMin.append(t1.minute)
     arraySec.append(t1.second)
     ls = float(time.mktime(t1.timetuple()))
     arrayone.append(ls)

    print(arraySec)

    print(arrayone)

     # ls = float(time.mktime(t1.timetuple()))

    #  # val = float(ls)
    #  secondval = time.mktime(t1.timetuple())
    #
    #  # print(ls)
    #  arrayone.append(ls)
    #  # fo.write(ls)
    #
    # # logMessage()
    # print(arrayone)
    # # print("print")
    # # print(arrayone)
    arrall =[]
    for i in range(len(arrayDay)):
     all = arrayDay[i],arrayMonth[i],arrayHour[i],arrayMin[i],arraySec[i],arrayone[i]
     # print(all)
     arrall.append(all)


    numpy.savetxt("ExtractedDataMon.csv", arrall, delimiter=",", fmt="%s")
  # numpy.savetxt("ExtractedDataDay.csv", arrayDay, delimiter=",", fmt="%s")
    # numpy.savetxt("ExtractedDataHour.csv", arrayHour, delimiter=",", fmt="%s")
    # numpy.savetxt("ExtractedDataMin.csv", arrayMin, delimiter=",", fmt="%s")
    # numpy.savetxt("ExtractedDataSec.csv", arraySec, delimiter=",", fmt="%s")



if __name__ == '__main__': main()
