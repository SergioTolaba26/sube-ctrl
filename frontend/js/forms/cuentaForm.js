export function crearFormularioCuenta(
    cuenta = {},
) {

    return `

        <form id="form-cuenta">

            <div class="campo">

                <label for="codigo">
                    Código
                </label>

                <input
                    id="codigo"
                    name="codigo"
                    type="text"
                    value="${cuenta.codigo ?? ""}"
                    required
                >

            </div>


            <div class="campo">

                <label for="nombre">
                    Nombre
                </label>

                <input
                    id="nombre"
                    name="nombre"
                    type="text"
                    value="${cuenta.nombre ?? ""}"
                    required
                >

            </div>


            <div class="campo">

                <label for="tipo">
                    Tipo
                </label>

                <select
                    id="tipo"
                    name="tipo"
                    required
                >

                    <option value="">
                        Seleccione...
                    </option>

                    <option
                        value="ACTIVO"
                        ${cuenta.tipo === "ACTIVO" ? "selected" : ""}
                    >
                        ACTIVO
                    </option>

                    <option
                        value="PASIVO"
                        ${cuenta.tipo === "PASIVO" ? "selected" : ""}
                    >
                        PASIVO
                    </option>

                    <option
                        value="PATRIMONIO"
                        ${cuenta.tipo === "PATRIMONIO" ? "selected" : ""}
                    >
                        PATRIMONIO
                    </option>

                    <option
                        value="RESULTADO_POSITIVO"
                        ${cuenta.tipo === "RESULTADO_POSITIVO" ? "selected" : ""}
                    >
                        RESULTADO POSITIVO
                    </option>

                    <option
                        value="RESULTADO_NEGATIVO"
                        ${cuenta.tipo === "RESULTADO_NEGATIVO" ? "selected" : ""}
                    >
                        RESULTADO NEGATIVO
                    </option>

                </select>

            </div>


            <div class="campo">

                <label>

                    <input
                        id="imputable"
                        name="imputable"
                        type="checkbox"
                        ${cuenta.imputable !== false ? "checked" : ""}
                    >

                    Imputable

                </label>

            </div>


            <div class="campo">

                <label>

                    <input
                        id="activa"
                        name="activa"
                        type="checkbox"
                        ${cuenta.activa !== false ? "checked" : ""}
                    >

                    Activa

                </label>

            </div>

        </form>

    `;

}