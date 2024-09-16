# Proyecto_PDC
Desarrollo del proyecto sobre encriptación de mensajes. Este proyecto está orientado a la seguridad de envio de mensajes a travpes de cifrados de transposición, logicos y/o polialfabeticos a través de algoritmos de Python



## Diagrama General

```mermaid
flowchart TD;
    a([inicio]) --> b[Ingrese el cifrado que desea usar]
    b -->c
    c-- no ---d
    c-- si ---C
    d -- no --- e
    d -- si --- D
    e -- no --- f
    e -- si --- E
    f -- no --- g
    f -- si --- F
    g -- no --- h
    g -- si --- G
    h -- no --- i
    h -- si --- H
    i -- no --- j
    i -- si --- I
    j -- no --- k
    j -- si --- J
    k -- no --- z([FIN])
    k -- si --- K

    c{Playfair?}
    d{Columnar transposition?}
    e{Albertis wheel?}
    f{Hill?}
    g{Vernam?}
    h{Vigenere?}
    i{XOR?}
    j{Bifid?}
    k{Porta?}
    C[[Playfair]]
    D[[Columnar transposition]]
    E[[Albertis wheel]]
    F[[Hill]]
    G[[Vernam]]
    H[[Vigenere]]
    I[[XOR]]
    J[[Bifid]]
    K[[Porta]]
```
## Cifrado Hill
Cifrado basado en operación modular, equivalencias de letras a números y operaciones de matrices

```mermaid
flowchart TD
    A([CIFRADO HILL])
    B[/Ingreso de dimension para la matriz cuadrada/]
    C[/ingreso de clave como cadena de caracteres/]
    G{¿la longitud de la cadena es igual a la cantidad de datos para la matriz?}
    H[Si]
    I[No]
    D[relleno de matriz a partir de valor numerico de cada caracter] 
    subgraph caracteres_a_numeros
    direction LR
    E["`Aa
    Bb
    Cc
    ...
    Zz
    H o l a`"]
    F["`0
    1
    2
    ...
    25
    7 14 11 0`"]
    E --> F
    end

    subgraph validez_de_matriz
    O[se obtiene el determinante de la matriz]
    P{¿el determinante es diferente de 0?}
    Q[Si]
    R[No]
    S[La matriz tiene inversa]
    O --> P
    P --> Q
    P --> R
    Q --> S
    end
    

    J[/Ingreso de cadena a encriptar/]
    K[Paso de caracter a valor numerico]
    L[Creacion de bloques de vectores a partir de la dimension de la matriz clave]
    subgraph bloques_de_vectores
    direction TB
    M[cadena: 'sabor']
    N["`v1  v2  v3
    (s)   (b)   (r)
    (a)   (o)   (x)
    vectores de dimension 2x1`"]
    M -- siendo la dinension de la matriz 2x2 --> N
    end
    T[multiplicar matriz clave por vector]
    U[aplicar operacion modular con modulo 26 a cada elemento del vector]
    V[/se obtiene nuevo vector /]
    W[paso de valor numerico a caracter]
    X{¿hay vectores restantes?}
    Y[Si]
    Z[No]
    AA[/cadena codificada/]
    AB([fin])
    AC[siguiente vector]

    A --> B
    B --> C
    C --> G
    C <--> R
    G --> H
    G --> I
    I --> C
    H --> caracteres_a_numeros
    caracteres_a_numeros --> D
    D --> validez_de_matriz
    S --> J
    J --> K
    K --> L
    L --> bloques_de_vectores
    bloques_de_vectores --> T
    T --> U
    U --> V
    V --> W
    W --> X
    X --> Y
    X --> Z
    Y --> AA
    AA --> AB
    Z --> AC
    AC --> T
```

Para el caso del desencriptado, se aplica inversa de matrices como paso adicional

