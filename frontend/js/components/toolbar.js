export function crearToolbar(
    titulo,
    botones = [],
) {

    let html = `
        <div class="toolbar">

            <div class="toolbar-titulo">

                <h2>${titulo}</h2>

            </div>

            <div class="toolbar-botones">
    `;

    botones.forEach(boton => {

        html += `
            <button id="${boton.id}">
                ${boton.icono} ${boton.texto}
            </button>
        `;

    });

    html += `
            </div>

        </div>
    `;

    return html;

}