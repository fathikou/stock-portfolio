
class Portfolio:
    def __init__(self):
        self._stocks = []
    def buy(self, stock_name, stock_quantity, stock_price):
        self._stocks.append((stock_name, stock_quantity, stock_price))
    def cost(self):
        return sum(
            stock_quantity * stock_price for stock_name, stock_quantity, stock_price in self._stocks
        )
