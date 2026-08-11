class EmpresaContext:
    """
    Provee la empresa activa.

    Por ahora devuelve una empresa fija.
    En el futuro obtendrá el empresa_id desde
    la sesión o el usuario autenticado.
    """

    def obtener_empresa_id(
        self,
    ) -> int:

        return 1