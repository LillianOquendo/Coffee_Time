#cli test


print('Hello, Welcome to something coffee')

user_location = input('Which of the 5 boroughs are you located in? ')

filterby = int(input('Do you want to 1: Go somewhere close  2: Go somewhere nice ?(1,2) '))
    
fillterby_vals = {'1':'location',
              '2':'rating'}

Locations = {'queens' : ['Ten Thousand Coffess','PlantShed','Hungry Ghost','Partners Coffee'],

'brooklyn' : ['Bakeri','Butler Bakeshop','Devocion','Maman','Arabica','Masseria','Stumptown Coffee'],

'manhattan' : ['Cafe Grumpy','Kobrick Coffee Company','Felix Roasting Company']}

Ratings = {'5' : ['Bakeri','Maman','Ralphs Coffee'],
'4' : ['Butler Bakeshop','Kobrick Coffee Company','Felix Roasting Company'],
'3' : ['Cafe Grumpy','Arabica','Masseria','Stumptown Coffee'],
'2' : ['Devocion','Plantshed','Partners Coffee'],
'1' : ['Ten Thousand Coffees','Hungry Ghost'] }

if filterby == 1:
    print(Locations[user_location.lower()])
    selected_shop = input('Which Shop from the list woud you like to go to? ')
    print(selected_shop)

if filterby ==2:
    rating_wanted = str(input("Rating (1-5)? "))
    print(Ratings[rating_wanted])
    
    selected_shop = input("Which shop from the list would you like to go to? ")

    print(selected_shop)