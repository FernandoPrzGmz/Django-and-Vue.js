.. Django y Vue.js documentation master file, created by
   sphinx-quickstart on Wed Jul 27 20:03:37 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
Introducción a Vue.js con Django
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/intro/index
   source/django/index
   source/vue/index

Instalación del proyecto
========================

.. admonition:: Pipenv
    :class: info

    Este proyecto utiliza pipenv para la creación de entornos virtuales y la
    instalación de dependencias requeridas en el proyecto.

    Por lo tanto, previamente debe tener la herramienta de pipenv instalada y
    configurada correctamente.


Para la creación del entorno e instalación de las dependencias del proyecto, ejecute
las siguientes instrucciones en la ruta principal del proyecto "/django".

.. code:: bash

    pipenv shell
    pipenv install

A continuación, ejecute el comando "demo" de los scripts definidos en el Makefile.

.. code:: bash

    make demo


.. admonition:: Contraseña superuser
    :class: important

    Al final de este scripts se le solicitará que introduzca una contraseña para el
    super usuario "pycun". Por favor, defina la contraseña de su preferencia.


Construcción de los archivos de documentación
=============================================

Utilice el comando "docs" de los scripts definidos en el Makefile

.. code:: bash

    make docs

A continuación, abra el archivo "index.html" desde el navegador.
