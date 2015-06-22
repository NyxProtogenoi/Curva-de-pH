BITÁCORA DEL PROGRAMA ph2.py
============================

#Objetivo 1:#
---------------
Que el programa me tome la cantidad de reactivos que le pongo y que me pida el nombre de los reactivos.
##Resuelto##
El usuario ingresa el número de reactivos, y en base a los condicionales, la computadora le

#Objetivo 2:#
---------------
Que el programa guarde los valores -los nombres de los reactivos- en variables diferentes.
##Resuelto##
Tuve que deshacerme del bucle **for** porque, después de meditar y de buscar respuestas en internet sin
encontrar una que satisfajera mis necesidades concretas, llegué a la conclución de que en realidad no
era necesario un loop porque se sabe que las reacciones químicas suelen estar comprendidas, comunmente,
de no más de cuatro o cinco reactivos, por lo que era más fácil emplear condiciones teniendo en cuenta
particularmente cada situación posible que intentar inventar una resolución de la nada misma.
###Bonus###
Falta concebir una manera en la que podamos emplear los condicionales **if** sin necesidad de repetir
variables mencionadas en etapas anteriores. ¿A qué me refiero? Que siento que es muy redundante que
si cant_reactivos == 3 entonces tenga que especificar en el código que el programa le pida al usuario
*reactivo-eins* y *reactivo-dois* cuando ya el condicional if cant_reactivos == 2 ya los pide. Lo que
quiero es que en el código, el condicional si son tres reactivos comprenda los procedimientos propios
del condicional de dos reactivos.
