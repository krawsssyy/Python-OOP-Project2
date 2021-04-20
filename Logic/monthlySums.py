from Domain.getter import getApart, getDate, getPrice


def getMonth(date):
    '''
    This function returns the month of a given date
    :param date: - string - the given date
    :return: the month of the given date
    '''
    dateList = date.split("/")
    return dateList[1]


def getYear(date):
    '''
    This function returns the year of a given date
    :param date: - string - the given date
    :return: the year of the given date
    '''
    dateList = date.split("/")
    return dateList[2]


def monthlySums(spendingsList):
    '''
    This function calculates the monthly spendings of every apartment
    :param spendingsList: - list - the list that contains the spendings
    :return: subList - list of lists - a big list that contains small lists in the form of [apartment number, month, total]
    '''
    subList = []
    for index in range(len(spendingsList)):
        currTotal = 0
        currApt = getApart(spendingsList[index])
        currMth = getMonth(getDate(spendingsList[index]))
        currYear = getYear(getDate(spendingsList[index]))
        for index2 in range(index + 1, len(spendingsList), 1):
            if getApart(spendingsList[index2]) == currApt and getMonth(getDate(spendingsList[index2])) == currMth \
                    and getYear(getDate(spendingsList[index2])) == currYear:
                currTotal += getPrice(spendingsList[index2])
        currTotal += getPrice(spendingsList[index])
        currSubList = [currApt, str(currMth) + "/" + str(currYear), currTotal]
        subList.append(currSubList)
    subList = removeDuplicates(subList)
    return subList


def removeDuplicates(lists):
    '''
    This function removes the duplicates from a list in list object based on first and second elements
    :param lists: - list in list
    :return: - lists - the new list in list,with the removed duplicates
    '''
    index = 0
    while index < len(lists):
        currFirst = lists[index][0]
        currSecond = lists[index][1]
        index2 = index + 1
        while index2 < len(lists):
            ok = 0
            if lists[index2][0] == currFirst and lists[index2][1] == currSecond:
                lists.pop(index2)
                ok = 1
            if not ok:
                index2 += 1
        index += 1
    return lists
