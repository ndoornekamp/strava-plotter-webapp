
function open_in_new_tab(element) { 
	var newTab = window.open();
	setTimeout(function(){newTab.document.body.innerHTML = element.innerHTML;},50); 
}
