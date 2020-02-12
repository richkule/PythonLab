$(document).ready(function(){
	 $('.one-post').hover(function(event){
	 	$(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.1'}, 300);
	 }, function(event){
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'},300);
	 })
});

$(document).ready(function(){
	 $('img').hover(function(event){
	 	$(event.currentTarget).animate({width:'120px',height:'120px'}, 800);
	 }, function(event){
	 	$(event.currentTarget).animate({width:'100px',height:'100px'}, 800);
	 })
});