const API_URL = 'http://127.0.0.1:8000';

export async function obtenerEjercicios() {
  const respuesta = await fetch(`${API_URL}/ejercicios`);

  if (!respuesta.ok) {
    throw new Error('No se pudieron obtener los ejercicios.');
  }

  return await respuesta.json();
}
export async function obtenerCuentas() {

    const respuesta = await fetch(
        `${API_URL}/cuentas`
    );

    if (!respuesta.ok) {

        throw new Error(
            "No se pudieron obtener las cuentas."
        );

    }

    return await respuesta.json();

}

export async function obtenerAsientos() {

    const respuesta = await fetch(
        `${API_URL}/asientos`
    );

    if (!respuesta.ok) {

        throw new Error(
            "No se pudieron obtener los asientos."
        );

    }

    return await respuesta.json();

}