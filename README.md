# App-PASTELERIA-113-4A

## Descripción

Aplicación web desarrollada con Django 5.0 y MySQL/MariaDB para gestionar los productos de una pastelería.

El proyecto implementa las operaciones CRUD (Create, Read, Update y Delete), permitiendo crear, consultar, modificar y eliminar productos desde una interfaz web.

Este desarrollo corresponde a la Evaluación Sumativa N.º 2 de Programación Back-End.

## Tecnologías utilizadas

- Python
- Django 5.0.14
- MySQL/MariaDB
- XAMPP
- mysqlclient 2.2.8
- HTML y CSS
- Git y GitHub

## Funcionalidades

- Página principal de la aplicación.
- Listado de productos registrados.
- Creación de nuevos productos.
- Consulta individual de productos.
- Edición de productos existentes.
- Eliminación de productos mediante confirmación.
- Validación de campos obligatorios.
- Validación de precios mayores o iguales a 1.
- Validación de stock no negativo.
- Presentación de errores en español.
- Persistencia de datos mediante MySQL/MariaDB.

## Requisitos previos

Para ejecutar la aplicación en un entorno local, se necesita:

- Python 3.12.
- MySQL/MariaDB, disponible mediante XAMPP.
- Git para clonar el repositorio.
- Visual Studio Code u otro editor de código.

## Instalación de dependencias

### 1. Clonar el repositorio

```powershell
git clone https://github.com/Mausgier/App-PASTELERIA-113-4A.git
cd App-PASTELERIA-113-4A
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Este comando instala las dependencias y versiones declaradas en `requirements.txt`, incluyendo Django 5.0.14 y mysqlclient 2.2.8.

## Configuración de la base de datos

### 1. Iniciar MySQL/MariaDB

Abre el panel de control de XAMPP e inicia los servicios **Apache** y **MySQL**.

Luego, accede a phpMyAdmin desde el navegador:

http://localhost/phpmyadmin/

### 2. Crear la base de datos

Desde phpMyAdmin, crea una base de datos con el siguiente nombre:

`pasteleria_db`

No es necesario crear manualmente las tablas de productos, ya que Django se encargará de ello mediante las migraciones.

### 3. Revisar la conexión de Django

Abre el archivo `pasteleria/settings.py` y verifica la sección `DATABASES`.

La configuración debe utilizar el motor MySQL y apuntar a la base de datos `pasteleria_db`.

El usuario, la contraseña, el servidor y el puerto deben coincidir con la configuración local de MySQL/MariaDB.

### 4. Aplicar las migraciones

Con MySQL/MariaDB iniciado y el entorno virtual activado, ejecuta desde la raíz del proyecto:

```powershell
python manage.py migrate
```

Este comando aplica las migraciones pendientes y crea las tablas necesarias en la base de datos.

## Ejecución de la aplicación

Para iniciar el servidor de desarrollo de Django, ejecuta:

```powershell
python manage.py runserver
```

Después, abre la siguiente dirección en el navegador:

http://127.0.0.1:8000/

Desde la aplicación podrás acceder al listado de productos y utilizar las operaciones CRUD.

Para detener el servidor, presiona `Ctrl + C` en la terminal.
