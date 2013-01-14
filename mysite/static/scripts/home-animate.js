$(document).ready(function() {
	$('#images').cycle({
		fx: 'scrollHorz', 
		speed: 700,
		timeout: 5000,
		next: '#right_arrow',
		prev: '#left_arrow' });
	$('#slider').mouseenter( function() {
		$('#slider img.arrow').fadeIn('200');
		$('#images').cycle('pause')
	}).mouseleave( function() {
		$('#slider img.arrow').fadeOut('200');
		$('#images').cycle('resume') });
	$('#slider img.arrow').mouseover( function() {
		$(this).fadeTo('100', '1');
	}).mouseout( function() {
		$(this).fadeTo('100', '.4'); });
	$('#right-block p#bottom-text').mouseover( function() {
		$(this).animate({backgroundColor: '#1a4d4a'}, '100');
	}).mouseout( function() { 
		$(this).animate({backgroundColor: '#25706b'}, '100'); });
	$('#left-block p#bottom-text').mouseover( function() {
		$(this).animate({backgroundColor: '#1a4d4a'}, '100');
	}).mouseout( function() { 
		$(this).animate({backgroundColor: '#25706b'}, '100'); });
	$('#slider p').mouseover( function() {
		$(this).animate({backgroundColor: '#25706b'}, '100'); 
	}).mouseout( function() {
		$(this).animate({backgroundColor: '#1e1e1e'}, '100');  });
	$('#center-block p').mouseover( function() {
		$(this).animate({backgroundColor: '#bc3b32'}, '100'); 
	}).mouseout( function() {
		$(this).animate({backgroundColor: '#1e1e1e'}, '100');  });
});
