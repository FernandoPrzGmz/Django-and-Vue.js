=======================
Conceptos fundamentales
=======================

Document Object Model - DOM
===========================

Es el árbol de nodos que generan los navegadores para entender nuestro código HTML.

.. image:: https://aprende-web.net/progra/objetos/arbol_dom.gif
    :alt: DOM (Document Object Model)


Virtual DOM
===========

Es una copia del DOM real en la memoria del navegador. Esta copia permite hacer cálculos pesados
sin afectar el rendimiento del verdadero DOM.

.. image:: https://sloboda-studio.com/wp-content/uploads/2018/04/2.png
    :alt: DOM y Virtual DOM


¿Por qué es lento realizar cambios en el DOM?
=============================================

Cada vez que modificamos un elemento dentro de él, todos sus hijos tengan que ser
pintados de nuevo (hayan o no cambiado).

Por lo tanto, cuantos más elementos queden por debajo de nuestro elemento modificado
en la estructura del DOM más elementos tendrán que ser vueltos a pintar en la interfaz
gráfica.

.. admonition:: Javascript y jquery
    :class: info

    Javascript ofrece algunas APIs como
    ``document.getElementByID`` o ``document.querySelector``
    para leer el contenido de nuestro documento HTML.
    Otras funciones como ``innerHTML`` o ``appendChild`` permiten cambiar el HTML.

    JQuery ofrece ofrece algunas APIs como
    ``$().html('...')``, ``$().append('...')``.




¿Comó se aprovecha el virtual DOM?
==================================

En Vue, cada pieza de la UI es un componente y cada uno posee un estado interno.

Este estado es observado por la libreria con el fin de detectar cambios, y cuando se presenta un cambio
en cualquiera de estos componentes se genera un nuevo Virtual DOM con el árbol resultante.

.. image:: https://miro.medium.com/max/700/1*wrh_lW6mpQHRsuGtw1FuqA.png
    :alt: Proceso del virtual DOM

Dado que este DOM es virtual, la interfaz gráfica aún no es actualizada, sino que se compara el DOM
real con este DOM virtual con el objetivo de:

- Calcular la forma más óptima de realizar las cambios (es decir, de renderear los menos cambios posibles).
- No enviar multiples cambios. Junta todos los cambios detectados para reducir el número de veces que la UI debe
  pintarse. Es decir, menor acceso al DOM.





