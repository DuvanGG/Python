import time

print(time.strftime('%Y-%m-%d %H:%M'))
if time.strftime('%H:%M') >= "19:00":
    hora = time.strftime('%H:%M')
    print(f'Son las {hora} y es hora de ir a casa')
else:
    hora = 19 - int(time.strftime('%H'))
    minutos = 60 - int(time.strftime('%M'))
    print(f'quedan {hora} horas y {minutos} minutos de trabajo')