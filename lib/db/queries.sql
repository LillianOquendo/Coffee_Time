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
    COARSE_VS_FINE BOOLEAN,
    PRICE DECIMAL
);

--SEED DATA
INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(2, 2, 'Cafe Bustelo', 'Dark Roast', True, 17.25);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(3, 3, 'LavAzza', 'Medium-Dark Roast', False, 6.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(4, 4, 'Maxwell House', 'Light Roast', True, 7.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(5, 5, 'Folgers', 'Medium Roast', False, 21.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(6, 6, 'Illy Caffe', 'Light Roast', True, 10.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(7, 7, 'Peets Coffee', 'Medium Roast', False, 44.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(8, 8, 'Cafe Rico', 'Dark Roast', True, 6.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(9, 9, 'Devil Mountain', 'Dark Roast', False, 21.99);

INSERT INTO COFFEE (Bean_id, COFFEESHOP_id, NAME, ROAST, COARSE_VS_FINE,PRICE) 
VALUES(10, 10, 'Breakfast Blend', 'Medium Roast', True, 6.99);

CREATE TABLE CoffeeShops(
    id INTEGER PRIMARY KEY,
    NAME TEXT,
    LOCATION TEXT
);

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Bakeri','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Cafe Grumpy','Manhattan');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Ten Thousand Coffees','Queens');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Butler Bakeshop','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Devocion','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Kobrick Coffee Company','Manhattan');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Maman','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Arabica','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Felix Roasting Company','Manhattan');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('PlantShed','Queens');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Masseria','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Hungry Ghost','Queens');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Ralphs Coffee','Queens');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Stumptown Coffee','Brooklyn');

INSERT INTO CoffeeShops(NAME, LOCATION)
VALUES('Partners Coffee','Queens');


CREATE TABLE Bean (
    id INTEGER PRIMARY KEY,
    BEAN_TYPE TEXT,
    LOCATION TEXT,
    FLAVOR_PROFILE TEXT
);

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('C. arabica', 'Colombia', '');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Interspecific hybrid', 'Dominican Republic', '');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('C. charrieriana', 'Venezuela', '');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('C. arabica', 'Puerto Rico', '');

INSERT INTO Bean (Bean_TYPE, LOCATION, FLAVOR_PROFILE)
VALUES ('Coffea liberica', 'Cuba', '');

