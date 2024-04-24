#!/usr/bin/node

// Importing required modules
const fs = require('fs');
const request = require('request');

// Using command line arguments to fetch the source URL and destination file path
const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];

// Making a request to the source URL and piping the response to a writable stream
request(sourceURL).pipe(fs.createWriteStream(destinationFilePath));
