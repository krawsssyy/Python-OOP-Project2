from Logic.max_spendings import maxSpending
from Domain.define import createSpending


def test_maxSpending():
    spending = createSpending(40, 500.0, "14 / 12 / 2013", "canal")
    spending2 = createSpending(51, 501.0, "15 / 12 / 2013", "canal")
    spending3 = createSpending(52, 501.50, "30 / 12 / 2014", "intretinere")
    spending4 = createSpending(49, 499.0, "14 / 12 / 2013", "canal")
    spending5 = createSpending(51, 502.0, "15 / 12 / 2013", "alte cheltuieli")
    spending6 = createSpending(52, 502.50, "30 / 12 / 2014", "alte cheltuieli")
    spendingsList = [spending, spending2, spending3, spending4, spending5, spending6]
    maxcanal = maxSpending(spendingsList, "canal")
    maxalte = maxSpending(spendingsList, "alte cheltuieli")
    maxintre = maxSpending(spendingsList, "intretinere")
    assert maxcanal == 501.0
    assert maxalte == 502.50
    assert maxintre == 501.50


if __name__ == "__main__":
    test_maxSpending()