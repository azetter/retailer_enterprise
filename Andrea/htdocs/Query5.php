<?php
$mysqli = new mysqli("localhost", "root", "Atmosphere55!", "sephora");
$result = $mysqli->query("SELECT productName AS 'Product Name', productType AS Type, amountSold AS Sold
                            FROM product INNER JOIN sales on product.ID
                            WHERE amountSold > 0
                            GROUP BY Type
                            ORDER BY Sold desc
                            LIMIT 3; ");
?>

<!doctype html>
<html>
<body bgcolor="#E6E6FA">
<h1 align="center">What are the top 3 types of product that customers buy in addition to Moisterizer?</h1>
<table border="1" align="center" style="line-height:25px;">
<tr>
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