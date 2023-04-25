<!DOCTYPE html>
GIF89a
<?php
// Create a blank image
$image = imagecreatetruecolor(200, 200);

// Set the background color to white
$bg_color = imagecolorallocate($image, 255, 255, 255);
imagefill($image, 0, 0, $bg_color);

// Draw a red circle
$circle_color = imagecolorallocate($image, 255, 0, 0);
imagefilledellipse($image, 100, 100, 150, 150, $circle_color);

// Set the content type header to PNG
header('Content-type: image/png');

// Output the image to the browser
imagepng($image);

// Free up memory
imagedestroy($image);
?>


