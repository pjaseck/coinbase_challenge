class Order:
    def __init__(self, price, quantity, count):
        self.price = price
        self.quantity = quantity
        self.count = count

    @staticmethod
    def from_json(json_data):
        return Order(
            json_data[0][0],
            json_data[0][1],
            json_data[0][2]
        )
