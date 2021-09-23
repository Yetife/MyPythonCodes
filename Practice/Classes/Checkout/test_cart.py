from unittest import TestCase

from cart import Cart
from item import Item

class TestCart(TestCase):
    def test_add(self):
        cart = Cart('KIm')
        self.assertEqual(0, len(cart.items))
        item = Item('Pampers', 230, 4)
        cart.add(item)
        self.assertEqual(1, len(cart.items))
 
           
    def test_constructor(self):
        cart = Cart('Kim')
        self.assertEqual("Kim", cart.owner_name)
        
        
    def test_calculate_total_price(self):
        cart = Cart('KIm')
        self.assertEqual(0, len(cart.items))
        item = Item('Pampers', 230, 4)
        cart.add(item)
        self.assertEqual(1, len(cart.items))
        self.assertEqual(160, cart.calculate_total_price())
        