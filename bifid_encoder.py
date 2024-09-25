def limpiar_cadena(string: str) -> str:
  string.replace("j", "i")
  string.replace("ñ", "n") 
  caracteres_no_deseados = '!#$%&()/=?¿*+~¨^>}<@|°¬,. ;:-_[]{"0123456789'
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

def cifrar_mensaje(msg,matriz):

    """
    Esta función cifra un mensaje dado de acuerdo a la matriz previamente creada
    Args:
        La función utiliza un string msg y una matriz como argumentos 

    Returns:
        La función retorna un string con el mensaje cifrado como msg_enc
    """

    x=[]
    y=[]
    for letra in msg:
        if letra.isalpha():
            for f in range(5):
                for c in range(5):
                    if matriz[f][c]==letra:
                        x.append(f)
                        y.append(c)
    cifrado=[]
    cifrado.extend(x)
    cifrado.extend(y)
    msg_enc=""
    for i in range(0,len(cifrado),2):
        ca=cifrado[i]
        cb=cifrado[i+1]
        msg_enc=msg_enc+matriz[ca][cb]
    return msg_enc


def bifid_enc():

    """
    Esta función es la función principal para cifrar a través del cifrado bifid

    La función recibe entrada del usuario e inprime el mensaje cifrado
    """

    msg=input("Escriba su mensaje: ")
    key=input("Ingrese su clave: ")
    matriz=crear_matriz(key)
    msg_enc=cifrar_mensaje(msg, matriz)
    print(f"Mensaje cifrado: {msg_enc}")