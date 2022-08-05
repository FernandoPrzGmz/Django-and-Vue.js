===================
Creando primera App
===================

¿Qúe es Vue?
============

Vue framework de JavaScript para construir interfaces de usuario.
Se basa en HTML, CSS y JavaScript, y proporciona un modelo de
programación basado en componentes.

Es un framework progresivo, es decir que esta diseñado para ser
flexible y adaptarse de la forma incremental cubriendo la mayoria
de las caracteristicas comunes necesarias en el desarrollo frontend
sin tener que implementar todas.


Comenzando a desarrollar nuestra primera aplicación
===================================================

Todas las aplicaciones de Vue comienzan creando una nueva instancia de
aplicación con la funcion ``createApp``:

Cada aplicación requiere un "componente raíz" que puede contener otros
componentes como sus hijos.

.. code:: js

    import { createApp } from 'vue';

    const app = createApp({
        /* Componente raíz */
    });


Montaje de la aplicación
========================

Una instancia de Vue no representará nada hasta que se llame a su método ``.mount()``.

Este método espera un argumento de "contenedor", que puede ser un elemento DOM real o un selector.

.. code:: html

    <!-- file: app.html -->
    <div id="app"></div>

.. code:: js

    // file: app.js
    app.mount('#app')

Múltiples instancias de aplicación
==================================

No existe limitación a manejar una única instancia de Vue en la misma página.
La API de ``createApp`` permite que varias aplicaciones de Vue coexistan en
la misma página, cada una con su propio instancia de configuración.

.. code:: js

    const app1 = createApp({
        /* ... */
    });
    app1.mount('#container-1');

    const app2 = createApp({
        /* ... */
    });
    app2.mount('#container-2');


.. admonition:: Area de oportunidad
    :class: important

    Puede aprovechar esta caracteristica de Vue para mejorar el HTML generado por Django.
    Puede utilizar instancias pequeñas de Vue para controlar partes específicas de una página grande.


"Hola PyCun" sin herramientas de compilación
============================================

.. code:: html

    <script src="https://unpkg.com/vue@3"></script>

    <div id="app">{{ message }}</div>

    <script>
        const { createApp } = Vue

        createApp({
            data() {
                return {
                    message: '¡Hola! bienvenidos y bienvenidas a PyCun.'
                }
            }
        }).mount('#app')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <script src="https://unpkg.com/vue@3"></script>

        <div id="app">{{ message }}</div>

        <script>
            const { createApp } = Vue

            createApp({
                data() {
                    return {
                        message: '¡Hola! bienvenidos y bienvenidas a PyCun.'
                    }
                }
            }).mount('#app')
        </script>
