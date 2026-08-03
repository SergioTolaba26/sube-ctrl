export function crearFormularioEjercicio(
    ejercicio = null,
) {

    return `

        <form id="form-ejercicio">

            <div class="form-group">

                <label for="anio">

                    Año

                </label>

                <input

                    id="anio"

                    name="anio"

                    type="number"

                    min="2000"

                    max="3000"

                    value="${ejercicio?.anio ?? ""}"

                    required

                >

            </div>

            <div class="form-group">

                <label for="fecha_apertura">

                    Fecha apertura

                </label>

                <input

                    id="fecha_apertura"

                    name="fecha_apertura"

                    type="date"

                    value="${ejercicio?.fecha_apertura ?? ""}"

                    required

                >

            </div>

        </form>

    `;

}