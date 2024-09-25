def limpiar_cadena(string: str) -> str:
    caracteres_no_deseados = '!#$%&()/=?¿*+~¨^>}<@|°¬,. ;:-_[]{"0123456789'
    cadena_limpia = ''.join([char for char in string if char not in caracteres_no_deseados])
    return cadena_limpia

def ingresar_parametros():
  mensaje = str(input("Ingrese el mensaje que desea descifrar: "))
  disco_interior = str(input("Ingrese el disco interior usado anteriormente: "))
  desfase_inicial = int(input("Ingrese el desfase inicial: "))
  incremento = int(input("Ingrese el incremento: "))
  periodo_incremento = int(input("Ingrese periodo: "))
  return mensaje, disco_interior, desfase_inicial, incremento, periodo_incremento

def des_rueda_alberti(disco_exterior="abcdefghijklmnopqrstuvwxyz"):
    mensaje_encriptado, disco_interior, desfase_inicial, incremento, periodo_incremento = ingresar_parametros()

    mensaje_encriptado = limpiar_cadena(mensaje_encriptado).lower()
    disco_interior = [letter for letter in disco_interior]
    disco_exterior = [letter.upper() for letter in disco_exterior]
    indices = []
    contador_periodo = 0
    incremento_actual = desfase_inicial

    for i in range(len(mensaje_encriptado)):
      if mensaje_encriptado[i] not in disco_interior:
        return "ERROR"

        # Calcular el nuevo índice
      nuevo_indice = (disco_interior.index(mensaje_encriptado[i]) - incremento_actual) % len(disco_interior)
      indices.append(nuevo_indice)
        
        # Manejo de contador de periodo
      contador_periodo += 1
        
      if contador_periodo == periodo_incremento:
        incremento_actual += incremento  # Aumentar el incremento después de un periodo
        contador_periodo = 0  # Reiniciar contador después de un periodo

    # Crear el mensaje_encriptado encriptado utilizando disco exterior
    mensaje_desencriptado = ""
    for indice in indices:
      mensaje_desencriptado += str(disco_interior[indice])
    print(mensaje_desencriptado.upper())

    return mensaje_desencriptado.upper()


    
