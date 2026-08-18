let empresaSeleccionada = null;


export function establecerEmpresa(
    empresa,
) {

    empresaSeleccionada = empresa;

}


export function obtenerEmpresaSeleccionada() {

    return empresaSeleccionada;

}