class ShoppingCart:
def __init__(self):
	self.items = []
	self.total_price = 0

def add_item(self, item, price):
	self.items.append((item, price))
	self.total_price += price

def remove_item(self, item):
	for i in range(len(self.items)):
		if self.items[i][0] == item:
			self.total_price -= self.items[i][1]
			del self.items[i]
			return True
	return False

def clear(self):
	self.items = []
	self.total_price = 0

def get_items(self):
	return self.items

def get_total_price(self):
	return self.total_price
