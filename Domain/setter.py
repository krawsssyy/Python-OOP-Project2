def setPrice(spending, newPrice):
    '''
    This function modifies the price of a spending
    :param spending: - the spending object
    :param newPrice: - float - the new price
    :return: -
    '''
    spending["sum"] = newPrice


def setDate(spending, newDate):
    '''
    This function modifies the date of a spending
    :param spending: - the spending object
    :param newDate: - string - the new date
    :return: -
    '''
    spending["date"] = newDate


def setType(spending, newType):
    '''
    This function modifies the type of a spending
    :param spending: - the spending object
    :param newType: - string - the new type
    :return: -
    '''
    spending["type"] = newType
