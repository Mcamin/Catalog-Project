#!/usr/bin/env python3
# Add some Items to Catalog Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Config import Category, Base, Product, User

engine = create_engine('sqlite:///Shop.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Amin", email="info@madev.de",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create 4 product categories
category1 = Category(user_id=1, name="Shoes")

session.add(category1)
session.commit()

category2 = Category(user_id=1, name="Clothing")

session.add(category2)
session.commit()

category3 = Category(user_id=1, name="Accessories")

session.add(category3)
session.commit()

category4 = Category(user_id=1, name="Sports")

session.add(category4)
session.commit()

#CAT SHOES
Item1 = Product(user_id=1,
                     name="APA - High-top trainers",
                     description="""MATERIAL & CARE
                     Upper material: Leather
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding
                     Care instructions: Treat with a suitable protector before wear""",
                     price="129,95 €", brand="CAT", category=category1)

session.add(Item1)
session.commit()


Item2 = Product(user_id=1,
                     name="DECADE - Casual lace-ups",
                     description="""MATERIAL & CARE
                     Upper material: Calfskin
                     Lining: Combination of leather and textile lining
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding""",
                     price="99,95 €", brand="CAT", category=category1)

session.add(Item2)
session.commit()

#ADIDAS SHOES
Item3 = Product(user_id=1,
                     name="Trainers",
                     description="""MATERIAL & CARE
                     Upper material: Textile/synthetics
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding
                     Fabric: Knit""",
                     price="83,95 €", brand="ADIDAS", category=category1)

session.add(Item3)
session.commit()


Item4 = Product(user_id=1,
                     name="CONTINENTAL 80 - Trainers",
                     description="""MATERIAL & CARE
                     Upper material: Leather and imitation leather
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding""",
                     price="99,95 €", brand="ADIDAS", category=category1)

session.add(Item4)
session.commit()

Item5 = Product(user_id=1,
                     name="NMD_R1 - Trainers",
                     description="""MATERIAL & CARE
                     Upper material: Textile
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding""",
                     price="149,95 €", brand="ADIDAS", category=category1)

session.add(Item5)
session.commit()

#NIKE SHOES

Item6 = Product(user_id=1,
                     name="ZOOM FLY SP",
                     description="""MATERIAL & CARE
                     Upper material: Synthetics/textile
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding""",
                     price="169,95 €", brand="NIKE", category=category1)

session.add(Item6)
session.commit()

Item7 = Product(user_id=1,
                     name="ROMALEOS 3",
                     description="""MATERIAL & CARE
                     Upper material: Synthetics/textile
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding
                     Fabric: Mesh""",
                     price="199,95 €", brand="NIKE", category=category1)

session.add(Item7)
session.commit()

Item8 = Product(user_id=1,
                     name="AIR VAPORMAX FLYKNIT 2 TIGER",
                     description="""MATERIAL & CARE
                     Upper material: Synthetics/textile
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding
                     Fabric: Knit""",
                     price="209,95 €", brand="NIKE", category=category1)

session.add(Item8)
session.commit()

Item9 = Product(user_id=1,
                     name="HYPERVENOM PHANTOM",
                     description="""MATERIAL & CARE
                     Upper material: Synthetics
                     Lining: Textile
                     Insole: Textile
                     Sole: Synthetics
                     Padding type: Cold padding""",
                     price="215,86 €", brand="NIKE", category=category1)

session.add(Item9)
session.commit()

print "added menu items!"
