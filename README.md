# Proyecto_PDC
Desarrollo del proyecto sobre encriptación de mensajes
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
