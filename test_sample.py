from sample import *

def test_single_item_no_fees_no_taxes():
    items = [{"Name": "Nocco", "Price": 50, "Weight": 1, "Quantity": 1}]
    expected = 50
    order = orders(1)
    actual = order.calculate_single_item_no_tax_nofees(items[0])
    assert expected == actual
    
