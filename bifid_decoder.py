def limpiar_cadena(string: str) -> str:
  string.replace("j", "i") 
  caracteres_no_deseados = '!#$%&()/=?¿*+~¨^>}<@|°¬,. ;:-_[]{"0123456789' # cadena de caracteres no deseados
  cadena_limpia = ''.join([char for char in string if char not in caracteres_no_deseados])
  return cadena_limpia

def crear_matriz(key):

    """
    Esta función crea una matriz de acuerdo a una clave para cifrar usando esta matriz

    Args:
        La función utiliza un string key como argumento 

    Returns:
        La función retorna una matriz con el abecedario reorganizado
    """

    key.lower()
    key=limpiar_cadena(key)
    Abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    matriz=[]

    for l in range(len(key)):
        letra=key[l]
        count=key.count(letra)
        if count!=0:
            for i in range(count):
                key=key.replace(letra, ".")
            key = key[:l] + letra + key[l+1:]
        if letra in Abecedario:
            Abecedario.remove(letra)
    key=key.replace(".", "")

    
    k=0
    for f in range(5):
        fila = [None] * 5
        matriz.append(fila)
    k = 0  
    for c in range(5):  
        for f in range(5):  
            if k < len(key):
                matriz[f][c] = key[k] 
                k += 1 
            else:
                if Abecedario:
                    matriz[f][c] = Abecedario[0]
                    Abecedario.pop(0)  
    return matriz

def descifrar_mensaje(msg, matriz):

    """
    Esta función descifra un mensaje dado de acuerdo a la matriz previamente creada

    Args:
        La función utiliza un string msg y una matriz como argumentos 

    Returns:
        La función retorna un string con el mensaje descifrado como msg_dec
    """

    coord=[]
    for letra in msg:
        if letra.isalpha():
            for f in range(5):
                for c in range(5):
                    if matriz[f][c]==letra:
                        coord.append(f)
                        coord.append(c)
    print(coord)
    c_it=int((len(coord))/2)
    x=coord[:c_it]
    y=coord[c_it:]
    dec=""
    for c in range(len(x)):
        ca=x[c]
        cb=y[c]
        dec=dec+matriz[ca][cb]
    return dec

def bifid_dec():

    """
    Esta función es la función principal para descifrar a través del cifrado bifid

    La función recibe entrada del usuario e inprime el mensaje cifrado
    """

    dec=input("Mensaje a descifrar: ")
    key=input("Ingrese su clave: ")
    matriz=crear_matriz(key)
    msg_dec=descifrar_mensaje(dec, matriz)
    print(f"mensaje descifrado {msg_dec}")