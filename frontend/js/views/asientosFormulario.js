/******************************************************************
 * asientosFormulario.js
 *
 * Formulario de alta / edición de Asientos Contables.
 ******************************************************************/

import {
  listarCuentas,
  obtenerAsiento,
  crearAsiento,
  actualizarAsiento,
} from '../api.js';

import { abrirModal, cerrarModal } from '../components/modal.js';

import {
  inicializarLineas,
  limpiarLineas,
  establecerLineas,
  renderizarLineas,
  obtenerLineas,
  agregarLinea,
  crearLineaDesdeFormulario,
  validarLinea,
  balanceaAsiento,
} from './asientosLineas.js';

import { mostrarToast } from '../components/toast.js';

/******************************************************************
 * Estado
 ******************************************************************/

let modoEdicion = false;

let asientoActual = null;

let cuentas = [];

/******************************************************************
 * HTML del formulario
 ******************************************************************/

function crearFormularioHTML() {
  return `

<form id="frmAsiento">

    <div class="grupo">

        <label>Fecha</label>

        <input
            id="txtFecha"
            type="date"
            required
        >

    </div>

    <div class="grupo">

        <label>Descripción</label>

        <input
            id="txtDescripcion"
            type="text"
            maxlength="200"
            required
        >

    </div>

    <hr>

    <div class="grupo-linea">

        <select id="cmbCuenta">

            <option value="">
                Seleccione una cuenta
            </option>

        </select>

        <select id="cmbTipoAfectacion">

            <option value="DEBITO">
                Débito
            </option>

            <option value="CREDITO">
                Crédito
            </option>

        </select>

        <input
            id="txtImporte"
            type="number"
            min="0.01"
            step="0.01"
        >

        <button
            id="btnAgregarLinea"
            type="button"
        >

            Agregar

        </button>

    </div>

    <table class="tabla">

        <thead>

            <tr>

                <th>Código</th>

                <th>Cuenta</th>

                <th>Tipo</th>

                <th>Importe</th>

                <th></th>

            </tr>

        </thead>

        <tbody id="tbodyLineas">

        </tbody>

    </table>

</form>

`;
}

/******************************************************************
 * Nuevo Asiento
 ******************************************************************/

export async function abrirNuevoAsiento(
    onGuardado = null,
) {

    modoEdicion = false;

    asientoActual = null;

    await inicializarLineas();

    abrirModal({

        titulo: 'Nuevo Asiento',

        contenido: crearFormularioHTML(),

        onAceptar: async () => {

            await guardarAsiento();

            if (onGuardado) {
                await onGuardado();
            }

        },

    });

    await cargarComboCuentas();

    conectarFormularioAsiento();

    limpiarFormulario();

    renderizarLineas();

}
/******************************************************************
 * Editar Asiento
 ******************************************************************/

export async function abrirEditarAsiento(
    movimientoId,
    onGuardado = null,
) {

    modoEdicion = true;

    asientoActual = await obtenerAsiento(
        movimientoId,
    );

    await inicializarLineas();

    abrirModal({

        titulo: 'Editar Asiento',

        contenido: crearFormularioHTML(),

        onAceptar: async () => {

            await guardarAsiento();

            if (onGuardado) {
                await onGuardado();
            }

        },

    });

    await cargarComboCuentas();

    conectarFormularioAsiento();

    limpiarFormulario();

    cargarFormulario(
        asientoActual,
    );

}
/******************************************************************
 * Cargar cuentas
 ******************************************************************/

async function cargarComboCuentas() {
  cuentas = await listarCuentas();

  const combo = document.querySelector('#cmbCuenta');

  if (!combo) {
    return;
  }

  combo.innerHTML = `

<option value="">

Seleccione una cuenta

</option>

`;

  cuentas.forEach((cuenta) => {
    combo.innerHTML += `

<option value="${cuenta.id}">

${cuenta.codigo} - ${cuenta.nombre}

</option>

`;
  });
}

/******************************************************************
 * Limpiar formulario
 ******************************************************************/

