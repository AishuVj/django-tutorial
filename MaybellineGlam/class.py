import csv #Importing the csv module 

#Creating empty list 'full_list'     
full_list=[]

# Creating Products class and a Constructor to initialize on an instance being created for the class 'Products' with list called 'List_of_products' as parameter
class Products():
    def __init__(self,List_of_products):
        # Assign the values from 'List_of_products' at given index to the respective attribute of the 'Products' class
        self.id = List_of_products[0]
        self.brand = List_of_products[1]
        self.name = List_of_products[2]
        self.price = List_of_products[3]
        self.image_link = List_of_products[4]
        self.product_link = List_of_products[5]
        self.website_link = List_of_products[6]
        self.description = List_of_products[7]
        self.rating = List_of_products[8]
        self.category = List_of_products[9]
        self.product_type = List_of_products[10]       
        self.api_featured_image = List_of_products[11]

#Using with open method to open and read a csv file and given an alias 'my_file'
with open('products.csv','r',newline='') as my_file:
    #Using try and except to catch any errors when reading the csv file
    try:
        # creating a csv reader object 'reader' to read the csv file(my_file)
        reader = csv.reader(my_file,delimiter=',')
        #Creating 'counter' variable and assigning 0 value to it 
        counter=0
        #Iterating through each item in the 'reader' and store in 'items'
        for items in reader:
            #If counter is not 0 create an empty'temp_data' list and Iterate through the items starting from index 1 and append specific index data to 'temp_data'
            if counter!=0:
                temp_data=[]
                for i in range(1,len(items)):
                    if i in[1,2,3,4,7,8,9,10,11,12,13,19]:
                        temp_data.append(items[i])
            #Create an instance for the 'Products' class using 'temp_data' and append it to full_list
                full_list.append(Products(temp_data))
            # Set the counter to 1 after the first iteration
            counter=1
    except:
        print("Error while reading the CSV file:")
#Iterating through 'full_list' and store it in 'x' and checking if the product_type is bronzer and printing the name,rating if it is true.
for x in full_list:
    if x.product_type =='bronzer':
        print(x.name,x.rating)
#print(full_list[3].product_type)
    
        

       