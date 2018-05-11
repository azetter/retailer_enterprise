#!/usr/bin/python
import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                        user="root",         # your username
                        password="Hammania",  # your password
                        db="projectcoffee")        # name of the data base
            
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT productUPC FROM product")

    # File to print ProductUPCs to
    path = '/home/hameed/Documents/Github/retailer_enterprise/upcs.txt'
    upc_file = open(path, 'w')

    # print all the first cell of all the rows
    for productUPC in cur:
        upc = str(productUPC)[1:-2]
        print (('Query result: {}').format(upc))
        upc_file.write(upc + ',\n')

    upc_file.close()
    db.close()
except Exception as e:
    print("Failed to connect to database...", "Error:", e)
