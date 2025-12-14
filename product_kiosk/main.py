from flask import Flask, render_template
import sqlite3
import init_db

app = Flask(__name__, static_folder="static", template_folder="templates")

def get_db_connection():
    conn = sqlite3.connect("instance/kiosk.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def read_root():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM projects")
    projects = c.fetchall()
    c.execute("SELECT * FROM mushroom_items")
    mushroom_items = c.fetchall()
    c.execute("SELECT * FROM apothecary")
    apothecary = c.fetchall()
    c.execute("SELECT * FROM plants")
    plants = c.fetchall()
    c.execute("SELECT * FROM craft")
    craft = c.fetchall()
    c.execute("SELECT * FROM brand")
    brand = c.fetchone()
    conn.close()
    return render_template(
        "index.html",
        projects=projects,
        brand=brand,
        mushroom_items=mushroom_items,
        apothecary=apothecary,
        plants=plants,
        craft=craft

    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
    #app.run(debug=True)