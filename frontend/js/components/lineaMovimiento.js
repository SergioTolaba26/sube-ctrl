export function crearLineaMovimiento(
    cuentas = [],
    linea = null,
) {

    const opciones = cuentas
        .map(
            cuenta => {

                const selected =
                    linea &&
                    linea.cuenta_id === cuenta.id
                        ? "selected"
                        : "";

                return `
                    <option
                        value="${cuenta.id}"
                        ${selected}
                    >
                        ${cuenta.codigo} - ${cuenta.nombre}
                    </option>
                `;

            },
        )
        .join("");

    const debe =
        linea &&
        linea.tipo_afectacion === "DEBITO"
            ? linea.importe
            : "";

    const haber =
        linea &&
        linea.tipo_afectacion === "CREDITO"
            ? linea.importe
            : "";

    return `

        <div class="linea-movimiento">

            <select class="cuenta">

                <option value="">

                    Seleccione cuenta

                </option>

                ${opciones}

            </select>

            <input
                type="number"
                class="debito"
                placeholder="Debe"
                step="0.01"
                min="0"
                value="${debe}"
            >

            <input
                type="number"
                class="credito"
                placeholder="Haber"
                step="0.01"
                min="0"
                value="${haber}"
            >

            <button
                type="button"
                class="btn-eliminar-linea"
                title="Eliminar línea"
            >
                ❌
            </button>

        </div>

    `;
}