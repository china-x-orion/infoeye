var exec = require('child_process').exec;
var cmd = "python ../tools/issue.py";
	exec(cmd, function(error, stdout, stderr) {
		console.log("helloword");
		console.log(stdout);
		console.log("helloword");
//		document.getElementById("os-info").value=stdout;
	});

