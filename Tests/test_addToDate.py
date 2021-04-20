from Logic.add_to_date import addValToDate
from Domain.define import createSpending
from Domain.getter import getPrice


def test_addToDate():
    # This function is used to test the function that adds a value on top of the existing one
    # for a given date
    spending = createSpending(15, 20.0, "15/12/2012", "canal")
    spending2 = createSpending(49, 25.50, "14/11/2014", "intretinere")
    spendingsList = [spending, spending2]
    addValToDate("15/12/2012", 12.25, spendingsList)
    assert getPrice(spendingsList[0]) == 32.25
    assert getPrice(spendingsList[1]) == 25.50
    addValToDate("14/11/2014", 10.50, spendingsList)
    assert getPrice(spendingsList[0]) == 32.25
    assert getPrice(spendingsList[1]) == 36.00


if __name__ == "__main__":
    test_addToDate()
