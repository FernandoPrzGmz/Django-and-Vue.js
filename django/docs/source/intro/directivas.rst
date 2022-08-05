==========
Directivas
==========

.. raw:: html

    <script src="https://unpkg.com/vue@3"></script>


Son atributos especiales que se colocan en las etiquetas HTML o
componentes y están prefijados por ``v-``. Permiten realizar
acciones dinámicas como bucles, condicionales, etc.

.. imagen:: https://lenguajejs.com/vuejs/directivas-vue/que-son-directivas/directivas-vue.png


Directiva ``v-text``
====================

Vue permite acceder a las variables desde la parte del templates (HTML) escribiendo la variable
entre ``{{`` dos llaves ``}}`` lo que se conoce como, "sintaxis de plantillas" o "formato mustache".

La directiva ``v-text`` hace exactamente lo mismo. En la práctica no se utiliza ya que es menos legible.

.. code:: html

    <div id="app-1">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app1 = Vue.createApp({})

        app1.component('my-component-name', {
            template: `<h4 v-text="'Hola PyCun'"></h4>`,
        })

        const vm1 = app1.mount('#app-1')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-1">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app1 = Vue.createApp({})

            app1.component('my-component-name', {
                template: `<h4 v-text="txt"></h4>`,
                data: function () {
                    return {
                        txt: 'Hola PyCun',
                    }
                }
            })

            const vm1 = app1.mount('#app-1')
        </script>


Directiva ``v-html``
====================

La directiva ``v-html`` funciona exactamente igual que ``v-text``, solo que en lugar de mostrar
las etiquetas, las procesa y renderiza.

.. code:: html

    <div id="app-2">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app2 = Vue.createApp({})

        app2.component('my-component-name', {
            template: `<div v-html="html"></div>`,
            data: function () {
                return {
                    html: `<h4 style='color: red;'>Hola PyCun</h4>`,
                }
            }
        })

        const vm2 = app2.mount('#app-2')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-2">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app2 = Vue.createApp({})

            app2.component('my-component-name', {
                template: `<div v-html="html"></div>`,
                data: function () {
                    return {
                        html: `<h4 style='color: red;'>Hola PyCun</h4>`,
                    }
                }
            })

            const vm2 = app2.mount('#app-2')
        </script>

Directiva ``v-pre``
===================

Nos permite escribir texto literal evitando que se rendericen los elementos del template y sus hijos.


.. code:: html

    <div id="app-3">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app3 = Vue.createApp({})

        app3.component('my-component-name', {
            template: `<div>
                            <!-- Se renderiza al valor de la variable -->
                            <div>{{ txt }}</div>

                            <!-- No se renderiza -->
                            <div v-pre>{{ txt }}</div>
                       </div>`,
            data: function () {
                return {
                    txt: 'Hola PyCun'
                }
            }
        })

        const vm3 = app3.mount('#app-3')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-3">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app3 = Vue.createApp({})

            app3.component('my-component-name', {
                template: `<div>
                                <!-- Se renderiza al valor de la variable -->
                                <div>{{ txt }}</div>

                                <!-- No se renderiza -->
                                <div v-pre>{{ txt }}</div>
                           </div>`,
                data: function () {
                    return {
                        txt: 'Hola PyCun'
                    }
                }
            })

            const vm3 = app3.mount('#app-3')
        </script>


Directiva ``v-show``
=====================

Muestra u oculta (con display: none;) dependiendo del valor booleano que reciba.


.. code:: html

    <div id="app-4">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app4 = Vue.createApp({})

        app4.component('my-component-name', {
            template: `<div>
                            <button v-on:click="toggle = !toggle">
                                Click me!
                            </button>
                            <h4 v-show="toggle">Hola PyCun</h4>
                       </div>`,
            data: function () {
                return {
                    toggle: true
                }
            }
        })

        const vm4 = app4.mount('#app-4')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-4">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app4 = Vue.createApp({})

            app4.component('my-component-name', {
                template: `<div>
                            <button v-on:click="toggle = !toggle">
                                Click me!
                            </button>
                            <h4 v-show="toggle">Hola PyCun</h4>
                       </div>`,
                data: function () {
                    return {
                        toggle: true
                    }
                }
            })

            const vm4 = app4.mount('#app-4')
        </script>


Directiva ``v-if``, ``v-else-if`` y ``v-else``
==============================================

