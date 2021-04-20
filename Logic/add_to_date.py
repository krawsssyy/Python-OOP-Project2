from Domain.getter import getDate, getPrice
from Domain.setter import setPrice


def addValToDate(givenDate, value, spendingsList):
    '''
    This functions adds a given value to all the spendings from a given date
    :param givenDate: - string - the given date of the spendings
    :param value: - float - the value to be added to the spendings
    :param spendingsList: - list - the list that contains the spendings
    :return: -
    '''
    for spending in spendingsList:
        if getDate(spending) == givenDate:
            setPrice(spending, getPrice(spending) + value)
