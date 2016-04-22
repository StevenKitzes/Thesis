<?php
// Code below borrowed in part from W3C Schools at:
// http://www.w3schools.com/php/php_mysql_connect.asp

$dbAddr = "192.168.0.99";
$dbUser = "php";
$dbPass = "secretpass";
$dbName = "employees";

// Create connection
$connection = new mysqli($dbAddr, $dbUser, $dbPass, $dbName);

// Check connection
if ($connection->connect_error) {
	die("Connection failed: " . $connection->connect_error);
}

//$query = 'SELECT `last_name`, `first_name`, `salary`, `dept_name` FROM `Departments`, `dept_emp`, `employees`, `salaries` WHERE `salary` = (SELECT MAX(`salary`) FROM `salaries`) AND departments.dept_no = dept_emp.dept_no AND dept_emp.emp_no = employees.emp_no AND employees.emp_no = salaries.emp_no ORDER BY `salary`;';
$query = 'SELECT last_name FROM `employees` WHERE first_name = "Steve" LIMIT 3;';
$queryb = 'SELECT last_name FROM `employees` WHERE first_name = "Tran" LIMIT 3;';

$result = $connection->query($query);
$resultb = $connection->query($queryb);

while($row = $result->fetch_assoc()) {
	print($row["last_name"] . "<br>");
}
while($row = $resultb->fetch_assoc()) {
	print($row["last_name"] . "<br>");
}

?>
