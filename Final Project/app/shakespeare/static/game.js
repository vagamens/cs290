function button(but) {
	var main = document.getElementById('main');
	var br = document.createElement("br");
	var cont = 'Button ';
	if(but === 1) {
		cont = cont + '1 ';
	} else if (but === 2) {
		cont = cont + '2 ';
	} else if (but === 3) {
		cont = cont + '3 ';
	}
	cont = cont + 'was clicked.';
	var content = document.createTextNode(cont);
	main.appendChild(content);
	main.appendChild(br);
}

function reset() {
	var main = document.getElementById('main');
	main.innerHTML = '';
}