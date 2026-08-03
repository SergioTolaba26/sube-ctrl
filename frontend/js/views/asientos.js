import {

    obtenerAsientos,

    obtenerAsiento,

    crearAsiento as apiCrearAsiento,

    actualizarAsiento as apiActualizarAsiento,

    eliminarAsiento as apiEliminarAsiento,

} from "../api.js";

import { crearPagina } from '../components/page.js';

import { abrirModal, cerrarModal } from '../components/modal.js';

import { conectarEventosTabla } from '../components/table.js';

import { crearFormularioAsiento } from '../forms/asientoForm.js';

import { crearLineaMovimiento } from '../components/lineaMovimiento.js';

import { obtenerCuentas } from '../api.js';

import {

    actualizarLineaAsiento,

} from "../api.js";

let asientos = [];
let cuentas = [];

/*********************************************
 * LISTAR
 *********************************************/

export async function mostrarAsientos() {
  const contenido = document.getElementById('contenido');

  contenido.innerHTML = '<h2>Asientos</h2><p>Cargando...</p>';

  try {
    asientos = await obtenerAsientos();

    asientos.sort((a, b) => a.numero_asiento - b.numero_asiento);

    contenido.innerHTML = crearPagina({
      titulo: 'Asientos',

      botones: [
        {
          id: 'btn-nuevo-asiento',

          texto: 'Nuevo',

          icono: '➕',
        },

        {
          id: 'btn-actualizar-asientos',

          texto: 'Actualizar',

          icono: '🔄',
        },
      ],

      columnas: ['N°', 'Fecha', 'Descripción', 'Estado'],

      filas: asientos.map((asiento) => [
        asiento.numero_asiento,

        asiento.fecha,

        asiento.descripcion,

        asiento.estado,
      ]),

      acciones: true,
    });

    conectarEventosTabla({
      onEditar: editarAsiento,

      onEliminar: eliminarAsiento,
    });

    document

      .getElementById('btn-nuevo-asiento')

      ?.addEventListener(
        'click',

        nuevoAsiento,
      );

    document

      .getElementById('btn-actualizar-asientos')

      ?.addEventListener(
        'click',

        mostrarAsientos,
      );
  } catch (error) {
    contenido.innerHTML = `

            <h2>Asientos</h2>

            <p>Error al consultar la API.</p>

        `;

    console.error(error);
  }
}

/*********************************************
 * NUEVO
 *********************************************/

async function nuevoAsiento() {
  cuentas = await obtenerCuentas();

  cuentas.sort((a, b) => a.codigo.localeCompare(b.codigo));

  abrirModal({
    titulo: 'Nuevo Asiento',

    contenido: crearFormularioAsiento(),
    
    textoAceptar: 'Guardar',

    textoCancelar: 'Cancelar',

    onAceptar: guardarAsiento,
  });

  inicializarLineas();
}

/*********************************************
 * INICIALIZAR LINEAS
 *********************************************/

function inicializarLineas() {
  const contenedor = document.getElementById('lineas-container');

  if (!contenedor) {
    return;
  }

  contenedor.innerHTML =
    crearLineaMovimiento(cuentas) + crearLineaMovimiento(cuentas);

  conectarEventosLineas();
}

/*********************************************
 * AGREGAR LINEAS
 *********************************************/

function conectarEventosLineas() {
  document

    .getElementById('btn-agregar-linea')

    ?.addEventListener(
      'click',

      () => {
        document

          .getElementById('lineas-container')

          .insertAdjacentHTML(
            'beforeend',

            crearLineaMovimiento(cuentas),
          );

        conectarEliminarLineas();
      },
    );

  conectarEliminarLineas();
}

/*********************************************
 * ELIMINAR LINEAS
 *********************************************/

function conectarEliminarLineas() {
  document

    .querySelectorAll('.btn-eliminar-linea')

    .forEach((boton) => {
      boton.onclick = () => {
        boton

          .closest('.linea-movimiento')

          .remove();
      };
    });
}
/*********************************************
 * GUARDAR
 *********************************************/

async function guardarAsiento() {
  const formulario = document.getElementById('form-asiento');

    
  const lineas = [...document.querySelectorAll('.linea-movimiento')].map(
    (linea) => ({
      cuenta_id: Number(linea.querySelector('.cuenta').value),

      debito: Number(linea.querySelector('.debito').value || 0),

      credito: Number(linea.querySelector('.credito').value || 0),
    }),
  );
  const datos = {
    fecha: formulario.fecha.value,

    descripcion: formulario.descripcion.value,

    estado: formulario.estado.value,
    lineas,
  };
  console.log('DATOS A ENVIAR:', datos);

  try {
    await apiCrearAsiento(datos);

    cerrarModal();

    await mostrarAsientos();
  } catch (error) {
    console.error(error);
  }
}

/*********************************************
 * EDITAR
 *********************************************/

