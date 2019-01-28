from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, User, Item

engine = create_engine('sqlite:///catalog_app.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

category = Category(name="Soccer",
                    link_name="Soccer")
session.add(category)
session.commit()

category = Category(name="Basketball",
                    link_name="Basketball")
session.add(category)
session.commit()

category = Category(name="Tennis",
                    link_name="Tennis")
session.add(category)
session.commit()

category = Category(name="Boxing",
                    link_name="Boxing")
session.add(category)
session.commit()

category = Category(name="Running",
                    link_name="Running")
session.add(category)
session.commit()

user = User(name="Yasemin",
            email="yasemin@abc123.com")
session.add(user)
session.commit()

item = Item(name="Soccer Ball",
            link_name="SoccerBall",
            description="It is a special ball designed to play soccer.",
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Soccer Cleat",
            link_name="SoccerCleat",
            description="It is a special shoe designed to play soccer "
                        "in grass fields.",
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Shin Guard",
            link_name="ShinGuard",
            description="It is a protection gear to protect the shin.",
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Goalkeeper Gloves",
            link_name="GoalkeeperGloves",
            description="It is a special glove designed to "
                        "catch moving soccer ball.",
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Basketball Ball",
            link_name="BasketballBall",
            description="It is a special ball designed to play basketball.",
            category_id=2,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Basketball Hoop",
            link_name="BasketballHoop",
            description="Horizontal circular metal hoop "
                        "supporting a net through which "
                        "players try to throw the basketball.",
            category_id=2,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Basketball Shoe",
            link_name="BasketballShoe",
            description="It is a special shoe to play basketball.",
            category_id=2,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Tennis Ball",
            link_name="TennisBall",
            description="It is a special ball designed to play tennis.",
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Racket",
            link_name="Racket",
            description="A tennis racket is the racket that you use "
                        "when you play tennis.",
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Tennis Shoe",
            link_name="TennisShoe",
            description="It is a special shoe to play tennis.",
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Boxing Gloves",
            link_name="BoxingGloves",
            description="It is a special padded glove designed for boxing.",
            category_id=4,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Hand Wrap",
            link_name="HandWrap",
            description="It is a wrap which is used "
                        "before wearing boxing glove.",
            category_id=4,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Punching Bag",
            link_name="PunchingBag",
            description="It is a heavy haning bag that "
                        "boxers punch as a triaing.",
            category_id=4,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Running Shoe",
            link_name="RunnigShoe",
            description="It is a special shoe to run without injury.",
            category_id=5,
            user_id=1)
session.add(item)
session.commit()

item = Item(name="Water Bottle",
            link_name="WaterBottle",
            description="It is a water bottle "
                        "which can be carried by runner.",
            category_id=5,
            user_id=1)
session.add(item)
session.commit()