Muy similar al ``{% if var %}``, ``{% elif %}`` y ``{% else %}`` de Django

.. code:: html

    <div id="app-5">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app5 = Vue.createApp({})

        app5.component('my-component-name', {
            template: `<div>
                            <input v-model="value"/>
                            <h4 v-if="!value">Error!</h4>
                            <h4 v-else-if="value % 2 === 0">{{ value }} es un número par</h4>
                            <h4 v-else>{{ value }} es un número impar</h4>
                       </div>`,
            data: function () {
                return {
                    value: 2022
                }
            }
        })

        const vm5 = app5.mount('#app-5')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-5">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app5 = Vue.createApp({})

            app5.component('my-component-name', {
                template: `<div>
                                <input v-model="value"/>
                                <h4 v-if="value % 2 === 0">{{ value }} es un número par</h4>
                                <h4 v-else>{{ value }} es un número impar</h4>
                           </div>`,
                data: function () {
                    return {
                        value: 2022
                    }
                }
            })

            const vm5 = app5.mount('#app-5')
        </script>


Directiva ``v-for``
===================

Muy similar al ``{% for v in var %}`` de Django. La directiva ``v-bind:key`` o ``:key``
es un elemento importante cuando se utiliza el ``v-for``.

El valor de ``:key`` debe ser un valor unico para que Vue identifique qué elemento
renderizar si ocurre algun cambio.

.. code:: html

    <div id="app-6">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app6 = Vue.createApp({})

        app6.component('my-component-name', {
            template: `<div>
                            <h4 v-for="(item, index) in array" v-bind:key="item + index">
                                {{ item }}
                            </h4>
                       </div>`,
            data: function () {
                return {
                    array: ['Django', 'Flask', 'FastAPI', 'Web2Py']
                }
            }
        })

        const vm6 = app6.mount('#app-6')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-6">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app6 = Vue.createApp({})

            app6.component('my-component-name', {
                template: `<div>
                                <h4 v-for="(item, index) in array" v-bind:key="item + index">
                                    {{ item }}
                                </h4>
                           </div>`,
                data: function () {
                    return {
                        array: ['Django', 'Flask', 'FastAPI', 'Web2Py']
                    }
                }
            })

            const vm6 = app6.mount('#app-6')
        </script>



Directiva ``v-on`` **
=====================

La directiva v-on (abreviada como @) es una directiva utilizada para gestionar los eventos del DOM,
haciendo más cómodo y práctico su uso, permitiendo escribir mucho menos código.

.. code:: html

    <button class="alert">Click me</button>

    <script>
        const button = document.querySelector("button.alert");
        button.addEventListener("click", () => {
          alert("Hola PyCun");
        });
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <button class="alert">Click me</button>

        <script>
            const button = document.querySelector("button.alert")
            button.addEventListener("click", () => {
              alert("Hola PyCun")
            })
        </script>

Así pues, nos ahorramos realizar ``.addEventListener()``, y en su lugar definimos las acciones de forma
mucho más directa.


.. code:: html

    <div id="app-7">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app7 = Vue.createApp({})

        app7.component('my-component-name', {
            template: `
                        <button v-on:click="handleClick">Click me</button>`,
            methods: {
                handleClick: function () {
                    alert("Hola PyCun")
                }
            }
        })

        const vm7 = app7.mount('#app-7')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-7">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app7 = Vue.createApp({})

            app7.component('my-component-name', {
                template: `
                        <button v-on:click="handleClick">Click me</button>`,
                methods: {
                    handleClick: function () {
                        alert("Hola PyCun")
                    }
                }
            })

            const vm7 = app7.mount('#app-7')
        </script>



