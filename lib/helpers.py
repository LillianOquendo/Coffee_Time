 



def shop_info(shop): #return the shop name location and rating
    name = shop.name 
    rating = shop.rating
    location = shop.location
    shop_info = f'{name} is located in {location} and has a rating of {rating}'
    return shop_info

def filtering(filterby, val): #Generic filter?
    #filterby should rating, location, 

    shops = CoffeeShop.all     #All the coffeeshops

    return [shop_list]


def select_shop(shoplist):
   #for id in shopidlist find the matching one and return the values
   #shop = shop.id
   #name = shop
   #get menu
   pass

def get_menu(shop):
    #get the id of the shop and query the coffee table for rows that have coffeeshop_id match that match
    #return the info to the list
    pass

def cart():
    order_list = [] 
    pass



def add_cart(coffee): #Add a coffee to the cart
    pass

def clear_cart():
    pass




def total(cart):
    total = 0
    for coffee in cart:
        total += coffee.price
    return total