```mermaid
flowchart TD
    A([DESCIFRADO HILL])
    B[/Ingreso de dimension para la matriz cuadrada/]
    C[/ingreso de clave de desencriptado como cadena de caracteres/]
    D[relleno de matriz a partir de valor numerico de cada caracter] 
    subgraph caracteres_a_numeros
    direction LR
    E["`Aa
    Bb
    Cc
    ...
    Zz
    H o l a`"]
    F["`0
    1
    2
    ...
    25
    7 14 11 0`"]
    E --> F
    end
    
    G[Se obtiene la inversa de la matriz clave]
    J[/Ingreso de cadena a encriptar/]
    K[Paso de caracter a valor numerico]
    L[Creacion de bloques de vectores a partir de la dimension de la matriz clave]
    subgraph bloques_de_vectores
    direction TB
    M[cadena: 'sabor']
    N["`v1  v2  v3
    (s)   (b)   (r)
    (a)   (o)   (x)
    vectores de dimension 2x1`"]
    M -- siendo la dinension de la matriz 2x2 --> N
    end
    T[multiplicar inversa de matriz clave por vector]
    U[aplicar operacion modular con modulo 26 a cada elemento del vector]
    V[/se obtiene nuevo vector /]
    W[paso de valor numerico a caracter]
    X{¿hay vectores restantes?}
    Y[Si]
    Z[No]
    AA[/cadena codificada/]
    AB([fin])
    AC[siguiente vector]

    A --> B
    B --> C
    C --> caracteres_a_numeros
    caracteres_a_numeros --> D
    D --> G
    G --> J
    J --> K
    K --> L
    L --> bloques_de_vectores
    bloques_de_vectores --> T
    T --> U
    U --> V
    V --> W
    W --> X
    X --> Y
    X --> Z
    Y --> AA
    AA --> AB
    Z --> AC
    AC --> T
```
## Cifrado Playfair
Este cifrado es de sustitución poligráfica, cifrando pares de letras en una matriz de 5x5 basada en una palabra clave

```mermaid
flowchart TD;
    a([Cifrado de Playfair]) --> b[/Ingresar la clave/]
    b --> c{¿Tiene letras repetidas?}
    c -- si ---da[Remover despues de la primera aparición]
    da --> c
    c -- no ---db[Generar una matriz 5x5]
    db --> e[Ingresar a la matriz las letras de la clave desde la primera fila ]
    e --> f[Ingresar a la matriz el resto del ABC en orden]
    f --> g[/Ingresar el mensaje a encriptar/]
    g --> h[Remover espacios]
    h --> i[Contar cantidad de caracteres]
    i --> j{¿La cantidad de letras es par?}
    j -- no ---ka[Agregar x al final del mensaje]-->j
    j -- si ---kb[Separar en parejas de letras el mensaje]
    kb --> l{¿Está el mismo elemento en una pareja?}
    l -- si ---ma[Reemplazar el ultimo por una x] --> l
    l -- no ---mb{¿Los elementos de la pareja están en la misma fila?}
    mb -- si --- na[Desplazar cada letra a la derecha en la matriz] --> x[Almacenar la nueva pareja de letras]
    mb -- no --- nb{¿Los elementos de la pareja están en la misma columna?}
    nb -- si --- oa[Desplazar cada elemento hacía abajo en la matriz] --> x
    nb -- no --- ob[Tomar los extremos en la fila del rectangulo formado por las letras] --> x
    x --> q[Unir las nuevas parejas en orden] --> p[/Retornar el mensaje encriptado/]-->z([fin])
```
Por otro lado, su proceso de desencriptación es simplemente aplicar el mismo proceso pero deshaciendo los deplazamientos de los indices de las letras dentro de la matriz.
```mermaid
flowchart TD;
    a([Descifrado de Playfair]) --> b[/Ingresar la clave/]
    b --> c{¿Tiene letras repetidas?}
    c -- si ---da[Remover despues de la primera aparición]
    da --> c
    c -- no ---db[Generar una matriz 5x5]
    db --> e[Ingresar a la matriz las letras de la clave desde la primera fila]
    e --> f[Ingresar a la matriz el resto del ABC en orden]
    f --> g[/Ingresar el mensaje a desencriptar/]
    g --> i["Contar cantidad de caracteres(x)"]
    i --> j[i = 0]
    j --> j2[j = 0]
    j2 --> k{¿i == x?}
    q[Almacenar nuevo par de letras]
    k --si --- ka[Unir las nuevas parejas]-->y[/Retornar mensaje descifrado/]-->z([FIN])
    k --no --- kb[Buscar la letra del indice i] -->kc[Buscar la letra del indice j]
    kc --> l{¿Están en la misma fila?}
    l -- si --- la[Desplazar una posición hacía la izquierda cada letra]-->q--> p[i=i+1 , j=j+1]-->k
    l -- no --- lb{¿Están en la misma columna?}
    lb -- si --- n[Desplazar una posición hacía arriba cada letra] -->q
    lb -- no --- o[Tomar los extremos en la fila del rectangulo formado por las letras]-->q

```
## Cifrado vernam
Cifrado que se apoya en la operación XOR y equivalencias de letras a números, y que ademas, no posee un proceso para el desencriptado, puesto que mientras se tenga la msima clave de encriptado, se devolvera el mensaje original

