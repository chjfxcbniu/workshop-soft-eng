# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
    
    def test_normal_item_quality_decreases(self):
        items = [Item("Normal Item", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_quality_degrades_twice_after_expired(self):
        items = [Item("Normal Item", 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 8)

    def test_quality_never_negative(self): 
        items = [Item("Normal Item", 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 1)

    def test_aged_brie_increases_quality_twice_after_expired(self):
        items = [Item("Aged Brie", 0, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, -1)

    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_backstage_passes_increase_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)

    def test_backstage_passes_increase_quality_by_2_when_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_passes_increase_quality_by_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

        
if __name__ == '__main__':
    unittest.main()
