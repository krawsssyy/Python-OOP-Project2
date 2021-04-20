from Domain.getter import getApart


def delAllSpendings(apartNumber, spendingsList):
    '''
    This function deletes all the spendings for a given apartment
    :param apartNumber: - int - the apartment number of the wanted spending
    :param spendingsList: - list - the spendings list
    :return: -
    '''
    index = 0
    while index < len(spendingsList):
        ok = 0
        if getApart(spendingsList[index]) == apartNumber:
            spendingsList.pop(index)
            ok = 1
        if not ok:
            index += 1


