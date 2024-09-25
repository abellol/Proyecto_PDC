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

def determinante_2_cif (matriz_2 : list) -> int:
    return mod((matriz_2[0][0]* matriz_2[1][1]) - (matriz_2[1][0]*matriz_2[0][1]),26)

def determinante_3_cif (matriz_cuad:list) -> int:
    # diagonales LR
    LR = (matriz_cuad[0][0]*matriz_cuad[1][1]*matriz_cuad[2][2]) + (matriz_cuad[1][0]*matriz_cuad[2][1]*matriz_cuad[0][2]) + (matriz_cuad[0][1]*matriz_cuad[1][2]*matriz_cuad[2][0])
    # diagonales RL
    RL = (matriz_cuad[0][2]*matriz_cuad[1][1]*matriz_cuad[2][0]) + (matriz_cuad[0][1]*matriz_cuad[1][0]*matriz_cuad[2][2]) + (matriz_cuad[0][0]*matriz_cuad[1][2]*matriz_cuad[2][1])
    return mod(LR-RL,26)

def cofact_recur_cif (matriz:list) -> int:
    deter = 0
    new_mat = []
    fila = []
    dato = [0,0]
    while dato[1] < len(matriz[0]):
        for i in range(0,len(matriz)):
            for j in range(0,len(matriz[0])):
                if i != dato[0] and j != dato[1]:
                    fila.append(matriz[i][j])
            if len(fila) != 0:
                new_mat.append(fila)
            fila = []
            if type(new_mat) == list and len(new_mat) > 3:
                mini_det = cofact_recur(new_mat)
            if type(new_mat) == list and len(new_mat) == 3:
                mini_det = determinante_3(new_mat)
        if dato[1] % 2 == 0:
            deter += matriz[dato[0]][dato[1]] * (mini_det)
        if dato[1] % 2 != 0:
            deter -= matriz[dato[0]][dato[1]] * (mini_det)
        new_mat = []
        dato[1] += 1
    return mod(deter,26)

def rellenar_mat (dim: int, texto: list):
    mat = []
    fila = []
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    for i in range (0,len(texto)):
        if texto[i] not in puntuacion:
            fila.append(texto[i])
            if len(fila) == dim:
                mat.append(fila)
                fila = []
    if len(fila) < dim and len(fila) >= 1:
        while len(fila) < dim:
            fila.append(23)
        mat.append(fila)
    return mat

def rellenar_vec (dim: int, texto: list):
    list_vec = []
    mat = []
    fila = []
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    for i in range (0,len(texto)):
        if texto[i] not in puntuacion:
            fila.append(texto[i])
            mat.append(fila)
            fila = []
        if len(mat) == dim:
            list_vec.append(mat)
            mat = []
    if len(mat) < dim and len(mat) >= 1:
        while len(mat) < dim:
            fila.append(23)
            mat.append(fila)
        list_vec.append(mat)
    return list_vec
    
def matriz_mult (matriz1 : list, matriz2 : list) -> list:       # establecer la funcion
    matriz_mult = []    # definir la matriz resultante de la operacion
    fila = []           # establecer fila para asignar los datos
    dato_ij = 0         # establecer el dato a asignar 

    for i in range (len(matriz1)):  # recorrer las filas de la primera matriz
        for j in range (len(matriz2[0])):   # recorrer las columnas de la segunda matriz
            for h in range (len(matriz2)):  # recorrer las filas de la segunda matriz
                dato_ij += (int(matriz1[i][h]) * int(matriz2[h][j]))    # se asigna un valor al dato a partir de la sumatoria de las multiplicaciones de las filas por las columnas
            fila.append(dato_ij)    # se agrega el dato a la fila
            dato_ij = 0     # se reestablece el valor del dato a 0 
        matriz_mult.append(fila)    # una vez llenada la fila con los datos, se agrega a la matriz de multiplicacion
        fila = []           # se reestablece el valor de la fila

    return matriz_mult  # retorno de la multiplicacion de matrices

def mod(dato: int, base : int):
    mod = ((dato / base)-(dato // base)) * base
    mod = round(mod)
    if mod < 0:
        mod += base
    return int(mod)

def mat_a_list (matriz:list) -> list:
    lista = []
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[0])):
            lista.append(matriz[i][j])
    return lista

