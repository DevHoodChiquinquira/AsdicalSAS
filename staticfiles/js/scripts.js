// Funcion Flexslider
$(window).load(function() {
      $('.flexslider').flexslider();
 });

// Funcion tooltips de Bootstrap
$(function() {
    $('.tooltip-social').tooltip();
});

// Filtro portafolio
$(document).ready(function() {

	$("#portafolio-filtro li a").click(function() {
	
	 $("#portafolio-filtro li a.active").removeClass('active');

	 $(this).addClass('active');

	 var filterValue = 'cat-' + $(this).text().toLowerCase().replace(' ', '-');

	 if (filterValue === "cat-todo") {
			$('.portafolio-entrada').removeClass('escondidas');
		} else {
			
			$(".portafolio-entrada").each(function() {
				if (!$(this).hasClass(filterValue)) {
					$(this).addClass('escondidas');
				} else {
					$(this).removeClass('escondidas');
				}
			});
		}

		return false;
		
	});
		
		
});







		
		













		
		