class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def adjust_quality(self, item, adjust):
        new_quality = item.quality + adjust
        valid_quality = new_quality >= 0 or new_quality <= 50
        if (valid_quality):
            item.quality = new_quality

    def update_item(self, item):
        AGED_BRIE =  "Aged Brie"
        BACKSTAGE =  "Backstage passes to a TAFKAL80ETC concert"
        SULFURAS = "Sulfuras, Hand of Ragnaros"

        if item.name != AGED_BRIE and item.name != BACKSTAGE:
            if item.name != SULFURAS:
                self.adjust_quality(item, -1)
        else:
            self.adjust_quality(item, 1)
            if item.name == BACKSTAGE:
                if item.sell_in < 11:
                   self.adjust_quality(item, 1)
                if item.sell_in < 6:
                    self.adjust_quality(item, 1)
        if item.name != SULFURAS:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE:
                    if item.name != SULFURAS:
                       self.adjust_quality(item, -1)
                else:
                    item.quality = item.quality - item.quality
            else:
               self.adjust_quality(item, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)