from django.urls import path #import path from django.urls module
from .import views #import views module for the current directory

#urlpattens list contains the path for respective functions defined in views.py
urlpatterns=[
    #URL path for importing the data from a csv file using importingFromCsv function
    path('MaybellineGlam/import-data',views.importFromCSV,name='importData'),
    #URL path to load index page using index function 
    path('MaybellineGlam/index', views.index, name='index'),
    #URL path to load search_products page using filterByCategory function
    path('MaybellineGlam/search_products', views.filterByCategory, name='searchProducts'),
    #URL path to load contact page using contact function 
    path('MaybellineGlam/contact', views.contact, name='contact'),
    path('MaybellineGlam/index/search-products/', views.filterByCategory, name='search_products'),
    path('MaybellineGlam/all-products/', views.products, name='allProducts'),

]