```mermaid
flowchart TD
    A([CIFRADO VERNAM])
    subgraph caracteres_a_numeros
    direction LR
    E["`Aa
    Bb
    Cc
    ...
    Zz
    H o l a
    U n o `"]
    F["`0
    1
    2
    ...
    25
    7 14 11 0
    20 13 14`"]
    E --> F
    end
    subgraph relleno_de_cadena
    H["` cadena: Hola mundo
    clave: uno`"]
    I["`H o l a   m u n d o
    u n o u   n o u n o`"]
    H --> I
    end
    B[/ingreso de la cadena a encriptar/]
    C[/ingreso de clave para la cadena/]
    D[repetir la clave hasta completar la longitud de la cadena]
    G[paso de caracteres a numeros]
    J[Operacion XOR sobre los binarios de cada caracter]
    subgraph XOR
    K["` 7 = 0 0 1 1 1
    20 = 1 0 1 0 0`"]
    L[1 0 0 1 1 = 19]
    K --> L
    end
    M["`Paso del valor numerico a caracter
    19 = t`"]
    U{¿El valor recibido es mayor a 26?}
    V[Si]
    W[No]
    X[restar 26 al valor recibido]
    N[se agrega el caracter codificado a una nueva cadena]
    O{¿ya se codificaron todos los caracteres?}
    P[Si]
    Q[No]
    R[/cadena codificada/]
    S(siguiente caracter)
    T([fin])

    A --> B
    B --> C
    C --> D
    D --> relleno_de_cadena
    relleno_de_cadena --> G
    G --> caracteres_a_numeros
    caracteres_a_numeros --> J
    J --> XOR
    XOR --> M
    M --> U
    U --> V
    U --> W
    V --> X
    X --> N
    W --> N
    N --> O
    O --> P
    O --> Q
    Q --> S
    S --> J
    P --> R
    R --> T
```
## Cifrado Alberti´s wheel
Es uno de los primeros cifrados polialfabeticos, consiste en dos discos (uno contenido en el otro) que poseen un conjunto de letras; la mayoría de veces es el alfabeto y algunos numeros. Para cifrar el mensaje se debe mover el disco interno según una serie de instrucciones dadas por el emisor.
Para el cifrado se tomaron ambos "discos" como cadenas de texto que van cambiando sus indices según los requisitos del usuario.
```mermaid
flowchart TD;
    a([Cifrado Alberti´s wheel]) --> b[/Ingresar el mensaje/]
    b --> c[Eliminar espacios] -->x["contar caracteres(u)"] -->d[/"Ingresar el desfase inicial (x)"/]
    d --> e[/"Ingresar el incremento (y)"/]
    e --> f[/"Ingresar el periodo de incremento (z)"/]
    f --> m[/"Ingresar el disco pequeño"/]
    m --> n[contador periodo =  0]
    n --> h[i = 0]
    h --> i{"¿i == (u-1)?"}
    w[Obtener cada caracter de los indices almacenados]
    v[Unir los caracteres en el mismo orden]
    i -- no --- ja[Obtener letra del string en ese indice]
    i -- si --- w --> v-->y[/Retornar el mensaje encriptado/] -->z
    ja --> k{¿Letra en rueda pequeña?}
    k-- si ---la[Obtener indice] 
    k-- no ---lb[ERROR] -->z([FIN])
    la --> ñ[Indice - x]--> o{"¿Contador periodo == (z-1)?"}
    o -- si --- pb[y = 2y] --> pc[Almacenar indice - y] --> pe[contador periodo = 0] --> i
    o -- no --- pa[Almacenar indice - y] -->pd[contador periodo + 1] -->i
```
El descifrado sigue la misma lógica, la única condición es que hay que saber todas las instrucciones y el contenido del "disco pequeño". 
```mermaid
flowchart TD;
    a([Descifrado Alberti´s wheel]) --> b[/Ingresar el mensaje encriptado/]
    b --> c["contar caracteres(u)"] -->d[/"Ingresar el desfase inicial (x)"/]
    d --> e[/"Ingresar el incremento (y)"/]
    e --> f[/"Ingresar el periodo de incremento (z)"/]
    f --> g[/"Ingresar el disco pequeño"/]   
    g --> h[contador periodo =  0]
    h --> i[i = 0]
    i --> j{"¿i == (u-1)?"}
    w[Obtener cada caracter de los indices almacenados]
    v[Unir los caracteres en el mismo orden]
    j -- no --- ja[Obtener letra del string en ese indice]
    j -- si --- w --> v-->y[/Retornar el mensaje desencriptado/] -->z
    ja --> k{¿Letra en rueda pequeña?}
    k-- si ---la[Obtener indice] 
    k-- no ---lb[ERROR] -->z([FIN])
    la --> x[Indice - x] -->o{"¿Contador periodo == (z-1)?"}
    o -- si --- pb[y = 2y] --> pc[Almacenar indice + y] --> pe[contador periodo = 0] --> i
    o -- no --- pa[Almacenar indice + y] -->pd[contador periodo + 1] -->i
```

