$(document).ready(function() {
	$('#cssmenu ul li a').each( function() {
		if( $(this).attr('href') == window.location.pathname ) {
			$(this).addClass('active')
		}
	});
	$('#cssmenu ul li a').mouseenter( function() {
		$(this).addClass('hover');
	});
	$('#cssmenu ul li a').mouseleave( function() {
		$(this).removeClass('hover');
	});
	$('#cssmenu ul li a').click( function() {
		$('#cssmenu ul li a').each( function() {
			/*if( $(this).attr('href') == window.location.pathname ) {
				$(this).removeClass('active') */
		});
	});
});
