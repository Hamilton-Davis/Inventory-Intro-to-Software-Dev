import pandas as pd
import datetime
import xlwt
import openpyxl

# class Item:
#    def __init__(self, name, stock, sales, access, order):
 #       self.name = name
  #      self.stock = stock
   #     self.sales = sales
    #    self.access = access
     #   self.order = order


#item = Item("Pumpkin Spice Candles",
 #           32,
  #          15,
   #         True,
    #        "https://www.etsy.com/listing/1482214698/pumpkin-spice-soy-candle-pumpkin-maple?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=pumpkin+spice+candle&ref=sr_gallery-1-2&frs=1&content_source=839d2fa207add2501003a7398c3a02478c65a35a%253A1482214698&organic_search_click=1")


df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)
current_time = datetime.datetime.now()
print("Year :", current_time.year)

print("Month : ", current_time.month)

print("Day : ", current_time.day)
month = str(current_time.month)
day = str(current_time.day),'-'
year = str(current_time.year)
print(month)
print(day)
print(year)

date = month+day+year
print(date)
#df.to_excel('pandas_to_excel.xlsx', sheet_name='')