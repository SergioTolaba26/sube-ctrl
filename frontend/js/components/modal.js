let modalActual = null;

export function abrirModal({

    titulo,

    contenido,

    textoAceptar = "Aceptar",

    textoCancelar = "Cancelar",

    onAceptar = null,

}) {

    cerrarModal();

    const overlay = document.createElement(
        "div",
    );

    overlay.id = "modal-overlay";

    overlay.className = "modal-overlay";

    overlay.innerHTML = `

        <div class="modal">

            <div class="modal-header">

                <h3>${titulo}</h3>

            </div>

            <div class="modal-body">

                ${contenido}

            </div>

            <div class="modal-footer">

                <button id="btn-modal-cancelar">

                    ${textoCancelar}

                </button>

                <button id="btn-modal-aceptar">

                    ${textoAceptar}

                </button>

            </div>

        </div>

    `;

    document.body.appendChild(
        overlay,
    );

    modalActual = overlay;

    document
        .getElementById(
            "btn-modal-cancelar",
        )
        .addEventListener(

            "click",

            cerrarModal,

        );

    document
        .getElementById(
            "btn-modal-aceptar",
        )
        .addEventListener(

            "click",

            async () => {

                const formulario =
                    modalActual.querySelector("form");

                if (

                    formulario &&

                    !formulario.reportValidity()

                ) {

                    return;

                }

                if (onAceptar) {

                    await onAceptar();

                }

            },

        );
}
export function cerrarModal() {

    if (modalActual) {

        modalActual.remove();

        modalActual = null;

    }

}
//Mejora UX
export function mostrarMensaje(
    titulo,
    mensaje,
) {

    alert(`${titulo}\n\n${mensaje}`);

}