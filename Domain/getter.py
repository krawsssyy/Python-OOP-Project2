def getApart(spending):
    '''
    This function gets the apartment number of a given spending
    :param spending: - the spending object
    :return: - the apartment number of the given spending
    '''
    return spending["apartNumber"]


def getPrice(spending):
    '''
    This function gets the value of a given spending
    :param spending: - the spending object
    :return: - the value of the given spending
    '''
    return spending["sum"]


def getDate(spending):
    '''
    This function gets the date of a given spending
    :param spending: - the spending object
    :return: - the date of the given spending
    '''
    return spending["date"]


def getType(spending):
    '''
    This function gets the type of a given spending
    :param spending: - the spending object
    :return: - the type of the given spending
    '''
    return spending["type"]
