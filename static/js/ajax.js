
var proceso = new Object();
proceso.tipoPro = 1;
proceso.producto = new Array();
var table = new Array();
var cliente = new Object();

$(document).ready(function(){


  $('#c-buscar').submit(function(e){
    e.preventDefault();
    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(json){
        console.log(json)
        var html = ""
        for (var i = 0; i < json.length; i++) {
          html += 'DNI: '+json[i].dni + '<br>';
          html += 'Empresa : '+json[i].nombreEmpresa + '<br>';
          html += 'Empresa : '+json[i].nombreRepresentante + '<br>';
          html += 'apellidos: '+json[i].apellidoRepresentante + '<br>';

          cliente.dni = json[i].dni;
          cliente.nombreEmpresa = json[i].nombreEmpresa;
          cliente.nombreRepresentante = json[i].nombreRepresentante;
          cliente.apellidoRepresentante = json[i].apellidoRepresentante;

        }
        $('#clientes').html(html);
      }
    })
  })



})//principal