## Cifrado Vigenere
El primer cifrado polialfabetico 

```mermaid
flowchart TD
    A([CIFRADO VIGENERE])
    subgraph caracteres_a_numeros
    direction LR
    E["`Aa
    Bb
    Cc
    ...
    Zz
    H o l a
    U n o `"]
    F["`0
    1
    2
    ...
    25
    7 14 11 0
    20 13 14`"]
    E --> F
    end

    subgraph relleno_de_cadena
    H["` cadena: Hola mundo
    clave: uno`"]
    I["`H o l a   m u n d o
    u n o u   n o u n o`"]
    H --> I
    end
    
    B[/ingreso de la cadena a encriptar/]
    C[/ingreso de clave para la cadena/]
    D[repetir la clave hasta completar la longitud de la cadena]
    G[paso de caracteres a numeros]
    J["`para cada caracter se suma el valor numerico del caracter de la clave asignado
    cadena d = 3
    clave o = 14
    cifrado 3 + 14 = 17`"]
    M["`Paso del valor numerico a caracter
    17 = r`"]
    U{¿El valor recibido es mayor a 26?}
    V[Si]
    W[No]
    X[restar 26 al valor recibido]
    N[se agrega el caracter codificado a una nueva cadena]
    O{¿ya se codificaron todos los caracteres?}
    P[Si]
    Q[No]
    R[/cadena codificada/]
    S(siguiente caracter)
    T([fin])

    A --> B
    B --> C
    C --> D
    D --> relleno_de_cadena
    relleno_de_cadena --> G
    G --> caracteres_a_numeros
    caracteres_a_numeros --> J
    J --> M
    M --> U
    U --> V
    U --> W
    V --> X
    X --> N
    W --> N
    N --> O
    O --> P
    O --> Q
    Q --> S
    S --> J
    P --> R
    R --> T
```

