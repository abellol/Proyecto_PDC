import vernam
import columnar_transposition
import desencriptado_columnar
import desencriptado_columnar
import albertiwheel
import descifrado_albertis
import bifid_encoder
import bifid_decoder
import porta_encoder
import porta_decoder
import hill_encoder
import hill_decoder
import vigenere_decoder
import vigenere_encoder



def menu():
    print("")
    enc_dec=int(input("""
                    Selecciona si quieres
                      1) Encriptar
                      2) Desencriptar
                      Selecciona: """))
    print("""
Seleccione entre los siguientes cifrados:
          1)Vernam
          2)Columnar Trannsposition
          3)Alberti's Wheel
          4)Bifid
          5)Vigenere
          6)Hill

        """)
    opcion_cif = int(input("Ingrese la opción que desea usar: "))
    match enc_dec:
        case 1:
            match opcion_cif:
                case 1:
                    vernam.vernam()
                case 2:
                    columnar_transposition.columnar()
                case 3:
                    albertiwheel.rueda_alberti()
                case 4:
                    bifid_encoder.bifid_enc()
                case 5:
                    vigenere_encoder.vigenere()
                case 6:
                    hill_encoder.hill()
        case 2:
            match opcion_cif:
                case 1:
                    vernam.vernam()
                case 2:
                    desencriptado_columnar.desencriptar_columnar()
                case 3:
                    descifrado_albertis.des_rueda_alberti()
                case 4:
                    bifid_decoder.bifid_dec()
                case 5:
                    vigenere_decoder.des_vigenere()
                case 6:
                    hill_decoder.hill()
if __name__=="__main__":

    menu()