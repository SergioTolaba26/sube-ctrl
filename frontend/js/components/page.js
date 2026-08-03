import {
    crearToolbar,
} from "./toolbar.js";

import {
    crearTabla,
} from "./table.js";

export function crearPagina({

    titulo,

    botones = [],

    columnas = [],

    filas = [],

    acciones = false,

}) {

    let html = "";

    //
    // Barra de herramientas
    //
    html += crearToolbar(

        titulo,

        botones,

    );

    //
    // Tabla
    //
    html += crearTabla(

        columnas,

        filas,

        {

            mostrarAcciones:
                acciones,

        },

    );

    return html;

}