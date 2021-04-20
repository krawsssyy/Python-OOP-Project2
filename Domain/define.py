from Domain.getter import getApart
from Domain.setter import *


def createSpending(apartNumber, price, date, typeS):
    '''
    This function creates a spending object
    :param apartNumber: - int - the apartment number
    :param price: - float - the value of the spending
    :param date: - string - the date of the spending
    :param typeS: - string - the type of the spending
    :return: spending : - the spending object
    '''
    spending = { "apartNumber":apartNumber,
                 "sum":price,
                 "date":date,
                 "type":typeS}
    return spending


def addSpending(spending,spendingsList):
    '''
    This function adds a spending to a given spending list
    :param spending: - the spending object
    :param spendingsList: - list - the list that contains the spendings
    :return: -
    '''
    spendingsList.append(spending)


def modifySpending(spendingsList, apartNumber, newPrice, newDate, newType):
    '''
    This function modifies a spending to new values
    :param spendingsList: - list - the list that contains the spendings
    :param apartNumber: - int - the apartment number of the spending to be modified
    :param newPrice: - float - the new value of the spending
    :param newDate: -  string - the new date of the spending
    :param newType: - string - the new type of the spending
    :return: -
    '''
    for spending in spendingsList:
        if getApart(spending) == apartNumber:
            setPrice(spending, newPrice)
            setDate(spending, newDate)
            setType(spending, newType)


def removeSpending(apartNumber, spendingsList):
    '''
    This functions removes the spending that has the given apartment number
    :param apartNumber: - int - the apartment number of the spending
    :param spendingsList: - list - the list that contains the spendings
    :return: -
    '''
    for index in range(len(spendingsList)):
        if getApart(spendingsList[index]) == apartNumber:
            spendingsList.pop(index)
            break