El descifrado se logra realizando el proceso inverso, suma a resta, y el limitante de 26 pasa a ser de 0

```mermaid
flowchart TD
    A([DESCIFRADO VIGENERE])
    subgraph caracteres_a_numeros
    direction LR
    E["`Aa
    Bb
    Cc
    ...
    Zz
    H o l a
    U n o `"]
    F["`0
    1
    2
    ...
    25
    7 14 11 0
    20 13 14`"]
    E --> F
    end

    subgraph relleno_de_cadena
    H["` cadena: Hola mundo
    clave: uno`"]
    I["`H o l a   m u n d o
    u n o u   n o u n o`"]
    H --> I
    end
    
    B[/ingreso de la cadena a desencriptar/]
    C[/ingreso de clave para la cadena/]
    D[repetir la clave hasta completar la longitud de la cadena]
    G[paso de caracteres a numeros]
    J["`para cada caracter se resta el valor numerico del caracter de la clave asignado
    cadena r = 17
    clave o = 14
    cifrado 17 - 14 = 3`"]
    M["`Paso del valor numerico a caracter
    3 = d`"]
    U{¿El valor recibido es menor a 0?}
    V[Si]
    W[No]
    X[sumar 26 al valor recibido]
    N[se agrega el caracter codificado a una nueva cadena]
    O{¿ya se codificaron todos los caracteres?}
    P[Si]
    Q[No]
    R[/cadena codificada/]
    S(siguiente caracter)
    T([fin])

    A --> B
    B --> C
    C --> D
    D --> relleno_de_cadena
    relleno_de_cadena --> G
    G --> caracteres_a_numeros
    caracteres_a_numeros --> J
    J --> M
    M --> U
    U --> V
    U --> W
    V --> X
    X --> N
    W --> N
    N --> O
    O --> P
    O --> Q
    Q --> S
    S --> J
    P --> R
    R --> T
```
## Columnar Transposition
Este tipo de cifrado es de trasposición, donde las letras se reordenan según un esquema específico, en este caso es según el orden alfabético de la clave.
```mermaid
flowchart TD;
    a([Cifrado columnar transposition]) --> b[/Ingresar la clave/] --> c["Contar la cantidad de caracteres(x)"]
    c --> d[/Ingresar el mensaje a encriptar/] --> e[Remover espacios] --> f["Contar la cantidad de caracteres(y)"]
    f --> g[z = y / x]
    g -->h{¿x % z == 0?}
    h -- si --- ia["Crear una matriz (y+1)*x"] -->o
    h -- no --- ib[Agregar x al final del mensaje] -->f
    o[i = 0] --> p{"¿i==(x-1)?"}
    p -- si ---r
    p -- no ---q[Agregar la letra del indice i de la clave a la primera celda de la primera fila de la matriz] --> s[i += 1] -->p
    r[j = 0] --> j{"¿ j == (y-1)"}
    j -- no --- t[Agregar la letra del indice j del mensaje a la matriz] --> j
    j -- si ---u[Ordenar las columnas según el orden alfabético de la primera fila]-->m
    m[Unir las letras de cada columna] --> n[/Retornar el mensaje encriptado/]
    n --> z([Fin])
```
Su descifrado es simplemente revertir los pasos ya hechos, el único requisito es conocer la clave con la que fue cifrado el mensaje.
```mermaid
 flowchart TD;
    a([Descifrado Columnar transposition]) --> b[/Ingresar la clave/] --> c["Contar la cantidad de caracteres(x)"]
    c --> d[/Ingresar el mensaje encriptado/] --> f["Contar la cantidad de caracteres(y)"]
    e[Ordenar alfabeticamente la clave]
    f --> g[z = y / x]
    g -->h{¿x % z == 0?}
    h -- si --- ia["Crear una matriz (y+1)*x"] -->e -->o
    h -- no --- ib[Agregar x al final del mensaje] -->f
    o[i = 0] --> p{"¿i==(x-1)?"}
    p -- si ---r
    p -- no ---q[Agregar la letra del indice i de la clave a la primera celda de la primera fila de la matriz] --> s[i += 1] -->p
    r[j = 0] --> j{"¿ j == (y-1)"}
    j -- no --- t[Agregar la letra del indice j del mensaje de abajo hacia arriba en cada columna] --> j
    j -- si ---u[Ordenar las columnas en el orden de la clave original]-->m
    m[Unir las letras de cada fila] --> n[/Retornar el mensaje desencriptado/]
    n --> z([Fin])
```
## XOR

