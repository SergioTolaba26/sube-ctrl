import {

    mostrarDashboard,
    mostrarEjercicios,
    mostrarCuentas,
    mostrarAsientos,

} from "./router.js";


if ("serviceWorker" in navigator) {

    navigator.serviceWorker.register(
        "service-worker.js",
    );

}


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


mostrarDashboard();