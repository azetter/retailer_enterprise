# Retailer Enterprise Project

This repo includes our data that was apart of our individual database.
For your convience, we deployed all of our websites and our **Merged** database for you to run our queries yourself.

## We set up a remote Database for your Convience
We  stood up One remote database by migrating all of our data into an Amazon Rds Instance.
You can access it with the credentials we provided you. 
The name of the database : __projectcoffee__. **Please do not share the credentials with anyone**

## We stood up Three web application using Mysql, Php and Heroku.
Andrea - Sephora deployed [Website](https://serene-castle-27562.herokuapp.com/SephoraRetailer.html)

Isaac - Ikea deployed [Website](https://serene-depths-85562.herokuapp.com/home_page.php)

Hameed - HMart deployed [Website](https://morning-chamber-83520.herokuapp.com/)

# Queries
Connect to the remote Database. Credentials provided with submision, databasename is __projectcoffee__. Run the follow to get our results yourself.

**What are the top 20 products at each Store?**
__Note not every store has 20 transactions__

`select Rank, productName as Product, units as 'Units Sold', storeName as Store
from (select product_ID as upc, amountSold as units_sold, store_ID, storeName,
			  @cur_rank := IF(@store = store_ID, @cur_rank + 1, 1) as Rank, 
              @store := store_ID,
              @units := amountSold as units  
				from  (	select product_ID, amountSold, store_ID, storeName 					 
							from sales inner join store on store.ID = sales.store_ID
							order by store_ID, amountSold desc) as top_items
) as rankings inner join product on upc = product.ID
where Rank <= 20`

**What are the top 20 products in each State?**
__Note not every state is included__

`select Rank, productName as Product, units as 'Units Sold', storeState as State
from (select product_ID as upc, amountSold as units_sold, store_ID, storeState,
			  @cur_rank := IF(@cur_state = storeState, @cur_rank + 1, 1) as Rank, 
              @cur_state := storeState,
              @units := amountSold as units  
              from  (	select product_ID, amountSold, store_ID, storeState
							from sales inner join store on store.ID = sales.store_ID
							order by storeState, amountSold desc) as top_items
) as rankings inner join product on upc = product.ID
where Rank <= 20;`

**Which 5 Stores have the most sales?**

`select storeName as Store, store_ID as StoreID, sum(amountSold) as 'Total Sales'
from sales inner join store on store.ID = sales.store_ID
group by store_ID -- Allows the aggreate function sum based on each store to occur
order by sum(amountSold) desc -- Order the results from largest to smallest
limit 5;`



**In how many stores does Coke outsell Pepsi? (Or, a similar query for enterprises that(don’t sell soda.)**

`SELECT storeName as StoreName, productType as Type, MAX(amountSold) as Sold
		FROM sales 	INNER JOIN product ON sales.product_ID = product.ID
					INNER JOIN store   ON sales.store_ID = store.ID
		WHERE productType = "'Cup'" OR productType = "'Bowl'" OR productType = "Outdoor" OR productType = "Living Room" 
		OR productType = 'Foundation' OR productType = 'Moisterizer'
		GROUP BY store.ID
		ORDER BY productType;`


**What are the top 3 types of product that customers buy in addition to milk? (Or similar question for nonfood enterprises.)**

`
SELECT productType as Type, productName as ProductName, amountSold as Sold
        FROM product INNER JOIN sales ON product.ID = sales.product_ID
        WHERE productType != "'Cup'" or productType != "Bedroom" 
        GROUP BY productType
        ORDER BY MAX(amountSold) DESC
        LIMIT 3;`