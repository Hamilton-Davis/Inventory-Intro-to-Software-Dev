class Item:
    def __init__(self, name, stock, sales, access, order):
        self.name = name
        self.stock = stock
        self.sales = sales
        self.access = access
        self.order = order

item = Item("Pumpkin Spice Candles",
            32,
            15,
            True,
            "https://www.etsy.com/listing/1482214698/pumpkin-spice-soy-candle-pumpkin-maple?ga_order=most"
            "_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=pumpkin+spice+candle&ref=sr_gallery"
            "-1-2&frs=1&content_source=839d2fa207add2501003a7398c3a02478c65a35a%253A1482214698&organic_search_click=1" )

print("The item,", item.name ,"is currently ", end='')

if item.access:
    print("in stock.")