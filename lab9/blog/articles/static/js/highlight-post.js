$(document).ready(function(){
	 $('.one-post').hover(function(event){
	 	$(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.1'}, 300);
	 }, function(event){
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'},300);
	 })
});

$(document).ready(function(){
	 $('.logo').hover(function(event){
	 	$(event.currentTarget).animate({width:'620px',height:'310px'}, 800);
	 }, function(event){
	 	$(event.currentTarget).animate({width:'600px',height:'300px'}, 800);
	 })
});