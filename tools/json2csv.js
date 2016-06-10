#!/usr/bin/env node
/*
 * Fully read JSON file, parse included objects and output them as CSV using NodeJS.
 * 
 * Call it like json2csv.js -f test.json [-r objectName] [-p 'comma separated list of to be converted properties']
 * 
 * No escaping of output data is done. The input data is assumed to be an array of objects. The objects should have 
 * all relevant fields in common. The number of columns in the CSV output is the sum over all different object fields.
 * The parameter objectName may point to a first level object included the array of interest (Json like {"object": [...]}).
 * 
 * The script can be easily adjusted to collect only certain fields - see commented out section below.
 */

'use strict';

var filename;
if(process.argv.indexOf("-f") != -1){
	filename = process.argv[process.argv.indexOf("-f") + 1];
}

var fs = require('fs');
var text = fs.readFileSync(filename).toString();

var list;
if(process.argv.indexOf("-r") != -1){
	var objectName = process.argv[process.argv.indexOf("-r")+1];
	list = JSON.parse(text)[objectName];
} else {
	list = JSON.parse(text);
}
var listLength = list.length;

var properties = {};
if(process.argv.indexOf("-p") != -1){
	 process.argv[process.argv.indexOf("-p")+1].split(',').reduce(function fct(properties, name){properties[name]=null; return properties}, properties);
} else {

	for (var i = 0; i < listLength; i++) {
		var obj = list[i];
		for(var propt in obj) {
			properties[propt] = null;
		}
	}

}

/*
 * Hard coded list of properties of interest.
 */
//properties = {
//		propA: null,
//		propB: null
//} 

var csvLine = "";
for(var propt in properties) {
	if (csvLine.length > 0) {
		csvLine += ",";
	}
	csvLine += propt;
}
console.log(csvLine);

for (var i = 0; i < listLength; i++) {
	var obj = list[i];
	var csvLine = "";
	for(var propt in properties) {
		if (csvLine.length > 0) {
			csvLine += ",";
		}
		csvLine += obj[propt];
	}
	console.log(csvLine);
}

