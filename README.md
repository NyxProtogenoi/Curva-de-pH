BITÁCORA DEL PROGRAMA ph2.py
============================

##Objetivo 1:##
---------------
Que el programa me tome la cantidad de reactivos que le pongo y que me pida el nombre de los reactivos.
#Resuelto#
Empecé con **una variable** y el bucle **for**, pero me dí cuenta de que me faltaba especificar algo,
porque el loop sólamente itera lo que sea string, así que no podía utilizar *input* para que el
usuario ingresara los datos -porque el número de reactivos es un entero, justamente un número-:
sí o sí tenía que poner **raw_input**.
Entendí que el bucle *for* te itera por la cantidad de caracteres que tenés dentro de la variable,
ya que si yo, al probar el programa, ponía *cant_react = 2*, este me iba a pedir un sólo nombre de
reactivo; y si ponía *cant_reactivos = 22*, me iba a pedir dos; cuando lo que yo necesitaba era, en el
primer caso, que me pida dos nombres y, en el segundo, veintidos.
La forma en que respondí a ese problema fue con la variable **a_iterar**. Esta variable toma el ahora valor
entero de la variable *cant_reactivos* y **multiplica** a un literal cualquiera que yo asigné para el proposito,
haciendo que la variable a_iterar guardara un valor equivalente a *x* veces el literal, x siendo
determinada por el valor de cant_reactivos.
A su vez, como mencioné, el bucle *for* sólo puede iterar *strings*, así que **volví al valor de la variable**
**a_iterar una string**; y así solucioné el problema: al ejecutar el programa, pongo cualquier valor, y me
pide la misma cantidad de reactivos.

##Objetivo 2:##
---------------
Que el programa guarde los valores -los nombres de los reactivos- en variables diferentes.
#Sin resolver#
El primer problema es la forma de accionar del iterado del bucle. Está bien, hace lo que le pido:
toma la cantidad de reactivos que le pongo y me pide los nombres de éstos, pero el tema es que guarda,
por cómo lo compuse, todos los nombres en la misma variable (**reactivos**), por lo que, al final,
sigo trabajando con una sola variable y necesito poder trabajar con la cantidad de variables igual
a la cantidad de reactivos que estipulé al principio.
