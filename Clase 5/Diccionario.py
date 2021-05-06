jugador = {
    'nombre': 'Ruben',
    'apellido': 'Paz',
    'equipo hincha' : ['Racing','Peñarol']
}

print(jugador['nombre'])
print(jugador)

jugador['goles']=150

print(jugador)

otro_clubes = {
    'clubes' : ['Racing','Peñarol','Internacional','Racing Paris','Genoa']
}

jugador.update(otro_clubes)
print(jugador)
