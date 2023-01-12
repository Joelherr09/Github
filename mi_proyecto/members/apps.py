from django.apps import AppConfig

"""
En este caso, la clase MembersConfig se utiliza para especificar el nombre de la aplicación y el campo de clave principal predeterminado
para la aplicación "members". Estos valores se utilizarán por Django durante la ejecución del proyecto. Por ejemplo, el nombre de la aplicación
se utilizará para nombrar la base de datos y para referirse a la aplicación en mensajes de error y mensajes de depuración.
El campo de clave principal predeterminado se utilizará cuando se cree un modelo de base de datos para la aplicación
y no se especifique explícitamente un campo de clave principal.
"""

class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
