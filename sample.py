class orders():
    def __init__(self, price):
        self.price = price
        self.tax = 0.08
        self.shipping = 0.05
    
    def calculate_single_item_no_tax_nofees(self, item):
        return item["Price"] * item["Quantity"]
    
