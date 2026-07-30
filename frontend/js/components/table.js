export function crearTabla(
    columnas,
    filas,
) {

    let html = `
        <table border="1" cellpadding="5">

            <tr>
    `;

    columnas.forEach(columna => {

        html += `<th>${columna}</th>`;

    });

    html += "</tr>";

    filas.forEach(fila => {

        html += "<tr>";

        fila.forEach(celda => {

            html += `<td>${celda}</td>`;

        });

        html += "</tr>";

    });

    html += "</table>";

    return html;

}