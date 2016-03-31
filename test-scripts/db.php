<?php
// Code below borrowed in part from W3C Schools at:
// http://www.w3schools.com/php/php_mysql_connect.asp

$dbAddr = "192.168.0.99";
$dbUser = "php";
$dbPass = "secretpass";

// Create connection
$connection = new mysqli($dbAddr, $dbUser, $dbPass);

// Check connection
if ($connection->connect_error) {
	die("Connection failed: " . $connection->connect_error);
}
print("Connected successfully.");
?>