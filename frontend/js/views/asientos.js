/******************************************************************
 * asientos.js
 *
 * Vista principal de Asientos Contables
 ******************************************************************/

import { obtenerAsientos,  confirmarAsiento as confirmarAsientoAPI, eliminarAsiento } from '../api.js';

import { crearTabla, conectarEventosTabla } from '../components/table.js';

import { abrirNuevoAsiento, abrirEditarAsiento } from './asientosFormulario.js';

import {

    obtenerCuentas,

} from "../api.js";

/*************************************************
 * MOSTRAR
 *************************************************/

export async function mostrarAsientos() {
  const asientos = await obtenerAsientos();

  const columnas = ['N°', 'Fecha', 'Descripción', 'Importe','Estado'];

  const filas = asientos.map((asiento) => [
    asiento.numero_asiento,
    asiento.fecha,
    asiento.descripcion,
    Number(asiento.importe).toFixed(2),
    asiento.estado,
]);

  const contenedor = document.getElementById('contenido');

  if (!contenedor) {
    console.error('No existe #contenido');

    return;
  }

  //  .innerHTML = crearTabla(
  //   columnas,

  //   filas,
  contenedor.innerHTML = `

  <div class="toolbar">

      <button id="btnNuevoAsiento">

          + Nuevo

      </button>

      <button id="btnActualizarAsientos">

          Actualizar

      </button>

  </div>

  ${crearTabla(

      columnas,

      filas,

      {

          mostrarAcciones: true,

      },

  )}

  `;

  //   {
  //     mostrarAcciones: true,
  //   },
  // );

  conectarEventosTabla({

      onEditar: (indice) =>

          editarAsiento(
              asientos[indice].id,
          ),

      onConfirmar: (indice) =>

          confirmarAsiento(
              asientos[indice].id,
              asientos[indice].numero_asiento,
          ),

      onEliminar: (indice) =>

          eliminarAsientoUI(
              asientos[indice].id,
              asientos[indice].numero_asiento,
              asientos[indice].descripcion,
          ),

  });
  document
      .getElementById(
          "btnNuevoAsiento",
      )
      ?.addEventListener(
          "click",
          nuevoAsiento,
      );

  document
      .getElementById(
          "btnActualizarAsientos",
      )
      ?.addEventListener(
          "click",
          mostrarAsientos,
      );
}

/*************************************************
 * NUEVO
 *************************************************/

export async function nuevoAsiento() {
  await abrirNuevoAsiento();
}

/*************************************************
 * EDITAR
 *************************************************/

export async function editarAsiento(movimientoId) {
  await abrirEditarAsiento(movimientoId);
}
async function confirmarAsiento(

    movimientoId,

    numeroAsiento,

) {

    const confirmar = confirm(

        `¿Confirmar el Asiento Nº ${numeroAsiento}?`,

    );

    if (!confirmar) {

        return;

    }

    try {

        await confirmarAsientoAPI(

            movimientoId,

        );

        await mostrarAsientos();

    }

    catch (error) {

        alert(

            error.message,

        );

    }

}
/*************************************************
 * ELIMINAR
 *************************************************/

async function eliminarAsientoUI(
    movimientoId,
    numeroAsiento,
    descripcion,
) {

    const confirmar = confirm(
        `¿Desea eliminar el Asiento Nº ${numeroAsiento}?\n\n` +
        `Descripción: ${descripcion}`,
    );

    if (!confirmar) {
        return;
    }

    try {

        await eliminarAsiento(
            movimientoId,
        );

        await mostrarAsientos();

    } catch (error) {

        alert(
            error.message,
        );

    }
}
/******************************************************************
 * EXPORTAR
 ******************************************************************/

export default {

    mostrarAsientos,

    nuevoAsiento,

    editarAsiento,

};

/******************************************************************
 * FIN DEL ARCHIVO
 ******************************************************************/
