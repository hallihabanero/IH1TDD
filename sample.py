class orders():
    def __init__(self, price):
        self.price = price
        self.tax = {
            "USA": 0.8,
            "Panama": 0.0,
            "Iceland": 2.8
        }
        self.shipping = 0.05
    
    def calculate_single_item_no_tax_nofees(self, item):
        return item["Price"] * item["Quantity"]
    
    def calculate_multiple_items_no_tax_no_fees(self, items):
        total_cost = 0
        for item in items:
            total_cost += self.calculate_single_item_no_tax_nofees(item)
        return total_cost
    
    def calculate_taxed_order(self, items, location):
        total_cost = self.calculate_multiple_items_no_tax_no_fees(items)
        for i in self.tax:
            if location == i:
                total_cost += total_cost * self.tax[i]
        return total_cost
