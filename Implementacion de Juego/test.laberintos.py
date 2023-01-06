import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((600,500))
pygame.display.set_caption("Laberinto")
ventana.fill((0,0,0))
#texto 
fuente = pygame.font.Font(None,80)
miTexto = fuente.render("GAME OVER",True,(255,0,0))
miTexto2= fuente.render("GANASTE",True,(0,255,0))

#variables de mi jugador
ladoX = 0
ladoY= 0
velocidad_teclasX = 0
velocidad_teclasY = 0
negro = (0,0,0)
blanco = (255,255,255)
#variables del rectangulo_uno
rectangulo_uno = pygame.Rect(230,80,40,25)
posX1 = 230
posY1 = 40
velocidad1 = 0.05
derecha_izquierda = True
# variables del rectangulo_dos
rectangulo_dos = pygame.Rect(125,85,25,25)
posX = 125
velocidad = 0.05
arriba_abajo = True
# variables del rectangulo_dos22
rectangulo_dos22 = pygame.Rect(160,200,25,25)
posX22 = 200
velocidad22 = 0.05
arriba_abajo22 = True
# variables del rectangulo_tres
rectangulo_tres = pygame.Rect(215,125,30,15)
posX2 = 215
velocidad2 = 0.05
arriba_abajo2 = True
# variables del rectangulo_cuatro
rectangulo_cuatro = pygame.Rect(270,155,30,40)
posX4 = 270
velocidad4 = 0.05
derecha_izquierda4 = True
# variables del rectangulo_cinco
rectangulo_cinco = pygame.Rect(405,249,30,40)
posX5 = 400
velocidad5 = 0.05
derecha_izquierda5 = True
# variables del rectangulo_seis
rectangulo_seis = pygame.Rect(330,155,30,30)
posY6 = 155
velocidad6 = 0.05
arriba_abajo6 = True
# variables del rectangulo_siete
rectangulo_siete = pygame.Rect(423,0,15,13)
posY7 = 0
velocidad7 = 0.4
arriba_abajo7 = True
# variables del rectangulo_ocho
rectangulo_ocho = pygame.Rect(2,280,22,20)
posY8 = 280
velocidad8 = 0.05
arriba_abajo8 = True
# variables del rectangulo_nueve
rectangulo_nueve = pygame.Rect(2,410,30,34)
posX9 = 2
velocidad9 = 0.05
derecha_izquierda9 = True
# variables del rectangulo_diez
rectangulo_diez = pygame.Rect(145,320,42,15)
posY10 = 320
velocidad10 = 0.05
arriba_abajo10 = True

# variables del rectangulo_once
rectangulo_once = pygame.Rect(215,290,30,15)
posY11 = 290
velocidad11 = 0.05
arriba_abajo11 = True

