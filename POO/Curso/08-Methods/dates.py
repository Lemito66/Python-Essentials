from ast import If
from datetime import datetime, date, time, timedelta, timezone
import calendar
fecha_ahora = datetime.now()

# print(f'{fecha_ahora.hour}:{fecha_ahora.minute}:{fecha_ahora.second}')

# hora_minuto_segundo_ahora = f'{fecha_ahora.hour}:{fecha_ahora.minute}:{fecha_ahora.second}'

# print(hora_minuto_segundo_ahora)

# print(type(hora_minuto_segundo_ahora))

# print(type(fecha_ahora.hour))

""" fechita = datetime.now()
print(f'{fechita.hour}')
autenticado = True

#hora = int(input('Ingresa tu hora \n'))

if 17 <= fechita.hour <= 22 and autenticado:
  print(f'Paso')
elif autenticado and 6 <= fechita.hour <= :
  print(f'Falta fuera de rango') """
""" elif 23 <= hora <= 16:
  print(f'No esta en el rango') """
  

hora_actual = datetime.now()
hora_inicio = time(17, 0,0)
hora_cierre = time(22,0,0)

autenticado = True

print(hora_actual)

nueva_hora_actual = datetime.strftime(hora_actual, '%H:%M:%S')



print(type(nueva_hora_actual))
print(type(hora_inicio))
print(type(hora_cierre))

# if autenticado:
#   if hora_inicio ==





# print(f'{hora_inicio} otra {hora_cierre}')

# print(datetime.now())

# hora_actual = datetime.now()

# print(f'{hora_actual.hour}:{hora_actual.minute}')

      