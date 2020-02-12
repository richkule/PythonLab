$(document).ready(function(){
	var scrolled = 0;
	var $parallaxElements = $('.icons-for-parallax img');
	var logo = $('.logo')
	$(window).scroll(function() {
		scrolled = $(window).scrollTop();
		for (var i = 0; i < $parallaxElements.length; i++){
			yPosition = (scrolled * 0.15*(i + 1));
			$parallaxElements.eq(i).css({ top: yPosition });
			yPositionlogo = scrolled*0.37;
			logo.css({top: yPositionlogo})
		}

	});

});