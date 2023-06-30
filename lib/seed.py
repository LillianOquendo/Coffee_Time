from app import app
from models import db, Coffee, Shop, Bean, ShopMenu, Location


if __name__ == "__main__":
    with app.app_context():
##Coffee Data
        coffee1 = Coffee(
            name='Cafe Bustelo',
            roast='Dark Roast',
            coarse_vs_fine=True,
            price=17.25
        )
        db.session.add(coffee1)
        
        coffee2 = Coffee(
            name='LavAzza',
            roast='Medium-Dark Roast',
            coarse_vs_fine= False,
            price=6.99
        )
        coffee3 = Coffee(
            name='Maxwell House',
            roast='Light Roast',
            coarse_vs_fine= True,
            price=7.99
        )
        coffee4 = Coffee(
            name='Folgers',
            roast='Medium Roast',
            coarse_vs_fine= False,
            price=21.99
        )
        coffee5 = Coffee(
            name='Illy Caffe',
            roast='Light Roast',
            coarse_vs_fine= True,
            price=10.99
        )
        coffee6 = Coffee(
            name='Peets Coffee',
            roast='Medium Roast',
            coarse_vs_fine= False,
            price=44.99
        )
        coffee7 = Coffee(
            name='Cafe Rico',
            roast='Dark Roast',
            coarse_vs_fine= True,
            price=6.99
        )
        coffee8 = Coffee(
            name='Devil Mountain',
            roast='Dark Roast',
            coarse_vs_fine= False,
            price=21.99
        )
        db.session.add(coffee2)
        coffee9 = Coffee(
            name='LavAzza',
            roast='Medium-Dark Roast',
            coarse_vs_fine= False,
            price=17.25
        )
        coffee10 = Coffee(
            name='Breakfast Blend',
            roast='Medium Roast',
            coarse_vs_fine= True,
            price=6.99
        )

##Coffee Shop Data
        coffee_shop1= Shop(
            shop_name = 'Bakeri',
            shop_location = 'Brooklyn',
            rating = '5'
        )
        coffee_shop2= Shop(
            shop_name = 'Cafe Grumpy',
            shop_location = 'Manhattan',
            rating = '3'
        )
        coffee_shop3= Shop(
            shop_name = 'Ten Thousand Coffees',
            shop_location = 'Queens',
            rating = '1'
        )
        coffee_shop4= Shop(
            shop_name = 'Butler Bakeshop',
            shop_location = 'Brooklyn',
            rating = '4'
        )
        coffee_shop5= Shop(
            shop_name = 'Devocion',
            shop_location = 'Brooklyn',
            rating = '2'
        )
        coffee_shop6= Shop(
            shop_name = 'Kobrick Coffee Company',
            shop_location = 'Manhattan',
            rating = '4'
        )
        coffee_shop7= Shop(
            shop_name = 'Maman',
            shop_location = 'Brooklyn',
            rating = '5'
        )
        coffee_shop8= Shop(
            shop_name = 'Arabica',
            shop_location = 'Brooklyn',
            rating = '3'
        )
        coffee_shop9= Shop(
            shop_name = 'Felix Roasting Company',
            shop_location = 'Manhattan',
            rating = '4'
        )
        coffee_shop10= Shop(
            shop_name = 'PlantShed',
            shop_location = 'Queens',
            rating = '2'
        )
        coffee_shop11= Shop(
            shop_name = 'Masseria',
            shop_location = 'Brooklyn',
            rating = '5'
        )
        coffee_shop12= Shop(
            shop_name = 'Hungry Ghost',
            shop_location = 'Queens',
            rating = '1'
        )
        coffee_shop13= Shop(
            shop_name = 'Ralphs Coffee',
            shop_location = 'Queens',
            rating = '5'
        )
        coffee_shop14= Shop(
            shop_name = 'Stumptown Coffee',
            shop_location = 'Brooklyn',
            rating = '3'
        )
        coffee_shop15= Shop(
            shop_name = 'Partners Coffee',
            shop_location = 'Queens',
            rating = '2'
        )

##Bean data
        bean1 = Bean(
            bean_type = 'Coffea arabica',
            location = 'Colombia',
            flavor_profile = 'Chocolatey, spicy, floral, caramelly, bright acidity.'
        )
        bean2 = Bean(
            bean_type = 'Typica',
            location = 'Dominican Republic',
            flavor_profile = 'Lemon and floral notes with a sweet aftertaste.'
        )
        bean1 = Bean(
            bean_type = 'Robusta',
            location = 'Venezuela',
            flavor_profile = 'Dark chocolate, nuts like almonds, and whiskey. Little to no acidity.'
        )
        bean1 = Bean(
            bean_type = 'Kopi luwak',
            location = 'Puerto Rico',
            flavor_profile = 'Earthy and musty with hints of caramel and chocolate.'
        )
        bean1 = Bean(
            bean_type = 'Coffea liberica',
            location = 'Cuba',
            flavor_profile = 'Smoky, nutty, floral with hints of dark chocolate, ripe berry and spice.'
        )
