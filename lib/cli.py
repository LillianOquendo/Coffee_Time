from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Shop, Coffee
from helpers import get_menu

#!/usr/bin/env python3

engine = create_engine('sqlite:///db/coffee_database.db')

session = sessionmaker(bind=engine)()

if __name__ == '__main__':

#CLI structure 
#Welcome to the coffee something
#Where in New York are you located? Ask for which of the 5 buroughs you want
#Do you want to view shops near you or view shops by rating

    print('Hello, Welcome to something coffee')
 
    user_location = input('Which of the 5 boroughs are you located in? ')

    filterby = str(input('Do you want to 1: Go somewhere close  2: Go somewhere nice ?(1,2)'))
    
    filterby_vals = {'1':'location',
                     '2':'rating'}
    
    #Tree.

    if filterby == 1:
         #Go somewhere close scenario. 
         # 1. Get a list of coffee shops in the same burough. Query for shops in by name and get a list of shops
         # 2. Print out the list of shops 
         # 3. User selects a shop on the list

         shop_list = session.query(Shop).filter(Shop.shop_location == user_location)   #list of records where shop location matches the users location.
         print(shop_list)

         for shop in shop_list:  #print out the shops in the list
             print(shop.shop_name)

         selected_shop = input("Which shop from the list would you like to go to? ")

         print(selected_shop)

    elif filterby ==2:
         #Get shops by rating scenario 
         #1. Ask the user what the minumum rating they want
         #2. Get a list of coffee shops with at least that rating. Query for shops bby rating and get a list
         #3. Print out a list of shops
         #4. User selects a shop on the list
        
        rating_wanted = input("Minimum rating (1-5)? ")

        shop_list = session.query(Shop).filter(Shop.rating >= rating_wanted) 

        for shop in shop_list:
            print(shop.shop_name)

        selected_shop = input("Which shop from the list would you like to go to? ")

        print(selected_shop)

    else:
        raise Exception



    print('Here is the menu for the shop you selected')
    #Print out the menu for the shop
    #1. Get the id for the shop
    #2. Look in the shop menu table for all items with the same shop id and put them in a list
    #3. Print out the list with name and price
    #get_menu(session,selected_shop) will be a function to do this 

    shop_id = session.query(Shop.id).filter(selected_shop == Shop.shop_name) #in theory i get back just the id filtering by shop name? i wish i could test this out lfjljlj
    
    coffee_list_id = session.query(Shop_Menu).filter(Shop_Menu.shop_id == shop_id) #Going through the new shop menu table and finding coffee id a list. this new table feels unneccesary and just adds more searching for no reason. Have to know go through this list of coffee id to get the names of the coffee?

    for id in coffee_list_id:
        coffee_record = session.query(Coffee).filter(Coffee.id == id).first()
        print (f'{coffee_record.name} is {coffee_record.price}')
    
     
    tobuy = input('Name of coffee you wish to buy. ') 
    cart = [] #names of all coffes to buy
    cart.append(tobuy)
    

    print('Your total is:')
    total = 0
    for item in cart:
        price = session.query(Coffee.price).filter(item == Coffee.name).first()
        total += price
    
    print(total)

    print('Thank You have a nice day')
