El archivo model.py requiere la instalacion de los requerimientos en "requirements.txt"
El modelo divide a los clientes en 3 categorias dependiendo de que tanto gastan en el almacen.
El modelo esta dividido en 6 funciones para tener la facilidad a la hora de evaluar.
load_data(): Carga datos desde un archivo de excel.
preprocess_data(): Normaliza los datos de la fecha de compra.
calculate_features(): Calcula las caracteristicas de cada cliente.
create_model(): crea un modelo de keras.
train_model(): Entrena el modelo con la configuracion que deseemos.
evaluate_model(): Evalua el rendimiento del modelo (perdida y precision)

Para probar el correcto funcionamiento podemos ejecutar "Unit test 1.py" y otros archivos de pruebas