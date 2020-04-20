function clickobj(){
	alert("laifuo");
	var obj = document.getElementsByName('answer13');
	var demand =new Array();
	for (var i =0;i<obj.length;i++){
		if(obj[i].checked){
			demand.push(obj[i].nextSibling.nodeValue);
		}
	}
	alert(demand);

}
