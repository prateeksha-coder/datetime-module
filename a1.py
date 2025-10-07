import random
import time


def getRandomDate(starDate, endDate):
    print("Printing random date between", starDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    print(starttime)
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    print(endtime)
    randomTime = starttime + randomGenerator * (endtime - starttime)
    print(randomTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate


print("Random Date = ", getRandomDate("1/1/2020", "12/12/2024"))
