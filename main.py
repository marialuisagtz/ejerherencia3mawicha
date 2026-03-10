from clases.herencia1.taxi import Taxi
from clases.herencia1.auto_particular import AutoParticular


def main():
    coche= Taxi("123-GTO", "Versa", "1000","123-a")
    
    
    print()
    print(coche)
    coche.encender()
    coche.subirPasajero( )
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()
    
    ap= AutoParticular("456", "Maria Luisa", "19", "Volvo", "rojo", "ABC")
    ap.subirAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajarAuto()
    print("Datos del usuario")
    
    print(ap)
    
    
if __name__ == "__main__":
    main()
    