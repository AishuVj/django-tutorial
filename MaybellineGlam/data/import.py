import pandas as pd
from models import Maybelline

dataframe = pd.read_csv('/Users/ishuvijay/Documents/djangotutorial/makeup_products/MaybellineGlam/data/products1.csv',encoding='latin1')
dataframe=dataframe.tail(-1)

#dataframe = dataframe.iloc[0]['id']
#print(dataframe)
products = Maybelline()

products.brand = dataframe.iloc[0]['brand']
products.name = dataframe.iloc[0]['name']
products.price = dataframe.iloc[0]['price']
products.image_link = dataframe.iloc[0]['image_link']
products.product_link = dataframe.iloc[0]['product_link']
products.website_link = dataframe.iloc[0]['website_link']
products.description = dataframe.iloc[0]['description']
products.rating = dataframe.iloc[0]['rating']
products.category = dataframe.iloc[0]['category']
products.product_type = dataframe.iloc[0]['product_type']
products.colour_name = dataframe.iloc[0]['colour_name']

print(products)






