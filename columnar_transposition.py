def limpiar_cadena(string: str) -> str:
  caracteres_no_deseados = '!#$%&()/=?¿*+~¨^>}<@|°¬,. ;:-_[]{"0123456789' # cadena de caracteres no deseados
  cadena_limpia = ''.join([char for char in string if char not in caracteres_no_deseados])
  return cadena_limpia

def ingresar_parametros():
  clave = str(input("Ingrese la clave bajo la que desea cifrar: "))
  mensaje = str(input("Ingrese el mensaje que desea cifrar: "))
  mensaje = mensaje.lower()
  return clave, mensaje

def columnar():
  clave, mensaje = ingresar_parametros()
  clave = limpiar_cadena(clave)
  mensaje = limpiar_cadena(mensaje)
  while len(mensaje) % len(clave) != 0: mensaje += "x"
  matriz : list = []
  for i in range(len(clave)):
    filas = []
    filas.append(clave[i])
    matriz.append(filas)

  indice = 0
  for i in range(len(mensaje) // len(clave)):  
    for j in range(len(clave)):
      if indice < len(mensaje):
        matriz[j].append(mensaje[indice])
        indice += 1
  matriz = sorted(matriz)
  
  mensaje_encriptado = ""
  for fila in matriz:
    for i in range(1, len(matriz[0])):
      mensaje_encriptado += str(fila[i])
  print(mensaje_encriptado)
  return mensaje_encriptado




