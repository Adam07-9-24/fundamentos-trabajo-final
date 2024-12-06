class Receipt:
    def __init__(self, receipt_id, customer_name, pizza_type, quantity, total_price):
        self._id = receipt_id
        self._customer_name = customer_name
        self._pizza_type = pizza_type
        self._quantity = quantity
        self._total_price = total_price

    def get_details(self):
        return {
            "id": self._id,
            "customer_name": self._customer_name,
            "pizza_type": self._pizza_type,
            "quantity": self._quantity,
            "total_price": self._total_price,
        }

    def update(self, customer_name=None, pizza_type=None, quantity=None, total_price=None):
        if customer_name:
            self._customer_name = customer_name
        if pizza_type:
            self._pizza_type = pizza_type
        if quantity:
            self._quantity = quantity
        if total_price:
            self._total_price = total_price
