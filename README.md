# App Pastelería — Sistema de gestión de productos

Aplicación web desarrollada con **Python, Django y MySQL/MariaDB** para administrar un catálogo de productos de pastelería. Incluye una interfaz HTML para el usuario, autenticación mediante sesión y token, validaciones de datos y una **API REST** que permite consultar, registrar, actualizar y eliminar productos mediante JSON.

El repositorio está organizado para continuar incorporando funcionalidades sin reemplazar la base existente.

## Contenido

- [Descripción y alcance](#descripción-y-alcance)
- [Tecnologías](#tecnologías)
- [Funcionalidades](#funcionalidades)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación y configuración](#instalación-y-configuración)
- [Ejecución y uso](#ejecución-y-uso)
- [Modelo de datos y validaciones](#modelo-de-datos-y-validaciones)
- [Autenticación y control de acceso](#autenticación-y-control-de-acceso)
- [API REST](#api-rest)
- [Verificación manual del funcionamiento](#verificación-manual-del-funcionamiento)
- [Solución de problemas frecuentes](#solución-de-problemas-frecuentes)
- [Consideraciones de seguridad](#consideraciones-de-seguridad)
- [Posibles ampliaciones](#posibles-ampliaciones)

## Descripción y alcance

El sistema gestiona la información básica de los productos disponibles en una pastelería. Cada producto contiene un nombre, una descripción opcional, una categoría, un precio y una cantidad en stock.

La aplicación ofrece dos formas de interactuar con esos datos:

1. **Interfaz web:** páginas HTML con navegación, formularios de productos y mensajes de error. JavaScript envía solicitudes a la API y actualiza la información mostrada.
2. **API REST:** endpoints protegidos que reciben y responden datos JSON. Utilizan los modelos de Django para consultar y persistir registros en MySQL/MariaDB.

La página de bienvenida es pública. Para gestionar productos desde la interfaz se requiere iniciar sesión. Los endpoints de productos exigen un token de autenticación válido.

**Alcance actual:** gestión del catálogo de productos y autenticación de usuarios. El proyecto no incorpora todavía pedidos, ventas, carrito de compras, pagos ni gestión de clientes.

## Tecnologías

| Tecnología | Uso en el proyecto |
| --- | --- |
| Python 3.12 | Lenguaje utilizado en el entorno de desarrollo |
| Django 5.0.14 | Framework web, modelos, rutas, vistas, sesiones y migraciones |
| Django REST Framework 3.17.2 | API REST, serialización, validaciones y autenticación por token |
| MySQL/MariaDB | Almacenamiento persistente de productos, usuarios y tokens |
| `mysqlclient` 2.2.8 | Conexión de Django con la base de datos |
| HTML y CSS | Estructura y presentación de las páginas |
| JavaScript | Solicitudes `fetch`, envío de JSON e interacción con la API |
| XAMPP y phpMyAdmin | Administración local de MySQL/MariaDB y consulta de tablas |
| Git y GitHub | Control de versiones y mantenimiento del código |

Las dependencias de Python y sus versiones están registradas en [`requirements.txt`](requirements.txt).

## Funcionalidades

### Interfaz web

- Página de inicio con navegación hacia el catálogo y la autenticación.
- Formulario de inicio de sesión con mensajes ante credenciales incorrectas.
- Cierre de sesión.
- Listado de productos registrados, con mensaje cuando no existen registros.
- Formulario para crear productos.
- Consulta del detalle de un producto.
- Formulario para editar la información existente.
- Página de confirmación antes de eliminar un producto.
- Presentación de errores devueltos por la API, incluidos los de validación y autenticación.

### API y persistencia

- Operaciones **GET, POST, PUT y DELETE** sobre productos.
- Consultas del listado y de productos individuales por ID.
- Intercambio de información mediante JSON.
- Comprobación de credenciales y entrega de un token al iniciar sesión.
- Restricción de endpoints mediante `TokenAuthentication` e `IsAuthenticated`.
- Validaciones antes de crear o actualizar registros.
- Respuestas HTTP apropiadas para operaciones exitosas, datos inválidos, falta de autenticación y registros inexistentes.
- Persistencia de datos mediante el ORM de Django y MySQL/MariaDB.

## Estructura del proyecto

```text
App-PASTELERIA-113-4A/
├── manage.py
├── requirements.txt
├── README.md
├── pasteleria/
│   ├── settings.py                 # Configuración de Django, MySQL y DRF
│   └── urls.py                     # Rutas principales del proyecto
└── pasteleria_app/
    ├── models.py                   # Modelo Producto
    ├── forms.py                    # Formulario basado en Producto
    ├── serializers.py              # Conversión y validación de datos JSON
    ├── views.py                    # Páginas web, login, logout y perfil
    ├── api_views.py                # Operaciones REST de productos
    ├── urls.py                     # Rutas web y endpoints API
    ├── migrations/
    │   └── 0001_initial.py         # Migración inicial de Producto
    ├── static/
    │   └── pasteleria_app/
    │       └── api.js              # Funciones JavaScript para la API
    └── templates/
        └── pasteleria_app/
            ├── inicio.html
            ├── login.html
            ├── lista.html
            ├── crear.html
            ├── detalle.html
            ├── editar.html
            └── eliminar.html
```

Los directorios también pueden contener otros archivos generados por Django, como `__init__.py`, `apps.py`, `admin.py` y `tests.py`, además de los indicados en el esquema.

## Requisitos previos

Para ejecutar la aplicación localmente se necesita:

- **Python 3.12** instalado.
- **MySQL o MariaDB** en funcionamiento. En Windows puede utilizarse XAMPP.
- **Git**, si se clonará el repositorio.
- Un navegador web actualizado.
- Un editor de código, como Visual Studio Code, si se realizarán modificaciones.

Los comandos siguientes utilizan **PowerShell en Windows**. Se asume que el servidor MySQL escucha en `127.0.0.1:3306`, como establece la configuración actual del proyecto.

## Instalación y configuración

### 1. Obtener el código

```powershell
git clone https://github.com/Mausgier/App-PASTELERIA-113-4A.git
cd App-PASTELERIA-113-4A
```

### 2. Crear y activar el entorno virtual

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si `py -3.12` no está disponible, comprueba la instalación de Python y ajusta el comando según la versión instalada.

### 3. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 4. Iniciar y preparar MySQL/MariaDB

1. Abre el panel de XAMPP e inicia **MySQL**.
2. Abre phpMyAdmin, normalmente en <http://localhost/phpmyadmin/>. Para utilizar phpMyAdmin desde XAMPP, puede ser necesario iniciar también Apache.
3. Crea una base de datos denominada **`pasteleria_db`** si todavía no existe.
4. Revisa la configuración `DATABASES` de `pasteleria/settings.py` y comprueba que coincidan el nombre de la base, usuario, contraseña, host y puerto con tu instalación local.

La configuración incluida actualmente utiliza `pasteleria_db`, el usuario `root`, contraseña vacía, `127.0.0.1` y puerto `3306`. **Es una configuración de desarrollo local y no debe reutilizarse en producción.**

No es necesario crear manualmente las tablas: Django las administra mediante migraciones.

### 5. Aplicar migraciones

```powershell
python manage.py migrate
```

Este comando prepara las tablas del framework, la autenticación, los tokens, las sesiones y el modelo de productos. Para revisar el estado de las migraciones:

```powershell
python manage.py showmigrations
```

Las migraciones aplicadas aparecen marcadas con `[X]`.

### 6. Crear un usuario de acceso

```powershell
python manage.py createsuperuser
```

Sigue las instrucciones de la terminal para registrar el usuario y su contraseña. Este comando es una forma sencilla de crear una cuenta inicial; la aplicación también puede autenticar usuarios activos normales de Django.

No incluyas contraseñas ni tokens reales en el repositorio.

### 7. Comprobar la configuración

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
```

El primer comando revisa la configuración de Django. El segundo comprueba si hay cambios del modelo que todavía requieran una migración.

## Ejecución y uso

Inicia el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador. El flujo normal es:

1. Entrar en **Iniciar sesión** e introducir un usuario y una contraseña válidos.
2. Acceder a **Ver productos** para consultar el catálogo.
3. Seleccionar **Crear nuevo producto** para registrar uno.
4. Abrir **Ver detalle** para consultar, editar o eliminar un producto.
5. Usar **Cerrar sesión** desde la página de inicio cuando finalices.

Las operaciones de la interfaz consumen la API mediante JavaScript. Los datos creados o modificados se guardan en MySQL/MariaDB.

Detén el servidor con `Ctrl + C` cuando termines de trabajar.

### Rutas de la interfaz

| Ruta | Función | Acceso |
| --- | --- | --- |
| `/` | Página de bienvenida | Público |
| `/login/` | Formulario de inicio de sesión | Público; redirige si ya hay sesión |
| `/logout/` | Cierre de sesión mediante POST | Sesión requerida |
| `/productos/` | Listado | Sesión requerida |
| `/productos/crear/` | Formulario de creación | Sesión requerida |
| `/productos/<id>/` | Detalle | Sesión requerida |
| `/productos/<id>/editar/` | Formulario de edición | Sesión requerida |
| `/productos/<id>/eliminar/` | Confirmación de eliminación | Sesión requerida |

`<id>` representa el identificador numérico del producto. Las páginas HTML muestran los formularios y los datos; las operaciones de lectura y escritura sobre productos se realizan a través de la API.

## Modelo de datos y validaciones

El modelo `Producto` se define en `pasteleria_app/models.py`.

| Campo | Tipo | Reglas principales |
| --- | --- | --- |
| `id` | `BigAutoField` | Clave primaria generada automáticamente; no editable desde la API |
| `nombre` | `CharField` | Obligatorio; hasta 100 caracteres; no puede contener solo espacios |
| `descripcion` | `TextField` | Opcional; admite una cadena vacía |
| `categoria` | `CharField` | Una de las categorías admitidas |
| `precio` | `DecimalField` | Hasta 10 dígitos y 0 decimales; valor mínimo de 1 |
| `stock` | `PositiveIntegerField` | Número entero mayor o igual a 0 |

Categorías admitidas: `torta`, `pastel`, `galleta` y `otro`.

La API exige que las solicitudes de creación y actualización incluyan `nombre`, `categoria`, `precio` y `stock`. `descripcion` es opcional. Aunque algunos campos del modelo tienen valores predeterminados, la API exige explícitamente los campos indicados.

**Tipos JSON:** `nombre`, `descripcion` y `categoria` deben enviarse como texto; `precio` y `stock`, como números enteros JSON. Por ejemplo, `12000` es válido como precio y `"12000"` es rechazado.

`ProductoSerializer` comprueba los datos antes de guardarlos. Si existen errores, responde con HTTP `400 Bad Request` y la operación no se persiste.

## Autenticación y control de acceso

La aplicación utiliza dos mecanismos complementarios:

- **Sesión de Django:** permite acceder a las páginas HTML protegidas mediante `@login_required`.
- **Token de Django REST Framework:** permite acceder a los endpoints protegidos mediante un encabezado HTTP.

El formulario de `/login/` envía las credenciales a `POST /api/login/`. Si son correctas, el servidor inicia una sesión de Django y entrega un token asociado al usuario. El código JavaScript de la interfaz guarda ese token en `sessionStorage` y lo utiliza en las solicitudes posteriores.

El encabezado de autenticación tiene este formato:

```http
Authorization: Token TU_TOKEN
```

Reemplaza `TU_TOKEN` por un token válido. No compartas el token en capturas, registros públicos ni commits.

Al cerrar sesión, la aplicación elimina el token asociado al usuario y finaliza su sesión de Django. Los tokens básicos de `rest_framework.authtoken` **no tienen expiración automática configurada** en este proyecto; se revocan al cerrar sesión.

Si se pierde el token de `sessionStorage` mientras la sesión web sigue activa, el JavaScript mostrará un mensaje para cerrar sesión y autenticarse nuevamente. Una solicitud directa a la API sin token, o con un token incorrecto, devuelve HTTP `401 Unauthorized`.

## API REST

Los endpoints se registran en `pasteleria_app/urls.py`. Las operaciones de productos se implementan en `api_views.py` y están protegidas mediante `TokenAuthentication` e `IsAuthenticated`.

| Método | Endpoint | Descripción | Éxito |
| --- | --- | --- | --- |
| `POST` | `/api/login/` | Valida credenciales, inicia sesión y entrega un token | `200 OK` |
| `GET` | `/api/perfil/` | Comprueba la autenticación por token y devuelve el usuario | `200 OK` |
| `GET` | `/api/productos/` | Obtiene todos los productos | `200 OK` |
| `POST` | `/api/productos/` | Crea un producto | `201 Created` |
| `GET` | `/api/productos/<id>/` | Obtiene un producto por ID | `200 OK` |
| `PUT` | `/api/productos/<id>/` | Actualiza todos los campos editables de un producto | `200 OK` |
| `DELETE` | `/api/productos/<id>/` | Elimina un producto | `204 No Content` |

### Ejemplo de producto en JSON

```json
{
  "id": 1,
  "nombre": "Torta de chocolate",
  "descripcion": "Torta con cobertura de chocolate",
  "categoria": "torta",
  "precio": "12000",
  "stock": 5
}
```

Esta es una **representación de respuesta**: el campo `id` lo genera Django y el serializer puede representar el precio decimal como una cadena. Al crear o actualizar desde la API, el precio debe enviarse como **número JSON entero**, sin comillas, por ejemplo:

```json
{
  "nombre": "Torta de chocolate",
  "descripcion": "Torta con cobertura de chocolate",
  "categoria": "torta",
  "precio": 12000,
  "stock": 5
}
```

### Ejemplo de inicio de sesión

El cuerpo JSON que envía el formulario es:

```json
{
  "username": "usuario_de_ejemplo",
  "password": "contraseña_de_ejemplo"
}
```

Si las credenciales son válidas, la respuesta incluye `mensaje`, `usuario` y `token`. El login de la interfaz también utiliza la protección CSRF de Django; por ello, para el uso habitual se recomienda iniciar sesión desde `/login/`.

### Consultar productos desde PowerShell

Con un token válido y el servidor iniciado, puedes comprobar un endpoint protegido:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/productos/" `
  -Method Get `
  -Headers @{ Authorization = "Token TU_TOKEN"; Accept = "application/json" }
```

Esta operación solo consulta registros. Sustituye `TU_TOKEN` por el valor correspondiente y evita compartirlo.

### Respuestas y errores habituales

| Código HTTP | Significado en el proyecto |
| --- | --- |
| `200 OK` | Consulta, autenticación o actualización correcta |
| `201 Created` | Producto creado correctamente |
| `204 No Content` | Producto eliminado; respuesta sin cuerpo |
| `400 Bad Request` | Datos JSON o campos inválidos |
| `401 Unauthorized` | Credenciales incorrectas en el login o token ausente/inválido en la API protegida |
| `404 Not Found` | No existe el producto solicitado |

Al intentar acceder a una **página HTML** protegida sin sesión, Django normalmente redirige hacia el login en lugar de devolver el mismo JSON `401` de la API.

## Verificación manual del funcionamiento

Para comprobar el sistema desde el navegador y phpMyAdmin:

1. Verifica que MySQL está funcionando y que `python manage.py check` no informa problemas.
2. Abre `/productos/` sin sesión para comprobar la redirección hacia el login.
3. Intenta iniciar sesión con credenciales incorrectas y observa el mensaje de error; después utiliza credenciales válidas.
4. Crea un producto desde el formulario y comprueba su registro en `pasteleria_app_producto` mediante phpMyAdmin.
5. Consulta el detalle y actualiza el precio o stock; verifica el cambio tanto en la web como en MySQL.
6. Intenta guardar un precio negativo u otro dato inválido. La API debe rechazarlo y conservar los datos válidos anteriores.
7. Elimina un producto de prueba y comprueba que desaparezca de la tabla.
8. Abre directamente <http://127.0.0.1:8000/api/productos/> sin enviar un token: la API debe responder `401` con un mensaje JSON de autenticación.

Para observar los métodos y códigos HTTP, utiliza **Herramientas de desarrollador → Network → Fetch/XHR** y, si hay redirecciones, activa **Preserve log**. Evita capturar tokens o cookies de sesión completas.

## Solución de problemas frecuentes

**MySQL no conecta (`OperationalError 2002`):** comprueba que MySQL esté iniciado en XAMPP, que no haya instancias en conflicto y que el puerto coincida con `DATABASES` en `settings.py`.

**No existen tablas:** inicia MySQL y ejecuta `python manage.py migrate`.

**No se puede ingresar:** comprueba que el usuario exista y que la contraseña sea correcta. Si estás configurando una instalación nueva, crea una cuenta con `python manage.py createsuperuser`.

**Aparece un mensaje de token ausente o inválido:** vuelve a Inicio, cierra sesión y autentícate nuevamente.

**Una solicitud devuelve HTTP 400:** revisa los campos obligatorios, los tipos JSON y las reglas de precio y stock.

**Un producto devuelve HTTP 404:** comprueba que el identificador corresponda a un registro existente.

## Consideraciones de seguridad

Este repositorio está preparado para **desarrollo y ejecución local**. La configuración actual contiene valores que deben cambiarse antes de publicar el proyecto en un servidor accesible desde Internet, entre ellos `DEBUG=True`, la clave secreta de Django en `settings.py` y las credenciales locales de la base de datos.

Para un despliegue real sería necesario gestionar secretos mediante variables de entorno, usar credenciales restringidas para la base de datos, desactivar el modo DEBUG, configurar hosts permitidos y HTTPS, y revisar la gestión de sesiones y tokens.

