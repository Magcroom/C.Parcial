from machine import Pin as pin,ADC,I2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf

color = 1

sensorx = ADC(pin(32))   # pines usados el 35,34,33,36, 39 , 32, 
sensory = ADC(pin(33))   # pines usados el 35,34,33,36, 39 , 32, 

sensorx.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx.width(ADC.WIDTH_12BIT) # establecer resolución
sensory.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory.width(ADC.WIDTH_12BIT) # establecer resolución


ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
# print(i2c.scan())

boton = pin(13,pin.IN, pin.PULL_UP)
led = pin(2,pin.OUT)

movimientoX = 16
movimientoY = 15

modulo = 2
a = 0
b = 0

for i in range(5):
        print("Turno del jugador 1 - X")
        valor="X"
        #empiezan a jugar - Jugador1
        jugada(valor)
        huboGanador()
        if ganador != "X" and i < 4 :
            for j in range(3):
                print("Turno del jugador 2 - O")
                valor="O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("Felicadadesss!!! Jugador 2 GANADOR del TA-TE-TI")
                break
        elif ganador=="X":
            print("Felicadadesss!!! Jugador 1 GANADOR del TA-TE-TI")
            break
        else:
            print("Empataron del TA-TE-TI")
def huboGanador():
    global ganador
    controlLinea()
    controlVertical()
    controlDiagonal()
def controlLinea():
    global ganador
    if tablero[0]== tablero[1]==tablero[2] !="-":
        ganador = tablero[0]
    elif tablero[3] ==  tablero[4] == tablero[5] != "-":
        ganador = tablero[3]
    elif tablero[6] ==  tablero[7] == tablero[8] != "-":
        ganador = tablero[6]
def controlVertical():
    global ganador
    if tablero[0] ==  tablero[3] == tablero[6] != "-":
        ganador = tablero[0]
    elif tablero[1] ==  tablero[4] == tablero[7] != "-":
        ganador = tablero[1]
    elif tablero[2] ==  tablero[5] == tablero[8] != "-":
        ganador = tablero[2]
def controlDiagonal():
    global ganador
    if tablero[0] ==  tablero[4] == tablero[8] != "-":
        ganador = tablero[0]
    elif tablero[2] ==  tablero[4] == tablero[6] != "-":
        ganador = tablero[2]
def jugada(valor):
    anoto = False
    while anoto==False:
        posicion = int(input("Elegi una posicion del 1 al 9: "))
        posicion -= 1
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("Esa posicion ya esta ocupada")
    tablero[posicion] = valor
    ver_tablero()


while True:


  quedaEscrito = a

  while b==0:

    led.value(boton.value())

    x=sensorx.read()
    y=sensory.read()
    #oled.fill(1)
    oled.text("TRIQUI", 41, 00,color)

    #verticales
    oled.line(42,10,42,64,1)
    oled.line(85,10,85,64,1)
    
    #Horizontales
    oled.line(0,47,128,47,1)
    oled.line(0,27,128,27,1)

    #x
    #oled.line(0,10,38,25,1)
    #led.line(0,25,38,10,1)

    equis = oled.text("X", movimientoX, movimientoY,color)

  #Izquierda
    if x>3600:
      movimientoX = movimientoX-44 
      if movimientoX<16:
        movimientoX=16
          
      oled.text("X", movimientoX, movimientoY,color)
  #Derecha
    elif x<150:
      movimientoX = movimientoX+44 
      if movimientoX>104:
        movimientoX=104

      oled.text("X", movimientoX, movimientoY,color)

  #Arriba
    if y>3600:
      movimientoY = movimientoY-20 
      if movimientoY<15:
        movimientoY=15
          
      oled.text("X", movimientoX, movimientoY,color)
      
  #Abajo    
    elif y<150:
      movimientoY = movimientoY+20
      if movimientoY>56:
        movimientoY=56

      oled.text("X", movimientoX, movimientoY,color)
    
    
    if boton.value()==0:
      #modulo = modulo+1
      oled.text("X", movimientoX, movimientoY,color)
      a = oled.text("X", movimientoX, movimientoY,color)
      b=1
      
      
    oled.show()
    sleep_ms(200)

    #if modulo%2==0:
    
    oled.fill(0)



  #while 2
  while b==1:

    led.value(boton.value())

    x=sensorx.read()
    y=sensory.read()
    #oled.fill(1)
    oled.text("TRIQUI", 41, 00,color)

    #verticales
    oled.line(42,10,42,64,1)
    oled.line(85,10,85,64,1)
    
    #Horizontales
    oled.line(0,47,128,47,1)
    oled.line(0,27,128,27,1)

    #x
    #oled.line(0,10,38,25,1)
    #led.line(0,25,38,10,1)

    equis = oled.text("O", movimientoX, movimientoY,color)

  #Izquierda
    if x>3600:
      movimientoX = movimientoX-44 
      if movimientoX<16:
        movimientoX=16
          
      oled.text("O", movimientoX, movimientoY,color)
  #Derecha
    elif x<150:
      movimientoX = movimientoX+44 
      if movimientoX>104:
        movimientoX=104

      oled.text("O", movimientoX, movimientoY,color)

  #Arriba
    if y>3600:
      movimientoY = movimientoY-20 
      if movimientoY<15:
        movimientoY=15
          
      oled.text("O", movimientoX, movimientoY,color)
      
  #Abajo    
    elif y<150:
      movimientoY = movimientoY+20
      if movimientoY>56:
        movimientoY=56

      oled.text("O", movimientoX, movimientoY,color)
    
    
    if boton.value()==0:
      modulo = modulo+1
      oled.text("O", movimientoX, movimientoY,color)
      a = oled.text("O", movimientoX, movimientoY,color)
      b = 0
      
    oled.show()
    sleep_ms(200)
      
    elif not boton.value():
      oled.fill(0)

