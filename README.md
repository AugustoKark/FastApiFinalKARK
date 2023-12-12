# FastApiFinalKARK
Diseño de Sistemas 2023

Alumno: Augusto Kark


En este repositorio se encuentra el proyecto final de la materia de Diseño de Sistemas 2023, el cual consiste en la implementación de una API REST utilizando el framework FastAPI.
Dicha API se ha modelado siguiendo la arquitectura vista en JAVA durante el cursado, por lo que se ha implementado una capa de controladores, una capa de servicios y una capa de repositorios. Además, se ha utilizado una base de datos PostgreSQL para almacenar los datos de la API.

## Instalación
Para instalar el proyecto, se debe clonar el repositorio y crear un entorno virtual con el siguiente comando:

```bash
python -m venv env
```
Posteriormente, se debe activar el entorno virtual y ejecutar el siguiente comando para instalar las dependencias:
```bash
source env/bin/activate
pip install -r requirements.txt
```
## Ejecución
Para ejecutar el proyecto, se debe activar el entorno virtual y ejecutar el siguiente comando:
```bash
uvicorn main:app --reload
``` 
o bien, se puede ejecutar directamente el archivo main.py


## Uso
Para utilizar la API, se adjunta un archivo de Postamn con los endpoints correspondientes.




