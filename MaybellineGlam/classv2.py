


'''mykeys=['id','brand', 'name', 'price', 'price_sign', 'currency', 'image_link', 'product_link',       'website_link', 'description', 'rating', 'category','product_type' ]
    product_colors_keys = ['hex_value', 'colour_name']
'''

import csv   #Importing the csv for csv files 

# Creating Prod class
class Prod():
    # Constructor to initialize on an instance being created for the class Prod with list called List_of_products as parameter
    def __init__(self,List_Of_Products):
        #Using try and except block to handle any Index error
        try:
            # Assign the values from List_of_products at given index to the respective attribute of the prod class
            self.id = List_Of_Products[0]
            self.brand = List_Of_Products[1]
            self.name = List_Of_Products[2]
            self.price = List_Of_Products[3]
            self.image_link =List_Of_Products[4]
            self.product_link = List_Of_Products[5]
            self.website_link = List_Of_Products[6]
            self.description = List_Of_Products[7]
            self.rating = List_Of_Products[8]
            self.category = List_Of_Products[9]
            self.product_type = List_Of_Products[10]
            self.hex_value = List_Of_Products[11]
            self.colour_name = List_Of_Products[12]
        except:
            print("An Error Occured")
             
#Creating two empty list        
temp_list = []   
full_list=[]

#Using with open method to open and read a csv file and given an alias myfile 
with open('products.csv','r',newline='') as myfile :
    
    # creating a csv reader object data_file to read the csv file(myfile)
    data_file = csv.reader(myfile)
    
    #Skip the header row
    next(data_file)
    
    #Using for loop to iterate through data_file and store the values in items
    for items in data_file:
        #appending the values in items to temp_list
        temp_list.append(items)
        #Create an instance for the Prod class using items and append it to full_list
        full_list.append(Prod(items))


        
    
#Using for loop to iterate through full_list and store it in Products and checking if the product category is bronzer and printing the name,rating and description if it is true.
for Products in full_list:
    if Products.product_type == 'bronzer':
        print(Products.name,Products.rating)
        
#Printing the value of the hex_value attribute at the index 4 in full_list 
print(full_list[4].hex_value)
        
        
        
    
