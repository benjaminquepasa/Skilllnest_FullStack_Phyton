from mysqlconnection import connectToMySQL

class Usuario:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en un objeto Usuario.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.apellido = data["apellido"]

        self.email = data["email"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Recupera todos los usuarios de la base de datos.

        Retorna una lista de objetos Usuario.
        """

        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id;
        """

        resultados = connectToMySQL(
            "esquema_usuarios"
        ).query_db(query)

        usuarios = []

        for usuario in resultados:

            usuarios.append(
                cls(usuario)
            )

        return usuarios

    @classmethod
    def save(cls, data):
        """
        Inserta un nuevo usuario en la base de datos.

        Recibe un diccionario con:

        nombre
        apellido
        email
        """

        query = """
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s,
                NOW(),
                NOW()
            );
        """

        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )