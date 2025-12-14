import sqlite3

loc_i = "assets/icons/"
loc_t = "assets/thumbnails/"


projects = [
    # personal GitHub projects to showcase
    {
        "title": "Mushroom Supplies"
    },
    {
        "title": "Apothecary"
    },
    {
        "title": "Plants & Cacti",
    },
    {
        "title": "Crafts",
    }
]

mushroom_items = [
    {"item": "Grow Kit",
     "price": "20.00"
     },
    {"item": "Agar Plate",
     "price": "10.00"
     },
    {"item": "Grain Bag",
     "price": "15.00"
     },
    {"item": "Substrate Bag",
     "price": "15.00"
     }
]

apothecary = [
    {"item": "Reishi Tinctures",
     "price": "25.00"
     },
     {"item": "LM Powder",
     "price": "20.00"
     },
     {"item": "Beeswax Salve",
     "price": "20.00"
     },
     {"item": "Lip Salve",
     "price": "5.00"
     }
]

plants = [
    {"item": "Small Animal",
     "price": "10.00"
     },
     {"item": "Large Animal",
     "price": "15.00"
     },
     {"item": "Small Round",
     "price": "10.00"
     },
     {"item": "Small Pedro",
     "price": "10.00"
     },
     {"item": "Med Pedro",
     "price": "15.00"
     },
     {"item": "Large Pedro",
     "price": "20.00"
     }
]

craft = [
    {"item": "Mush Card",
     "price": "10.00"
     },
     {"item": "Reishi Mounts",
     "price": "15.00"
     },
     {"item": "Stone Wrap",
     "price": "20.00"
     },
     {"item": "Macro Bracelet",
     "price": "10.00"
     },
     {"item": "Stone Bracelet",
     "price": "15.00"
     }
     
]

brand = [
    {
        "name": "Folkish Farms",
        "title": "Mushroom Supplies & Apothecary",
    }
]

conn = sqlite3.connect('instance/kiosk.db')
c = conn.cursor()


c.execute('DROP TABLE IF EXISTS projects')
c.execute('DROP TABLE IF EXISTS brand')
c.execute('DROP TABLE IF EXISTS mushroom_items')
c.execute('DROP TABLE IF EXISTS apothecary')
c.execute('DROP TABLE IF EXISTS plants')
c.execute('DROP TABLE IF EXISTS craft')


c.execute('CREATE TABLE projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)')
c.execute('CREATE TABLE brand (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT)')
c.execute('CREATE TABLE mushroom_items (item TEXT, price TEXT)')
c.execute('CREATE TABLE apothecary (item TEXT, price TEXT)')
c.execute('CREATE TABLE plants (item TEXT, price TEXT)')
c.execute('CREATE TABLE craft (item TEXT, price TEXT)')


c.executemany('INSERT INTO projects (title) VALUES (:title)', projects)
c.executemany('INSERT INTO brand (name, title) VALUES (:name, :title)', brand)
c.executemany('INSERT INTO mushroom_items (item, price) VALUES (:item, :price)', mushroom_items)
c.executemany('INSERT INTO apothecary (item, price) VALUES (:item, :price)', apothecary)
c.executemany('INSERT INTO plants (item, price) VALUES (:item, :price)', plants)
c.executemany('INSERT INTO craft (item, price) VALUES (:item, :price)', craft)

conn.commit()
conn.close()

print("Database tables dropped and repopulated in instance/portfolio.db!")