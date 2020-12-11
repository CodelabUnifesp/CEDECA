
    
    function limpa_formulario_cep() {
            //Limpa valores do formulário de cep.
            document.getElementById('rua').value=("");
            document.getElementById('bairro').value=("");
            document.getElementById('cidade').value=("");
            document.getElementById('estado').value=("");
            
    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('rua').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('cidade').value=(conteudo.localidade);
            document.getElementById('estado').value=(conteudo.uf);
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulario_cep();
            alert("CEP não encontrado.");
            document.getElementById('cep').value=("");
        }
    }
        
    function pesquisacep(valor, parte) {
        //Nova variável "cep" somente com dígitos.
        var cep = valor//.replace(/\D/g, '');
        console.log(valor, 'ugywv')
        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.

        $.ajax({
        url: `http://www.viacep.com.br/ws/${cep}/json/`,
        type: 'post',
        dataType: 'jsonp',
        crossDomain: true,
        data: {},
        }).done(function(response){

            console.log(response)
            
        if(response.erro == true){
        alert("CEP inválido!");
        }else{
        if(parte == "assistido"){//Fazer o resto do endereco
          $("input#rua.assistido").attr("value", response.logradouro);
          $("input#bairro.assistido").attr("value", response.bairro);
          $("input#cidade.assistido").attr("value", response.localidade);
          $("input#estado.assistido").attr("value", response.uf);
        }else{
          $("input#rua.parte-contraria").attr("value", response.logradouro);
          $("input#bairro.parte-contraria").attr("value", response.bairro);
          $("input#cidade.parte-contraria").attr("value", response.localidade);
          $("input#estado.parte-contraria").attr("value", response.uf);
        }

        }
        });

        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulario_cep();
        }
    }

function formatar(mascara, documento){
  var i = documento.value.length;
  var saida = mascara.substring(0,1);
  var texto = mascara.substring(i);
  
  if (texto.substring(0,1) != saida){
            documento.value += texto.substring(0,1);
  }
  
}
 
function idade (){
    var data=document.getElementById("dtnasc").value;
    var dia=data.substr(0, 2);
    var mes=data.substr(3, 2);
    var ano=data.substr(6, 4);
    var d = new Date();
    var ano_atual = d.getFullYear(),
        mes_atual = d.getMonth() + 1,
        dia_atual = d.getDate();
        
        ano=+ano,
        mes=+mes,
        dia=+dia;
        
    var idade=ano_atual-ano;
    
    if (mes_atual < mes || mes_atual == mes_aniversario && dia_atual < dia) {
        idade--;
    }
return idade;
} 
  
  
function exibe(i) {
    
   
        
	document.getElementById(i).readOnly= true;
	    
		
	
    
}

function desabilita(i){
    
     document.getElementById(i).disabled = true;    
    }
function habilita(i)
    {
        document.getElementById(i).disabled = false;
    }


function showhide()
 {
       var div = document.getElementById("newpost");
       
       if(idade()>=18){
 
    div.style.display = "none";
}
else if(idade()<18) {
    div.style.display = "inline";
}

 }

var x = 1;

var idContador = 0;
            
    function exclui(id){
        var campo = $("#"+id.id);
        campo.hide(200);
    }

    $( document ).ready(function() {
        
        $("#btnAdicionaEmail").click(function(e){
            e.preventDefault();
            var tipoCampo = "email";
            adicionaCampo(tipoCampo);
        })
        
        $("#btnAdicionaTelefone").click(function(e){
            e.preventDefault();
            var tipoCampo = "telefone";
            adicionaCampo(tipoCampo);
        })
        
        function adicionaCampo(tipo){

            idContador++;
            
            var idCampo = "campoExtra"+idContador;
            var idForm = "formExtra"+idContador;
        
            var html = "";
            
            html += "<div style='margin-top: 8px;' class='input-group' id='"+idForm+"'>";
            html += "<input type='text' id='"+idCampo+"' class='form-control novoCampo' placeholder='Insira um "+tipo+"'/>";
            html += "<span class='input-group-btn'>";
            html += "<button class='btn' onclick='exclui("+idForm+")' type='button'><span class='fa fa-trash'></span></button>";html += "<button class='btn' onclick='exclui("+idForm+")' type='button'><span class='fa fa-trash'></span></button>";
            html += "</span>";
            html += "</div>";
            
            $("#imendaHTML"+tipo).append(html);
        }
        
        $(".btnExcluir").click(function(){
            console.log("clicou");
            $(this).slideUp(200);
        })
        
        $("#btnSalvar").click(function(){
        
        var mensagem = "";
        var novosCampos = [];
        var camposNulos = false;
        
            $('.campoDefault').each(function(){
                if($(this).val().length < 1){
                    camposNulos = true;
                }
            });
            $('.novoCampo').each(function(){
                if($(this).is(":visible")){
                    if($(this).val().length < 1){
                        camposNulos = true;
                    }
                    //novosCampos.push($(this).val());
                    mensagem+= $(this).val()+"\n";
                }
            });
            
            if(camposNulos == true){
                alert("Atenção: existem campos nulos");
            }else{
                alert("Novos campos adicionados: \n\n "+mensagem);
            }
            
            novosCampos = [];
        })
        
    });
