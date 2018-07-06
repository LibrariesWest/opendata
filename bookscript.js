// IE compatible fetch command
var getJSON = function (url, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.responseType = 'json';
	xhr.onload = function () {
		var status = xhr.status;
		if (status === 200) {
			callback(null, xhr.response);
		} else {
			callback(status, xhr.response);
		}
	};
	xhr.send();
};

document.addEventListener("DOMContentLoaded", function () {
	// Get the current page
	var path = window.location.pathname;
	var page = path.split("/").pop();

	if (page === 'all-files.html') {
		getJSON('https://api.github.com/repos/librarieswest/opendata/commits',
			function (err, data) {
				if (data) {
					console.log(data);
				}
			});
	}
});