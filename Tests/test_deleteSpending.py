from Domain.define import createSpending
from Logic.delete_spendings import delAllSpendings


def test_delAll():
    # This function tests if all the spendings will be deleted
    spending = createSpending(49, 200.0, "11/11/2012", "alte cheltuieli")
    spending2 = createSpending(50, 100.0, "12/12/2012", "canal")
    spending3 = createSpending(49, 150.0, "15/12/2014", "intretinere")
    spendingsList = [spending, spending2, spending3]
    delAllSpendings(49, spendingsList)
    assert len(spendingsList) == 1
    delAllSpendings(50, spendingsList)
    assert len(spendingsList) == 0


if __name__ == "__main__":
    test_delAll()