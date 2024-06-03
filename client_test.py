import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # for quote in quotes:
    #     stock = quote['stock']
    #     bid_price = quote['top_bid']['price']
    #     ask_price = quote['top_ask']['price']
    #     price = (ask_price + bid_price) / 2
    #     result = getDataPoint(quote)
    #     self.assertEqual(result, (stock, price), f"Failed for stock: {stock}")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
  def test_Ratio(self):
     quotes = [
      {'top_ask': {'price': 119, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 119, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    #  for quote in quotes:
    #     stock = quote['stock']
    #     bid_price = quote['top_bid']['price']
    #     ask_price = quote['top_ask']['price']
    #     ratio = (ask_price/bid_price)
    #     result = getDataPoint(quote)
    #     self.assertEqual(result, (ratio, 1), f"Failed for stock: {ratio}")



if __name__ == '__main__':
    unittest.main()
