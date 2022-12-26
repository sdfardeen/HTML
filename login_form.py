<!DOCTYPE html>
<html>
<head>
	<title>Login form</title>
	<meta name="view port" content="widh=device-width, intitial-scale=1">
	<style>
		body{font-family: Arial, Helvetica,sans-serif;}
		input[type=text], input[type=password]{
			width: 100%;
			padding: 12px 20px;
			margin: 8px 0;
			display: inline-block;
			border: 1x solid #ccc;
			box-sizing: border-box;
		}
		button{
			background-color: darkgreen;
			color: white;
			padding: 14px 20px;
			margin: 8px;
			border: none;
			cursor: pointer;
			width: 100;
		}
		button:hover{
			opacity: 0.8;
		}
		.cancelbutton{
			width: auto;
			padding: 10px 18px;
			background-color: red;
		}
		.imgcontainer{
			text-align: center;
			margin: 24px 0 12px 0;
			position: relative;
		}
		.imgavatar{
			width: 40%;
			border-radius: 50%;
		}
		.container{
			padding: 16px;
		}
		.span.psw{
			float: right;
			padding-top: 16px;
		}
		.modal{
			display: none;
			position: fixed;
			z-index: 1;
			left: 0;
			top: 0;
			width: 100%;
			height: 100%;
			overflow: auto;
			background-color: rgb(0, 0, 0);
			background-color: rgba(0, 0, 0, 0.4);
			padding: 60px;
		}
		.modal-content{
			background-color: lightgray;
			margin: 5% auto 15% auto;
			border: 1px solid none;
			width: 50%;
		}
		.close{
			position: absolute;
			right: 25px;
			top: 0;
			color: white;
			font-size: 35px;
			font-weight: bold;
		}
		.close:hover,
		.close:focus{
			color: darkred;
			cursor: pointer;
		}
		.animate{
			-webkit-animation: animatezoom 0.6s;
			animation: animatezoom 0.6s
		}
		@-webkit-keyframes animatezoom{
			from {-webkit-tranform: scale(0)}
			to {-webkit-transform: scale(1)}
		}
		@keyframes animatezoom{
			from {transform: scale(0);}
			top {transform: scale(1.0);}
		}
		@media screen and (max-width: 300px){
			span.psw{
				display: block;
				float: none;
			}
			.cancelbutton{
				width: 100%;
			}
		}
	</style>
</head>
<body>
	<h2>	Login Form
	</h2>
	<marquee hspace="1%" direction = "right" height = "20px" vspan ='20%' scrollamount='12'>Click Login to sign</marquee>
	<button onclick="document.getElementById('id01').style.display='block'" style="width: auto;">Login
	</button>
	<div id="id01" class="modal">
		<form class="modal-content animate" action="/action_page.php" method="post">
			<div class="imgcontainer">
				<span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;
				</span>
				<img src="C:\\Users\\SYED ZAHIRA\\Desktop\\pics\\img_avatar.png" alt="Avatar" class="avatar">
			</div>
			<div class="container">
				<label for="uname">
					<b>Username</b>
				</label>
				<input type="text" name="uname" placeholder="Enter Username" required>
				<label for="psw">
					<b>Password</b>
				</label>
				<input type="password" placeholder="Enter Password" name="psw" required>

				<button type="submit">Login
				</button>
				<label>
					<input type="checkbox" checked="checked" name="remember"> Remember me
				</label>
			</div>
			<div class="container" style="background-color:#f1f1f1">
				<button type="button" onclick="document.getElementById('id01').style.display='none'" class="cnclbutton">Cancel
				</button>
				<span class="psw">Forgot <a href="#">password?</a>
				</span>
			</div>
		</form>
	</div>
	<script>
		var modal = document.getElementById('id01');
		window.onclick = function(event){
			if (event.target == modal) {
				modal.style.display = "none;"
			}
		}
	</script>
</body>
</html>