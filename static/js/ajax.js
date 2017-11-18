
var proceso = new Object();
proceso.tipoPro = 1;
proceso.producto = new Array();
proceso.obrero = new Array();
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
          html += 'Nombre representante : '+json[i].nombreRepresentante + '<br>';
          html += 'Nombre Apellidos: '+json[i].apellidoRepresentante + '<br>';

          cliente.dni = json[i].dni;
          cliente.nombreEmpresa = json[i].nombreEmpresa;
          cliente.nombreRepresentante = json[i].nombreRepresentante;
          cliente.apellidoRepresentante = json[i].apellidoRepresentante;

        }
        $('#clientes').html(html);
      }
    })
  })

  $("#c-seleccionar").click(function(){
    proceso.clienProv = cliente.dni;
    $("#c-dni").text(cliente.dni);
    $("#c-nombreEmpresa").text(cliente.nombreEmpresa);
    $("#c-nombreRepresentante").text(cliente.nombreRepresentante);
    $("#c-apellidoRepresentante").text(cliente.apellidoRepresentante);
    //alert(texto);
    //alert(textot);
  })



    /*productos ajax*/
    $('#p-buscar').submit(function(e){
      e.preventDefault();
      $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: $(this).serialize(),
        success: function(json){
          console.log(JSON.stringify(json))
          var html = ""
          for (var i = 0; i < json.length; i++) {
            html += 'Codigo: '+json[i].fields.codigo + '<br>';
            html += 'Producto: '+json[i].fields.producto + '<br>';
            html += 'Descripción: '+json[i].fields.descripcion + '<br>';
            html += 'Cantidad: '+json[i].fields.cantidad + '<br>';
            html += '<input name="p-cantidad" id="p-cantidad" type="number" min="1" max="200" step="1" value=1 autocomplete="off" required="required">';

            var fila = new Object();
            fila.codigo = json[i].fields.codigo;
            fila.producto = json[i].fields.producto;
            fila.descripcion = json[i].fields.descripcion;
            fila.cantidad = json[i].fields.cantidad;
            fila.cantidad = 1;
            table.push(fila);
          }
          $('#productos').html(html);
        }
      })
    })


    $("#p-seleccionar").click(function(){
      var d = table;
      var t = document.getElementById('tb-p-detalle').getElementsByTagName('tbody')[0];
      var rowCount = t.rows.length;
      var row = t.insertRow(rowCount);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      var cell4 = row.insertCell(3);
      cell1.innerHTML = d[d.length-1].codigo;
      cell2.innerHTML = d[d.length-1].producto;
      cell3.innerHTML = d[d.length-1].descripcion;
      d[d.length-1].cantidad = $('#p-cantidad').val();
      cell4.innerHTML = d[d.length-1].cantidad;
      cell1.setAttribute('align','center');
      cell2.setAttribute('align','center');
      cell3.setAttribute('align','center');
      cell4.setAttribute('align','center');

      proceso.producto.push({'codigo': d[d.length-1].codigo, 'cantidad': d[d.length-1].cantidad});
    })


    $('#o-buscar').submit(function(e){
      e.preventDefault();
      $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: $(this).serialize(),
        success: function(json){
          console.log(JSON.stringify(json))
          var html = ""
          for (var i = 0; i < json.length; i++) {
            html += 'Codigo: '+json[i].fields.dni + '<br>';
            html += 'Producto: '+json[i].fields.nombre + '<br>';
            html += 'Descripción: '+json[i].fields.apellido + '<br>';
            html += 'Cantidad: '+json[i].fields.telefono + '<br>';
            var fila = new Object();
            fila.dni = json[i].fields.dni;
            fila.nombre = json[i].fields.nombre;
            fila.apellido = json[i].fields.apellido;
            fila.telefono = json[i].fields.telefono;
            table.push(fila);
          }
          $('#obreros').html(html);
        }
      })
    })

    $("#o-seleccionar").click(function(){
      var d = table;
      var t = document.getElementById('tb-obreros').getElementsByTagName('tbody')[0];
      var rowCount = t.rows.length;
      var row = t.insertRow(rowCount);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      cell1.innerHTML = d[d.length-1].nombre;
      cell2.innerHTML = d[d.length-1].apellido;
      cell3.innerHTML = d[d.length-1].telefono;
      cell1.setAttribute('align','center');
      cell2.setAttribute('align','center');
      cell3.setAttribute('align','center');
      proceso.obrero.push({'dni': d[d.length-1].dni});
    })

    /*$("#o-calcular").click(function(){
      sumar();
    })*/


})//principal

//funciones aparte


