/******************************************************************
 * asientosLineas.js
 *
 * Maneja únicamente las líneas del asiento.
 ******************************************************************/

import {
    obtenerCuentas,
} from "../api.js";

let cuentas = [];

let lineas = [];

/*************************************************
 * INICIALIZAR
 *************************************************/

export async function inicializarLineas() {

    cuentas = await obtenerCuentas();

    lineas = [];

}

/*************************************************
 * OBTENER
 *************************************************/

export function obtenerLineas() {

    return lineas;

}

/*************************************************
 * REEMPLAZAR
 *************************************************/

export function establecerLineas(
    nuevasLineas,
) {

    lineas = [
        ...nuevasLineas,
    ];

}

/*************************************************
 * LIMPIAR
 *************************************************/

export function limpiarLineas() {

    lineas = [];

}

/*************************************************
 * AGREGAR
 *************************************************/

export function agregarLinea(
    linea,
) {

    lineas.push(
        linea,
    );

}

/*************************************************
 * ELIMINAR
 *************************************************/

export function eliminarLinea(
    indice,
) {

    lineas.splice(
        indice,
        1,
    );

}

/*************************************************
 * RENDERIZAR
 *************************************************/

export function renderizarLineas() {

    const tbody =
        document.querySelector(
            "#tbodyLineas",
        );

    if (
        !tbody
    ) {

        console.warn(
            "No existe #tbodyLineas",
        );

        return;

    }

    tbody.innerHTML = "";

    lineas.forEach(

        (
            linea,
            indice,
        ) => {

            const cuenta =
                cuentas.find(

                    c =>
                        c.id ===
                        Number(
                            linea.cuenta_id,
                        ),

                );

            const tr =
                document.createElement(
                    "tr",
                );

            tr.innerHTML = `

                <td>

                    ${cuenta?.codigo ?? ""}

                </td>

                <td>

                    ${cuenta?.nombre ?? ""}

                </td>

                <td>

                    ${linea.tipo_afectacion}

                </td>

                <td class="text-end">

                    ${Number(
                        linea.importe,
                    ).toFixed(
                        2,
                    )}

                </td>

                <td>

                    <button
                        class="btn btn-danger btn-sm"
                        data-indice="${indice}"
                    >

                        🗑️

                    </button>

                </td>

            `;

            tbody.appendChild(
                tr,
            );

        },

    );

    conectarEventosEliminar();

}

/*************************************************
 * EVENTOS
 *************************************************/

function conectarEventosEliminar() {

    document

        .querySelectorAll(

            "#tbodyLineas button",

        )

        .forEach(

            boton => {

                boton.addEventListener(

                    "click",

                    () => {

                        eliminarLinea(

                            Number(

                                boton.dataset.indice,

                            ),

                        );

                        renderizarLineas();

                    },

                );

            },

        );

}

/******************************************************************
 * CREAR LÍNEA DESDE EL FORMULARIO
 ******************************************************************/

export function crearLineaDesdeFormulario() {

    const cuenta =
        document.querySelector(
            "#cmbCuenta",
        );

    const tipo =
        document.querySelector(
            "#cmbTipoAfectacion",
        );

    const importe =
        document.querySelector(
            "#txtImporte",
        );

    if (
        !cuenta ||
        !tipo ||
        !importe
    ) {

        throw new Error(
            "No se encontraron los controles del formulario.",
        );

    }

    return {

        cuenta_id: Number(
            cuenta.value,
        ),

        tipo_afectacion:
            tipo.value,

        importe: Number(
            importe.value,
        ),

    };

}

/******************************************************************
 * VALIDAR LÍNEA
 ******************************************************************/

export function validarLinea(
    linea,
) {

    if (
        !linea.cuenta_id
    ) {

        throw new Error(
            "Debe seleccionar una cuenta.",
        );

    }

    if (
        !linea.tipo_afectacion
    ) {

        throw new Error(
            "Debe indicar Débito o Crédito.",
        );

    }

    if (
        Number(
            linea.importe,
        ) <= 0
    ) {

        throw new Error(
            "El importe debe ser mayor que cero.",
        );

    }

}

/******************************************************************
 * TOTALES
 ******************************************************************/

export function calcularTotales() {

    let totalDebito = 0;

    let totalCredito = 0;

    lineas.forEach(

        linea => {

            if (
                linea.tipo_afectacion ===
                "DEBITO"
            ) {

                totalDebito += Number(
                    linea.importe,
                );

            } else {

                totalCredito += Number(
                    linea.importe,
                );

            }

        },

    );

    return {

        totalDebito,

        totalCredito,

    };

}

/******************************************************************
 * ¿BALANCEA?
 ******************************************************************/

export function balanceaAsiento() {

    const {

        totalDebito,

        totalCredito,

    } = calcularTotales();

    return (

        totalDebito ===
        totalCredito

    );

}

/******************************************************************
 * EXPORTAR
 ******************************************************************/

export default {

    inicializarLineas,

    obtenerLineas,

    establecerLineas,

    limpiarLineas,

    agregarLinea,

    eliminarLinea,

    renderizarLineas,

    crearLineaDesdeFormulario,

    validarLinea,

    calcularTotales,

    balanceaAsiento,

};