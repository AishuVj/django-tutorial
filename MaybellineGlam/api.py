

import requests  #Importing the requests library for HTTP Request
import json      #Importing the json for json data
import csv       #Importing the json for json data
'''def check_size(x,y):
    sizer=int(y)
    if len(x)>y:
        sizer=len(x)
    return sizer'''
# Retriving the data from the API using get request and storing in a variable api_get
api_get = requests.get('http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline')

# Retriving and storing the json data to x variable
x = api_get.json()

#mykeys variable contains the list of the keys to retrive from the API 
mykeys = ['id', 'brand', 'name', 'price', 'price_sign', 'currency', 'image_link', 'product_link', 'website_link', 'description', 'rating', 'category', 'product_type', 'tag_list', 'created_at', 'updated_at', 'product_api_url', 'api_featured_image']

#product_colors_keys variable contains the list of the keys to retrive from the API 
product_colors_keys = ['hex_value', 'colour_name']

#creating an empty list called data
data = []

#for loop to iterate through values in x and store in items
for items in x:
    temp1=[] #Creating an empty temp1 list
    
    #for loop to iterate in the range of 'mykeys' length by incrementing
    for i in range(0,len(mykeys)):
        # Retrieving the values associated with mykeys[i] from items  and appending to temp1.
       temp1.append(items[mykeys[i]])
    
    #Creating a empty list called full_colors
    full_colors =[]
    
    # Retriving the values of product_colors key from items and storing in the list full_colors.
    full_colors = items['product_colors']
    
    #for loop to iterate through full_colors list and store it in color
    for color in full_colors:
        #Creating a empty list and looping in the range of product_colors_keys length by incrementing
        temp2=[]
        for i in range(0,len(product_colors_keys)):
            # Retrieving the values associated with product_colors_keys[i] from color and appending to temp2.
            temp2.append(color[product_colors_keys[i]])
        
        #concatenate temp1 and temp2 list and store in row list and append the row to data list
        row =[]
        row = temp1 + temp2
        data.append(row)

#Using with open method to write a csv file and providing an alias data_file 
with open('pro.csv', mode='w', newline='',encoding='utf-8') as data_file:
    
    #creating a csv writer object myfile that uses data_file to be used as a written file
    myFile = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    #wirting the headers (mykeys and product_colors_keys list) to  myfile 
    myFile.writerow(mykeys + product_colors_keys)
    
    # Using for loop to iterate through data list then store in x and write x to myfile 
    for x in data:
        myFile.writerow(x)
    
    
