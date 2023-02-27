class orders():
    def __init__(self, price):
        self.price = price
        self.tax = 0.08
        self.shipping = 0.05
    
    def calculate_single_item_no_tax_nofees(self, item):
        return item["Price"] * item["Quantity"]
    
    def calculate_multiple_items_no_tax_no_fees(self, items):
        total_cost = 0
        for item in items:
            total_cost += self.calculate_single_item_no_tax_nofees(item)
        return total_cost