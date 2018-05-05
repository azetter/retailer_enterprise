#!/usr/bin/python
import MySQLdb
import numpy as np  

upc_arr = np.array([],dtype=int)
transactions = np.array([],dtype=int)

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
    
    # print all the first cell of all the rows
    for productUPC in cur:
        upc = str(productUPC)[1:-2]
        upc_arr = np.append(upc_arr, upc)
        
    db.close()
except Exception as e:
    print("Failed to connect to database...", "Error:", e)


for x in np.nditer(upc_arr):
    print (x) 

def random_triplet():
    max = int(upc_arr[-1])
    x = np.random.randint(0, max) % 1995
    y = np.random.randint(0, max) % 1995
    z = np.random.randint(0, max) % 1995
    
#     return np.array(([upc[x],upc[y],upc[z]]))
    return np.array(([upc_arr[x],upc_arr[y],upc_arr[z]]))


