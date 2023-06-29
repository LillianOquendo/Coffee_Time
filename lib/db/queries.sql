--Create Coffee Table
--user can see all costs
--user can see coffee details (name, roast, flavor profile, bean)
--git stDecide on a many to many to show
--

CREATE TABLE COFFEE(
    id INTEGER PRIMARY KEY,
    Bean_id INTEGER,
    COFFEESHOP_id INTEGER,
    NAME TEXT,
    ROAST TEXT,
    BEAN_TYPE TEXT,
    COARSE_VS_FINE BOOLEAN,
    PRICE DECIMAL
);

--SEED DATA
INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(2, 2, 'Cafe Bustelo', 'Dark Roast', 'Coffea arabica', True, 17.25);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(3, 3, 'LavAzza', 'Medium-Dark Roast', 'Typica', False, 6.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(4, 4, 'Maxwell House', 'Light Roast', 'Robusta', True, 7.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(5, 5, 'Folgers', 'Medium Roast', 'Kopi luwak', False, 21.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(6, 6, 'Illy Caffe', 'Light Roast', 'Coffea liberica', True, 10.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(7, 7, 'Peets Coffee', 'Medium Roast', 'Kopi luwak', False, 44.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(8, 8, 'Cafe Rico', 'Dark Roast', 'Coffea liberica', True, 6.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(9, 9, 'Devil Mountain', 'Dark Roast', 'Coffea arabica', False, 21.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, BEAN_TYPE, COARSE_VS_FINE,PRICE) 
VALUES(10, 10, 'Breakfast Blend', 'Medium Roast','Typica', True, 6.99);

CREATE TABLE CoffeeShops(
    id INTEGER PRIMARY KEY,
    NAME TEXT,
    LOCATION TEXT,
    RATING INTEGER
);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Bakeri','Brooklyn', 5);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Cafe Grumpy','Manhattan', 3);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Ten Thousand Coffees','Queens', 1);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Butler Bakeshop','Brooklyn', 4);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Devocion','Brooklyn', 2);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Kobrick Coffee Company','Manhattan', 4);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Maman','Brooklyn', 5);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Arabica','Brooklyn', 3);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Felix Roasting Company','Manhattan', 4);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('PlantShed','Queens', 2);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Masseria','Brooklyn', 5);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Hungry Ghost','Queens', 1);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Ralphs Coffee','Queens', 5);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Stumptown Coffee','Brooklyn', 3);

INSERT INTO CoffeeShops(NAME, LOCATION, RATING)
VALUES('Partners Coffee','Queens', 2);


CREATE TABLE Bean (
    id INTEGER PRIMARY KEY,
    BEAN_TYPE TEXT,
    LOCATION TEXT,
    FLAVOR_PROFILE TEXT
);

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Coffea arabica', 'Colombia', 'Chocolatey, spicy, floral, caramelly, bright acidity.');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Typica', 'Dominican Republic', 'Lemon and floral notes with a sweet aftertaste.');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Robusta', 'Venezuela', 'Dark chocolate, nuts like almonds, and whiskey. Little to no acidity.');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Kopi luwak', 'Puerto Rico', 'Earthy and musty with hints of caramel and chocolate.');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Coffea liberica', 'Cuba', 'Smoky, nutty, floral with hints of dark chocolate, ripe berry and spice.');


