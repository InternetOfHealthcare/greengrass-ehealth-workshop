const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();
const uuid = require('uuid');


exports.handler = (event, context, callback) => {
    // TODO implement
    console.log("Systolic = "  + event.systolic + " Diastolic = " + event.diastolic);
	var params = {
		Item : {
		    "id" : uuid.v1(),
			"name" : "<<name>>",
			"bpm" : event.bpm,
			"sistolic" : event.systolic,
			"diastolic" : event.diastolic,
			"time_stamp" : new Date().toString()
		},
		TableName : "patient"
	};
	dynamoDB.put(params, function(err, data){
		callback(err, data);
	});
    callback(null, 'Hello from Lambda');
    
};