Este cifrado usa la logica XOR entre un mensaje y una clave para cifrar el mensaje

```mermaid
    flowchart TD
        A([Cifrar mensaje con cifrado XOR]) --> B
        B[/Imprimir "Escriba el mensaje para encriptar"/] -->C
        C[/Leer msg/]-->D
        D[/Imprimir "Ingrese la clave para encripción"/]-->E
        E[/Leer key/]-->F
        F[Convertir de msg a binario]-->G
        G[Convertir de key a binario]-->H
        H[Separar msg en una lista]-->I
        I[Separar key en una lista]-->J
        J[Inicializar i=0]-->K
        K[Inicializar j=0]-->L
        L{i < cantidad de elementos en msg}
        L-- SI -->M
        L-- NO -->T
        M{msg i = key j}
        M-- SI -->N
        M-- NO -->O
        N[Agregar 0 a lista msg_enc]
        O[Agregar 1 a lista msg_enc]
        N-->P
        O-->P
        P[i= i+1]-->Q
        Q{j= cantidad de elementos en key}
        Q -- SI -->R
        Q-- NO -->S
        R[j = -1]-->S
        S[j= j+1]-->L
        T[Unión de msg_enc en un string]-->U
        U[Convertir de msg_enc a alfanumerico]-->V
        V[Retornar msg_enc]-->W([ ])
```

Para descifrar hay que inferir el bit original de acuerdi a la logica XOR

```mermaid
    flowchart TD
        A([Descifrar mensaje con cifrado XOR]) --> B
        B[/Escribir "Ingresa el mensaje cifrado"/]-->C
        C[/Leer enc/]-->D
        D[Convertir enc a binario]-->E
        E[Separar enc en la lista enc]-->F
        F[/Escribir "Ingrese la clave"/]-->G
        G[/Leer key/]-->H
        H[Convertir key a binario]-->I
        I[Separar key en la lista key]-->J
        J[Inicializar i=0]-->K
        K[Inicializar j=0]-->L
        L{i< cantidad de elementos en enc}
        L-- SI -->M
        L-- NO -->X
        M{enc i = 0}
        M-- SI-->N
        M-- NO -->Q
        N{key j = 0}
        N-- SI-->O
        N-- NO -->P
        O[Añadir 1 a la lista dec]-->T
        P[Añadir 0 a la lista dec]-->T
        Q{key j=1}
        Q-- SI -->R
        Q-- NO -->S
        R[Añadir 1 a la lista dec]-->T
        S[Añadir 0 a la lista dec]-->T
        T[i=i+1]-->U
        U{j= cantidad de elementos en key}
        U -- SI -->V
        U-- NO -->W
        V[j = -1]-->W
        W[j=j+1]-->L
        X[Unión de dec en un string]-->Y
        Y[Convertir dec a alfanumerico]-->Z
        Z[Retornar dec]-->AA
        AA([ ])
```

## Bifid

Cifrado por transposición utilizando la matriz de polybius como base