while True:
    ventana.fill(negro)
    #obstaculos
    pygame.draw.rect(ventana,(blanco),rectangulo_uno)
    pygame.draw.rect(ventana,(blanco),rectangulo_dos)
    pygame.draw.rect(ventana,(blanco),rectangulo_dos22)
    pygame.draw.rect(ventana,(blanco),rectangulo_tres)
    pygame.draw.rect(ventana,(blanco),rectangulo_cuatro)
    pygame.draw.rect(ventana,(blanco),rectangulo_cinco)
    pygame.draw.rect(ventana,(blanco),rectangulo_seis)
    pygame.draw.rect(ventana,(blanco),rectangulo_siete)
    pygame.draw.rect(ventana,(blanco),rectangulo_ocho)
    pygame.draw.rect(ventana,(blanco),rectangulo_nueve)
    pygame.draw.rect(ventana,(blanco),rectangulo_diez)
    pygame.draw.rect(ventana,(blanco),rectangulo_once)

    #jugador
    player = pygame.draw.rect(ventana,(255,0,0),(ladoX,ladoY,10,10))
    ladoX += velocidad_teclasX 
    ladoY += velocidad_teclasY
    #bloque ganador 
    zz = pygame.draw.polygon(ventana,(0,255,0),((580,480),(600,480),(600,500),(580,500)))
    zz2 = pygame.draw.polygon(ventana,(0,255,0),((580,0),(600,0),(600,20),(580,20)))

    # Los muros del laberinto
    a = pygame.draw.polygon(ventana,(blanco),((44,32),(120,32),(120,45),(44,45)))
    b = pygame.draw.polygon(ventana,(blanco),((154,0),(154,80),(170,80),(170,0)))
    c = pygame.draw.polygon(ventana,(blanco),((27,100),(44,100),(44,200),(27,200)))
    d = pygame.draw.polygon(ventana,(blanco),((100,100),(120,100),(120,240),(100,240)))
    e = pygame.draw.polygon(ventana,(blanco),((0,260),(170,260),(170,274),(0,274)))
    f = pygame.draw.polygon(ventana,(blanco),((210,32),(225,32),(225,120),(210,120)))
    g = pygame.draw.polygon(ventana,(blanco),((190,190),(205,190),(205,274),(190,274)))
    h = pygame.draw.polygon(ventana,(blanco),((240,0),(240,15),(330,15),(330,0)))
    i = pygame.draw.polygon(ventana,(blanco),((250,108),(265,108),(265,173),(250,173)))
    j = pygame.draw.polygon(ventana,(blanco),((356,24),(386,24),(386,123),(356, 123)))
    k = pygame.draw.polygon(ventana,(blanco),((400,0),(400,60),(420,60),(420,0)))
    l = pygame.draw.polygon(ventana,(blanco),((280,135),(400,135),(400,150),(280,150)))
    m = pygame.draw.polygon(ventana,(blanco),((27,293),(140,293),(140,315),(27,315)))
    n = pygame.draw.polygon(ventana,(blanco),((140,390),(140,405),(27,405),(27,390)))
    o = pygame.draw.polygon(ventana,(blanco),((160,293),(210,293),(210,315),(160,315)))
    p = pygame.draw.polygon(ventana,(blanco),((27,450),(47,450),(47,500),(27,500)))
    q = pygame.draw.polygon(ventana,(blanco),((137,500),(157,500),(157,450),(137,450)))
    r = pygame.draw.polygon(ventana,(blanco),((190,420),(260,420),(260,435),(190,435)))
    s = pygame.draw.polygon(ventana,(blanco),((250,293),(320,293),(320,313),(250,313)))
    t = pygame.draw.polygon(ventana,(blanco),((340,293),(360,293),(360,330),(340,330)))
    u = pygame.draw.polygon(ventana,(blanco),((175,450),(300,450),(300,465),(175,465)))
    v = pygame.draw.polygon(ventana,(blanco),((375,293),(395,293),(395,365),(375,365)))
    x = pygame.draw.polygon(ventana,(blanco),((422,293),(435,293),(435,305),(422,305)))
    y = pygame.draw.polygon(ventana,(blanco),((557,480),(557,470),(600,470),(600,480)))
    aa = pygame.draw.polygon(ventana,(blanco),((44,45),(50,45),(50,70),(44,70)))
    ab = pygame.draw.polygon(ventana,(blanco),((0,70),(50,70),(50,85),(0,85)))
    ba = pygame.draw.polygon(ventana,(blanco),((154,80),(154,70),(70,70),(70,80)))
    bb = pygame.draw.polygon(ventana,(blanco),((185,0),(185,47),(195,47),(195,0)))
    ca = pygame.draw.polygon(ventana,(blanco),((44,150),(80,150),(80,165),(44,165)))
    da = pygame.draw.polygon(ventana,(blanco),((100,185),(100,195),(65,195),(65,185)))
    db = pygame.draw.polygon(ventana,(blanco),((27,220),(100,220),(100,240),(27,240)))
    ea = pygame.draw.polygon(ventana,(blanco),((145,230),(170,230),(170,260),(145,260)))
    fa = pygame.draw.polygon(ventana,(blanco),((210,60),(210,160),(195,160),(195,60)))
    ha = pygame.draw.polygon(ventana,(blanco),((260,15),(260,73),(275,73),(275,15)))
    hb = pygame.draw.polygon(ventana,(blanco),((310,30),(325,30),(325,73),(310,73)))
    ia = pygame.draw.polygon(ventana,(blanco),((265,108),(335,108),(335,120),(265,120)))
    ka = pygame.draw.polygon(ventana,(blanco),((440,0),(440,60),(460,60),(460,0)))
    kb = pygame.draw.polygon(ventana,(blanco),((480,0),(520,0),(480,50)))
    kc = pygame.draw.polygon(ventana,(blanco),((500,50),(525,15),(550,15),(550,30),(535,50)))
    kd = pygame.draw.polygon(ventana,(blanco),((555,50),(570,30),(600,30),(600,50)))
    la = pygame.draw.polygon(ventana,(blanco),((400,150),(420,150),(420,74),(400,74)))
    lb = pygame.draw.polygon(ventana,(blanco),((440,150),(460,150),(460,72.5),(440,72.5)))
    lc = pygame.draw.polygon(ventana,(blanco),((440,163),(460,163),(460,280),(440,280)))
    ma = pygame.draw.polygon(ventana,(blanco),((120,315),(140,315),(140,370),(120,370)))
    na = pygame.draw.polygon(ventana,(blanco),((27,390),(47,390),(47,335),(27,335)))
    nb = pygame.draw.polygon(ventana,(blanco),((67,330),(97,330),(97,370),(67,370)))
    oa = pygame.draw.polygon(ventana,(blanco),((210,315),(210,405),(190,405),(190,315)))
    pa = pygame.draw.polygon(ventana,(blanco),((47,480),(117,480),(117,500),(47,500)))
    sa = pygame.draw.polygon(ventana,(blanco),((250,313),(270,313),(270,405),(250,405)))
    ta = pygame.draw.polygon(ventana,(blanco),((360,330),(360,340),(287,340),(287,330)))
    tb = pygame.draw.polygon(ventana,(blanco),((287,340),(300,340),(300,405),(287,405)))
    ua = pygame.draw.polygon(ventana,(blanco),((185,465),(195,465),(195,482),(185,482)))
    ub = pygame.draw.polygon(ventana,(blanco),((215,480),(215,600),(225,600),(225,480)))
    uc = pygame.draw.polygon(ventana,(blanco),((245,465),(255,465),(255,482),(245,482)))
    ud = pygame.draw.polygon(ventana,(blanco),((275,480),(275,600),(285,600),(285,480)))
    va = pygame.draw.polygon(ventana,(blanco),((375,365),(375,355),(318,355),(318,365)))
    vb = pygame.draw.polygon(ventana,(blanco),((318,365),(318,385),(328,385),(328,365)))
    vc = pygame.draw.polygon(ventana,(blanco),((318,400),(318,540),(328,540),(328,400)))
    vd = pygame.draw.polygon(ventana,(blanco),((345,400),(345,390),(395,390),(395,400)))
    ve = pygame.draw.polygon(ventana,(blanco),((350,420),(360,420),(360,480),(350,480)))
    vf = pygame.draw.polygon(ventana,(blanco),((380,420),(390,420),(390,480),(380,480)))
    vg = pygame.draw.polygon(ventana,(blanco),((410,293),(422,293),(422,460),(410,460)))
    vh = pygame.draw.polygon(ventana,(blanco),((410,475),(422,475),(422,555),(410,555)))
    xa = pygame.draw.polygon(ventana,(blanco),((448,293),(600,293),(600,305),(448,305)))
    xb = pygame.draw.polygon(ventana,(blanco),((463,293),(475,293),(475,480),(463,480)))
    xc = pygame.draw.polygon(ventana,(blanco),((435,320),(435,500),(450,500),(450,320)))
    xd = pygame.draw.polygon(ventana,(blanco),((488,318),(498,318),(498,500),(488,500)))
    xe = pygame.draw.polygon(ventana,(blanco),((511,305),(521,305),(521,480),(511,480)))
    xf = pygame.draw.polygon(ventana,(blanco),((534,305),(544,305),(544,325),(534,325)))
    xg = pygame.draw.polygon(ventana,(blanco),((534,338),(544,338),(544,500),(534,500)))
    ya = pygame.draw.polygon(ventana,(blanco),((540,448),(540,458),(580,458),(580,448)))
    yb = pygame.draw.polygon(ventana,(blanco),((557,426),(557,436),(600,436),(600,426)))
    yc = pygame.draw.polygon(ventana,(blanco),((540,404),(540,414),(580,414),(580,404)))
    yd = pygame.draw.polygon(ventana,(blanco),((557,382),(557,392),(600,392),(600,382)))
    ye = pygame.draw.polygon(ventana,(blanco),((540,360),(540,370),(580,370),(580,360)))
    yf = pygame.draw.polygon(ventana,(blanco),((540,338),(540,348),(580,348),(580,338)))
    yg = pygame.draw.polygon(ventana,(blanco),((580,338),(580,320),(560,320),(560,338)))
    za = pygame.draw.polygon(ventana,(blanco),((460,72.5),(460,90),(582,90),(582,72.5)))
    zb = pygame.draw.polygon(ventana,(blanco),((475,105),(475,300),(495,300),(495,105)))
    zc = pygame.draw.polygon(ventana,(blanco),((510,90),(510,210),(530,210),(530,90)))
    zd = pygame.draw.polygon(ventana,(blanco),((510,222),(510,270),(530,270),(530,222)))
    ze = pygame.draw.polygon(ventana,(blanco),((530,222),(530,270),(580,246)))
    zf = pygame.draw.polygon(ventana,(blanco),((600,235),(600,190),(550,210)))
    zg = pygame.draw.polygon(ventana,(blanco),((530,200),(530,160),(580,180)))
    zh = pygame.draw.polygon(ventana,(blanco),((600,170),(600,130),(550,150)))
    zi = pygame.draw.polygon(ventana,(blanco),((530,90),(530,135),(582,115),(582,90)))

   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #movimiento por teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidad_teclasX = -0.15
                if ladoX <0:
                    ladoX = 0
            if event.key == pygame.K_RIGHT:
                velocidad_teclasX = 0.15
                if ladoX > (600-15):
                    ladoX = 600-15
            if event.key == pygame.K_UP:
                velocidad_teclasY = -0.15
                if ladoY <0:
                    ladoY = 0
            if event.key == pygame.K_DOWN:
                velocidad_teclasY = 0.15
                if ladoY > (500-15):
                    ladoY = 500-15

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velocidad_teclasX = 0
                if ladoX <0:
                    ladoX = 0
            if event.key == pygame.K_RIGHT:
                velocidad_teclasX = 0
                if ladoX > (600-15):
                    ladoX = 600-15
            if event.key == pygame.K_UP:
                velocidad_teclasY = 0
                if ladoY <0:
                    ladoY = 0
            if event.key == pygame.K_DOWN:
                velocidad_teclasY = 0
                if ladoY > (500-15):
                    ladoY = 500-15
          
    #Es para que se mueva de derecha a izquierda el rectangulo_uno
    if derecha_izquierda == True:
        if posX1 < 310:
            posX1 += velocidad1
            rectangulo_uno.left =  posX1
        else:
            derecha_izquierda = False
    else:
        if posX1 > 230:
            posX1 -= velocidad1
            rectangulo_uno.left = posX1
        else:
            derecha_izquierda = True

    # Es para que se mueva de arriba hacia abajo el rectangulo
    if arriba_abajo == True:
        if posX < 200:
            posX += velocidad
            rectangulo_dos.top =  posX
        else:
            arriba_abajo = False
    else:
        if posX > 85:
            posX -= velocidad
            rectangulo_dos.top = posX
        else:
            arriba_abajo = True
    
    # Es para que se mueva de arriba hacia abajo el rectangulo22
    if arriba_abajo22 == True:
        if posX22 < 200:
            posX22 += velocidad22
            rectangulo_dos22.top =  posX22
        else:
            arriba_abajo22 = False
    else:
        if posX22 > 85:
            posX22 -= velocidad22
            rectangulo_dos22.top = posX22
        else:
            arriba_abajo22 = True

    #Para que el rectangulo tres se mueva de arriba abajo     
    if arriba_abajo2 == True:
        if posX2 < 270:
            posX2 += velocidad2
            rectangulo_tres.top =  posX2
        else:
            arriba_abajo2 = False
    else:
        if posX2 > 120:
            posX2 -= velocidad2
            rectangulo_tres.top = posX2
        else:
            arriba_abajo2 = True

    #Es para que se mueva de derecha a izquierda el rectangulo_cuatro
    if derecha_izquierda4 == True:
        if posX4 < 400:
            posX4 += velocidad4
            rectangulo_cuatro.left =  posX4
        else:
            derecha_izquierda4 = False
    else:
        if posX4 > 270:
            posX4 -= velocidad4
            rectangulo_cuatro.left = posX4
        else:
            derecha_izquierda4 = True
    #Es para que se mueva de derecha a izquierda el rectangulo_cinco
    if derecha_izquierda5 == True:
        if posX5 < 400:
            posX5 += velocidad4
            rectangulo_cinco.left =  posX5
        else:
            derecha_izquierda5 = False
    else:
        if posX5 > 270:
            posX5 -= velocidad5
            rectangulo_cinco.left = posX5
        else:
            derecha_izquierda5 = True

    #Para que el rectangulo seis se mueva de arriba abajo     
    if arriba_abajo6 == True:
        if posY6 < 260:
            posY6 += velocidad6
            rectangulo_seis.top =  posY6
        else:
            arriba_abajo6 = False
    else:
        if posY6 > 155:
            posY6 -= velocidad6
            rectangulo_seis.top = posY6
        else:
            arriba_abajo6 = True
    
    #Para que el rectangulo siete se mueva de arriba abajo     
    if arriba_abajo7 == True:
        if posY7 < 275:
            posY7 += velocidad7
            rectangulo_siete.top =  posY7
        else:
            arriba_abajo7 = False
    else:
        if posY7 > 0:
            posY7 -= velocidad7
            rectangulo_siete.top = posY7
        else:
            arriba_abajo7 = True
    
    #Para que el rectangulo ocho se mueva de arriba abajo     
    if arriba_abajo8 == True:
        if posY8 < 480:
            posY8 += velocidad8
            rectangulo_ocho.top =  posY8
        else:
            arriba_abajo8 = False
    else:
        if posY8 > 280:
            posY8 -= velocidad8
            rectangulo_ocho.top = posY8
        else:
            arriba_abajo8 = True
    
    #Es para que se mueva de derecha a izquierda el rectangulo_nueve
    if derecha_izquierda9 == True:
        if posX9 < 155:
            posX9 += velocidad9
            rectangulo_nueve.left =  posX9
        else:
            derecha_izquierda9 = False
    else:
        if posX9 > 2:
            posX9 -= velocidad9
            rectangulo_nueve.left = posX9
        else:
            derecha_izquierda9 = True

    #Para que el rectangulo diez se mueva de arriba abajo     
    if arriba_abajo11 == True:
        if posY10 < 433:
            posY10 += velocidad10
            rectangulo_diez.top =  posY10
        else:
            arriba_abajo11 = False
    else:
        if posY10 > 320:
            posY10 -= velocidad10
            rectangulo_diez.top = posY10
        else:
            arriba_abajo10 = True
    
    #Para que el rectangulo once se mueva de arriba abajo     
    if arriba_abajo11 == True:
        if posY11 < 400:
            posY11 += velocidad11
            rectangulo_once.top =  posY11
        else:
            arriba_abajo11 = False
    else:
        if posY11 > 290:
            posY11 -= velocidad11
            rectangulo_once.top = posY11
        else:
            arriba_abajo11 = True
    
    



    #colicion de obstaculos en movimiento en movimiento
    if player.colliderect(rectangulo_dos) or player.colliderect(rectangulo_uno) or  player.colliderect(a):
        velocidad = 0 
        velocidad1 = 0 
        velocidad_teclasX = 0
        velocidad_teclasY = 0
        ventana.blit(miTexto,(120,200))
        

    #LLEGADA A LA META
    if player.colliderect(zz) or player.colliderect(zz2):
        velocidad = 0 
        velocidad1 = 0 
        velocidad_teclasX = 0
        velocidad_teclasY = 0
        ventana.blit(miTexto2,(150,200))
    
   
    #print(pygame.mouse.get_pos())
    
    pygame.display.update()