.. code:: html

    <div id="app-8">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app8 = Vue.createApp({})

        app8.component('my-component-name', {
            template: `
                        <label for="onInput">onInput</label>
                        <input
                            id="onInput"
                            v-on:input="handleOnInputEvent"
                        />
                        <p>onInput: {{ onInputMessage }}</p>
                        <br><br>

                        <label for="onChange">onChange</label>
                        <input
                            id="onChange"
                            @change="handleOnChangeEvent"
                        />
                        <p>onChange: {{ onChangeMessage }}</p>
                      `,
            data: function () {
                return {
                    onInputMessage: 'Hola PyCun',
                    onChangeMessage: 'Hola PyCun'
                }
            },
            methods: {
                handleOnInputEvent: function (e) {
                    this.onInputMessage = e.target.value;
                },
                handleOnChangeEvent: function (e) {
                    this.onChangeMessage = e.target.value;
                }
            }
        })

        const vm8 = app8.mount('#app-8')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-8">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app8 = Vue.createApp({})

            app8.component('my-component-name', {
                template: `
                        <label for="onInput">onInput</label>
                        <input
                            id="onInput"
                            v-on:input="handleOnInputEvent"
                        />
                        <p>onInput: {{ onInputMessage }}</p>
                        <br><br>

                        <label for="onChange">onChange</label>
                        <input
                            id="onChange"
                            @change="handleOnChangeEvent"
                        />
                        <p>onChange: {{ onChangeMessage }}</p>
                      `,
                data: function () {
                    return {
                        onInputMessage: 'Hola PyCun',
                        onChangeMessage: 'Hola PyCun'
                    }
                },
                methods: {
                    handleOnInputEvent: function (e) {
                        this.onInputMessage = e.target.value;
                    },
                    handleOnChangeEvent: function (e) {
                        this.onChangeMessage = e.target.value;
                    }
                }
            })

            const vm8 = app8.mount('#app-8')
        </script>


Directiva ``v-bind`` **
=======================

La directiva v-bind (abreviada como : ) **es una de las directivas más utilizadas y populares de Vue**.

Esta directiva permite enlazar (bindear) una variable de Vue con un atributo específico de una etiqueta HTML
o props de nuestros componentes. De esta forma, podemos hacer dinamico el valor de un atributo HTML.

.. code:: html

    <div id="app-9">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app9 = Vue.createApp({})

        app9.component('my-component-name', {
            template: `
                        <p>https://static.djangoproject.com/img/logo-django.42234b631760.svg</p>
                        <p>https://flask.palletsprojects.com/en/2.1.x/_images/flask-logo.png</p>
                        <p>https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png</p>
                        <input @input="handleOnInputEvent"/>
                        <img v-bind:src="source"/>
                      `,
                data: function () {
                    return {
                        source: '',
                    }
                },
                methods: {
                    handleOnInputEvent: function (e) {
                        this.source = e.target.value
                    },
                }
        })

        const vm9 = app9.mount('#app-9')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-9">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app9 = Vue.createApp({})

            app9.component('my-component-name', {
                template: `
                        <p>https://static.djangoproject.com/img/logo-django.42234b631760.svg</p>
                        <p>https://flask.palletsprojects.com/en/2.1.x/_images/flask-logo.png</p>
                        <p>https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png</p>
                        <input @input="handleOnInputEvent"/>
                        <img v-bind:src="source"/>
                      `,
                data: function () {
                    return {
                        source: '',
                    }
                },
                methods: {
                    handleOnInputEvent: function (e) {
                        this.source = e.target.value
                    },
                }
            })

            const vm9 = app9.mount('#app-9')
        </script>


Bindeo de clases ``:class``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Permite añadir clases CSS a un elemento HTML


Bindeo de clases ``:class`` - ``string``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aplica la clase indicada en className al elemento

.. code:: html

    <div id="app-10">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app10 = Vue.createApp({})

        app10.component('my-component-name', {
            template: `<h4 :class="className"> Hola PyCun </h4>`,
            data: function () {
                return {
                    className: 'color-red',
                }
            },
        })

        const vm10 = app10.mount('#app-10')
    </script>
    <style>
        .color-red {
            color: red;
        }
        .border-yellow {
            border: solid 10px yellow;
        }
        .bg-color-cyan {
            background-color: cyan;
        }
    </style>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-10">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app10 = Vue.createApp({})

            app10.component('my-component-name', {
                template: `<h4 :class="className"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        className: 'color-red',
                    }
                },
            })

            const vm10 = app10.mount('#app-10')
        </script>
        <style>
            .color-red {
                color: red;
            }
            .border-yellow {
                border: solid 10px yellow;
            }
            .bg-color-cyan {
                background-color: cyan;
            }
        </style>

Bindeo de clases ``:class`` - ``array``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aplica todas las clases contenidas en className a la vez.

.. code:: html

    <div id="app-11">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app11 = Vue.createApp({})

        app11.component('my-component-name', {
            template: `<h4 :class="className"> Hola PyCun </h4>`,
            data: function () {
                return {
                    className: ['color-red', 'border-yellow', 'bg-color-cyan'],
                }
            },
        })

        const vm11 = app11.mount('#app-11')
    </script>
    <style>
        .color-red {
            color: red;
        }
        .border-yellow {
            border: solid 10px yellow;
        }
        .bg-color-cyan {
            background-color: cyan;
        }
    </style>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-11">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app11 = Vue.createApp({})

            app11.component('my-component-name', {
                template: `<h4 :class="className"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        className: ['color-red', 'border-yellow', 'bg-color-cyan'],
                    }
                },
            })

            const vm11 = app11.mount('#app-11')
        </script>
        <style>
            .color-red {
                color: red;
            }
            .border-yellow {
                border: solid 10px yellow;
            }
            .bg-color-cyan {
                background-color: cyan;
            }
        </style>

