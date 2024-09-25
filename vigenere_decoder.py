def caracter_a_numero(cadena:str) -> list:
    cadena.lower()
    cadena_conv = []
    puntuacion_dic = {39: "'",32:" ",191:"¿",63:"?",161:"¡",33:"!",44:",",46:".",59:";",58:":",45:"-",95:"_",34:'"',35:"#",36:"$",37:"%",38:"&",47:"/",40:"(",41:")",61:"=",47:"/",42:"*",45:"-",43:"+",176:"°",62:">",60:"<",64:"@",126:"~",96:"`",94:"^"}
    for i in range (0,len(cadena)):
        if ord(cadena[i]) not in puntuacion_dic:
            cambio = ord(cadena[i])-97
            match cambio:
                case 144:
                    cambio = 13
                case 128:
                    cambio = 0
                case 136:
                    cambio = 4
                case 140:
                    cambio = 8
                case 146:
                    cambio = 14
                case 153:
                    cambio = 20
                case 156:
                    cambio = 24
                case 134:
                    cambio = 2
            cadena_conv.append(cambio)
        else: 
            cadena_conv.append(puntuacion_dic[ord(cadena[i])])
    return cadena_conv

def numero_a_caracter(cadena:list) -> list:
    longitud = len(cadena)
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    for i in range (0,longitud):
        if cadena[i] not in puntuacion:
            cadena.append(chr(cadena[i]+97))
        else:
            cadena.append(cadena[i])
    for i in range (0, longitud):
        cadena.pop(0)
    return cadena

def des_vigenere () -> str:
    cadena, clave = parametros()
    cadena_vigenere : list = []
    j = 0
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    for i in range(0, len(cadena)):
            ope = 0
            if cadena[i] not in puntuacion:
                ope = cadena[i] - clave[j]
                if ope < 0:
                    ope+= 26
                cadena_vigenere.append(ope)
                j += 1
            else:
                cadena_vigenere.append(cadena[i])
            if j >= len(clave): 
                j = 0
    cadena_vigenere = numero_a_caracter(cadena_vigenere)
    cadena_vigenere = "".join(cadena_vigenere)
    print(cadena_vigenere)

def parametros():
    cadena : str = str(input("Por favor, ingrese el texto a descifrar: "))
    cadena_conv = caracter_a_numero(cadena)
    clave : str = str(input("Ahora, por favor ingrese la clave bajo la cual se descifrara el texto (una sola cadena sin espacios)"))
    clave_conv = caracter_a_numero(clave)
    return cadena_conv,clave_conv
