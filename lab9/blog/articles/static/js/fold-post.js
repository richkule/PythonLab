var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++)
{ 
	foldBtns[i].addEventListener("click", function(event) 
	{
		if (event.target.className == "fold-button folded")
		{
			event.target.innerHTML = "свернуть"; 
			event.target.className = "fold-button"; 
			event.target.parentElement.className="one-post";
		}
		else
		{
			event.target.innerHTML = "развернуть"; 
			event.target.className = "fold-button folded"; 
			event.target.parentElement.className="one-post folded";
		}
	});
}