Bindeo de clases ``:class`` - ``object``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Aplica todas las clases (el nombre de la key) que estén a true.

.. code:: html

    <div id="app-12">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app12 = Vue.createApp({})

        app12.component('my-component-name', {
            template: `<h4 :class="className"> Hola PyCun </h4>`,
            data: function () {
                return {
                    className: {
                        'color-red': true,
                        'border-yellow': true,
                        'bg-color-cyan': false,
                    },
                }
            },
        })

        const vm12 = app12.mount('#app-12')
    </script>
    <style>
        .color-red {
            color: red;
        }
        .border-yellow {
            border: solid 10px yellow;
        }
        .bg-color-cyan {
            background-color: cyan;
        }
    </style>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-12">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app12 = Vue.createApp({})

            app12.component('my-component-name', {
                template: `<h4 :class="className"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        className: {
                            'color-red': true,
                            'border-yellow': true,
                            'bg-color-cyan': false,
                        },
                    }
                },
            })

            const vm12 = app12.mount('#app-12')
        </script>
        <style>
            .color-red {
                color: red;
            }
            .border-yellow {
                border: solid 10px yellow;
            }
            .bg-color-cyan {
                background-color: cyan;
            }
        </style>



Bindeo de estilos ``:style``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Bindeo de estilos ``:style`` - ``string``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aplica la clase indicada en className al elemento

.. code:: html

    <div id="app-13">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app13 = Vue.createApp({})

        app13.component('my-component-name', {
            template: `<h4 :style="styles"> Hola PyCun </h4>`,
            data: function () {
                return {
                    styles: 'color: red',
                }
            },
        })

        const vm13 = app13.mount('#app-13')
    </script>



.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-13">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app13 = Vue.createApp({})

            app13.component('my-component-name', {
                template: `<h4 :style="styles"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        styles: 'color: red',
                    }
                },
            })

            const vm13 = app13.mount('#app-13')
        </script>

Bindeo de estilos ``:style`` - ``array``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aplica todas las clases contenidas en className a la vez.

