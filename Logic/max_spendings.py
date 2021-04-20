from Domain.getter import getType, getPrice


def maxSpending(spendingsList, spendingType):
    '''
    This function calculates the biggest spending of a given type
    :param spendingsList: - list - the list that contains the spendings
    :param spendingType: - string - the type of the given spendings
    :return: maxValue: - float - the maximum value of the spendings with the given type
    '''
    maxValue = -1
    for spending in spendingsList:
        if getType(spending) == spendingType:
            if getPrice(spending) > maxValue:
                maxValue = getPrice(spending)
    return maxValue
