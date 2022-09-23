from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms,sleep
import random

Cx=0
Cy=0
K=0
click=0
posO=[1,2,3,4,5,6,7,8,9]

ancho=128
alto=64
ejex= ADC(Pin(32))
ejex.atten(ADC.ATTN_11DB)
ejex.width(ADC.WIDTH_12BIT)

boton1=Pin(13,Pin.IN,Pin.PULL_UP)

ejey= ADC(Pin(33))
ejey.atten(ADC.ATTN_11DB)
ejey.width(ADC.WIDTH_12BIT)

i2c = I2C(0, scl=Pin(22), sda=Pin(23)) 
oled = SSD1306_I2C(ancho, alto, i2c)

def seleccionar(Cx, Cy, K): 
    if(Cx==0 and Cy==0):
        oled.text("! !", 15, 15, 1)
        K=1
    else:
        oled.text(" ", 15, 15, 1)

    if(Cx==1 and Cy==0):
        oled.text("! !", 50, 15, 10)
        K=2
    else:
        oled.text(" ", 50, 15, 10)

    if(Cx==2 and Cy==0):
        oled.text("! !", 85, 15, 10)
        K=3
    else:
        oled.text(" ", 85, 15, 10)

    if(Cx==0 and Cy==1):
        oled.text("! !", 15, 35, 10)
        K=4
    else:
        oled.text(" ", 15, 35, 10)

    if(Cx==1 and Cy==1):
        oled.text("! !", 50, 35, 1)
        K=5
    else:
        oled.text(" ", 50, 35, 1)

    if(Cx==2 and Cy==1):
        oled.text("! !", 88, 35, 10)
        K=6
    else:
        oled.text(" ", 88, 27, 10)
    
    if(Cx==0 and Cy==2):
        oled.text("! !", 17, 51, 10)
        K=7
    else:
        oled.text(" ", 17, 51, 10)
    
    if(Cx==1 and Cy==2):
        oled.text("! !", 49, 52, 10)
        K=8
    else:
        oled.text(" ", 49, 52, 10)
        
    if(Cx==2 and Cy==2):
        oled.text("! !", 88, 51, 10)
        K=9
    else:
        oled.text(" ", 88, 51, 10)

matriz=[[2,2,2],[2,2,2],[2,2,2]]
matriztxt=[["","",""],["","",""],["","",""]]

def ponerXyO(K, click,turno):
  
  contador= turno

  if(turno==0):
    

    
    if(click==1 and matriz[0][0]==2):
        matriz[0][0]=1
        matriztxt[0][0]="x"
        contador=not contador
    if(click==2 and matriz[0][1]==2):
        matriz[0][1]=1
        matriztxt[0][1]="x"
        contador=not contador
    if(click==3 and matriz[0][2]==2):
        matriz[0][2]=1
        matriztxt[0][2]="x"
        contador=not contador
    if(click==4 and matriz[1][0]==2):
        matriz[1][0]=1
        matriztxt[1][0]="x"
        contador=not contador
    if(click==5 and matriz[1][1]==2):
        matriz[1][1]=1
        matriztxt[1][1]="x"
        contador=not contador
    if(click==6 and matriz[1][2]==2):
        matriz[1][2]=1
        matriztxt[1][2]="x"
        contador=not contador
    if(click==7 and matriz[2][0]==2):
        matriz[2][0]=1
        matriztxt[2][0]="x"
        contador=not contador
    if(click==8 and matriz[2][1]==2):
        matriz[2][1]=1
        matriztxt[2][1]="x"
        contador=not contador
    if(click==9 and matriz[2][2]==2):
        matriz[2][2]=1
        matriztxt[2][2]="x"
        contador=not contador
            
                    

  else:
    
    if(click==1 and matriz[0][0]==2):
      matriz[0][0]=0
      matriztxt[0][0]="o"
      contador=not contador
    if(click==2 and matriz[0][1]==2):
      matriz[0][1]=0
      matriztxt[0][1]="o"
      contador=not contador
    if(click==3 and matriz[0][2]==2):
      matriz[0][2]=0
      matriztxt[0][2]="o"
      contador=not contador
    if(click==4 and matriz[1][0]==2):
      matriz[1][0]=0
      matriztxt[1][0]="o"
      contador=not contador
    if(click==5 and matriz[1][1]==2):
      matriz[1][1]=0
      matriztxt[1][1]="o"
      contador=not contador
    if(click==6 and matriz[1][2]==2):
      matriz[1][2]=0
      matriztxt[1][2]="o"
      contador=not contador
    if(click==7 and matriz[2][0]==2):
      matriz[2][0]=0
      matriztxt[2][0]="o"
      contador=not contador
    if(click==8 and matriz[2][1]==2):
      matriz[2][1]=0
      matriztxt[2][1]="o"
      contador=not contador
    if(click==9 and matriz[2][2]==2):
      matriz[2][2]=0
      matriztxt[2][2]="o"
      contador=not contador
            
   
   
  oled.text(matriztxt[0][0], 23, 15, 1)
  oled.text(matriztxt[0][1], 58, 15, 1)
  oled.text(matriztxt[0][2], 93, 15, 1) 

  oled.text(matriztxt[1][0], 23, 34, 1)
  oled.text(matriztxt[1][1], 59, 34, 1)
  oled.text(matriztxt[1][2], 95, 34, 1)       

  oled.text(matriztxt[2][0], 25, 51, 10)
  oled.text(matriztxt[2][1], 58, 52, 10)
  oled.text(matriztxt[2][2], 95, 51, 10)

  return contador
