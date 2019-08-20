import json
from ibm_watson import VisualRecognitionV3

# autenticación mediante API_KEY
visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='Y4Db8xaokVYtKrTgZQY8P3Dskwat_9Jn74KJ-9qQeD1h')
        

#Creación del modelo, se debe sustituir {model_name} por el nombre que desee asignarle al modelo, al
#igual que hicimos en la interface, asiganmos a una clase positiva los ejemplos con ojos cerrados y
#como negativa los ejemplos con ojos abiertos

with open('./../Imagenes_vehiculos_danados/Entrenamiento/espejo_roto_entrenamiento.zip', 'rb') as espejos_rotos, open('./../Imagenes_vehiculos_danados/Entrenamiento/faros_rotos_entrenamiento.zip', 'rb') as faros_rotos, open('./../Imagenes_vehiculos_danados/Entrenamiento/neumaticos_pinchados_entrenamiento.zip', 'rb') as neumaticos_pinchados, open('./../Imagenes_vehiculos_danados/Entrenamiento/neumaticos_sanos_entrenamiento.zip', 'rb') as neumaticos_sanos, open('./../Imagenes_vehiculos_danados/Entrenamiento/paragolpes_roto_entrenamiento.zip', 'rb') as paragolpes_roto, open('./../Imagenes_vehiculos_danados/Entrenamiento/puerta_chocada_entrenamiento.zip', 'rb') as puerta_chocada, open('./../Imagenes_vehiculos_danados/Entrenamiento/vidrio_frontal_roto_entrenamiento.zip', 'rb') as vidrio_frontal_roto, open('./../Imagenes_vehiculos_danados/Entrenamiento/vidrio_lateral_roto_entrenamiento.zip', 'rb') as vidrio_lateral_roto, open('./../Imagenes_vehiculos_danados/Entrenamiento/vehiculos_sanos_entrenamiento.zip', 'rb') as vehiculos_sanos:
    model = visual_recognition.create_classifier('tasador_eXpand',
        positive_examples={'espejos_rotos': espejos_rotos, 'faros_rotos': faros_rotos, 'neumaticos_pinchados': neumaticos_pinchados,'neumaticos_sanos': neumaticos_sanos,'paragolpes_roto': paragolpes_roto,'puerta_chocada': puerta_chocada,'vidrio_frontal_roto': vidrio_frontal_roto,'vidrio_lateral_roto': vidrio_lateral_roto},
        negative_examples=vehiculos_sanos).get_result()  
    #obtener datos del modelo recien creado
    model_id = model['classifier_id']
    model_name = model['name']
    model_status = model['status']
    model_create_date = model['created']
    model_class = model['classes'][0]['class']

print("Datos del Modelo recien creado.")
print("Nombre del modelo: " + model_id)
print("ID del modelo: " + model_id)
print("Fecha de creación: " + model_create_date)



#obtener el clasificador recien creado
classifier = visual_recognition.get_classifier(classifier_id=model_id).get_result()