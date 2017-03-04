function setMain(content) {
	var main = document.getElementById('main');
	main.innerHTML = content;
}

function addMain(content) {
	var main = document.getElementById('main');
	var text = document.createTextNode(content);
	var para = document.createElement('p');
	para.appendChild(text);
	main.appendChild(para);
}

function button(but) {
	var content = 'Button ';
	if(but === 1) {
		content = content + '1 ';
	} else if (but === 2) {
		content = content + '2 ';
	} else if (but === 3) {
		content = content + '3 ';
	}
	content = content + 'was clicked.';
	addMain(content);
}

function reset() {
	setMain('');
}

function sendRequest(data) {
	var xmlhttp = null;
	if (window.XMLHttpRequest) {
		xmlhttp = new XMLHttpRequest();
	} else {
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.open("POST", '/shakespeare/game', true);
	xmlhttp.setRequestHeader("Content-type", "application/json");
	xmlhttp.onReadyStateChange = function() {
		if(xmlhttp.status == 200) {
			addMain(JSON.stringify(JSON.parse(this.response)));
		}
	}
	xmlhttp.send(JSON.stringify(data));
}

function testJSON() {
	var data = { 'command':'', 'name': 'Kevin', 'password': 'thisIsMyPassword'};
	var response = sendRequest(data);
	addMain(JSON.stringify(data));
	addMain(response);
	addMain(typeof response);
}

function getInsult() {
	var data = {'command': 'insult'};
	response = sendRequest(data);
	console.log(response);
}