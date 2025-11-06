import os
from django.shortcuts import render #importing render function from django.shortcuts
from django.http import HttpResponse #importing HttpResponse from django.http 
from django.template import loader #importing loader from django.template
from .models import Maybelline #importing the Maybelline model
import pandas as pd  #importing pandas library

#Defining a function called importFromCSV that takes Http request parameter
def importFromCSV(request):
  
  current_dir = os.path.dirname(os.path.abspath(__file__))
  csv_path = os.path.join(current_dir,'data','products1.csv')
  #Reading a Csv file 'products1.csv' using read_csv function in pandas library and store it to dataframe variable and excluding the header row using tail(-1) method
  dataframe = pd.read_csv(csv_path)
  dataframe=dataframe.tail(-1)

  #dataframe = dataframe.iloc[0]['id']
  #print(dataframe)
  
 # for loop to iterate over the range of dataframe length and store it in x variable
  for x in range(len(dataframe)):
    
  #creating an instance of the Maybelline class
    products = Maybelline()
    #Assigning respective values from the dataframe at index location 'x' to the respective attribute of the 'products' instance and save them to the database.
    products.brand = dataframe.iloc[x]['brand']
    products.name = dataframe.iloc[x]['name']
    products.price = dataframe.iloc[x]['price']
    products.image_link = dataframe.iloc[x]['image_link']
    products.product_link = dataframe.iloc[x]['product_link']
    products.website_link = dataframe.iloc[x]['website_link']
    products.description = dataframe.iloc[x]['description']
    products.rating = dataframe.iloc[x]['rating']
    products.category = dataframe.iloc[x]['category']
    products.product_type = dataframe.iloc[x]['product_type']
    products.colour_name = dataframe.iloc[x]['colour_name']

    products.save()
  
  #Return 'Data successfully imported' when the data is stored from the csv file to the database 
  return HttpResponse('Data Successfully imported')

#Defining a function called index that takes Http request parameter
def products(request):
    #Retrieve all 'Maybelline' objects from the database
    products = Maybelline.objects.all()
    #Loading 'index.html' template
    template= loader.get_template('all_products.html')
    #Assigning the context data to be used in the template
    context = {
       'products': products
    }
    # Return the HTTP response of the template with the context data 
    return HttpResponse(template.render(context,request))

#Defining a function called filterByCategory  that takes Http request parameter
def filterByCategory(request):
   
  # Checking and Retrieving the value of the 'product_type' parameter from the GET request and storing in 'search_result' variable
   if 'product_type' in request.GET:
        search_result = request.GET['product_type']

        # Filtering the Maybelline class objects based on the 'product_type' using a case-insensitive search and storing in 'queryset' variable 
        queryset = Maybelline.objects.filter(product_type__icontains=search_result)
        
        #Loading 'search_results.html' template
        template = loader.get_template('search_results.html')

        #Assigning the context data to be used in the template
        context = {
            'products': queryset
        }

        # Return the HTTP response of the template with the context data
        return HttpResponse(template.render(context, request))
   # If the 'product_type' parameter is not present in the GET request,render the 'search_products.html' template
   else:
        return render(request, 'search_products.html')
   

#Defining a function called contact that takes Http request parameter
def contact(request):
    
    #Loading 'contact.html' template
    template= loader.get_template('contact.html')
    #Assigning the context data to be used in the template
    context = {
       'products': template
    }
    # Return the HTTP response of the template with the context data 
    return HttpResponse(template.render(context,request))


#Defining a function called contact that takes Http request parameter
def index(request):
    
    #Loading 'contact.html' template
    template= loader.get_template('index.html')
    #Assigning the context data to be used in the template
    context = {
       'products': template
    }
    # Return the HTTP response of the template with the context data 
    return HttpResponse(template.render(context,request))



    

