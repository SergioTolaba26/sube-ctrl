import {
    obtenerEjercicios,
    obtenerCuentas,
    obtenerAsientos,
} from "./api.js";

import {
    crearPagina,
} from "./components/page.js";


export function mostrarDashboard() {

    document.getElementById(
        "contenido",
    ).innerHTML = `

        <h2>Dashboard</h2>

        <p>Bienvenido a Cloud Conta</p>

    `;

}


// --------------------------------------------------
// EJERCICIOS
// --------------------------------------------------

export async function mostrarEjercicios() {

    const contenido =
        document.getElementById(
            "contenido",
        );

    contenido.innerHTML =
        "<h2>Ejercicios</h2><p>Cargando...</p>";

    try {

        const ejercicios =
            await obtenerEjercicios();

        contenido.innerHTML =
            crearPagina({

                titulo: "Ejercicios",

                botones: [

                    {
                        id: "btn-nuevo-ejercicio",
                        texto: "Nuevo",
                        icono: "➕",
                    },

                    {
                        id: "btn-actualizar-ejercicio",
                        texto: "Actualizar",
                        icono: "🔄",
                    },

                ],

                columnas: [

                    "ID",
                    "Año",
                    "Estado",

                ],

                filas: ejercicios.map(

                    ejercicio => [

                        ejercicio.id,
                        ejercicio.anio,
                        ejercicio.estado,

                    ]

                ),

            });

    }

    catch (error) {

        contenido.innerHTML = `

            <h2>Ejercicios</h2>

            <p>Error al consultar la API.</p>

        `;

        console.error(error);

    }

}


// --------------------------------------------------
// PLAN DE CUENTAS
// --------------------------------------------------

export async function mostrarCuentas() {

    const contenido =
        document.getElementById(
            "contenido",
        );

    contenido.innerHTML =
        "<h2>Plan de cuentas</h2><p>Cargando...</p>";

    try {

        const cuentas =
            await obtenerCuentas();

        contenido.innerHTML =
            crearPagina({

                titulo: "Plan de cuentas",

                botones: [

                    {
                        id: "btn-nueva-cuenta",
                        texto: "Nueva",
                        icono: "➕",
                    },

                    {
                        id: "btn-actualizar-cuentas",
                        texto: "Actualizar",
                        icono: "🔄",
                    },

                ],

                columnas: [

                    "Código",
                    "Nombre",
                    "Tipo",
                    "Activa",

                ],

                filas: cuentas.map(

                    cuenta => [

                        cuenta.codigo,
                        cuenta.nombre,
                        cuenta.tipo,
                        cuenta.activa ? "Sí" : "No",

                    ]

                ),

            });

    }

    catch (error) {

        contenido.innerHTML = `

            <h2>Plan de cuentas</h2>

            <p>Error al consultar la API.</p>

        `;

        console.error(error);

    }

}


// --------------------------------------------------
// ASIENTOS
// --------------------------------------------------

export async function mostrarAsientos() {

    const contenido =
        document.getElementById(
            "contenido",
        );

    contenido.innerHTML =
        "<h2>Asientos</h2><p>Cargando...</p>";

    try {

        const asientos =
            await obtenerAsientos();

        contenido.innerHTML =
            crearPagina({

                titulo: "Asientos",

                botones: [

                    {
                        id: "btn-nuevo-asiento",
                        texto: "Nuevo",
                        icono: "➕",
                    },

                    {
                        id: "btn-actualizar-asientos",
                        texto: "Actualizar",
                        icono: "🔄",
                    },

                ],

                columnas: [

                    "ID",
                    "Fecha",
                    "Descripción",
                    "Estado",

                ],

                filas: asientos.map(

                    asiento => [

                        asiento.id,
                        asiento.fecha,
                        asiento.descripcion,
                        asiento.estado,

                    ]

                ),

            });

    }

    catch (error) {

        contenido.innerHTML = `

            <h2>Asientos</h2>

            <p>Error al consultar la API.</p>

        `;

        console.error(error);

    }

}