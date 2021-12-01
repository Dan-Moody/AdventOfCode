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
    <h1>Day 1</h1>


    <!-- Part1 -->
    <h2>Sonar Sweep Part 1:</h2>
    <?php
        $homepage = file_get_contents('file://C:/xampp/htdocs/AdventOfCode/AdventOfCode2021/Day1/input.txt');
        $arr = explode("\n", $homepage);
        // echo $homepage;
        // print_r($arr);
        $count = 0;
        $previous = $arr[0];
        foreach ($arr as &$value) {
            if ($value > $previous) {
                $count++;
            }
            $previous = $value;
        }
        echo $count;
    ?>
    <br>
    <br>


    <!-- Part 2 -->
    <h2>Sonar Sweep Part 2:</h2>
    <?php
        $homepage = file_get_contents('file://C:/xampp/htdocs/AdventOfCode/AdventOfCode2021/Day1/input.txt');
        $arr = explode("\n", $homepage);
        // echo $homepage;
        // print_r($arr);
        $count = 0;
        // First sum (because I am strictly doing less than when it chekcs the first against previous it wont matter)
        $previous = $arr[0] + $arr[1] + $arr[2];
        // Loop over each value
        foreach ($arr as $index => &$value) {
            // We dont want to start doing the sum until we have a full set of 3
            if ( $index > 0 && $index < count($arr)-1 ) {
                // echo $previous;
                // echo "{$arr[$index - 1]} + {$arr[$index]} + {$arr[$index + 1]}";
                if ( $previous < ($arr[$index-1] + $arr[$index] + $arr[$index+1]) ) {
                    $count++;
                }
                $previous = ($arr[$index - 1] + $arr[$index] + $arr[$index + 1]);
            }
        }
        echo $count;
    ?>
</body>

</html>