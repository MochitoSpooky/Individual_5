1 -Restricción de acceso basada en autenticación:
   - Limita el acceso a partes de la aplicación solo a usuarios autenticados.
   - Utiliza decoradores o middleware para verificar si un usuario está autenticado.
   - Redirecciones: Los usuarios no autenticados serán redirigidos a la página de inicio de sesión.

Cuando se implementa una restricción de acceso basada en autenticación, se garantiza que solo los usuarios autenticados puedan acceder a ciertas partes o funcionalidades de un sitio web. Esto significa que un usuario debe haber iniciado sesión en su cuenta para poder acceder a esas áreas restringidas.

a.- El usuario visita una página o funcionalidad en el sitio web que requiere autenticación, por ejemplo, una página de perfil personalizada o un panel de administración.

b.- Si el usuario no ha iniciado sesión, se le redirige automáticamente a la página de inicio de sesión.

c.- El usuario completa el formulario de inicio de sesión con su nombre de usuario y contraseña.

d.- El sitio web verifica las credenciales del usuario. Si son válidas, se considera que el usuario está autenticado y se le permite acceder a la página restringida.

e.- Si las credenciales son incorrectas, el usuario recibirá un mensaje de error y se le pedirá que vuelva a intentarlo.

Una vez que el usuario ha iniciado sesión correctamente, puede acceder libremente a todas las páginas y funcionalidades restringidas durante su sesión activa. Si el usuario intenta acceder a esas áreas restringidas después de que su sesión haya expirado, se le pedirá que inicie sesión nuevamente.


2 -Restriccion de acceso basada en desconeccion por inactividad:

La restricción de acceso por tiempo inactivo es una medida de seguridad que desconecta automáticamente a un usuario si ha estado inactivo durante un período de tiempo determinado. Es útil para proteger la sesión de un usuario y prevenir el acceso no autorizado en caso de que el usuario se olvide de cerrar sesión.

La implementación de esta restricción implica el seguimiento del tiempo de la última actividad del usuario. Si el tiempo transcurrido desde la última actividad supera un umbral predefinido, el usuario se desconecta y se le redirige a la página de inicio de sesión.

En resumen, la restricción de acceso por tiempo inactivo garantiza que los usuarios sean desconectados automáticamente si no interactúan con la aplicación durante un tiempo especificado, lo que ayuda a proteger su información y mejorar la seguridad de la sesión.