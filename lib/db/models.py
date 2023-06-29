from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_seralizer import SerializerMixin

db = SQLAlchemy()

class Coffee(db.Model):
    __tablename__ = "coffees"

    id = db.Column(db.Integer, primary_key = True)
    coffeeshop_id = db.Column(db.Integer)
    name = db.Column(db.String)
    roast = db.Column(db.String)
    coarse_vs_fine = db.Column(db.Boolean)
    price = db.Column(db.Decimal)

class Bean(db.Model):
    __tablename__ = "beans"

    id = db.Column(db.Integer, primary_key = True)
    bean_type = db.Column(db.String)
    location  = db.Column(db.String)
    flavor_profile = db.Column(db.String)

class Shop(db.Model):
    __tablename__ = "shops"

    id = db.Column(db.Integer, primary_key = True)
    shop_name = db.Column(db.String)
    shop_location  = db.Column(db.String)
    rating = db.Column(db.String)


##RELATIONSHIPS COFFEE BEANS TABLE (coffee id and beans id) & Shop menu (coffee id and shop id) 
##Connect these below (these are your many to many)
