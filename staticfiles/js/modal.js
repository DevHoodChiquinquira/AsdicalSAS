$('.galeria__img').click(function(e){
    var img = e.target.src;
    var modal = '<div class="modal"><img src="'+img+'" class="modal__img"><div class="modal__boton">X</div></div>;
    $('body').append(modal);
})