```mermaid
    flowchart TD
        A([Cifrar mensaje con cifrado Bifid]) --> B
        B[/Escribir "Escriba el mensaje para encriptar"/]-->C
        C[/Leer msg/]-->DA
        DA[/Escribir "Escriba la clave"/]-->DB
        DB[/Leer key/]-->DC
        DC[[Crear Matriz Personalizada con la clave]]-->D
        D[Separar msg en una lista de letras msg]-->E
        E[Inicializar i=0]-->F
        F{i < cantidad de elementos en msg}
        F-- SI -->G
        F-- NO -->K
        G[Buscar la letra en la matriz de Polybius personalizada]-->H
        H[Guardar 1ra coordenada en lista x]-->I
        I[Guardar 2da coordenada en lista y]-->J
        J[i=i+1]-->F
        K[Re inicializar i=0]-->L
        L{i < cantidad de elementos en listas x, y}
        L-- SI -->M
        L-- NO -->P
        M[Añadir xi y xi+1 como elemento i de la lista msg_enc]-->NA
        NA[Añadir yi y yi+1 como elemento i+1 de la lista msg_enc]-->N
        N[i= i+2]-->O
        O[Reemplazar elemento i de msg_enc con su letra correspondiente de la matriz]-->L
        P[Unir los elementos de la lista msg_enc en un string]-->Q
        Q[Retornar msg_enc]-->R
        R([ ])
```

Se descifrado es simetrico, aunque la manera de operar el str ingresado original cambia

```mermaid
    flowchart TD
        A([Descifrar mensaje con cifrado Bifid]) --> B
        B[/Escribir "Ingresa el mensaje cifrado"/]-->C
        C[/Leer enc/]-->DA
        DA[/Escribir "Escriba la clave"/]-->DB
        DB[/Leer key/]-->DC
        DC[[Crear Matriz Personalizada con la clave]]-->D
        D[Separar enc en una lista de letras enc]-->E
        E[Inicializar i=0]-->F
        F{i < cantidad de elementos en enc}
        F-- SI -->G
        F-- NO -->K
        G[Buscar la letra en la matriz de Polybius personalizada]-->H
        H[Guardar 1ra coordenada en lista x]-->I
        I[Guardar 2da coordenada en lista y]-->J
        J[i=i+1]-->F
        K[Re inicializar i=0]-->L
        L{i < cantidad de elementos en listas x, y}
        L-- SI -->M
        L-- NO -->P
        M[Añadir xi y xi+1 como elemento i de la lista dec]-->NA
        NA[Añadir yi y yi+1 como elemento i+1 de la lista dec]-->N
        N[i= i+2]-->O
        O[Reemplazar elemento i de dec con su letra correspondiente de la matriz]-->L
        P[Unir los elementos de la lista dec en un string]-->Q
        Q[Retornar dec]-->R
        R([ ])
```

## Porta

Cifrado basado en varios abecedarios

```mermaid
      flowchart TD
        A([Cifrar mensaje con cifrado Porta]) --> B
        B[/Escribir "Escriba el mensaje para encriptar"/]-->C
        C[/Leer msg/]-->D
        D[/Escribir "Ingresa la clave"/]-->E
        E[/Leer key/]-->FA
        FA[[Crear matriz de abecedarios con la clave]]-->F
        F[Separar key y msg en listas key y msg]-->G
        G[Inicializar i,j=0]-->H
        H{i < elementos en msg}
        H-- SI-->I
        H-- NO-->N
        I[Añadir el elemento corresponndiente al i de msg de la fila j correspondiente a la clave a la lista msg_enc]-->J
        J[i=i+1]-->K
        K{j=Cantidad de elementos en key}
        K-- SI-->L
        K-- NO -->M
        L[j=-1]-->M
        M[j=j+1]-->H
        N[Unir msg_enc en un string]-->O
        O[Retornar msg_enc]-->P
        P([ ])
```

Su descifrado es simetrico pero el proceso de busqueda en las listas es inverso

   ```mermaid
           flowchart TD
        A([Descifrar mensaje con cifrado Porta]) --> B
        B[/Escribir "Escriba el mensaje cifrado"/]-->C
        C[/Leer enc/]-->D
        D[/Escribir "Ingresa la clave"/]-->E
        E[/Leer key/]-->FA
        FA[[Crear matriz de abecedarios con la clave]]-->F
        F[Separar key y enc en listas key y enc]-->G
        G[Inicializar i,j=0]-->H
        H{i < elementos en enc}
        H-- SI-->I
        H-- NO-->N
        I[Añadir el elemento corresponndiente al i de enc del abecedario original de acuerdo a la fila j de key a dec]-->J
        J[i=i+1]-->K
        K{j=Cantidad de elementos en key}
        K-- SI-->L
        K-- NO -->M
        L[j=-1]-->M
        M[j=j+1]-->H
        N[Unir dec en un string]-->O
        O[Retornar dec]-->P
        P([ ])
```
# ////////////////////////////////////////

