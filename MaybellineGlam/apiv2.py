import requests #Importing the requests library for HTTP Request
import json     #Importing the json module 
import csv      #Importing the csv module 


# Make HTTP GET request to the specified URL using the requests library.
api_get = requests.get('http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline')

#Headers to write into CSV file
my_keys= ['key','id', 'brand', 'name', 'price', 'price_sign', 'currency', 'image_link', 'product_link', 'website_link', 'description', 'rating', 'category', 'product_type', 'tag_list', 'created_at', 'updated_at', 'product_api_url', 'api_featured_image']
color_keys=['hex_value1','colour_name1','hex_value2','colour_name','hex_value3','colour_name3','hex_value4','colour_name4','hex_value5','colour_name5','hex_value6','colour_name6','hex_value7','colour_name7','hex_value8','colour_name8','hex_value9','colour_name9','hex_value10','colour_name10','hex_value11','colour_name11','hex_value12','colour_name12']

# Retrieving and storing the json data to 'x' variable
x=api_get.json()

#Creating two empty list 'data' and 'real_colours'
data=[]
real_colours=[]

# Iterating through the elements in 'x' store them in items and appending the values of 'myitems' as a list to 'data'
for myitems in x:
    data.append(list(myitems.values()))

#Creating two empty list 'Data' and 'colours_Cleanup'
Data=[]
colours_Cleanup =[]

#Ceating a variable sizer and assign 0 value to it
sizer=0

# Iterating through 'data' using enumerate to get the index 'i' and store the elements in 'items'
for i, items in enumerate(data):
    #Creating foreign key variable by incrementing the index 'i' by 1
    foreing_key= i+1

    #Creating empty list 'temp_data' and 'temp_colors' to store 'data' and ''colors
    temp_data =[]
    temp_colors=[]

    #Appending 'foreing_key' to 'temp_data' and 'temp_colors'
    temp_data.append(foreing_key)
    temp_colors.append(foreing_key)

    # Iterating through the last element in 'items' list and storing each dictionary in 'things'
    for things in items[len(items)-1]:
    
    # Iterating through the values of 'things' dictionary ans storing eacg value in 'thing' and append values of 'thing' to 'temp_colors' list
        for thing in things.values():       
            temp_colors.append(thing)
    
    #Iterating through the range excluding the last element of 'items' and appending each element to 'temp_data' and then appending 'temp_data' to 'Data'               
    for i in range(len(items)-1):
        temp_data.append(items[i])
    Data.append(temp_data)

    #Updating 'sizer' to the length of 'temp_colors' if it has more elements and Appending 'temp_colors' to colours_cleanup list
    if len(temp_colors)>sizer:
        sizer = len(temp_colors)
    colours_Cleanup.append(temp_colors)
   
    #Iterating through 'colours_Cleanup' using enumerate to get the index 'i' and store the elements in 'items'
for i,items in enumerate(colours_Cleanup):
    #Creating an mepty list 'temp2' and storing the current element from items
    temp2=[]
    temp2=items
    
    #Appending string 'N/A' to 'temp2' list until the length of 'temp2'matches sizer and append the updated 'temp2' to 'real_colours' list
    while len(temp2)<sizer:
        temp2.append("N/A")    
    real_colours.append(temp2)

#Creating an empty list 'wholeFile' and Iterating through 'Data'list using enumerate to get the index 'i' and store the elements in 'whole' and append 'whole'and'real_colours' excluding the first index and store in 'newList'.Append 'newList' to 'wholeFile' list 
wholeFile=[]
for i , whole in enumerate(Data):
    newList=whole+real_colours[i][1:len(real_colours[i])]
    wholeFile.append(newList)

#Creating empty 'my_sizes' list and Iterating through the first element of 'wholeFile' and appending zeros to 'my_sizes'  
my_sizes=[]
for items in wholeFile[1]:
    my_sizes.append(0)
#Iterating through 'wholeFile' and store in 'items', then Iterate through 'items' using enumerate to get the index 'i' and store the elements in 'item' 
for items in wholeFile:
    for i,item in enumerate(items):
         #Store the length of the current item as a string to 'item_size'
        item_size=len(str(item))
        #Checking if the item size is greater than the 'mysizes' at index 'i' (excluding the foreign key) and update 'mysizes' at index 'i' with the new 'item_size'
        if item_size>my_sizes[i] and i > 0:
            my_sizes[i]=item_size

#Assigning heaers to 'xxx' variable 
xxx=my_keys + color_keys 


#Getting column headers along with their datatype, size, attributes, and nullability   
for i,items in enumerate(xxx):
    j=True
    if i < len(my_keys):
        j=False
    #print(f"{items} \t| {type(wholeFile[1][i])} \t| {my_sizes[i]} \t| {j}")

#Using with open method to write a csv file and providing an alias 'data_file' 
with open('products.csv','w',newline='',encoding='utf-8') as data_file:
    #creating a csv writer object 'myFile' that uses 'data_file' to be used as a written file
    myFile= csv.writer(data_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    #wirting the headers (mykeys and colors_keys list) to  'myFile' 
    myFile.writerow(my_keys + color_keys)
    # Using for loop to iterate through 'wholeFile' then store in x and write x to 'myFile' 
    for x in wholeFile:
        myFile.writerow(x)


    


