<?php
// Database configuration
$host = 'localhost';
$username = 'luke';
$password = 'snack snake soup sandwhich';
$database = 'mydatabase';

// Connect to the database
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $studentNo = $_POST['studentNo'];
    $passwd = $_POST['passwd'];

    // Insert data into the database
    $sql = "INSERT INTO my_table (studentNo, passwd) VALUES ('$studentNo', '$passwd')";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close database connection
$conn->close();
?>
