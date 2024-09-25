def limpiar_cadena(string: str) -> str:
  caracteres_no_deseados = '!#$%&()/=?¿*+~¨^>}<@|°¬,. ;:-_[]{"0123456789' # cadena de caracteres no deseados
  cadena_limpia = ''.join([char for char in string if char not in caracteres_no_deseados])
  return cadena_limpia

def ingresar_parametros():
  clave = str(input("Ingrese la clave bajo la que desea descifrar: "))
  mensaje = str(input("Ingrese el mensaje que desea descifrar: "))
  return clave, mensaje

def desencriptar_columnar():
  clave, mensaje_encriptado = ingresar_parametros()
  clave = limpiar_cadena(clave)
  mensaje_encriptado = limpiar_cadena(mensaje_encriptado)
  num_columnas = len(clave)
  num_filas = len(mensaje_encriptado) // num_columnas
  # Crear la matriz vacía
  matriz = []
  for i in range(num_columnas):
    matriz.append([])
  # Ordenar la clave y obtener el orden original de las columnas
  clave_ordenada = []
  for i in range(len(clave)):
    clave_ordenada.append((clave[i], i))
  clave_ordenada.sort()
  orden_original = []
  for par in clave_ordenada:
    orden_original.append(par[1])
  # Llenar la matriz con el mensaje encriptado
  indice = 0
  for i in range(num_columnas):
    for j in range(num_filas):
      matriz[orden_original[i]].append(mensaje_encriptado[indice])
      indice += 1
  # Reconstruir el mensaje desencriptado
  mensaje_desencriptado = ""
  for fila in range(num_filas):
    for columna in range(num_columnas):
      mensaje_desencriptado += matriz[columna][fila]
      
  print(mensaje_desencriptado)
  return mensaje_desencriptado





