<?php
$mysqli = new mysqli("localhost", "root", "Atmosphere55!", "sephora");
$result = $mysqli->query("SELECT storeName AS 'Store Name', store.ID AS 'StoreID', productName AS 'Product Name', 
                            productType AS 'Type', amountSold AS 'Sold'
                            FROM sales INNER JOIN product on sales.product_ID = product.ID
			                INNER JOIN store on sales.store_ID = store.ID
                            WHERE productType = 'Foundation' OR productType = 'Moisterizer'
                            GROUP BY store.ID
                            ORDER BY store.ID; ");
?>

<!doctype html>
<html>
<body bgcolor="#E6E6FA">
<h1 align="center">In how many stores does Foundation outsell Moisterizer?</h1>
<table border="1" align="center" style="line-height:25px;">
<tr>
<th>Store Name</th>
<th>StoreID</th>
<th>Product Name</th>
<th>Type</th>
<th>Sold</th>
</tr>
<?php
//Fetch Data form database
if($result->num_rows > 0){
 while($row = $result->fetch_assoc()){
 ?>
 <tr>
 <td><?php echo $row['Store Name']; ?></td>
 <td><?php echo $row['StoreID']; ?></td>
 <td><?php echo $row['Product Name']; ?></td>
 <td><?php echo $row['Type']; ?></td>
 <td><?php echo $row['Sold']; ?></td>
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
</body>
</html>