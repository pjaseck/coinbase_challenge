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

class Book:
    def __init__(self, bids, asks, sequence, auction_mode, auction, time):
        self.bids = bids
        self.asks = asks
        self.sequence = sequence
        self.auction_mode = auction_mode
        self.auction = auction
        self.time = time
    
    @staticmethod
    def from_json(json_data):
        bids = Order.from_json(json_data['bids'])
        asks = Order.from_json(json_data['asks'])
        return Book(
            bids,
            asks,
            json_data['sequence'],
            json_data['auction_mode'],
            json_data['auction'],
            json_data['time']
        )