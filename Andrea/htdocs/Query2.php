<?php
    $mysqli = new mysqli("localhost", "root", "Atmosphere55!", "sephora");
    $result = $mysqli->query("SELECT Rank, productName AS Product, units AS 'Units Sold', storeState AS State
    FROM (SELECT product_ID AS upc, amountSold AS units_sold, store_ID, storeState,
                -- Leveraged mysql session variables to track ranking 
                -- If the storeStae is = to the previous one than increase the rank, otherwise start back at 1
                  @cur_rank := IF(@cur_state = storeState, @cur_rank + 1, 1) AS Rank, 
                  @cur_state := storeState,
                  @units := amountSold AS units
                    -- In order to get the correct ranking order a Subquery that orders by State and amount sold in descending order is needed
                    FROM  (SELECT product_ID, amountSold, store_ID, storeState
                                FROM sales INNER JOIN store ON store.ID = sales.store_ID
                                ORDER BY storeState, amountSold DESC) AS top_items) AS rankings INNER JOIN product ON upc = product.ID
                            -- Cap the ranking at the top 20 items
                                WHERE rank <= 20;");
?>

<!-- QUERIES WILL BE OUTPUT -->
<!doctype html>
<html>
<body bgcolor="#E6E6FA">
<h1 align="center">What are the 20 top-selling products in each state?</h1>
<table border="1" align="center" style="line-height:25px;">
<tr>
<th>Rank</th>
<th>Product</th>
<th>Units Sold</th>
<th>State</th>
</tr>
<?php
//Fetch Data form database
if($result->num_rows > 0){
 while($row = $result->fetch_assoc()){
 ?>
 <tr>
 <td><?php echo $row['Rank']; ?></td>
 <td><?php echo $row['Product']; ?></td>
 <td><?php echo $row['Units Sold']; ?></td>
 <td><?php echo $row['State']; ?></td>
 </tr>
 <?php
 }
}
else
{
 ?>
 <tr>
 <th colspan="2">There's No data found!!!</th>
 </tr>
 <?php
}
?>
</table>