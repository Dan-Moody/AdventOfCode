<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <meta name="author" content="Daniel Moody">
    <title>Advent of Code 2021</title>
</head>

<body>
    <h1>Day 2</h1>


    <!-- Part1 -->
    <h2>Dive! Part 1:</h2>
    <?php
        $homepage = file_get_contents('file://C:/xampp/htdocs/AdventOfCode/AdventOfCode2021/Day2/input.txt');
        $arr = explode("\n", $homepage);
        // echo $homepage;
        // print_r($arr);
        $horizontal = 0;
        $depth = 0;
        foreach ($arr as $direction) {
            $instructions = explode(" ", $direction);
            if ($instructions[0] == "forward") {
                $horizontal += $instructions[1];
            } else if ($instructions[0] == "up") {
                $depth -= $instructions[1];
            } else if ($instructions[0] == "down") {
                $depth += $instructions[1];
            }
        }
        echo $horizontal*$depth;
    ?>
    <br>
    <br>


    <!-- Part 2 -->
    <h2>Dive! Part 2:</h2>
    <?php
    $homepage = file_get_contents('file://C:/xampp/htdocs/AdventOfCode/AdventOfCode2021/Day2/input.txt');
    $arr = explode("\n", $homepage);
    // echo $homepage;
    // print_r($arr);
    $horizontal = 0;
    $depth = 0;
    $aim = 0;
    foreach ($arr as $direction) {
        $instructions = explode(" ", $direction);
        if ($instructions[0] == "forward") {
            $horizontal += $instructions[1];
            $depth += $instructions[1] * $aim;            
        } else if ($instructions[0] == "up") {
            $aim -= $instructions[1];
        } else if ($instructions[0] == "down") {
            $aim += $instructions[1];
        }
    }
    echo $horizontal * $depth;
    ?>
</body>

</html>