
import {

    mostrarDashboard,
    mostrarEjercicios,
    mostrarCuentas,
    mostrarAsientos,

} from "./router.js";

import {

    listarEmpresas,

} from "./api.js";



import {

    establecerEmpresa,

} from "./estado.js";

let empresas = [];
// ======================================================
// EMPRESAS
// ======================================================

async function cargarEmpresas() {

    const selector =
        document.getElementById(
            "empresa-select",
        );

    if (!selector) {

        return;

    }

    try {

        empresas =
            await listarEmpresas();

        selector.innerHTML = `

            <option value="">
                Seleccionar empresa
            </option>

        `;

        empresas.forEach(

            empresa => {

                const opcion =
                    document.createElement(
                        "option",
                    );

                opcion.value =
                    empresa.id;

                opcion.textContent =
                    empresa.nombre_fantasia;

                selector.appendChild(
                    opcion,
                );

            },

        );

        // ----------------------------------------------
        // Selección inicial
        // ----------------------------------------------

        const empresaInicial =
            empresas.find(

                empresa =>
                    empresa.id === 1,

            );

        if (empresaInicial) {

            selector.value =
                empresaInicial.id;

            establecerEmpresa(
                empresaInicial,
            );

            console.log(
                "Empresa seleccionada:",
                empresaInicial,
            );

        }

    }

    catch (error) {

        console.error(
            "Error al cargar empresas:",
            error,
        );

    }

}


// ======================================================
// CAMBIO DE EMPRESA
// ======================================================

function configurarSelectorEmpresa() {

    const selector =
        document.getElementById(
            "empresa-select",
        );

    if (!selector) {

        return;

    }

    selector.addEventListener(

        "change",

        event => {

            const empresaId =
                Number(
                    event.target.value,
                );

            if (!empresaId) {

                establecerEmpresa(
                    null,
                );

                console.log(
                    "Empresa deseleccionada",
                );

                return;

            }
            //Cambio para que quede en memoria la Empresa seleccionada
            const empresa =
                empresas.find(

                    empresa =>
                        empresa.id ===
                        empresaId,

                );

            if (empresa) {

                establecerEmpresa(
                    empresa,
                );

                console.log(
                    "Empresa seleccionada:",
                    empresa,
                );

            }
        },

    );

}


// ======================================================
// SERVICE WORKER
// ======================================================

if ("serviceWorker" in navigator) {

    navigator.serviceWorker.register(
        "service-worker.js",
    );

}


// ======================================================
// NAVEGACIÓN
// ======================================================

document
    .getElementById(
        "btn-dashboard",
    )
    .addEventListener(
        "click",
        mostrarDashboard,
    );


document
    .getElementById(
        "btn-ejercicios",
    )
    .addEventListener(
        "click",
        mostrarEjercicios,
    );


document
    .getElementById(
        "btn-cuentas",
    )
    .addEventListener(
        "click",
        mostrarCuentas,
    );


document
    .getElementById(
        "btn-asientos",
    )
    .addEventListener(
        "click",
        mostrarAsientos,
    );


// ======================================================
// INICIO
// ======================================================

await cargarEmpresas();

configurarSelectorEmpresa();

mostrarDashboard();