##Shop Menu Data
        menu_item1 = ShopMenu(
            shop_id = 1,
            coffee_id = 4
        )
        menu_item2 = ShopMenu(
            shop_id = 1,
            coffee_id = 3
        )
        menu_item3 = ShopMenu(
            shop_id = 1,
            coffee_id = 6
        )
        menu_item4 = ShopMenu(
            shop_id = 1,
            coffee_id = 2
        )
        menu_item5 = ShopMenu(
            shop_id = 2,
            coffee_id = 5
        )
        menu_item6 = ShopMenu(
            shop_id = 2,
            coffee_id = 7
        )
        menu_item7 = ShopMenu(
            shop_id = 2,
            coffee_id = 9
        )
        menu_item8 = ShopMenu(
            shop_id = 2,
            coffee_id = 10
        )
        menu_item9 = ShopMenu(
            shop_id = 3,
            coffee_id = 1
        )
        menu_item10 = ShopMenu(
            shop_id = 3,
            coffee_id = 3
        )
        menu_item11 = ShopMenu(
            shop_id = 3,
            coffee_id = 2
        )
        menu_item12 = ShopMenu(
            shop_id = 3,
            coffee_id = 5
        )
        menu_item13 = ShopMenu(
            shop_id = 4,
            coffee_id = 8
        )
        menu_item14 = ShopMenu(
            shop_id = 4,
            coffee_id = 9
        )
        menu_item15 = ShopMenu(
            shop_id = 4,
            coffee_id = 4
        )
        menu_item16 = ShopMenu(
            shop_id = 4,
            coffee_id = 6
        )
        menu_item17 = ShopMenu(
            shop_id = 5,
            coffee_id = 8
        )
        menu_item18 = ShopMenu(
            shop_id = 5,
            coffee_id = 4
        )
        menu_item19 = ShopMenu(
            shop_id = 5,
            coffee_id = 3
        )
        menu_item20 = ShopMenu(
            shop_id = 5,
            coffee_id = 1
        )
        menu_item21 = ShopMenu(
            shop_id = 6,
            coffee_id = 3
        )
        menu_item22 = ShopMenu(
            shop_id = 6,
            coffee_id = 2
        )
        menu_item23 = ShopMenu(
            shop_id = 6,
            coffee_id = 10
        )
        menu_item24 = ShopMenu(
            shop_id = 6,
            coffee_id = 8
        )
        menu_item25 = ShopMenu(
            shop_id = 7,
            coffee_id = 9
        )
        menu_item26 = ShopMenu(
            shop_id = 7,
            coffee_id = 7
        )
        menu_item27 = ShopMenu(
            shop_id = 7,
            coffee_id = 6
        )
        menu_item28 = ShopMenu(
            shop_id = 7,
            coffee_id = 2
        )
        menu_item29 = ShopMenu(
            shop_id = 8,
            coffee_id = 1
        )
        menu_item30 = ShopMenu(
            shop_id = 8,
            coffee_id = 3
        )
        menu_item31 = ShopMenu(
            shop_id = 8,
            coffee_id = 4
        )
        menu_item32 = ShopMenu(
            shop_id = 8,
            coffee_id = 7
        )
        menu_item33 = ShopMenu(
            shop_id = 9,
            coffee_id = 2
        )
        menu_item34 = ShopMenu(
            shop_id = 9,
            coffee_id = 5
        )
        menu_item35 = ShopMenu(
            shop_id = 9,
            coffee_id = 8
        )
        menu_item36 = ShopMenu(
            shop_id = 9,
            coffee_id = 6
        )
        menu_item37 = ShopMenu(
            shop_id = 10,
            coffee_id = 3
        )
        menu_item38 = ShopMenu(
            shop_id = 10,
            coffee_id = 7
        )
        menu_item39 = ShopMenu(
            shop_id = 10,
            coffee_id = 9
        )
        menu_item40 = ShopMenu(
            shop_id = 10,
            coffee_id = 10
        )
        menu_item41 = ShopMenu(
            shop_id = 11,
            coffee_id = 4
        )
        menu_item42 = ShopMenu(
            shop_id = 11,
            coffee_id = 3
        )
        menu_item43 = ShopMenu(
            shop_id = 11,
            coffee_id = 2
        )
        menu_item44 = ShopMenu(
            shop_id = 11,
            coffee_id = 1
        )
        menu_item45 = ShopMenu(
            shop_id = 12,
            coffee_id = 5
        )
        menu_item46 = ShopMenu(
            shop_id = 12,
            coffee_id = 6
        )
        menu_item47 = ShopMenu(
            shop_id = 12,
            coffee_id = 7
        )
        menu_item48 = ShopMenu(
            shop_id = 12,
            coffee_id = 8
        )
        menu_item49 = ShopMenu(
            shop_id = 13,
            coffee_id = 10
        )
        menu_item50 = ShopMenu(
            shop_id = 13,
            coffee_id = 9
        )
        menu_item51 = ShopMenu(
            shop_id = 13,
            coffee_id = 1
        )
        menu_item52 = ShopMenu(
            shop_id = 13,
            coffee_id = 2
        )
        menu_item53 = ShopMenu(
            shop_id = 14,
            coffee_id = 3
        )
        menu_item54 = ShopMenu(
            shop_id = 14,
            coffee_id = 4
        )
        menu_item55 = ShopMenu(
            shop_id = 14,
            coffee_id = 5
        )
        menu_item56 = ShopMenu(
            shop_id = 14,
            coffee_id = 6
        )
        menu_item57 = ShopMenu(
            shop_id = 15,
            coffee_id = 7
        )
        menu_item58 = ShopMenu(
            shop_id = 15,
            coffee_id = 8
        )
        menu_item59 = ShopMenu(
            shop_id = 15,
            coffee_id = 9
        )
        menu_item60 = ShopMenu(
            shop_id = 15,
            coffee_id = 10
        )
        ##Location Data
        location1 = Location('Colombia')

        location2 = Location('Dominican Republic')

        location3 = Location('Venezuela')

        location4 = Location('Puerto Rico')

        location5 = Location('Cuba')

        location6 = Location('Queens')

        location7 = Location('Brooklyn')

        location8 = Location('Manhattan')
        
        db.session.commit()