function onEnviar(){
        //proceso.serie = $('#p-serie').val();
        //proceso.numero = $('#p-num').val();
        var descripcion = $("#o-descripcion").val();
        var direccion = $("#o-direccion").val();
        var fechaInicio = $("#o-fechaInicio").val();
        var fechaFinal = $("#o-fechaFinal").val();
        var porcentajeA = $("#o-porcentajeA").val();
        var valorA = $("#o-valorA").val();
        var porcentajeI = $("#o-porcentajeI").val();
        var valorI = $("#o-valorI").val();
        var porcentajeU = $("#o-porcentajeU").val();
        var valorU = $("#o-valorU").val();
        var tipoPago = $("#o-tipoPago").val();
        var ivaU = $("#o-iva").val();
        var subtotal = $("#o-subtotal").val();
        var total = $("#o-total").val();
        var estado = $("#o-estado").val();


        proceso.descripcion = descripcion;
        proceso.direccion = direccion;
        proceso.fechaInicio = fechaInicio;
        proceso.fechaFinal = fechaFinal;
        proceso.porcentajeA = porcentajeA;
        proceso.valorA = valorA;
        proceso.porcentajeI = porcentajeI;
        proceso.valorI = valorI;
        proceso.porcentajeU = porcentajeU;
        proceso.valorU = valorU;
        proceso.tipoPago = tipoPago;
        proceso.ivaU = ivaU;
        proceso.subtotal = subtotal;
        proceso.total = total;
        proceso.estado = estado;
        console.log(JSON.stringify(proceso));
        document.getElementById("proceso").value=JSON.stringify(proceso);
    }


/* prueba */


/**

  * Funcion que se ejecuta cada vez que se añade una letra en un cuadro de texto

  * Suma los valores de los cuadros de texto

  */

 function sumar()

 {
     var iva=0.16
     var pValorA=verificar("o-porcentajeA");
     var pValorI=verificar("o-porcentajeI");
     var pValorU=verificar("o-porcentajeU");
     var vTotal=verificar("o-total");
     // realizamos la suma de los valores y los ponemos en la casilla del
     // formulario que contiene el total o-subtotal

     var valorA = vTotal* (pValorA/100);
     var ValorI = vTotal* (pValorI/100);
     var ValorU = vTotal* (pValorU/100);
     var ivaU = ValorU* iva;
     var subtotal= vTotal-(valorA+ValorI+ValorU+ivaU);

     /*buscar Real*/
     valorA = subtotal* (pValorA/100);
     ValorI = subtotal* (pValorI/100);
     ValorU = subtotal* (pValorU/100);
     ivaU = ValorU* iva;
     var totalReal = subtotal+valorA+ValorI+ValorU+ivaU;

     while (vTotal > totalReal) {
       subtotal+=2;
       valorA = subtotal* (pValorA/100);
       ValorI = subtotal* (pValorI/100);
       ValorU = subtotal* (pValorU/100);
       ivaU = ValorU* iva;
       totalReal = subtotal+valorA+ValorI+ValorU+ivaU;
     }


     document.getElementById("o-valorA").value= valorA;
     document.getElementById("o-valorI").value= ValorI;
     document.getElementById("o-valorU").value= ValorU;
     document.getElementById("o-iva").value= ivaU
     document.getElementById("o-subtotal").value= subtotal








 }
 /**
  * Funcion para verificar los valores de los cuadros de texto. Si no es un
  * valor numerico, cambia de color el borde del cuadro de texto
  */
 function verificar(id)
 {
     var obj=document.getElementById(id);
     if(obj.value=="")
         value="0";
     else
         value=obj.value;
     if(validate_importe(value,1))
     {
         // marcamos como erroneo
         obj.style.borderColor="#808080";
         return value;
     }else{
         // marcamos como erroneo
         obj.style.borderColor="#f00";
         return 0;
     }
 }
 /**
  * Funcion para validar el importe
  * Tiene que recibir:
  *  El valor del importe (Ej. document.formName.operator)
  *  Determina si permite o no decimales [1-si|0-no]
  * Devuelve:
  *  true-Todo correcto
  *  false-Incorrecto
  */
 function validate_importe(value,decimal)
 {
     if(decimal==undefined)
         decimal=0;
     if(decimal==1)
     {
         // Permite decimales tanto por . como por ,
         var patron=new RegExp("^[0-9]+((,|\.)[0-9]{1,2})?$");
     }else{
         // Numero entero normal
         var patron=new RegExp("^([0-9])*$")
     }
     if(value && value.search(patron)==0)
     {
         return true;
     }
     return false;
 }