async function editarAsiento(indice) {

    const resumen =
        asientos[indice];

    const asiento =
        await obtenerAsiento(
            resumen.id,
        );

    //
    // Cargar todas las cuentas
    //
    window.cuentas =
        await obtenerCuentas();

    abrirModal({

        titulo: "Editar Asiento",

        contenido:
            crearFormularioAsiento(
                asiento,
            ),

        textoAceptar: "Guardar",

        textoCancelar: "Cancelar",

        onAceptar: () =>
            actualizarAsiento(
                asiento.id,
            ),

    });

    inicializarFormularioAsiento();

}
function inicializarFormularioAsiento() {

    //
    // Botón eliminar
    //
    document
        .querySelectorAll(".btn-eliminar-linea")
        .forEach((boton) => {

            boton.onclick = () => {

                const fila =
                    boton.closest(
                        ".linea-asiento",
                    );

                if (fila) {

                    fila.remove();

                }

            };

        });

    //
    // Botón agregar
    //
    const btnAgregar =
        document.getElementById(
            "btn-agregar-linea",
        );

    if (btnAgregar) {

        btnAgregar.onclick =
            agregarLineaFormulario;

    }

}
function agregarLineaFormulario() {

    const contenedor =
        document.getElementById(
            "lineas-container",
        );

    const html = `

<div class="linea-asiento">

    <div class="fila-linea">

        <label>Cuenta</label>

        <select class="cuenta-id">

            ${window.cuentas.map(cuenta => `

                <option value="${cuenta.id}">

                    ${cuenta.codigo} - ${cuenta.nombre}

                </option>

            `).join("")}

        </select>

    </div>

    <div class="fila-linea">

        <label>Tipo</label>

        <select class="tipo-afectacion">

            <option value="DEBITO">

                Débito

            </option>

            <option value="CREDITO">

                Crédito

            </option>

        </select>

    </div>

    <div class="fila-linea">

        <label>Importe</label>

        <input
            class="importe"
            type="number"
            value="0"
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

`;

    contenedor.insertAdjacentHTML(
        "beforeend",
        html,
    );

    inicializarFormularioAsiento();

}
/*********************************************
 * ACTUALIZAR
 *********************************************/

async function actualizarAsiento(id) {

    const formulario =
        document.getElementById(
            "form-asiento",
        );

    //
    // Armamos el asiento completo.
    //
    const datos = {

        fecha:
            formulario.fecha.value,

        descripcion:
            formulario.descripcion.value,

        estado:
            "BORRADOR",

        lineas:
            obtenerLineasFormulario(),

    };
    const resultado =
        validarAsientoBalanceado(
            datos.lineas,
        );

    if (!resultado.balanceado) {

        alert(

            `⚠ El asiento está desbalanceado.\n\n` +

            `Débitos : ${resultado.debitos}\n` +

            `Créditos: ${resultado.creditos}\n` +

            `Diferencia: ${resultado.diferencia}`

        );

        return;

    }

    console.log(
        "ASIENTO A ENVIAR:",
        datos,
    );

    try {

        //
        // Ahora TODO se guarda en un único PUT.
        //
        await apiActualizarAsiento(

            id,

            datos,

        );

        cerrarModal();

        await mostrarAsientos();

    } catch (error) {

        console.error(
            "ERROR AL ACTUALIZAR:",
            error,
        );

    }

}
/*********************************************
 * ELIMINAR
 *********************************************/

async function eliminarAsiento(indice) {
  const asiento = asientos[indice];

  if (!confirm(`¿Eliminar el asiento Nº ${asiento.numero_asiento}?`)) {
    return;
  }

  try {
    await apiEliminarAsiento(asiento.id);

    await mostrarAsientos();
  } catch (error) {
    console.error(error);
  }
}

/***********DIBUJAR LINEAS DEL ASIENTO AL EDITAR */
function cargarLineasExistentes(
    lineas,
) {

    const contenedor =
        document.getElementById(
            "lineas-container",
        );

    contenedor.innerHTML = "";

    lineas.forEach(
        (linea) => {

            contenedor.insertAdjacentHTML(
                "beforeend",
                crearLineaMovimiento(
                    cuentas,
                    linea,
                ),
            );

        },
    );

    conectarEventosLineas();

}
function obtenerLineasFormulario() {

    const lineas = [];

    document.querySelectorAll(".linea-asiento").forEach((fila) => {

        lineas.push({

            cuenta_id: Number(
                fila.querySelector(".cuenta-id").value
            ),

            tipo_afectacion:
                fila.querySelector(".tipo-afectacion").value,

            importe: Number(
                fila.querySelector(".importe").value
            ),

        });

    });

    return lineas;

}

// Nejora UX
function validarAsientoBalanceado(lineas) {

    let totalDebitos = 0;
    let totalCreditos = 0;

    lineas.forEach((linea) => {

        if (linea.tipo_afectacion === "DEBITO") {

            totalDebitos += Number(linea.importe);

        } else {

            totalCreditos += Number(linea.importe);

        }

    });

    return {

        balanceado: totalDebitos === totalCreditos,

        debitos: totalDebitos,

        creditos: totalCreditos,

        diferencia: Math.abs(totalDebitos - totalCreditos),

    };

}