class Order:
    """
    A class used to represent an order details.

    Attributes
    ----------
    price : float
        the price of the transaction (buy or sell)
    quantity : float
        a quantity of the product that can be purchased/selled for the price
    count : float
        a number of transactions at this price level

    Methods
    -------
    from_json
        Converts response in json file into callable Order object.

    """
    def __init__(self, price, quantity, count):
        """
        Parameters
        ----------
        price : float
            the price of the transaction (buy or sell)
        quantity : float
            a quantity of the product that can be purchased/selled for the price
        count : float
            a number of transactions at this price level
        """
        self.price = price
        self.quantity = quantity
        self.count = count

    @staticmethod
    def from_json(json_data):
        """Converts a list of order parameters into Order object.

        Parameters
        ----------
        json_data : list
            A list containing order data in JSON format.
        
        Returns
        -------
        class
            Order object
        """
        return Order(
            json_data[0][0],
            json_data[0][1],
            json_data[0][2]
        )