.. code:: html

    <div id="app-14">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app14 = Vue.createApp({})

        app14.component('my-component-name', {
            template: `<h4 :style="styles"> Hola PyCun </h4>`,
            data: function () {
                return {
                    styles: [
                        'color: red',
                        'border: solid 10px yellow',
                        'background-color: cyan'
                    ],
                }
            },
        })

        const vm14 = app14.mount('#app-14')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-14">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app14 = Vue.createApp({})

            app14.component('my-component-name', {
                template: `<h4 :style="styles"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        styles: [
                            'color: red',
                            'border: solid 10px yellow',
                            'background-color: cyan'
                        ],
                    }
                },
            })

            const vm14 = app14.mount('#app-14')
        </script>


Bindeo de estilos ``:style`` - ``object``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Aplica todas las clases (el nombre de la key) que estén a true.

.. code:: html

    <div id="app-15">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app15 = Vue.createApp({})

        app15.component('my-component-name', {
            template: `<h4 :style="styles"> Hola PyCun </h4>`,
            data: function () {
                return {
                    styles: {
                        color: 'red',
                        border: 'solid 10px yellow',
                    },
                }
            },
        })

        const vm15 = app15.mount('#app-15')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-15">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app15 = Vue.createApp({})

            app15.component('my-component-name', {
                template: `<h4 :style="styles"> Hola PyCun </h4>`,
                data: function () {
                    return {
                        styles: {
                            color: 'red',
                            border: 'solid 10px yellow',
                        },
                    }
                },
            })

            const vm15 = app15.mount('#app-15')
        </script>


Directiva ``v-model``
=====================

Esta directiva permite crear un modelo de datos bidireccional. entre un elemento HTML concreto y una variable de Vue.
Es decir, **podemos sincronizar el contenido de una variable de Vue con el contenido que tenga un elemento HTML**.


Recordando ``v-bind``
~~~~~~~~~~~~~~~~~~~~~

.. code:: html

    <div id="app-16">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app16 = Vue.createApp({})

        app16.component('my-component-name', {
            template: `
                <input
                    id="input-app-16"
                    type="text"
                    v-bind:value="inputValue"
                />
                <p>{{ inputValue }}</p>
            `,
            data: function () {
                return {
                    inputValue: 'Hola PyCun',
                }
            },
        })

        const vm16 = app16.mount('#app-16')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-16">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app16 = Vue.createApp({})

            app16.component('my-component-name', {
                template: `
                    <input
                        id="input-app-16"
                        type="text"
                        v-bind:value="inputValue"
                    />
                    <p>{{ inputValue }}</p>
                `,
                data: function () {
                    return {
                        inputValue: 'Hola PyCun',
                    }
                },
            })

            const vm16 = app16.mount('#app-16')
        </script>


Recordando ``v-on``
~~~~~~~~~~~~~~~~~~~

.. code:: html

    <div id="app-17">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app17 = Vue.createApp({})

        app17.component('my-component-name', {
            template: `
                <input
                    id="input-app-17"
                    type="text"
                    v-on:input="(e) => inputValue = e.target.value"
                />
                <p>{{ inputValue }}</p>
            `,
            data: function () {
                return {
                    inputValue: 'Hola PyCun',
                }
            },
        })

        const vm17 = app17.mount('#app-17')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-17">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app17 = Vue.createApp({})

            app17.component('my-component-name', {
                template: `
                    <input
                        id="input-app-17"
                        type="text"
                        v-on:input="(e) => inputValue = e.target.value"
                    />
                    <p>{{ inputValue }}</p>
                `,
                data: function () {
                    return {
                        inputValue: 'Hola PyCun',
                    }
                },
            })

            const vm17 = app17.mount('#app-17')
        </script>



Bidireccional con ``v-bind`` y ``v-on``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: html

    <div id="app-18">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app18 = Vue.createApp({})

        app18.component('my-component-name', {
            template: `
                <input
                    id="input-app-18"
                    type="text"
                    :value="inputValue"
                    @input="(e) => inputValue = e.target.value"
                />
                <p>{{ inputValue }}</p>
            `,
            data: function () {
                return {
                    inputValue: 'Hola PyCun',
                }
            },
        })

        const vm18 = app18.mount('#app-18')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-18">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app18 = Vue.createApp({})

            app18.component('my-component-name', {
                template: `
                    <input
                        id="input-app-18"
                        type="text"
                        :value="inputValue"
                        @input="(e) => inputValue = e.target.value"
                    />
                    <p>{{ inputValue }}</p>
                `,
                data: function () {
                    return {
                        inputValue: 'Hola PyCun',
                    }
                },
            })

            const vm18 = app18.mount('#app-18')
        </script>

Bidireccional con ``v-model`` (opción altamente recomendada)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: html

    <div id="app-19">
        <my-component-name></my-component-name>
    </div>

    <script>
        const app19 = Vue.createApp({})

        app19.component('my-component-name', {
            template: `
                <input
                    id="input-app-19"
                    type="text"
                    v-model="inputValue"
                />
                <p>{{ inputValue }}</p>
            `,
            data: function () {
                return {
                    inputValue: 'Hola PyCun',
                }
            },
        })

        const vm19 = app19.mount('#app-19')
    </script>


.. admonition:: .
    :class: hint

    .. raw:: html

        <div id="app-19">
            <my-component-name></my-component-name>
        </div>

        <script>
            const app19 = Vue.createApp({})

            app19.component('my-component-name', {
                template: `
                    <input
                        id="input-app-19"
                        type="text"
                        v-model="inputValue"
                    />
                    <p>{{ inputValue }}</p>
                `,
                data: function () {
                    return {
                        inputValue: 'Hola PyCun',
                    }
                },
            })

            const vm19 = app19.mount('#app-19')
        </script>