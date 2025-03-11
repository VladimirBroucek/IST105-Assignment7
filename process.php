<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bitwise Operations Result</title>
</head>
<body>
<h1>Bitwise Operations Processing</h1>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $numbers = escapeshellarg($_POST['numbers']);
    $threshold = escapeshellarg($_POST['threshold']);

    $command = "python3 bitwise_operations.py $numbers $threshold";
    $output = shell_exec($command);

    if ($output === null) {
        echo "<p>Error: Unable to execute the Python script.</p>";
    } else {
        echo "<pre>$output</pre>";
    }
} else {
    echo "<p>Error: Invalid request method.</p>";
}
?>
</body>
</html>