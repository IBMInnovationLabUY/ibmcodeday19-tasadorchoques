const VisualRecognitionV3 = require('ibm-watson/visual-recognition/v3');
const fs = require('fs');

const IAM_APIKEY = '';
const CLASSIFIER_ID = '';

// Ejemplo: IMAGE_FILE_NAME = 'd001.jpeg';
const IMAGE_FILE_NAME = '';
const THRESHOLD = 0.4;

let visualRecognition = new VisualRecognitionV3({
	version: '2018-03-19',
	iam_apikey: IAM_APIKEY
});

let images_file = fs.createReadStream('../Imagenes_vehiculos_danados/Test/' + IMAGE_FILE_NAME);
let classifier_ids = [CLASSIFIER_ID];

let params = {
	images_file: images_file,
	classifier_ids: classifier_ids,
	threshold: THRESHOLD
};

visualRecognition.classify(params, function(err, response) {
	if (err) { 
		console.log(err);
	} else {
		response.images[0].classifiers[0].classes.forEach(element => {
			console.log("Problema: "+element.class+" con una confianza de "+(element.score)*100+"%");
		});
	}
});
