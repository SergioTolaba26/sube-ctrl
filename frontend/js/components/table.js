export function crearTabla(

    columnas,

    filas,

    opciones = {},

) {

    const {

        mostrarAcciones = false,

    } = opciones;

    let html = `

        <table class="tabla">

            <thead>

                <tr>

    `;

    columnas.forEach(

        columna => {

            html += `<th>${columna}</th>`;

        },

    );

    if (

        mostrarAcciones

    ) {

        html += "<th>Acciones</th>";

    }

    html += `

                </tr>

            </thead>

            <tbody>

    `;

    filas.forEach(

        (

            fila,

            indice,

        ) => {

            html += "<tr>";

            fila.forEach(

                celda => {

                    html += `<td>${celda}</td>`;

                },

            );

            if (

                mostrarAcciones

            ) {

                html += `

                    <td class="acciones">

                        <button

                            class="btn-editar"

                            data-index="${indice}"

                            title="Editar"

                        >

                            ✏️

                        </button>

                            <button class="btn-confirmar">

                                Confirmar

                            </button>

                        <button

                            class="btn-eliminar"

                            data-index="${indice}"

                            title="Eliminar"

                        >

                            🗑️

                        </button>

                    </td>

                `;

            }

            html += "</tr>";

        },

    );

    html += `

            </tbody>

        </table>

    `;

    return html;

}


/*************************************************
 * CONECTAR EVENTOS DE LA TABLA
 *************************************************/

export function conectarEventosTabla({

    onEditar = null,
    onConfirmar = null,
    onEliminar = null,

}) {

    if (

        onEditar

    ) {

        document

            .querySelectorAll(

                ".btn-editar",

            )

            .forEach(

                boton => {

                    boton.addEventListener(

                        "click",

                        () => {

                            onEditar(

                                Number(

                                    boton.dataset.index,

                                ),

                            );

                        },

                    );

                },

            );

    }
    if (onConfirmar) {

        document
            .querySelectorAll(".btn-confirmar")
            .forEach((boton, indice) => {

                boton.addEventListener(

                    "click",

                    () => onConfirmar(indice),

                );

            });

    }

    if (

        onEliminar

    ) {

        document

            .querySelectorAll(

                ".btn-eliminar",

            )

            .forEach(

                boton => {

                    boton.addEventListener(

                        "click",

                        () => {

                            onEliminar(

                                Number(

                                    boton.dataset.index,

                                ),

                            );

                        },

                    );

                },

            );

    }

}