from obj.order import Order

class ProductBook:
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
        return ProductBook(
            bids,
            asks,
            json_data['sequence'],
            json_data['auction_mode'],
            json_data['auction'],
            json_data['time']
        )
