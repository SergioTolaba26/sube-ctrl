// ======================================================
// CONFIGURACIÃ“N
// ======================================================

const API_URL = "http://192.168.0.9:8000";     // Casa
// const API_URL = "http://192.168.3.124:8000";   // Trabajo

//const API_URL = "http://127.0.0.1:8000";

async function procesarRespuesta(respuesta) {

    if (!respuesta.ok) {

        let error;

        try {

            error = await respuesta.json();

        } catch {

            throw new Error(
                await respuesta.text()
            );

        }

        throw new Error(
            JSON.stringify(
                error,
                null,
                2
            )
        );
    }

    return await respuesta.json();
}



// ======================================================
// EJERCICIOS
// ======================================================

export async function obtenerEjercicios() {

    const respuesta = await fetch(

        `${API_URL}/ejercicios`

    );

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
}



// ======================================================
// PLAN DE CUENTAS
// ======================================================

export async function obtenerCuentas() {

    const respuesta = await fetch(

        `${API_URL}/cuentas`

    );

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
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

    return await procesarRespuesta(
        respuesta
    );
}
//---------fin uno
// ======================================================
// ASIENTOS
// ======================================================

export async function obtenerAsientos() {

    const respuesta = await fetch(

        `${API_URL}/asientos/`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function obtenerAsiento(
    id,
) {

    const respuesta = await fetch(

        `${API_URL}/asientos/${id}`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function crearAsiento(
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/asientos/`,

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

    return await procesarRespuesta(
        respuesta
    );

}



export async function actualizarAsiento(
    id,
    datos,
) {

    const respuesta = await fetch(

        `${API_URL}/asientos/${id}`,

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

    return await procesarRespuesta(
        respuesta
    );

}


export async function eliminarAsiento(
    id,
) {

    const respuesta = await fetch(

        `${API_URL}/asientos/${id}`,

        {

            method: "DELETE",

        },

    );

    return await procesarRespuesta(
        respuesta
    );

}
//-----------fin txt 2
// ======================================================
// REPORTES CONTABLES
// ======================================================

export async function obtenerLibroDiario() {

    const respuesta = await fetch(

        `${API_URL}/libro-diario`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function obtenerLibroMayor() {

    const respuesta = await fetch(

        `${API_URL}/libro-mayor`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function obtenerBalanceSumasSaldos() {

    const respuesta = await fetch(

        `${API_URL}/balance-sumas-saldos`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function obtenerBalanceGeneral() {

    const respuesta = await fetch(

        `${API_URL}/balance-general`

    );

    return await procesarRespuesta(
        respuesta
    );

}



export async function obtenerEstadoResultados() {

    const respuesta = await fetch(

        `${API_URL}/estado-resultados`

    );

    return await procesarRespuesta(
        respuesta
    );

}

export async function confirmarAsiento(
    movimientoId,
) {

    const response = await fetch(

        `${API_URL}/asientos/${movimientoId}/confirmar`,

        {
            method: "POST",
        },

    );

    if (!response.ok) {

        const error = await response.json();

        throw new Error(

            error.detail ||

            "No se pudo confirmar el asiento.",

        );

    }

    return await response.json();

}
