<?php

$dbServer = "50.62.209.147"; 
$username = "AustinK";
$password = "secondOne2";
$dbName   = "Events";

// Create connection
$conn = new mysqli($dbServer, $username, $password, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// $workload = $_REQUEST["wkld"];
$sql = "SELECT * FROM dsmEvents";

$result = $conn->query($sql);

echo json_encode($result);

$conn->close();
?>
