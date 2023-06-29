from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy.orm import validates
# from sqlalchemy_serializer import SerializerMixin


##Unsure of imports
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



db = SQLAlchemy()



class Coffee(db.Model):
    __tablename__ = "coffees"

    id = db.Column(db.Integer, primary_key=True)
    coffeeshop_id = db.Column(db.Integer, ForeignKey('shops.id'))
    name = db.Column(db.String)
    roast = db.Column(db.String)
    coarse_vs_fine = db.Column(db.Boolean)
    price = db.Column(db.Numeric)

##Migrations

##creates a many to many relationship between coffee and bean tables
    beans = relationship('Bean', secondary='coffee_beans', backref='coffees')

class Bean(db.Model):
    __tablename__ = "beans"

    id = db.Column(db.Integer, primary_key=True)
    bean_type = db.Column(db.String)
    location = db.Column(db.String, ForeignKey('locations.id'))
    flavor_profile = db.Column(db.String)

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, unique=True)
    shops = relationship('Shop', backref='locations')
    beans = relationship('Bean', backref='locations')

class Shop(db.Model):
    __tablename__ = "shops"

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String)
    shop_location = db.Column(db.String, ForeignKey('locations.id'))
    rating = db.Column(db.String)

    
##creates a one to many relationship between shop and coffee tables
    coffees = relationship('Coffee', backref='shop')

##JOIN table to create the many to many relationship between the coffee and bean tables

coffee_beans = db.Table('coffee_beans',
    db.Column('coffee_id', db.Integer, ForeignKey('coffees.id'), primary_key=True),
    db.Column('bean_id', db.Integer, ForeignKey('beans.id'), primary_key=True)
)


class ShopMenu (db.Model):
    __tablename__= "shopsmenu"

    id = db.Column(db.Integer, primary_key= True)
    shop_id = db.Column(db.Integer)
    coffee_id = db.Column(db.Integer)


#creates a many to many relationship between the coffee and shop menu tables
coffee_menus = db.Table('coffee_menus',
    db.Column('coffee_id', db.Integer, ForeignKey('coffees.id'), primary_key = True),
    db.Column('shop_id', db.Integer, ForeignKey('shops.id'), primary_key = True)   
)