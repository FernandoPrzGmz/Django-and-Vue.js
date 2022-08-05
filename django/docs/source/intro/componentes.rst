=============================
Fundamentos sobre Componentes
=============================

.. raw:: html

    <script src="https://unpkg.com/vue@3"></script>

¿Qué es un componente?
======================

Los componentes son instancias reutilizables de Vue con un nombre.
Podemos usar este componente como un elemento personalizado dentro
de una instancia de Vue.

.. code:: html

    <div id="app-1">
        <button-counter></button-counter>
    </div>

    <script>
        // Componente raíz
        const app = Vue.createApp({})

        // Componente Boton
        app.component('button-counter', {
            template: `<button v-on:click="count++">
                            Me han pulsado {{ count }} veces.
                       </button>`,
            data: function () {
                return {
                    count: 0
                }
            },
        })

        // Instancia de Vue
        const vm = app.mount('#app-1')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-1">
            <button-counter></button-counter>
        </div>

        <script>
            // Componente raíz
            const app = Vue.createApp({})

            // Componente Boton
            app.component('button-counter', {
                template: `<button v-on:click="count++">
                                Me han pulsado {{ count }} veces.
                           </button>`,
                data: function () {
                    return {
                        count: 0
                    }
                },
            })

            // Instancia de Vue
            const vm = app.mount('#app-1')
        </script>

Los componentes se pueden reutilizar tantas veces como se desee
===============================================================

Debido a que **los componentes mantienen su propio estado independiente**,
cada componente que invoquemos mantendra el valor de ``count`` por separado.

Cada vez que se utiliza un componente se crea una instancia del mismo.


.. code:: html

    <div id="app-2">
        <button-counter></button-counter>
        <button-counter></button-counter>
        <button-counter></button-counter>
    </div>

    <script>
        // Componente raíz
        const app2 = Vue.createApp({})

        // Componente Boton
        app2.component('button-counter', {
            template: `<button v-on:click="count++">
                            Me han pulsado {{ count }} veces.
                       </button>`,
            data: function () {
                return {
                    count: 0
                }
            },
        })

        // Instancia de Vue
        const vm2 = app2.mount('#app-2')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-2">
            <button-counter></button-counter>
            <br><br>
            <button-counter></button-counter>
            <br><br>
            <button-counter></button-counter>
        </div>

        <script>
            // Componente raíz
            const app2 = Vue.createApp({})

            // Componente Boton
            app2.component('button-counter', {
                template: `<button v-on:click="count++">
                                Me han pulsado {{ count }} veces.
                           </button>`,
                data: function () {
                    return {
                        count: 0
                    }
                },
            })

            // Instancia de Vue
            const vm2 = app2.mount('#app-2')
        </script>


Nomenclatura
============

Cuando registramos un componente, siempre se le asignará un nombre.
Puede definirse el nombre del componente con:

- ``kebab-case``
    .. code:: js

        app.component('my-component-name', { /* ... */ })

- ``PascalCase``.
    .. code:: js

        app.component('MyComponentName', { /* ... */ })

Organización de Componentes
===========================

Una aplicación comunmente se organiza en un árbol de componentes anidados.

.. image:: https://es.vuejs.org/images/components.png
    :alt: Arbol de componentes

.. image:: https://vuejs.org/assets/components.7fbb3771.png


Vue Option API (Vue 2+)
=======================

Esta modalidad de API se basa en el uso de un objeto que contiene varias propiedades
clave para el funcionamiento de los componentes Vue.

.. code:: js

    const options = {
        template: '...',
        data: '...',
        props: '...',
        computed: '...',
        watch: '...',
        methods: '...',
    }

    const app = Vue.createApp({})
    app.component('my-component-name', options)
    const vm = app.mount('#app')


data - ``function``
~~~~~~~~~~~~~~~~~~~

Función que devuelve un ``object`` con las variables del componente Vue.

.. code:: html

    <div id="app-3">
        <my-component-name/>
    </div>

    <script>
        const app3 = Vue.createApp({})

        app3.component('my-component-name', {
            template: `<div>
                            <p>Hello {{ name }}.</p>
                       </div>`,
            data: function () {
                return {
                    name: 'Fernando Pérez Gómez'
                }
            },
        })

        const vm3 = app3.mount('#app-3')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

            <div id="app-3">
                <my-component-name/>
            </div>

            <script>
                const app3 = Vue.createApp({})

                app3.component('my-component-name', {
                    template: `<div>
                            <p>Hello {{ name }}.</p>
                       </div>`,
                    data: function () {
                        return {
                            name: 'Fernando Pérez Gómez'
                        }
                    },
                })

                const vm3 = app3.mount('#app-3')
            </script>

props - ``array`` | ``object``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lista de atributos (props) aceptados desde el componente padre.

