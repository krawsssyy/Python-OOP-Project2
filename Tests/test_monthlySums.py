from Logic.monthlySums import monthlySums
from Domain.define import createSpending


def test_monthly():
    # This function is used to test the monthlysums function
    spending = createSpending(40, 500.0, "14 / 11 / 2013", "canal")
    spending2 = createSpending(51, 501.0, "14 / 12 / 2013", "canal")
    spending3 = createSpending(52, 501.50, "30 / 12 / 2014", "intretinere")
    spending4 = createSpending(52, 499.0, "14 / 12 / 2013", "canal")
    spending5 = createSpending(51, 502.0, "15 / 12 / 2013", "alte cheltuieli")
    spending6 = createSpending(40, 502.50, "30 / 12 / 2014", "alte cheltuieli")
    spendingsList = [spending, spending2, spending3, spending4, spending5, spending6]
    result = monthlySums(spendingsList)
    assert result == [[40, ' 11 / 2013', 500.0], [51, ' 12 / 2013', 1003.0], [52, ' 12 / 2014', 501.5],
                      [52, ' 12 / 2013', 499.0], [40, ' 12 / 2014', 502.5]]


if __name__ == "__main__":
    test_monthly()