```python
# CIFRADO VIGENERE

def caracter_a_numero(cadena:str) -> list:
    cadena.lower()
    cadena_conv = []
    for i in range (0,len(cadena)):
        if ord(cadena[i]) != 32:
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
            cadena_conv.append(" ")
    return cadena_conv

def numero_a_caracter(cadena:list) -> list:
    longitud = len(cadena)
    for i in range (0,longitud):
        if cadena[i] != " ":
            cadena.append(chr(cadena[i]+97))
        else:
            cadena.append(" ")
    for i in range (0, longitud):
        cadena.pop(0)
    return cadena

def vigenere (cadena:list, clave:list) -> list:
    cadena_vigenere : list = []
    j = 0
    for i in range(0, len(cadena)):
            ope = 0
            if cadena[i] != " ":
                ope = cadena[i] + clave[j]
                if ope > 25:
                    ope-= 26
                cadena_vigenere.append(ope)
                j += 1
            else:
                cadena_vigenere.append(" ")
            if j >= len(clave): 
                j = 0
    cadena_vigenere = numero_a_caracter(cadena_vigenere)
    cadena_vigenere = "".join(cadena_vigenere)
    return cadena_vigenere

if __name__ == "__main__":
    cadena : str = str(input("Por favor, ingrese el texto a cifrar: "))
    cadena_conv = caracter_a_numero(cadena)
    clave : str = str(input("Ahora, por favor ingrese la clave bajo la cual se cifrara el texto (una sola cadena sin espacios)"))
    clave_conv = caracter_a_numero(clave)
    cifrado =vigenere(cadena_conv, clave_conv)
    print(f"el texto codificado resultante a partir de la clave {clave} es:")
    print(cifrado)
```

```python
# DESCIFRADO VIGENERE

def caracter_a_numero(cadena:str) -> list:
    cadena.lower()
    cadena_conv = []
    for i in range (0,len(cadena)):
        if ord(cadena[i]) != 32:
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
            cadena_conv.append(" ")
    return cadena_conv

def numero_a_caracter(cadena:list) -> list:
    longitud = len(cadena)
    for i in range (0,longitud):
        if cadena[i] != " ":
            cadena.append(chr(cadena[i]+97))
        else:
            cadena.append(" ")
    for i in range (0, longitud):
        cadena.pop(0)
    return cadena

def des_vigenere (cadena:list, clave:list) -> list:
    cadena_vigenere : list = []
    j = 0
    for i in range(0, len(cadena)):
            ope = 0
            if cadena[i] != " ":
                ope = cadena[i] - clave[j]
                if ope < 0:
                    ope+= 26
                cadena_vigenere.append(ope)
                j += 1
            else:
                cadena_vigenere.append(" ")
            if j >= len(clave): 
                j = 0
    cadena_vigenere = numero_a_caracter(cadena_vigenere)
    cadena_vigenere = "".join(cadena_vigenere)
    return cadena_vigenere

if __name__ == "__main__":
    cadena : str = str(input("Por favor, ingrese el texto a descifrar: "))
    cadena_conv = caracter_a_numero(cadena)
    clave : str = str(input("Ahora, por favor ingrese la clave bajo la cual se descifrara el texto (una sola cadena sin espacios)"))
    clave_conv = caracter_a_numero(clave)
    cifrado =des_vigenere(cadena_conv, clave_conv)
    print(f"el texto decodificado resultante a partir de la clave {clave} es:")
    print(cifrado)
```
