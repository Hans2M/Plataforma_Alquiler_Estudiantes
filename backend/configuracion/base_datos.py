# Configuración de base de datos.
# Este archivo será responsable de preparar posteriormente la conexión del backend con PostgreSQL mediante SQLAlchemy.
# Las credenciales no se escribirán directamente aquí; se obtendrán desde variables de entorno.
# Las implementaciones de repositorios utilizarán la sesión/conexión configurada desde esta capa.
# Flujo previsto: Servicio -> interfaz/repositorio -> SQLAlchemy -> PostgreSQL.
