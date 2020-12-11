$(document).ready(function(){
	$("#sendlogin").click(function(){
		data = {"Email": $("#email.form-control").val(), "Senha": $("#senha.form-control")};
		console.log(data);
	});
});