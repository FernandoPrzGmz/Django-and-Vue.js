================================
Creando el componente raíz o App
================================

Previo a realizar cualquier cambio instalaremos ``axios`` que es similar
a ``requests`` de Python.

Para obtener la información de la lista de mascotas utilizaremos ``axios``
para hacer peticiones al API que construimos con Django REST Framework.

.. code:: bash

    npm install axios


Cambio #1 - Uso del componente CardMascota y directivas v-if y v-for
====================================================================

Django
~~~~~~
.. image:: https://user-images.githubusercontent.com/85954707/183151347-bfe68efa-00fe-42da-979b-e8567a0ccc6c.png

Vue
~~~
.. image:: https://user-images.githubusercontent.com/85954707/183151492-dced3d1c-f3a9-4ebe-8c8d-e2c3c58deb54.png

.. code:: html

    <script>
    import axios from "axios";
    import CardMascota from './components/CardMascota.vue'

    export default {
      name: 'App',

      components: {
        CardMascota
      },

      data: function () {
        return {
          listaMascotas: [],
        }
      },

      methods: {
        fetchListaMascotas: async function () {
          const response = await axios.get('/api/mascotas/')
          this.listaMascotas = response.data;
        }
      },

      mounted() {
        this.fetchListaMascotas()
      }
    }
    </script>


.. raw:: html

    <a class="btn" href="/vue">Ir a la lista de mascotas de Vue.js</a>