.. code:: html

    <div id="app-4">
        <my-component-name
            location="PyCun"
        />
    </div>

    <script>
        const app4 = Vue.createApp({})

        app4.component('my-component-name', {
            template: `<div>
                            <p>Hello {{ name }}.</p>

                            <!-- New: props -->
                            <p>Welcome to {{ location }}</p>

                       </div>`,
            data: function () {
                return {
                    name: 'Fernando Pérez Gómez'
                }
            },

            // New: props
            props: ['location'],
            /*
            props: {
                location: String,
                id: {
                    type: Number,
                    default: 1,
                    required: true,
                    validator: number => number > 0
                },
            },
            */
        })

        const vm4 = app4.mount('#app-4')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-4">
            <my-component-name
                location="PyCun"
            />
        </div>

        <script>
            const app4 = Vue.createApp({})

            app4.component('my-component-name', {
                template: `<div>
                                <p>Hello {{ name }}.</p>

                                <!-- New: props -->
                                <p>Welcome to {{ location }}</p>

                           </div>`,
                data: function () {
                    return {
                        name: 'Fernando Pérez Gómez'
                    }
                },

                // New: props
                props: ['location'],
                /*
                props: {
                    location: String
                },
                */
            })

            const vm4 = app4.mount('#app-4')
        </script>

.. code:: python

    class Foo:
        def __init__(self, bar):
            self.bar = bar
        
    foo = Foo(bar='bar')


computed - ``object``
~~~~~~~~~~~~~~~~~~~~~
Funciones que se ejecutarán cuando se acceda a la propiedad en cuestión.

.. code:: html

    <div id="app-5">
        <my-component-name
            location="PyCun"
        />
    </div>

    <script>
        const app5 = Vue.createApp({})

        app5.component('my-component-name', {
            template: `<div>
                            <p>Hello {{ name }}.</p>
                            <p>Welcome to {{ location }}</p>

                            <!-- New: computed-->
                            <p>Date: {{ today }}</p>
                       </div>`,
            data: function () {
                return {
                    name: 'Fernando Pérez Gómez'
                }
            },
            props: ['location'],

            // New: computed
            computed: {
                today: function () {
                    const date = new Date()
                    return date.toString()
                }
            }
        })

        const vm5 = app5.mount('#app-5')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-5">
            <my-component-name
                location="PyCun"
            />
        </div>

        <script>
            const app5 = Vue.createApp({})

            app5.component('my-component-name', {
                template: `<div>
                                <p>Hello {{ name }}.</p>
                                <p>Welcome to {{ location }}</p>
                                <p>Date: {{ today }}</p>
                           </div>`,
                data: function () {
                    return {
                        name: 'Fernando Pérez Gómez'
                    }
                },
                props: ['location'],

                computed: {
                    today: function () {
                        const date = new Date()
                        return date.toString()
                    }
                }
            })

            const vm5 = app5.mount('#app-5')
        </script>

Podemos ver este funcionamiento en python.

.. code:: python

    class Example:
        @property
        def today(self):
            date = datetime.datetime.today()
            return str(date)

    e = Example()
    e.today  # 2022-07-31 15:25:40.485661

watch - ``object``
~~~~~~~~~~~~~~~~~~~~
Lista de funciones que se disparan cuando detecten cambios en variables con su nombre.

.. code:: html

    <div id="app-6">
        <my-component-name/>
    </div>

    <script>
        const app6 = Vue.createApp({})

        app6.component('my-component-name', {
            template: `<button v-on:click="count++">
                            Me han pulsado {{ count }} veces.
                       </button>`,
            data: function () {
                return {
                    count: 0
                }
            },

            // New: watch
            watch: {
                count: function (val, oldVal) {
                    console.log(`Count ha cambiado!...
                                Su anterior valor era ${oldVal}
                                y ahora es ${val}`)
                }
            }
        })

        const vm6 = app6.mount('#app-6')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-6">
            <my-component-name
                location="PyCun"
            />
        </div>

        <script>
            const app6 = Vue.createApp({})

            app6.component('my-component-name', {
                template: `<button v-on:click="count++">
                                Me han pulsado {{ count }} veces.
                           </button>`,
                data: function () {
                    return {
                        count: 0
                    }
                },

                // New: watch
                watch: {
                    count: function (val, oldVal) {
                        console.log(`Count ha cambiado!... Su anterior valor era ${oldVal} y ahora es ${val}`)
                    }
                }
            })

            const vm6 = app6.mount('#app-6')
        </script>

methods - ``object``
~~~~~~~~~~~~~~~~~~~~
Lista de funciones (métodos) disponibles en el componente Vue.

.. code:: html

    <div id="app-7">
        <my-component-name/>
    </div>

    <script>
        const app7 = Vue.createApp({})

        app7.component('my-component-name', {
            template: `<button v-on:click="handleClick">
                            Me han pulsado {{ count }} veces.
                       </button>`,
            data: function () {
                return {
                    count: 0
                }
            },

            // New: methods
            methods: {
                handleClick: function () {
                    this.count++
                }
            }
        })

        const vm7 = app7.mount('#app-7')
    </script>

.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-7">
            <my-component-name
                location="PyCun"
            />
        </div>

        <script>
            const app7 = Vue.createApp({})

            app7.component('my-component-name', {
                template: `<button v-on:click="handleClick">
                                Me han pulsado {{ count }} veces.
                           </button>`,
                data: function () {
                    return {
                        count: 0
                    }
                },

                // New: methods
                methods: {
                    handleClick: function () {
                        this.count++
                    }
                }
            })

            const vm7 = app7.mount('#app-7')
        </script>