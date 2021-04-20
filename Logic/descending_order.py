from Domain.getter import getPrice


def orderDescending(spendingsList):
    '''
    This functions orders the given list of the spendings in a descending order
    :param spendingsList: - list - the list that contains the spendings
    :return: -
    '''
    for index in range(len(spendingsList)):
        swapped = False
        for index2 in range(0, len(spendingsList) - index - 1):
            if getPrice(spendingsList[index2]) < getPrice(spendingsList[index2 + 1]):
                spendingsList[index2], spendingsList[index2 + 1] = spendingsList[index2 + 1], spendingsList[index2]
                swapped = True
        if not swapped:
            break
