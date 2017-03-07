function addNav(element) {
	var nav = document.getElementById('nav');
	var li = document.createElement('li');
	li.appendChild(element);
	nav.appendChild(li);
}

function setNav(content) {
	var nav = document.getElementById('nav');
	nav.innterHTML = content;
}

function setMain(content) {
	var main = document.getElementById('main');
	main.innerHTML = content;
}

function createButton(com, text) {
	var button = document.createElement('button');
	var t = document.createTextNode(text);
	var click = document.createAttribute('onClick');
	click.value = 'javascript:button(\''+com+'\')';
	button.setAttributeNode(click);
	button.appendChild(t);
	return button;
}

function addMain(element) {
	var main = document.getElementById('main');
	main.appendChild(element);
}

function addContent(content) {
	var text = document.createTextNode(content);
	var para = document.createElement('p');
	para.appendChild(text);
	addMain(para);
}

function resetMain() {
	setMain('');
}

function button(command) {
	var data = {};
	if(command === 1) {
		addContent('Button 1 was clicked.');
		addNav(createButton('test', 'test'));
	} else if (command === 2) {
		addContent('Button 2 was clicked.');
	} else if (command === 3) {
		addContent('Button 3 was clicked.');
	} else if (command === 'insult') {
		data = {'command': 'insult'};
		sendRequest(data);
	} else if (command === 'reset') {
		resetMain();
	} else if (command === 'test') {
		addContent('Button creation works!!!!!');
	}
}

function addJSONMain(j) {
	j = JSON.parse(j);
	if(j['command'] === 'insult') {
		addContent('You have been insulted:');
		addContent('\t'+j['insult']);
	}
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
	xmlhttp.onreadystatechange = function (e) {
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			addJSONMain(xmlhttp.response);
		}
	};
	xmlhttp.send(JSON.stringify(data));
}