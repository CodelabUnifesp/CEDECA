$(document).ready(function(){
	$('#errolog').hide(); //Esconde o elemento com id errolog
	$('#form-login').submit(function(){ 	//Ao submeter formulário
		$.ajax({			//Função AJAX
			url:"",			//Arquivo php
			type:"post",				//Método de envio
			data: {"login":$('#email').val(), "senha":$('#senha').val()},	//Dados
			success: function (result){			//Sucesso no AJAX
						if(result==1){						
							location.href=''	//Redireciona
						}else{
							$('#errolog').show();		//Informa o erro
						}
					}
		})
		return false;	//Evita que a página seja atualizada
	})
})