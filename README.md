# magneto-api
Una interfaz para ayudar a Magneto a identificar mutantes

## Requerimientos locales
    * Python 3.7
    * pip3
    * Base de datos postgres    

### Como instalar
    * Una vez clonado el proyecto, ejecutar en la carpeta raiz del proyecto el siguiente comando: 
        pip install -r requierments.txt
        
    * Ejecutar los siguientes comandos:
        export FLASK_APP=main
        export FLASK_DEBUG=1
        
    * Crear la estructura de la base de datos en postgres ejecutando lo siguienteen psql:
        create database magneto_api
        CREATE TABLE dna (
             id SERIAL ,
             sequences json NOT NULL,	 
             is_mutant BOOLEAN NOT NULL,
             created_date timestamp DEFAULT now(),
             updated_date timestamp DEFAULT now()	 
        );
    * Modificar el archivo config.ini colocando los parametros correctos de tu conexion al servidor de postgres
       
### Para levantar la interfaz
    flask run --host=0.0.0.0
    
### Para ejecutar los tests
    python -m unittest /path/al/proyecto/magneto-api/api/controllers/tests/test_mutant_controller.py
    python -m unittest /path/al/proyecto/magneto-api/api/tests/test_mutant_endpoint.py
     
## Ejecutar remoto (GAE)

    URL: https://magneto-api.rj.r.appspot.com