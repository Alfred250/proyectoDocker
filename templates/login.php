<?php
$servername = "localhost";
$username = "root";   
$password = "";       
$dbname = "login_db"; 


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Error en la conexión: " . $conn->connect_error);
}


$usuario = $_POST['usuario'];
$pass = $_POST['password'];


$sql = "SELECT * FROM usuarios WHERE usuario='$usuario' AND password='$pass'";
$result = $conn->query($sql);


?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Resultado Login</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #3ba8a5, #6cc57c);
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: Arial, sans-serif;
    }
    .box {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      border-radius: 20px;
      padding: 40px;
      width: 400px;
      box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.2);
      text-align: center;
      color: #fff;
    }
    .btn-custom {
      background: #004d40;
      color: #fff;
      border-radius: 10px;
      padding: 10px 20px;
      text-decoration: none;
    }
    .btn-custom:hover {
      background: #00796b;
      color: #fff;
    }
  </style>
</head>
<body>
  <div class="box">
    <?php
    if ($result->num_rows > 0) {
        echo "<h2>✅ Bienvenido, $usuario</h2>";
        echo "<p>Has iniciado sesión correctamente.</p>";
        echo "<a href='login.html' class='btn-custom'>Cerrar sesión</a>";
    } else {
        echo "<h2>❌ Usuario o contraseña incorrectos</h2>";
        echo "<a href='login.html' class='btn-custom'>Volver al Login</a>";
    }
    ?>
  </div>
</body>
</html>

<?php
$conn->close();
?>
