-- --Create Coffee Table
-- --user can see all costs
-- --user can see coffee details (name, roast, flavor profile, bean)
-- --git stDecide on a many to many to show


-- CREATE TABLE COFFEE(
--     id INTEGER PRIMARY KEY,
--     COFFEESHOP_id INTEGER,
--     COFFEE_NAME TEXT,
--     ROAST TEXT,
--     COARSE_VS_FINE BOOLEAN,
--     PRICE DECIMAL
-- );

-- --SEED DATA
-- --take out bean_type
-- --put coffeshop ids in coffee
-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(2, 'Cafe Bustelo', 'Dark Roast', True, 17.25);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(3, 'LavAzza', 'Medium-Dark Roast', False, 6.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(4, 'Maxwell House', 'Light Roast', True, 7.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(5, 'Folgers', 'Medium Roast', False, 21.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(6, 'Illy Caffe', 'Light Roast', True, 10.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(7, 'Peets Coffee', 'Medium Roast', False, 44.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(8, 'Cafe Rico', 'Dark Roast', True, 6.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(9, 'Devil Mountain', 'Dark Roast', False, 21.99);

-- INSERT INTO COFFEE (COFFEESHOP_id, COFFEE_NAME, ROAST, COARSE_VS_FINE,PRICE) 
-- VALUES(10, 'Breakfast Blend', 'Medium Roast', True, 6.99);

-- CREATE TABLE COFFEE_SHOPS(
--     id INTEGER PRIMARY KEY,
--     SHOP_NAME TEXT,
--     SHOP_LOCATION TEXT,
--     RATING INTEGER
-- );

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Bakeri','Brooklyn', 5);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Cafe Grumpy','Manhattan', 3);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Ten Thousand Coffees','Queens', 1);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Butler Bakeshop','Brooklyn', 4);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Devocion','Brooklyn', 2);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Kobrick Coffee Company','Manhattan', 4);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Maman','Brooklyn', 5);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Arabica','Brooklyn', 3);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Felix Roasting Company','Manhattan', 4);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('PlantShed','Queens', 2);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Masseria','Brooklyn', 5);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Hungry Ghost','Queens', 1);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Ralphs Coffee','Queens', 5);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Stumptown Coffee','Brooklyn', 3);

-- INSERT INTO COFFEE_SHOPS(SHOP_NAME, SHOP_LOCATION, RATING)
-- VALUES('Partners Coffee','Queens', 2);


-- CREATE TABLE BEAN (
--     id INTEGER PRIMARY KEY,
--     BEAN_TYPE TEXT,
--     LOCATION TEXT,
--     FLAVOR_PROFILE TEXT
-- );

-- INSERT INTO BEAN (BEAN_TYPE, LOCATION, FLAVOR_PROFILE)
-- VALUES ('Coffea arabica', 'Colombia', 'Chocolatey, spicy, floral, caramelly, bright acidity.');

-- INSERT INTO BEAN (BEAN_TYPE, LOCATION, FLAVOR_PROFILE)
-- VALUES ('Typica', 'Dominican Republic', 'Lemon and floral notes with a sweet aftertaste.');

-- INSERT INTO BEAN (BEAN_TYPE, LOCATION, FLAVOR_PROFILE)
-- VALUES ('Robusta', 'Venezuela', 'Dark chocolate, nuts like almonds, and whiskey. Little to no acidity.');

-- INSERT INTO BEAN (BEAN_TYPE, LOCATION, FLAVOR_PROFILE)
-- VALUES ('Kopi luwak', 'Puerto Rico', 'Earthy and musty with hints of caramel and chocolate.');

-- INSERT INTO BEAN (BEAN_TYPE, LOCATION, FLAVOR_PROFILE)
-- VALUES ('Coffea liberica', 'Cuba', 'Smoky, nutty, floral with hints of dark chocolate, ripe berry and spice.');




