// Ejecuta solicitudes JSON a la API protegida.
async function apiProductos(metodo, ruta, datos) {

    const token = sessionStorage.getItem('token');

    if (!token) {
        throw new Error(
            'No hay token disponible. Regresa al inicio, ' +
            'cierra sesión y vuelve a ingresar.'
        );
    }

    const headers = {
        'Accept': 'application/json',
        'Authorization': 'Token ' + token
    };

    if (datos !== undefined) {
        headers['Content-Type'] = 'application/json';
    }

    let respuesta;

    try {
        respuesta = await fetch(ruta, {
            method: metodo,
            headers: headers,
            body: datos !== undefined
                ? JSON.stringify(datos)
                : undefined
        });
    } catch (error) {
        throw new Error('No se pudo conectar con el servidor.');
    }

    const resultado = respuesta.status === 204
        ? null
        : await respuesta.json();

    if (!respuesta.ok) {

        if (respuesta.status === 401) {
            sessionStorage.removeItem('token');
            throw new Error(
                'Token inválido o expirado. Regresa al inicio, ' +
                'cierra sesión y vuelve a ingresar.'
            );
        }

        if (respuesta.status === 404) {
            throw new Error('Producto no encontrado.');
        }

        // Convertir los errores de validación en texto legible.
        if (resultado && typeof resultado === 'object') {
            const mensajes = Object.entries(resultado).map(
                ([campo, errores]) => {
                    const detalle = Array.isArray(errores)
                        ? errores.join(', ')
                        : String(errores);

                    return campo + ': ' + detalle;
                }
            );

            throw new Error(mensajes.join(' | '));
        }

        throw new Error('Error HTTP ' + respuesta.status);
    }

    return resultado;
}


// Obtener los datos del formulario como un objeto 'JSON'.
function leerProducto(formulario) {

    const datos = new FormData(formulario);

    function leerNumero(campo) {
        const valor = datos.get(campo);
        return valor === '' ? null : Number(valor);
    }

    return {
        nombre: datos.get('nombre'),
        descripcion: datos.get('descripcion'),
        categoria: datos.get('categoria'),
        precio: leerNumero('precio'),
        stock: leerNumero('stock')
    };
}


// Obtener nombre legible de una categoría.
function nombreCategoria(categoria) {

    const categorias = {
        torta: 'Torta',
        pastel: 'Pastel',
        galleta: 'Galleta',
        otro: 'Otro'
    };

    return categorias[categoria] || categoria;
}

