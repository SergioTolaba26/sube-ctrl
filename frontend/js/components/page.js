import { crearToolbar }
    from "./toolbar.js";

import { crearTabla }
    from "./table.js";


export function crearPagina({

    titulo,

    botones = [],

    columnas = [],

    filas = [],

}) {

    let html = "";

    html += crearToolbar(

        titulo,

        botones,

    );

    html += crearTabla(

        columnas,

        filas,

    );

    return html;

}