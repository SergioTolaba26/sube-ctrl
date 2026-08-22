
import {
    obtenerEjercicios,
    crearEjercicio,
    actualizarEjercicio,
    eliminarEjercicio,
} from "../api.js";

import {
    obtenerEmpresaSeleccionada,
} from "../estado.js";

import {
    crearPagina,
} from "../components/page.js";

import {
    abrirModal,
    cerrarModal,
} from "../components/modal.js";

import {
    conectarEventosTabla,
} from "../components/table.js";

import {
    crearFormularioEjercicio,
} from "../forms/ejercicioForm.js";

import {
    mostrarToast,
} from "../components/toast.js";


let ejercicios = [];


/*********************************************
 * LISTAR
 *********************************************/

export async function mostrarEjercicios() {

    const contenido =
        document.getElementById(
            "contenido",
        );

    contenido.innerHTML =
        "<h2>Ejercicios</h2><p>Cargando...</p>";

    try {

        const empresa =
            obtenerEmpresaSeleccionada();


        if (!empresa) {

            contenido.innerHTML = `
                <h2>Ejercicios</h2>
                <p>Seleccione una empresa.</p>
            `;

            return;
        }


        ejercicios =
            await obtenerEjercicios(
                empresa.id,
            );


        console.log(
            "Empresa para Ejercicios:",
            empresa,
        );

        console.log(
            "EJERCICIOS:",
            ejercicios,
        );


        contenido.innerHTML =
            crearPagina({

                titulo:
                    "Ejercicios",

                botones: [

                    {
                        id:
                            "btn-nuevo-ejercicio",

                        texto:
                            "Nuevo",

                        icono:
                            "➕",
                    },

                    {
                        id:
                            "btn-actualizar-ejercicio",

                        texto:
                            "Actualizar",

                        icono:
                            "🔄",
                    },

                ],

                columnas: [

                    "ID",

                    "Año",

                    "Estado",

                ],

                filas:
                    ejercicios.map(

                        ejercicio => [

                            ejercicio.id,

                            ejercicio.anio,

                            ejercicio.estado,

                        ],

                    ),

                acciones:
                    true,

            });


        conectarEventosTabla({

            onEditar:
                editarEjercicio,

            onEliminar:
                eliminarEjercicioConfirm,

        });


        document
            .getElementById(
                "btn-nuevo-ejercicio",
            )
            ?.addEventListener(
                "click",
                nuevoEjercicio,
            );


        document
            .getElementById(
                "btn-actualizar-ejercicio",
            )
            ?.addEventListener(
                "click",
                mostrarEjercicios,
            );

    }

    catch (
        error
    ) {

        contenido.innerHTML = `

            <h2>Ejercicios</h2>

            <p>
                Error al consultar la API.
            </p>

        `;

        console.error(
            error,
        );
    }

}


/*********************************************
 * NUEVO
 *********************************************/

function nuevoEjercicio() {

    abrirModal({

        titulo:
            "Nuevo ejercicio",

        contenido:
            crearFormularioEjercicio(),

        textoAceptar:
            "Guardar",

        textoCancelar:
            "Cancelar",

        onAceptar:
            guardarEjercicio,

    });

}


/*********************************************
 * GUARDAR
 *********************************************/

async function guardarEjercicio() {

    const formulario =
        document.getElementById(
            "form-ejercicio",
        );


    const datos = {

        anio:
            Number(
                formulario.anio.value,
            ),

        fecha_apertura:
            formulario.fecha_apertura.value,

        fecha_cierre:
            null,

    };


    try {

        const empresa =
            obtenerEmpresaSeleccionada();


        if (!empresa) {

            throw new Error(
                "No hay una empresa seleccionada.",
            );
        }


        await crearEjercicio(
            empresa.id,
            datos,
        );


        mostrarToast(
            "Ejercicio creado correctamente.",
            "success",
        );


        cerrarModal();


        await mostrarEjercicios();

    }

    catch (
        error
    ) {

        mostrarToast(
            error.message,
            "error",
        );

        console.error(
            error,
        );
    }

}


/*********************************************
 * EDITAR
 *********************************************/

function editarEjercicio(
    indice,
) {

    const ejercicio =
        ejercicios[
            indice
        ];


    abrirModal({

        titulo:
            "Editar ejercicio",

        contenido:
            crearFormularioEjercicio(
                ejercicio,
            ),

        textoAceptar:
            "Guardar",

        textoCancelar:
            "Cancelar",

        onAceptar:
            () =>
                actualizar(
                    ejercicio.id,
                ),

    });

}


/*********************************************
 * ACTUALIZAR
 *********************************************/

async function actualizar(
    id,
) {

    const formulario =
        document.getElementById(
            "form-ejercicio",
        );


    const datos = {

        anio:
            Number(
                formulario.anio.value,
            ),

        fecha_apertura:
            formulario.fecha_apertura.value,

        fecha_cierre:
            null,

    };


    try {

        const empresa =
            obtenerEmpresaSeleccionada();


        if (!empresa) {

            throw new Error(
                "No hay una empresa seleccionada.",
            );
        }


        await actualizarEjercicio(
            empresa.id,
            id,
            datos,
        );


        mostrarToast(
            "Ejercicio actualizado.",
            "success",
        );


        cerrarModal();


        await mostrarEjercicios();

    }

    catch (
        error
    ) {

        mostrarToast(
            error.message,
            "error",
        );

        console.error(
            error,
        );
    }

}


/*********************************************
 * ELIMINAR
 *********************************************/

function eliminarEjercicioConfirm(
    indice,
) {

    const ejercicio =
        ejercicios[
            indice
        ];


    abrirModal({

        titulo:
            "Eliminar ejercicio",

        contenido: `

            <p>

                ¿Eliminar el ejercicio

                <b>
                    ${ejercicio.anio}
                </b>?

            </p>

        `,

        textoAceptar:
            "Eliminar",

        textoCancelar:
            "Cancelar",

        onAceptar:
            () =>
                eliminar(
                    ejercicio.id,
                ),

    });

}


async function eliminar(
    id,
) {

    try {

        const empresa =
            obtenerEmpresaSeleccionada();


        if (!empresa) {

            throw new Error(
                "No hay una empresa seleccionada.",
            );
        }


        await eliminarEjercicio(
            empresa.id,
            id,
        );


        mostrarToast(
            "Ejercicio eliminado.",
            "success",
        );


        cerrarModal();


        await mostrarEjercicios();

    }

    catch (
        error
    ) {

        mostrarToast(
            error.message,
            "error",
        );

        console.error(
            error,
        );
    }

}

