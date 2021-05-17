<?php


if(!isset($_POST['submit']))
{echo "error; you need to submit the form!";
}

$name = $_POST['name'];
$email = $_POST['email'];
$text = $_POST['text'];

if(empty($name)||empty($email)
{echo "Name and email are required!";
exit}

$email_from = 'nataliasuska01@gmail.com';
$email_subject = "Art Commission";
$email_body = "You have a new message from the user $name.\n".
    "Email Address: $email\n".
    "Here is the message:\n $message".

$to = "nataliasuska01@gmail.com";
$headers = "From: $email_from \r\n";

function IsInjected($str)
{
    $injections = array('(\n+)',
           '(\r+)',
           '(\t+)',
           '(%0A+)',
           '(%0D+)',
           '(%08+)',
           '(%09+)'
           );
               
    $inject = join('|', $injections);
    $inject = "/$inject/i";
    
    if(preg_match($inject,$str))
    {
      return true;
    }
    else
    {
      return false;
    }
}

if(IsInjected($visitor_email))
{
    echo "Bad email value!";
    exit;
}

mail($to,$email_subject,$email_body,$headers);
header('Location: home.html');

?>   