=====================================
Configuracion para el build de Vue.js
=====================================

Webpack
=======

.. image:: https://www.campusmvp.es/recursos/image.axd?picture=/2017/4T/Webpack-Concepto.gif

Nuevas dependencias
===================

Instalación del paquete ``django-webpack-loader``. Nos permite **consumir desde django** el bundle de
los paquetes generados con webpack.

.. code:: bash

    pip install django-webpack-loader


Configuración del settings.py
=============================

Primero se debe agregar la dependencia en los ``INSTALLED_APPS`` de Django.

.. code:: python

    INSTALLED_APPS = [
        # ...

        'webpack_loader',

        # ...
    ]


.. code:: python

    # settings.py
    # ...

    VUE_DIR = BASE_DIR.parent.parent / 'vue/'

    WEBPACK_LOADER = {
        'DEFAULT': {
            'CACHE': not DEBUG,
            'BUNDLE_DIR_NAME': 'webpack_bundles/',

            'STATS_FILE': VUE_DIR / 'webpack-stats.json',

            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
            'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
            'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
        }
    }

    # ...


.. literalinclude :: ./../../../../../vue/webpack-stats.json
   :language: js

Indicando el bundle de Vue.js en las plantillas de Django
=========================================================

.. literalinclude :: ./../../../../src/apps/refugio/views/vue.py
   :language: python

.. literalinclude :: ./../../../../src/templates/vue/index.html
   :language: html

.. code:: python

   from django.urls import path

   from src.apps.refugio import views

   urlpatterns = [
       # ...
       path('vue/', views.VueView.as_view(), name='vue'),
   ]