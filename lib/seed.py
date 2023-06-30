from app import app
from models import db, Coffee, Shop, Location, Bean, ShopMenu


if __name__ == "__main__":
    with app.app_context():
##Coffee Data
        coffees = [
            Coffee(
                name='Cafe Bustelo',
                roast='Dark Roast',
                coarse_vs_fine=True,
                price=17.25
            ),
            Coffee(
                name='LavAzza',
                roast='Medium-Dark Roast',
                coarse_vs_fine= False,
                price=6.99
            ),
            Coffee(
                name='Maxwell House',
                roast='Light Roast',
                coarse_vs_fine= True,
                price=7.99
            ),
            Coffee(
                name='Folgers',
                roast='Medium Roast',
                coarse_vs_fine= False,
                price=21.99
            ),
            Coffee(
                name='Illy Caffe',
                roast='Light Roast',
                coarse_vs_fine= True,
                price=10.99
            ),
            Coffee(
                name='Peets Coffee',
                roast='Medium Roast',
                coarse_vs_fine= False,
                price=44.99
            ),
            Coffee(
                name='Cafe Rico',
                roast='Dark Roast',
                coarse_vs_fine= True,
                price=6.99
            ),
            Coffee(
                name='Devil Mountain',
                roast='Dark Roast',
                coarse_vs_fine= False,
                price=21.99
            ),
            Coffee(
                name='LavAzza',
                roast='Medium-Dark Roast',
                coarse_vs_fine= False,
                price=17.25
            ),
            Coffee(
                name='Breakfast Blend',
                roast='Medium Roast',
                coarse_vs_fine= True,
                price=6.99
            )
        ]

##Coffee Shop Data
        shops = [
            Shop(
                shop_name = 'Bakeri',
                shop_location_id = 7,
                rating = '5'
            ),
            Shop(
                shop_name = 'Cafe Grumpy',
                shop_location_id = 8,
                rating = '3'
            ),
            Shop(
                shop_name = 'Ten Thousand Coffees',
                shop_location_id = 6,
                rating = '1'
            ),
            Shop(
                shop_name = 'Butler Bakeshop',
                shop_location_id = 7,
                rating = '4'
            ),
            Shop(
                shop_name = 'Devocion',
                shop_location_id = 7,
                rating = '2'
            ),
            Shop(
                shop_name = 'Kobrick Coffee Company',
                shop_location_id = 8,
                rating = '4'
            ),
            Shop(
                shop_name = 'Maman',
                shop_location_id = 7,
                rating = '5'
            ),
            Shop(
                shop_name = 'Arabica',
                shop_location_id = 7,
                rating = '3'
            ),
            Shop(
                shop_name = 'Felix Roasting Company',
                shop_location_id = 8,
                rating = '4'
            ),
            Shop(
                shop_name = 'PlantShed',
                shop_location_id = 6,
                rating = '2'
            ),
            Shop(
                shop_name = 'Masseria',
                shop_location_id = 7,
                rating = '5'
            ),
            Shop(
                shop_name = 'Hungry Ghost',
                shop_location_id = 6,
                rating = '1'
            ),
            Shop(
                shop_name = 'Ralphs Coffee',
                shop_location_id = 6,
                rating = '5'
            ),
            Shop(
                shop_name = 'Stumptown Coffee',
                shop_location_id = 7,
                rating = '3'
            ),
            Shop(
                shop_name = 'Partners Coffee',
                shop_location_id = 6,
                rating = '2'
            )
        ]
# ##Bean data
        beans = [
            Bean(
                bean_type = 'Coffea arabica',
                location = 1,
                flavor_profile = 'Chocolatey, spicy, floral, caramelly, bright acidity.'
            ),
            Bean(
                bean_type = 'Typica',
                location = 2,
                flavor_profile = 'Lemon and floral notes with a sweet aftertaste.'
            ),
            Bean(
                bean_type = 'Robusta',
                location = 3,
                flavor_profile = 'Dark chocolate, nuts like almonds, and whiskey. Little to no acidity.'
            ),
            Bean(
                bean_type = 'Kopi luwak',
                location = 4,
                flavor_profile = 'Earthy and musty with hints of caramel and chocolate.'
            ),
            Bean(
                bean_type = 'Coffea liberica',
                location = 5,
                flavor_profile = 'Smoky, nutty, floral with hints of dark chocolate, ripe berry and spice.'
            )
        ]

# ##Shop Menu Data
        menus = [
            ShopMenu(
                shop_id = 1,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 1,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 1,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 1,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 2,
                coffee_id = 5
            ),
            ShopMenu(
                shop_id = 2,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 2,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 2,
                coffee_id = 10
            ),
            ShopMenu(
                shop_id = 3,
                coffee_id = 1
            ),
            ShopMenu(
                shop_id = 3,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 3,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 3,
                coffee_id = 5
            ),
            ShopMenu(
                shop_id = 4,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 4,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 4,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 4,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 5,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 5,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 5,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 5,
                coffee_id = 1
            ),
            ShopMenu(
                shop_id = 6,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 6,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 6,
                coffee_id = 10
            ),
            ShopMenu(
                shop_id = 6,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 7,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 7,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 7,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 7,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 8,
                coffee_id = 1
            ),
            ShopMenu(
                shop_id = 8,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 8,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 8,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 9,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 9,
                coffee_id = 5
            ),
            ShopMenu(
                shop_id = 9,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 9,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 10,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 10,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 10,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 10,
                coffee_id = 10
            ),
            ShopMenu(
                shop_id = 11,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 11,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 11,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 11,
                coffee_id = 1
            ),
            ShopMenu(
                shop_id = 12,
                coffee_id = 5
            ),
            ShopMenu(
                shop_id = 12,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 12,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 12,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 13,
                coffee_id = 10
            ),
            ShopMenu(
                shop_id = 13,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 13,
                coffee_id = 1
            ),
            ShopMenu(
                shop_id = 13,
                coffee_id = 2
            ),
            ShopMenu(
                shop_id = 14,
                coffee_id = 3
            ),
            ShopMenu(
                shop_id = 14,
                coffee_id = 4
            ),
            ShopMenu(
                shop_id = 14,
                coffee_id = 5
            ),
            ShopMenu(
                shop_id = 14,
                coffee_id = 6
            ),
            ShopMenu(
                shop_id = 15,
                coffee_id = 7
            ),
            ShopMenu(
                shop_id = 15,
                coffee_id = 8
            ),
            ShopMenu(
                shop_id = 15,
                coffee_id = 9
            ),
            ShopMenu(
                shop_id = 15,
                coffee_id = 10
            )
        ]

        ##Location Data
        locations = [
            Location(location = 'Colombia'),
            Location(location = 'Dominican Republic'),
            Location(location = 'Venezuela'),
            Location(location = 'Puerto Rico'),
            Location(location = 'Cuba'),
            Location(location = 'Queens'),
            Location(location = 'Brooklyn'),
            Location(location = 'Manhattan')
        ]
        db.session.add_all(beans)
        db.session.add_all(coffees)
        db.session.add_all(shops)
        db.session.add_all(locations)
        db.session.add_all(menus)
        db.session.commit()