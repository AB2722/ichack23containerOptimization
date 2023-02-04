
import sqlite3 as sql
import csv

def create_bottles():
    #Create database file/connect to it
    conn = sql.connect("bottle_database.db")

    #Create table
    conn.execute("""CREATE TABLE bottles (object TEXT, name TEXT, ratio TEXT, company TEXT, price TEXT, material TEXT)""")

    print("table created")

    conn.close()

def populate_bottles():
    # #Get all rows from csv file
    # with open('D:/Programming/VisualCode/Hackathon/Starhacks real/building-tuition/prototype/static/databases/bottle.csv', newline='') as f:
    #     reader = csv.reader(f)
    #     next(reader) #skip headers line
    #     data = list(reader)

    #Connect to database
    conn = sql.connect("bottle_database.db")
    cur = conn.cursor()

    # name TEXT, ratio TEXT, company TEXT, price TEXT, material TEXT
    data = [["water bottle", "Water Bottle 1", "2.11", "FUJI", "$1.00", "Plastic"],
            ["water bottle", "Water Bottle 2", "7.11", "Monster", "$1.50", "Glass"]]

    #Load all rows
    for row in data:
        print(row) #Debug
        insert_query = """INSERT INTO bottles (object, name, ratio, company, price, material)
                                        VALUES (?,?,?,?,?,?)"""
        cur.execute(insert_query, (row[0], row[1], row[2], row[3], row[4], row[5]))

    #Save changes
    conn.commit()

    conn.close()

    print("Loading completed")

create_bottles()
populate_bottles()