<?php

$name = $_GET["name"];
$myText = $_POST["email"];

if($action = "save") {
  $targetFolder = "/path/to/folder";
  file_put_contents($targetFolder."mytext.txt", $myText);
}
?>   