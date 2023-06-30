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
                shop_location_id = 'Brooklyn',
                rating = '5'
            ),
            Shop(
                shop_name = 'Cafe Grumpy',
                shop_location_id = 'Manhattan',
                rating = '3'
            ),
            Shop(
                shop_name = 'Ten Thousand Coffees',
                shop_location_id = 'Queens',
                rating = '1'
            ),
            Shop(
                shop_name = 'Butler Bakeshop',
                shop_location_id = 'Brooklyn',
                rating = '4'
            ),
            Shop(
                shop_name = 'Devocion',
                shop_location_id = 'Brooklyn',
                rating = '2'
            ),
            Shop(
                shop_name = 'Kobrick Coffee Company',
                shop_location_id = 'Manhattan',
                rating = '4'
            ),
            Shop(
                shop_name = 'Maman',
                shop_location_id = 'Brooklyn',
                rating = '5'
            ),
            Shop(
                shop_name = 'Arabica',
                shop_location_id = 'Brooklyn',
                rating = '3'
            ),
            Shop(
                shop_name = 'Felix Roasting Company',
                shop_location_id = 'Manhattan',
                rating = '4'
            ),
            Shop(
                shop_name = 'PlantShed',
                shop_location_id = 'Queens',
                rating = '2'
            ),
            Shop(
                shop_name = 'Masseria',
                shop_location_id = 'Brooklyn',
                rating = '5'
            ),
            Shop(
                shop_name = 'Hungry Ghost',
                shop_location_id = 'Queens',
                rating = '1'
            ),
            Shop(
                shop_name = 'Ralphs Coffee',
                shop_location_id = 'Queens',
                rating = '5'
            ),
            Shop(
                shop_name = 'stumptown coffee',
                shop_location_id = 'Brooklyn',
                rating = '3'
            ),
            Shop(
                shop_name = 'Partners Coffee',
                shop_location_id = 'Queens',
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
                shop_id = 'bakeri',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'bakeri',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'bakeri',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'bakeri',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'cafe grumpy',
                coffee_id = 'illy caffe'
            ),
            ShopMenu(
                shop_id = 'cafe grumpy',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'cafe grumpy',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'cafe grumpy',
                coffee_id = 'breakfast blend'
            ),
            ShopMenu(
                shop_id = 'ten thousand coffees',
                coffee_id = 'cafe bustelo'
            ),
            ShopMenu(
                shop_id = 'ten thousand coffees',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'ten thousand coffees',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'ten thousand coffees',
                coffee_id = 'illy caffe'
            ),
            ShopMenu(
                shop_id = 'butler bakeshop',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'butler bakeshop',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'butler bakeshop',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'butler bakeshop',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'devocion',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'devocion',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'devocion',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'devocion',
                coffee_id = 'cafe bustelo'
            ),
            ShopMenu(
                shop_id = 'kobrick coffee company',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'kobrick coffee company',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'kobrick coffee company',
                coffee_id = 'breakfast blend'
            ),
            ShopMenu(
                shop_id = 'kobrick coffee company',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'maman',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'maman',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'maman',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'maman',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'arabica',
                coffee_id = 'cafe bustelo'
            ),
            ShopMenu(
                shop_id = 'arabica',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'arabica',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'arabica',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'felix roasting company',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'felix roasting company',
                coffee_id = 'illy caffe'
            ),
            ShopMenu(
                shop_id = 'felix roasting company',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'felix roasting company',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'plantshed',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'plantshed',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'plantshed',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'plantshed',
                coffee_id = 'breakfast blend'
            ),
            ShopMenu(
                shop_id = 'masseria',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'masseria',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'masseria',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'masseria',
                coffee_id = 'cafe bustelo'
            ),
            ShopMenu(
                shop_id = 'hungry ghost',
                coffee_id = 'illy caffe'
            ),
            ShopMenu(
                shop_id = 'hungry ghost',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'hungry ghost',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'hungry ghost',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'ralphs coffee',
                coffee_id = 'breakfast blend'
            ),
            ShopMenu(
                shop_id = 'ralphs coffee',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'ralphs coffee',
                coffee_id = 'cafe bustelo'
            ),
            ShopMenu(
                shop_id = 'ralphs coffee',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'stumptown coffee',
                coffee_id = 'maxwell house'
            ),
            ShopMenu(
                shop_id = 'stumptown coffee',
                coffee_id = 'folgers'
            ),
            ShopMenu(
                shop_id = 'stumptown coffee',
                coffee_id = 'illy caffe'
            ),
            ShopMenu(
                shop_id = 'stumptown coffee',
                coffee_id = 'peets coffee'
            ),
            ShopMenu(
                shop_id = 'partners coffee',
                coffee_id = 'cafe rico'
            ),
            ShopMenu(
                shop_id = 'partners coffee',
                coffee_id = 'devil mountain'
            ),
            ShopMenu(
                shop_id = 'partners coffee',
                coffee_id = 'lavazza'
            ),
            ShopMenu(
                shop_id = 'partners coffee',
                coffee_id = 'breakfast blend'
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
        db.session.query(Shop).delete()
        db.session.query(Bean).delete()
        db.session.query(Coffee).delete()
        db.session.query(Location).delete()
        db.session.query(ShopMenu).delete()
        db.session.add_all(beans)
        db.session.add_all(coffees)
        db.session.add_all(shops)
        db.session.add_all(locations)
        db.session.add_all(menus)
        db.session.commit()