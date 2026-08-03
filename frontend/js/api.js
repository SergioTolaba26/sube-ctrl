//const API_URL = "http://192.168.0.9:8000";//casa
//const API_URL = "http://192.168.3.124:8000";//trabajo
const API_URL = "http://127.0.0.1:8000";
/*******************************
 * EJERCICIOS
 *******************************/

export async function obtenerEjercicios() {

    const respuesta = await fetch(

        `${API_URL}/ejercicios`

    );

    if (!respuesta.ok) {

        throw new Error(

            "No se pudieron obtener los ejercicios."

        );

    }

    return await respuesta.json();

}

export async function crearEjercicio(
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/ejercicios/`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(
                datos,
            ),

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}

export async function actualizarEjercicio(
    id,
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/ejercicios/${id}`,

        {

            method: "PUT",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(
                datos,
            ),

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}

export async function eliminarEjercicio(
    id,
) {

    const respuesta = await fetch(

        `${API_URL}/ejercicios/${id}`,

        {

            method: "DELETE",

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}

/*******************************
 * PLAN DE CUENTAS
 *******************************/

export async function obtenerCuentas() {

    const respuesta = await fetch(

        `${API_URL}/cuentas`

    );

    if (!respuesta.ok) {

        throw new Error(

            "No se pudieron obtener las cuentas."

        );

    }

    return await respuesta.json();

}


export async function crearCuenta(
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/cuentas/`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(
                datos,
            ),

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}


export async function actualizarCuenta(
    id,
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/cuentas/${id}`,

        {

            method: "PUT",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(
                datos,
            ),

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}


export async function eliminarCuenta(
    id,
) {

    const respuesta = await fetch(

        `${API_URL}/cuentas/${id}`,

        {

            method: "DELETE",

        },

    );

    if (!respuesta.ok) {

        const error =
            await respuesta.json();

        throw new Error(

            JSON.stringify(
                error,
                null,
                2,
            ),

        );

    }

    return await respuesta.json();

}

/*******************************
 * ASIENTOS
 *******************************/
export async function obtenerAsientos() {

    const respuesta = await fetch(

        `${API_URL}/movimientos/`

    );

    if (!respuesta.ok) {

        throw new Error(

            "No se pudieron obtener los asientos."

        );

    }

    return await respuesta.json();

}
export async function obtenerAsiento(
    id,
) {

    const respuesta = await fetch(
        `${API_URL}/movimientos/${id}`,
    );

    if (!respuesta.ok) {

        throw new Error(
            "No se pudo obtener el asiento.",
        );

    }

    return await respuesta.json();

}

export async function crearAsiento(

    datos,

) {

    const respuesta = await fetch(

        `${API_URL}/movimientos/`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(

                datos,

            ),

        },

    );

    if (!respuesta.ok) {

        const error =

            await respuesta.json();

        throw new Error(

            JSON.stringify(

                error,

                null,

                2,

            ),

        );

    }

    return await respuesta.json();

}


export async function actualizarAsiento(

    id,

    datos,

) {

    const respuesta = await fetch(

        `${API_URL}/movimientos/${id}`,

        {

            method: "PUT",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(

                datos,

            ),

        },

    );

    if (!respuesta.ok) {

        const error =

            await respuesta.json();

        throw new Error(

            JSON.stringify(

                error,

                null,

                2,

            ),

        );

    }

    return await respuesta.json();

}

export async function actualizarLineaAsiento(
    movimientoId,
    lineaIndex,
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/movimientos/${movimientoId}/lineas/${lineaIndex}`,

        {

            method: "PUT",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(datos),

        },

    );

    if (!respuesta.ok) {

        throw new Error(
            await respuesta.text(),
        );

    }

    return await respuesta.json();

}
export async function eliminarAsiento(

    id,

) {

    const respuesta = await fetch(

        `${API_URL}/movimientos/${id}`,

        {

            method: "DELETE",

        },

    );

    if (!respuesta.ok) {

        const error =

            await respuesta.json();

        throw new Error(

            JSON.stringify(

                error,

                null,

                2,

            ),

        );

    }

    return await respuesta.json();

}