<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bitwise Operations.</title>
</head>
<body>
<h1>Enter a List of Integers</h1>
<form action="process.php" method="POST">
    <label for="numbers">Enter integers separated by commas:</label><br>
    <input type="text" id="numbers" name="numbers" required><br><br>

    <label for="threshold">Enter threshold (for filtering):</label><br>
    <input type="number" id="threshold" name="threshold" required><br><br>

    <button type="submit">Submit</button>
</form>
</body>
</html>