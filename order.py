class Order:
    def __init__(self, order_id, customer, items):
        """Initializes an order object with an Order ID, customer, and items"""
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = "PENDING"  # Default status is PENDING

    def get_id(self):
        """Returns the order id as a string"""
        return f"{self.order_id}"

    def get_customer(self):
        """Returns the customer Customer object"""
        return self.customer

    def get_items(self):
        """Returns the items in the order as a list of Product objects"""
        return self.items

    def get_status(self):
        """Returns the currentstatus of the order as a string"""
        return self.status

    def set_status(self, status):
        """Sets the status of the order to a new value"""
        statuses = ["PENDING", "PROCESSING", "COMPLETED"]
        if status not in statuses:
            raise ValueError(f"Invalid status: {status}. Valid statuses are: {statuses}")
        else:
            self.status = status

    def calculate_total(self):
        """Calculates the total price of the order by summing the prices of all items"""
        total = sum(item.get_price() for item in self.items)
        return total