<?php

$name = $_GET["name"];
$myText = $_POST["email"];

if($name = "save") {
  $targetFolder = "/website/routes";
  file_put_contents($targetFolder."mytext.txt", $myText);
}
?>   