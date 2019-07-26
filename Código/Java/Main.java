package main_package;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.List;

import com.ibm.cloud.sdk.core.service.security.IamOptions;
import com.ibm.watson.visual_recognition.v3.VisualRecognition;
import com.ibm.watson.visual_recognition.v3.model.ClassResult;
import com.ibm.watson.visual_recognition.v3.model.ClassifiedImages;
import com.ibm.watson.visual_recognition.v3.model.ClassifyOptions;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String apiKey = "";
		String classifierId = "";
		String imageFileName = "";
		Float threshold = new Float(0.4);
		
		IamOptions options = new IamOptions.Builder()
				  .apiKey(apiKey)
				  .build();

		VisualRecognition service = new VisualRecognition("2018-03-19", options);
		
		InputStream imagesStream = null;
		try {
			imagesStream = new FileInputStream("../../Imágenes_vehículos_dañados/Test/" + imageFileName);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		ClassifyOptions classifyOptions = new ClassifyOptions.Builder()
		  .imagesFilename(imageFileName)
		  .imagesFile(imagesStream)
		  .threshold(threshold)
		  .classifierIds(Arrays.asList(classifierId))
		  .build();
		ClassifiedImages result = service.classify(classifyOptions).execute().getResult();
		//System.out.println(result);
	    List<ClassResult> daños = result.getImages().get(0).getClassifiers().get(0).getClasses();
	    for(int i=0; i<daños.size(); i++) {
	    	System.out.println("Problema: "+daños.get(i).getClassName()+" con una confianza de "+daños.get(i).getScore()*100+"%");
	    }
	}

}
