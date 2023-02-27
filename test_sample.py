from sample import *

def test_single_item_no_fees_no_taxes():
    items = [{"Name": "Nocco", "Price": 50, "Weight": 1, "Quantity": 1}]
    expected = 50
    order = orders(1)
    actual = order.calculate_single_item_no_tax_nofees(items[0])
    assert expected == actual
    
def test_multiple_items_no_fees_no_taxes():
    items = [{"Name": "Nocco", "Price": 50, "Weight": 1, "Quantity": 1},
             {"Name": "Collab", "Price": 40, "Weight": 0.8, "Quantity": 2}]
    expected = 130
    order = orders(1)
    actual = order.calculate_multiple_items_no_tax_no_fees(items)
    assert expected == actual

def test_taxed_order():
    items = [{"Name": "Nocco", "Price": 50, "Weight": 1, "Quantity": 1},
             {"Name": "Collab", "Price": 40, "Weight": 0.8, "Quantity": 2}]
    expected = 234
    order = orders(1)
    actual = order.calculate_taxed_order(items, "USA")
    assert expected == actual