#!/usr/bin/env node
/*
 * Fully read JSON file, parse included objects and output them as CSV using NodeJS.
 * 
 * Call it like json2csv.js test.json 
 * 
 * No escaping of output data is done. The input data is assumed to be an array of objects. The objects should have 
 * all relevant fields in common. The number of columns in the CSV output is the sum over all different object fields.
 */

'use strict';

var filename = process.argv[2]; // first argument
var fs = require('fs');

var text = fs.readFileSync(filename).toString();

var list = JSON.parse(text);
var listLength = list.length;
var properties = {};
for (var i = 0; i < listLength; i++) {
	var obj = list[i];
	for(var propt in obj){
		properties[propt] = null;
	}
}

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

