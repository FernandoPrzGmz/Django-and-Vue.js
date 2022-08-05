===================================
Comenzando nuevo proyecto de Vue.js
===================================

Requisitos previos
==================

Node
~~~~
"Node.js es un entorno de ejecución para JavaScript construido con V8, motor de JavaScript de Chrome".
`Sitio oficial de Node.Js <https://nodejs.org/es/>`__

NPM
~~~
Gestor de paquetes de node. Tiene propocitos similares a herramientas como: pip, pipenv, poetry.


.. admonition:: Pipenv
    :class: info

    Npm viene integrado junto a la instalación de Node.js

    Una alternativa muy popular a "NPM" es `"Yarn" <https://yarnpkg.com/>`__.

Instalar @vue/cli
=================

Vue CLI es una librería que permite usar comandos en la consola del
ordenador para automatizar ciertas tareas. Podemos verlo como si fuera
el ``django-admin``.

.. code:: bash

    npm install -g @vue/cli

Iniciar proyecto de Vue.js con @vue/cli
=======================================

Nos posicionamos en el directorio que contendra el proyecto de vue.
Adicionalmente, utiliamos @vue/cli para que nos ayude en la creación
del proyecto de Vue.js

.. code:: bash

    cd vue
    vue create .

Nos preguntara si queremos generar proyecto en el directorio actual. A lo cual,
seleccionamos la opción ``Yes``. Adicionalmente, nos pedirá que seleccionemos
la opción de Vue.js. Para este proyecto seleccionaremos la opcion de Vue 3.

.. code:: bash

    Vue CLI v5.0.8
    ? Generate project in current directory? (Y/n): Yes

    ? Please pick a preset:
    ❯ Default ([Vue 3] babel, eslint)
      Default ([Vue 2] babel, eslint)
      Manually select features

    ✨  Creating project in /home/fernando/Documentos/Django-and-Vue.js/vue.
    ⚙️  Installing CLI plugins. This might take a while...


    added 849 packages, and audited 850 packages in 50s

    88 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities
    🚀  Invoking generators...
    📦  Installing additional dependencies...


    added 85 packages, and audited 935 packages in 8s

    99 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities
    ⚓  Running completion hooks...

    📄  Generating README.md...

    🎉  Successfully created project vue.
    👉  Get started with the following commands:

     $ npm run serve

Lo anterior nos generará el proyecto de vue con la siguiente estructura de
directorios

.. code:: text

    .
    ├── babel.config.js
    ├── jsconfig.json
    ├── package.json
    ├── package-lock.json
    ├── public
    │   ├── favicon.ico
    │   └── index.html
    ├── README.md
    ├── src
    │   ├── App.vue
    │   ├── assets
    │   │   └── logo.png
    │   ├── components
    │   │   └── HelloWorld.vue
    │   └── main.js
    └── vue.config.js

Podemos comprobar el proyecto iniciandolo con el siguiente comando.

.. code:: bash

    npm run serve

Lo anterior iniciara el proyecto en el puerto 8080, por lo que podemos
entrar al navegador a ver el proyecto inicial de Vue.

.. code:: text

    App running at:
      - Local:   http://localhost:8080/
      - Network: http://192.168.0.15:8080/

    Note that the development build is not optimized.
    To create a production build, run npm run build.

.. image:: https://user-images.githubusercontent.com/85954707/182753677-b3da8c28-9cf7-4491-8902-307b311a866d.png

Conexión con Django
===================

El primer paso es instalar el paquete de node llamado ``webpack-bundle-tracker``.

.. code:: bash

    npm install --save-dev webpack-bundle-tracker


.. admonition:: Objetivo de ``webpack-bundle-tracker``
    :class: important

    Se encarga de brindar información sobre el estado de la compilación de Webpack
    a un archivo JSON que será interpretado por ``django-webpack-loader``.

    .. literalinclude :: ./../../../../vue/webpack-stats.json
       :language: json

Posteriormente debemos modificar el fichero general de configuración del proyecto de Vue ``vue.config.js``.

Los cambios que se realizarán son sobre el comportamiento de webpack.

.. literalinclude :: ./../../../../vue/vue.config.js
   :language: js


.. image:: https://user-images.githubusercontent.com/85954707/182994780-61a5a459-afd0-44c6-8a49-ec1e9455163b.png