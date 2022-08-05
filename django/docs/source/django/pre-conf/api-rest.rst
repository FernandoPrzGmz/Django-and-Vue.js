===================================================================
Exponiendo los recursos mediante API REST con Django REST Framework
===================================================================

Configuración de Django REST Framework
======================================

.. admonition:: Configuración Django REST Framework
    :class: important

    Por fines prácticos, los recursos de la API REST son públicos. Es decir,
    no requieren ningún tipo de autentificación ni permisos.


.. code:: python

   # settings.py
   # ...

   REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [],
      'DEFAULT_PERMISSION_CLASSES': [],
      # ...
   }

   # ...


Endpoints
=========

.. literalinclude :: ./../../../../src/apps/refugio/api/views.py
   :language: python


.. admonition:: Documentación del API
    :class: important

    Puede consultar la documentación del API en los siguientes enlaces:
    `ReDoc </api/schema/redoc/>`__ o `Swagger </api/schema/swagger-ui/>`__