function limpiarFormulario() {
  const txtFecha = document.querySelector('#txtFecha');

  if (txtFecha) {
    txtFecha.value = '';
  }

  const txtDescripcion = document.querySelector('#txtDescripcion');

  if (txtDescripcion) {
    txtDescripcion.value = '';
  }

  const cmbCuenta = document.querySelector('#cmbCuenta');

  if (cmbCuenta) {
    cmbCuenta.selectedIndex = 0;
  }

  const cmbTipo = document.querySelector('#cmbTipoAfectacion');

  if (cmbTipo) {
    cmbTipo.selectedIndex = 0;
  }

  const txtImporte = document.querySelector('#txtImporte');

  if (txtImporte) {
    txtImporte.value = '';
  }

  limpiarLineas();
}

/******************************************************************
 * Cargar datos del asiento
 ******************************************************************/

function cargarFormulario(asiento) {
  const txtFecha = document.querySelector('#txtFecha');

  if (txtFecha) {
    txtFecha.value = asiento.fecha;
  }

  const txtDescripcion = document.querySelector('#txtDescripcion');

  if (txtDescripcion) {
    txtDescripcion.value = asiento.descripcion;
  }

  establecerLineas(
    asiento.lineas.map((linea) => ({
      cuenta_id: linea.cuenta_id,

      importe: Number(linea.importe),

      tipo_afectacion: linea.tipo_afectacion,
    })),
  );

  renderizarLineas();
}
/******************************************************************
 * Conectar eventos del formulario
 ******************************************************************/

function conectarFormularioAsiento() {
  const botonAgregar = document.querySelector('#btnAgregarLinea');

  if (botonAgregar) {
    botonAgregar.addEventListener(
      'click',

      agregarLineaFormulario,
    );
  }
}

/******************************************************************
 * Agregar línea
 ******************************************************************/

function agregarLineaFormulario() {
  try {
    const linea = crearLineaDesdeFormulario();

    validarLinea(linea);

    agregarLinea(linea);

    renderizarLineas();

    limpiarControlesLinea();
  } catch (error) {
    alert(error.message);
  }
}

/******************************************************************
 * Limpiar controles de captura de línea
 ******************************************************************/

function limpiarControlesLinea() {
  const cmbCuenta = document.querySelector('#cmbCuenta');

  if (cmbCuenta) {
    cmbCuenta.selectedIndex = 0;
  }

  const cmbTipo = document.querySelector('#cmbTipoAfectacion');

  if (cmbTipo) {
    cmbTipo.selectedIndex = 0;
  }

  const txtImporte = document.querySelector('#txtImporte');

  if (txtImporte) {
    txtImporte.value = '';
  }
}

/******************************************************************
 * Obtener datos del formulario
 ******************************************************************/

function obtenerFormulario() {
  return {
    fecha: document.querySelector('#txtFecha').value,

    descripcion: document.querySelector('#txtDescripcion').value.trim(),

    lineas: obtenerLineas(),
  };
}
/******************************************************************
 * Guardar asiento
 ******************************************************************/

async function guardarAsiento() {
  try {
    const datos = obtenerFormulario();

    if (!datos.fecha) {
      throw new Error('Debe ingresar la fecha.');
    }

    if (datos.descripcion.length === 0) {
      throw new Error('Debe ingresar la descripción.');
    }

    if (datos.lineas.length < 2) {
      throw new Error('Debe ingresar al menos dos líneas.');
    }

    if (!balanceaAsiento()) {
      throw new Error('El asiento no balancea.');
    }

    const payload = {
      fecha: datos.fecha,

      descripcion: datos.descripcion,

      lineas: datos.lineas,
    };

    if (modoEdicion) {
      await actualizarAsiento(asientoActual.id, payload);

      cerrarModal();

      mostrarToast('Asiento actualizado correctamente.', 'success');
    } else {
      await crearAsiento(payload);

      cerrarModal();

      mostrarToast('Asiento creado correctamente.', 'success');
    }

    //await mostrarAsientos();
  } catch (error) {
    alert(error.message);
  }
}

/******************************************************************
 * Exports
 ******************************************************************/

export { conectarFormularioAsiento, agregarLineaFormulario };
