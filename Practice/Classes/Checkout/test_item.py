from unittest import TestCase

from item import Item

class TestItem(TestCase):
    def test_calculate_total(self):
        # given
        item = Item(100, 2)
        # when
        total = item.calculate_total()
        # assert
        self.assertEqual(200, total)
        

        