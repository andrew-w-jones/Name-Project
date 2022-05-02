<html>

	<head>
		<title>Predictions</title>
		<link rel="stylesheet" href="styles.css">
		<meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
	</head>
	
	<body>
		<div class="container">
			<div class="inputs">
				<label>
					<?php
						
						$usersName = $_POST["name"];
						
						$command = escapeshellcmd("YOUR/PYTHON/LOCATION/python.exe /NameLookup.py " . $usersName);
						// ^^^ Update this line with your python environment location ^^^
						
						$output = shell_exec($command);
						
						echo(" Your name is <b>".$usersName."</b>.<br>"); 
						echo rtrim($output) . ".";
						
						
					?>
				</label>
			</div>
		</div>
	</body>
</html>
