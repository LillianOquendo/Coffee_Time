from helpers import filtering
#!/usr/bin/env python3

if __name__ == '__main__':

#CLI structure 
#Welcome to the coffee something
#Where in New York are you located? Ask for which of the 5 buroughs you want
#What type of coffee are you interested in 

    print('Hello, Welcome to something coffee')
 
    user_location = input('Which of the 5 boroughs are you located in? ')
    print(user_location)
 
    filterby = input('Do you want to 1: Go somewhere close  2: Want a specific drink  3: View shops by rating  ?(1,2,3)')
    filterby_vals = {1:'location',
                     2:'filter',
                     3:'rating'}
    
    value = input("coffee name? or something")

    def cont():
        if filterby == 1:
            print('Here are the coffee shops listed in your borough')
            #return list of shops
        if filterby ==2:
            pass
        if filterby ==3:
            print('Here is a list of coffee shops with the minimum rating')
            #return a list of shops
            print('Which shop would you like to go to')
            print('Here is the menu for your shop')
            print('see total items')
            print('Your total is ... have a good day!')
            pass
        else:
            raise Exception

    outlist = filtering(filterby_vals[filterby],value)



    #function filter coffeeshops
    print('Here are some possible shops')
    #Print the outlist
    print('Here are the shops closest to you')


 
