import {

    listarCuentas,

    crearCuenta,

    actualizarCuenta,

    eliminarCuenta,

} from "../api.js";

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

    crearFormularioCuenta,

} from "../forms/cuentaForm.js";

import {

    mostrarToast,

} from "../components/toast.js";


let cuentas = [];


/*********************************************
 * LISTAR
 *********************************************/

export async function mostrarCuentas() {

    const contenido = document.getElementById(
        "contenido",
    );
    
    contenido.innerHTML =
        "<h2>Plan de cuentas</h2><p>Cargando...</p>";

    try {

        cuentas =
            await listarCuentas();
        //Agregado para ver por qué las acciones no se ven    
        console.log("CUENTAS:", cuentas);

        console.log("crearPagina");
        contenido.innerHTML = crearPagina({

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

                "Imputable",

            ],

            filas: cuentas.map(

                cuenta => [

                    cuenta.codigo,

                    cuenta.nombre,

                    cuenta.tipo,

                    cuenta.activa
                        ? "Sí"
                        : "No",

                    cuenta.imputable
                        ? "Sí"
                        : "No",

                ],

            ),

            acciones: true,

        });


        conectarEventosTabla({

            onEditar: editarCuenta,

            onEliminar: eliminarCuentaConfirm,

        });


        document

            .getElementById(
                "btn-nueva-cuenta",
            )

            ?.addEventListener(

                "click",

                nuevaCuenta,

            );


        document

            .getElementById(
                "btn-actualizar-cuentas",
            )

            ?.addEventListener(

                "click",

                mostrarCuentas,

            );

    }

    catch (

        error

    ) {

        contenido.innerHTML = `

            <h2>Plan de cuentas</h2>

            <p>Error al consultar la API.</p>

        `;

        console.error(

            error,

        );

    }

}


/*********************************************
 * NUEVA
 *********************************************/

function nuevaCuenta() {

    abrirModal({

        titulo: "Nueva cuenta",

        contenido:
            crearFormularioCuenta(),

        textoAceptar: "Guardar",

        textoCancelar: "Cancelar",

        onAceptar:
            guardarCuenta,

    });

}


/*********************************************
 * GUARDAR
 *********************************************/

async function guardarCuenta() {

    const formulario = document.getElementById(

        "form-cuenta",

    );

    const datos = {

        codigo:
            formulario.codigo.value,

        nombre:
            formulario.nombre.value,

        tipo:
            formulario.tipo.value,

        activa:
            formulario.activa.checked,

        imputable:
            formulario.imputable.checked,

    };

    try {

        await crearCuenta(

            datos,

        );

        mostrarToast(

            "Cuenta creada correctamente.",

            "success",

        );

        cerrarModal();

        await mostrarCuentas();

    }

    catch (

        error

    ) {

        mostrarToast(

            error.message,

            "error",

        );

    }

}


/*********************************************
 * EDITAR
 *********************************************/

function editarCuenta(

    indice,

) {

    const cuenta =

        cuentas[indice];

    abrirModal({

        titulo:
            "Editar cuenta",

        contenido:
            crearFormularioCuenta(

                cuenta,

            ),

        textoAceptar:
            "Guardar",

        textoCancelar:
            "Cancelar",

        onAceptar: () =>

            actualizar(

                cuenta.id,

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

            "form-cuenta",

        );

    const datos = {

        codigo:
            formulario.codigo.value,

        nombre:
            formulario.nombre.value,

        tipo:
            formulario.tipo.value,

        activa:
            formulario.activa.checked,

        imputable:
            formulario.imputable.checked,

    };

    try {

        await actualizarCuenta(

            id,

            datos,

        );

        mostrarToast(

            "Cuenta actualizada.",

            "success",

        );

        cerrarModal();

        await mostrarCuentas();

    }

    catch (

        error

    ) {

        mostrarToast(

            error.message,

            "error",

        );

    }

}


/*********************************************
 * ELIMINAR
 *********************************************/

function eliminarCuentaConfirm(

    indice,

) {

    const cuenta =

        cuentas[indice];

    abrirModal({

        titulo:
            "Eliminar cuenta",

        contenido: `

            <p>

                ¿Eliminar la cuenta

                <b>${cuenta.codigo}</b>

                -

                <b>${cuenta.nombre}</b>?

            </p>

        `,

        textoAceptar:
            "Eliminar",

        textoCancelar:
            "Cancelar",

        onAceptar: () =>

            eliminar(

                cuenta.id,

            ),

    });

}


async function eliminar(

    id,

) {

    try {

        await eliminarCuenta(

            id,

        );

        mostrarToast(

            "Cuenta eliminada.",

            "success",

        );

        cerrarModal();

        await mostrarCuentas();

    }

    catch (

        error

    ) {

        mostrarToast(

            error.message,

            "error",

        );

    }

}