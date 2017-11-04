import datetime
import math
import numpy
def formatCheckDate(date, format):
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        return "Wrong Format"
    return 1


def formatCheck(entity, lengthParameter):  # checks format
    if math.isnan(entity)==False:
        print (str(entity)+" "+str(math.isnan(entity)))
        if len(str(int(entity))) == lengthParameter:
            return 1
        return "Wrong length"
    return 1 #for not counting the tupple who has null value


def nullCheck(entity, number):  # checks if null
    if entity in [' ', '	', None] or math.isnan(entity):
        return "The field is null"
    return 1
