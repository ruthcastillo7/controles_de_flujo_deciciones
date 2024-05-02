# Control de flujo
Nos permitee evaluar si una o mas condiciones se cumplen, para decir que accion vamos a ejecutar. Solo tendremos resultado verdadero o falso.
# ejemplo
1. `ciclos`: 
`For:` cuando se sabe cuando term,ina un bucle, ejem: es 1 a 10
`while:` no se sabe cuando termina el bucle; ejem: hasta que el usuario ingrese 10
2. `deciciones`: tenemos a 
`if`: ejecuta el codigo si cumple una funcion o condicion (es un flujo normal, va sucesuvamente)
`else`: caso contrario, debe estar a la altura de if, si no esta a la altura habra error.
`elif`: anida los if, o sea evalua mas condiciones
>ejemplo
``` python
if imc<=18.5:
    print("....")
elif imc<=25.0:
    print("estas....")
elif imc<=30.1:
    print("estas muy....")
else:
    print("......")