def caracter_a_numero(cadena:str) -> list:
    cadena = cadena.lower()
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

def lista_binario(binario:int) -> int:
    binario = bin(binario)
    num = []
    for i in range(0,len(binario)):
        if binario[i] != "b":
            num.append(int(binario[i]))
    if len(num) == 7:
        num.pop(0)
    while len(num) < 6:
        num.insert(0, 0)
    
    return num

def lista_a_bin(binario:list) -> int:
    for i in range(0, len(binario)):
        binario[i] = str(binario[i])
    binario_int = "".join(binario)
    return int(binario_int)

def XOR(caracter:list, caracter_clave:list) -> list:
    xor = []
    for i in range (0, len(caracter)):
        if caracter[i] == caracter_clave[i]:
            xor.append(0)
        elif caracter[i] != caracter_clave[i]:
            xor.append(1)
    return xor

def binario_a_decimal(binario:int):
	decimal = 0
	for i in range(0,len(str(binario))):
		cifra = binario % 10
		decimal += cifra * (2**i)
		binario = binario // 10
	return decimal

def vernam () -> str:
    cadena, clave = parametros()
    cadena_vernam : list = []
    j = 0
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    for i in range(0, len(cadena)):
            ope = 0
            if cadena[i] not in puntuacion:
                bin_cadena = lista_binario(cadena[i])
                bin_clave = lista_binario(clave[j])
                ope = binario_a_decimal(lista_a_bin(XOR(bin_cadena,bin_clave)))
                if ope > 25:
                    ope-= 26
                cadena_vernam.append(ope)
                j += 1
            else:
                cadena_vernam.append(cadena[i])
            if j >= len(clave): 
                j = 0
    cadena_vernam = numero_a_caracter(cadena_vernam)
    cadena_vernam = "".join(cadena_vernam)
    print(cadena_vernam)

def parametros():
    cadena : str = str(input("Por favor, ingrese el texto a cifrar: "))
    cadena_conv = caracter_a_numero(cadena)
    clave : str = str(input("Ahora, por favor ingrese la clave bajo la cual se cifrara el texto (una sola cadena sin espacios)"))
    clave_conv = caracter_a_numero(clave)
    return cadena_conv, clave_conv

