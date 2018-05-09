<?php
$mysqli = new mysqli("localhost", "root", "Atmosphere55!", "sephora");
$result = $mysqli->query("SELECT storeName AS 'Store', store_ID AS 'Store Number', MAX(amountSold) as 'Sales'
                        FROM store INNER JOIN sales ON store.ID = sales.store_ID
                        WHERE amountSold > 0
                        GROUP BY store_ID
                        ORDER BY MAX(amountSold) DESC
                        LIMIT 5; ");
?>

<!doctype html>
<html>
<body bgcolor="#E6E6FA">
<h1 align="center">What are the 5 stores with the most sales so far this year?</h1>
<table border="1" align="center" style="line-height:25px;">
<tr>
<th>Store</th>
<th>Store Number</th>
<th>Sales</th>
</tr>
<?php
//Fetch Data form database
if($result->num_rows > 0){
 while($row = $result->fetch_assoc()){
 ?>
 <tr>
 <td><?php echo $row['Store']; ?></td>
 <td><?php echo $row['Store Number']; ?></td>
 <td><?php echo $row['Sales']; ?></td>
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