def refrescar (oled):
   
    seleccionar(Cx, Cy, K)


    oled.show()

def Comprobar_partida():

  victoria=False

  for i in range(len(matriz)):
    if matriz[i][0]!=2 and matriz[i][1]!=2 and matriz[i][2]!=2 and (matriz[i][0]==matriz[i][1] and matriz[i][1]==matriz[i][2]):
      if matriz[i][0]==0:
        return 0
      else:
        return 1
        victoria=True
  for i in range(len(matriz[0])):
    if matriz[0][i]!=2 and matriz[1][i]!=2 and matriz[2][i]!=2 and (matriz[0][i]==matriz[1][i] and matriz[1][0]==matriz[2][i]):
      if matriz[0][i]==0:
        return 0
        victoria=True
      else:
        return 1
        victoria=True
  if matriz[1][1]!=2 and ((matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]) or (matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0])):
    if matriz[1][1]==0:
      return 0
      victoria=True
    else:
      return 1
      victoria=True

  empate=True
  
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j]==2:
        empate=False
  
  if empate==True and victoria==False:
    return 2

  return 3
def vaciar_matrices():
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j]=2
      matriztxt[i][j]=""

contador=0
end=False

while True:

  estado=Comprobar_partida()

  if estado==0:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Jugador O",32, 27, 1)
    oled.text("Ganaste!",37, 39, 1)
    oled.show()
    sleep(3)
  if estado==1:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Jugador x",32, 27, 1)
    oled.text("Ganaste!",37, 39, 1)
    oled.show()
    sleep(3)
  if estado==2:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Empate",32, 27, 1)
    oled.show()
    sleep(3)
  
  oled.text("TRIQUI", 41, 00,1)
  oled.line(42,15,42,64,1)
  oled.line(84,15,84,64,1)
  oled.line(110,30,18,30,1)
  oled.line(110,47,18,47,1)
  
  tempx=ejex.read()
  tempy=ejey.read()
  
  if(tempx==4095 and Cx!=2):
      Cx=Cx+1
      sleep_ms(200)
  if(tempx==0 and Cx!=0):
      Cx=Cx-1
      sleep_ms(200)
  if(tempy==4095 and Cy!=2):
      Cy=Cy+1
      sleep_ms(200)
  if(tempy==0 and Cy!=0):
      Cy=Cy-1
      sleep_ms(200)

  if(Cx==0 and Cy==0):
      K=1
  if(Cx==1 and Cy==0):
      K=2
  if(Cx==2 and Cy==0):
      K=3
  if(Cx==0 and Cy==1):
      K=4
  if(Cx==1 and Cy==1):
      K=5
  if(Cx==2 and Cy==1):
      K=6
  if(Cx==0 and Cy==2):
      K=7
  if(Cx==1 and Cy==2):
      K=8
  if(Cx==2 and Cy==2):
      K=9
  
  if(not boton1.value()):
      click=K
      sleep_ms(200)

  contador=ponerXyO(K, click, contador)
  refrescar(oled)

  oled.show()
  oled.fill(0)

