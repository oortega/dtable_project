# Listado de datos con Django y DataTables

### Instalación de Versiones

## __Python 2__ 

### 1._ Crear carpeta dentro de la carpeta venv2.
    mkdir .venv2
    
### 2._ poosicionarse en la carpeta .venv2 
    cd .venv2

### 3._ Exportar la variable WORKON_HOME, para que el entorno se cree en esta ruta.
    Ejemplo:
    pwd      
    /var/www/dtable_project/venv2/.venv2

    export WORKON_HOME=/var/www/dtable_project/venv2/.venv2

### 4._ Activar el entorno
    pipenv shell --two

### 5._ Instalar las dependencias
    pipenv update

    
## __Python 3__ 

### 1._ Crear carpeta dentro de la carpeta venv3.
    mkdir .venv3
    
### 2._ poosicionarse en la carpeta .venv3 
    cd .venv3

### 3._ Exportar la variable WORKON_HOME, para que el entorno se cree en esta ruta.
    Ejemplo:
    pwd      
    /var/www/dtable_project/venv3/.venv3

    export WORKON_HOME=/var/www/dtable_project/venv3/.venv3

### 4._ Activar el entorno
    pipenv shell --three

### 5._ Instalar las dependencias
    pipenv update

### Nota: si al realizar __pipenv update__ genera algun error, debe realizar las instalaciones de las dependencias del Pipfile una por una.