def determinante_2 (matriz_2 : list) -> int:
    return (matriz_2[0][0]* matriz_2[1][1]) - (matriz_2[1][0]*matriz_2[0][1])

def determinante_3 (matriz_cuad:list) -> int:
    # diagonales LR
    LR = (matriz_cuad[0][0]*matriz_cuad[1][1]*matriz_cuad[2][2]) + (matriz_cuad[1][0]*matriz_cuad[2][1]*matriz_cuad[0][2]) + (matriz_cuad[0][1]*matriz_cuad[1][2]*matriz_cuad[2][0])
    # diagonales RL
    RL = (matriz_cuad[0][2]*matriz_cuad[1][1]*matriz_cuad[2][0]) + (matriz_cuad[0][1]*matriz_cuad[1][0]*matriz_cuad[2][2]) + (matriz_cuad[0][0]*matriz_cuad[1][2]*matriz_cuad[2][1])
    return LR-RL

def cofact_recur (matriz:list) -> int:
    deter = 0
    new_mat = []
    fila = []
    dato = [0,0]
    while dato[1] < len(matriz[0]):
        for i in range(0,len(matriz)):
            for j in range(0,len(matriz[0])):
                if i != dato[0] and j != dato[1]:
                    fila.append(matriz[i][j])
            if len(fila) != 0:
                new_mat.append(fila)
            fila = []
            if type(new_mat) == list and len(new_mat) > 3:
                mini_det = cofact_recur(new_mat)
            if type(new_mat) == list and len(new_mat) == 3:
                mini_det = determinante_3(new_mat)
        if dato[1] % 2 == 0:
            deter += matriz[dato[0]][dato[1]] * (mini_det)
        if dato[1] % 2 != 0:
            deter -= matriz[dato[0]][dato[1]] * (mini_det)
        new_mat = []
        dato[1] += 1
    return deter

def hill() -> str:
    clave_mat, cadena_vec, cadena_encript = parametros()
    puntuacion = [" ","¿","?","¡","!",",",".",";",":","-","_",'"',"#","$","%","&","/","(",")","=","/","*","-","+","°",">","<","@","~","`","^","'"]
    recorrido = 0
    for i in range (0, len(cadena_vec)):
        cadena_vec[i] = matriz_mult(clave_mat, cadena_vec[i])
    for i in range (0, len(cadena_vec)):
        for j in range (0,len(cadena_vec[0])):
            for h in range (0, len(cadena_vec[0][0])):
                if cadena_vec[i][j][h] > 25:
                    cadena_vec[i][j][h] = mod(cadena_vec[i][j][h],26)
    cadena_vec = mat_a_list(cadena_vec)
    cadena_vec = mat_a_list(cadena_vec)
    for i in range(0,len(cadena_encript)):
        if cadena_encript[i] not in puntuacion:
            cadena_encript[i] = cadena_vec[recorrido]
            recorrido += 1
    cadena_encript = numero_a_caracter(cadena_encript)
    cadena_encript = "".join(cadena_encript)
    print(cadena_encript)

def parametros():
    det = 0
    dim_mat : int = int(input("Por favor, seleccione el tamaño de la matriz cuadrada, este tiene que ser un numero entero \n Recuerde que la longitud de la clave a ingresar sera igual al cuadrado del dato: "))
    while det == 0 or det % 2 == 0 or det % 13 == 0:
        clave : str = str(input(f"Ingrese la clave alfabetica de {dim_mat**2} digitos: "))
        while len(clave) < dim_mat**2 or len(clave) > dim_mat**2:
            clave = str(input(f"La clave ingresada no cumple con la condicion de tener {dim_mat**2} digitos: "))
        clave_num = caracter_a_numero(clave)
        clave_mat = rellenar_mat(dim_mat, clave_num)
        if len(clave_mat) > 3:
            det = cofact_recur_cif(clave_mat)
        if len(clave_mat) == 3:
            det = determinante_3_cif(clave_mat)
        if len(clave_mat) == 2:
            det = determinante_2_cif(clave_mat)
        if det != 0 and det % 2 != 0 and det % 13 != 0:
            print(f"La clave '{clave}' ingresada es valida")
    cadena : str = str(input("Ingrese la cadena a encriptar: "))
    cadena_num = caracter_a_numero(cadena)
    cadena_mat = rellenar_vec(dim_mat, cadena_num)
    return clave_mat, cadena_mat, cadena_num
