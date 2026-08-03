export function crearFormularioAsiento(asiento = {}) {

    return `

<form id="form-asiento">

    <div class="campo">

        <label>Fecha</label>

        <input
            type="date"
            name="fecha"
            value="${asiento.fecha ?? ""}"
            required
        >

    </div>

    <div class="campo">

        <label>Descripción</label>

        <input
            type="text"
            name="descripcion"
            value="${asiento.descripcion ?? ""}"
            maxlength="200"
            required
        >

    </div>

    <div class="campo">

        <label>Estado</label>

        <select name="estado">

            <option
                value="BORRADOR"
                ${asiento.estado === "BORRADOR" ? "selected" : ""}
            >
                BORRADOR
            </option>

            <option
                value="CONFIRMADO"
                ${asiento.estado === "CONFIRMADO" ? "selected" : ""}
            >
                CONFIRMADO
            </option>

        </select>

    </div>

    <hr>

    <h3>Líneas del asiento</h3>

    <div id="lineas-container">

        ${(asiento.lineas ?? []).map((linea, index) => `

        <div class="linea-asiento" data-index="${index}">

            <div class="fila-linea">

                <label>Cuenta</label>

                <select class="cuenta-id">

                    ${(window.cuentas ?? []).map(cuenta => `

                        <option
                            value="${cuenta.id}"
                            ${cuenta.id === linea.cuenta_id ? "selected" : ""}
                        >

                            ${cuenta.codigo} - ${cuenta.nombre}

                        </option>

                    `).join("")}

                </select>

            </div>

            <div class="fila-linea">

                <label>Tipo</label>

                <select class="tipo-afectacion">

                    <option
                        value="DEBITO"
                        ${linea.tipo_afectacion === "DEBITO" ? "selected" : ""}
                    >
                        Débito
                    </option>

                    <option
                        value="CREDITO"
                        ${linea.tipo_afectacion === "CREDITO" ? "selected" : ""}
                    >
                        Crédito
                    </option>

                </select>

            </div>

            <div class="fila-linea">

                <label>Importe</label>

                <input
                    type="number"
                    class="importe"
                    value="${linea.importe}"
                >

            </div>

            <div class="fila-linea">

                <button
                    type="button"
                    class="btn-eliminar-linea"
                >
                    🗑
                </button>

            </div>

        </div>

        `).join("")}

    </div>

    <br>

    <button
        type="button"
        id="btn-agregar-linea"
    >
        ➕ Agregar línea
    </button>

</form>

`;
}