from Logic.descending_order import orderDescending
from Domain.define import createSpending


def test_descending():
    # This function is used to test if the descending order function is working properly
    spending = createSpending(40, 500.0, "14/12/2013", "canal")
    spending2 = createSpending(51, 501.0, "15/12/2013", "canal")
    spending3 = createSpending(52, 501.50, "30/12/2014", "intretinere")
    spendingsList = [spending, spending2, spending3]
    orderDescending(spendingsList)
    assert spendingsList == [spending3, spending2, spending]


if __name__ == "__main__":
    test_descending()