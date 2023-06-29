 
#import models


# def shop_info(shop): #return the shop name location and rating
#     name = shop.name 
#     rating = shop.rating
#     location = shop.location
#     shop_info = f'{name} is located in {location} and has a rating of {rating}'
#     return shop_info


def select_shop(shoplist): #session to access the db
   #print out the list of shops
   print(shoplist)
   shop = input("Which shop would you like to go to?")
   return shop 

def get_menu(session, shop):

    shop_id = session.query 


    for record in menu:
        print(f'{record.name} is {record.price}')





def cart(session):
    order_list = [] 
    pass



def add_cart(coffee): #Add a coffee to the cart
    pass

def clear_cart():
    pass




def total(session, cart):
    pass
