let toastActual = null;

export function mostrarToast(
    mensaje,
    tipo = "info",
) {

    if (toastActual) {

        toastActual.remove();

    }

    const toast = document.createElement(
        "div",
    );

    toast.className = `toast toast-${tipo}`;

    toast.textContent = mensaje;

    document.body.appendChild(
        toast,
    );

    toastActual = toast;

    setTimeout(() => {

        toast.remove();

        if (toastActual === toast) {

            toastActual = null;

        }

    }, 3000);

}