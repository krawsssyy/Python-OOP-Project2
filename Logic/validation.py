from Logic.monthlySums import getMonth, getYear
import datetime

EPSILON = 0.0001


def getDay(date):
    '''
    This function returns the day of a given date
    :param date: - string - the given date
    :return: - day of the given date
    '''
    dateList = date.split("/")
    return dateList[0]


def representsInt(value):
    '''
    This function checks if a given parameter can be safely converted to int to avoid errors
    :param value: - the parameter to be checked
    :return: True/False
    '''
    try:
        int(value)
        return True
    except ValueError:
        return False


def representsFloat(value):
    '''
    This function checks if a given parameter can be safely converted to float to avoid errors
    :param value: - the parameter to be checked
    :return: True/False
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False


def dateValidation(date):
    '''
    This function is used to validate a date
    :param date: - string - given date
    :return: True/False
    '''
    if representsInt(getDay(date)) and representsInt(getMonth(date)) and representsInt(getYear(date)):
        if int(getDay(date)) < 1 or int(getMonth(date)) < 1 or int(getYear(date)) < 1:
            return False
        if int(getDay(date)) > 31 or int(getMonth(date)) > 12 or int(getYear(date)) > datetime.datetime.now().year:
            return False
        return True
    else:
        return False


def aptValidation(apartNumber):
    '''
    This function is used to validate an apartment number
    :param apartNumber: - int - the given apartment number
    :return: True/False
    '''
    if representsInt(apartNumber):
        if int(apartNumber) < 1 or int(apartNumber) > 10000:
            return False
        return True
    return False


def typeValidation(typeS):
    '''
    This function is used to validate the type of the spending
    :param typeS: - string - the given type
    :return: True/False
    '''
    if typeS == "alte cheltuieli" or typeS == "canal" or typeS == "intretinere":
        return True
    return False


def valueValidation(value):
    '''
    This function is used to validate the value of a spending
    :param value: - float - the given value
    :return: True/False
    '''
    if representsFloat(value):
        if float(value) <= 0 + EPSILON:
            return False
        return True
    return False


def dictValidation(dictt):
    '''
    This function is used to validate dictionary outputs
    :param dictt: - dictionary
    :return: True/False
    '''
    for key in dictt.keys():
        if dictt[key] is None:
            return False
    return True
