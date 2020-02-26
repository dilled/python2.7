try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
import pygame as pg
import random
import socket

HOST = 'localhost'
PORT = 8526
def sercli():
    global HOST
    global PORT
    global net
    global s
    print("1 = SERVER 2 = CLIENT 3 = Normal")
    try:
        net = input('?')
        if net == 1:
            print (net, 'SERVER')
            print ("Default HOST = 'localhost' ")
            print ("Default PORT = 8526")
        if net == 2:
            print (net, 'CLIENT')
            print ("Default HOST = 'localhost'") 
            print ("Default PORT = 8526")
        if net == 3:
            return net
    except:
        sercli()
    if net == 1:
            try:
                HOST = ''
                PORT = input ('port ')
            except:
                PORT = 8526
    
    if net == 2:
            try:
                HOST = input('Ip ')
                HOST = str(HOST)
            except:
                HOST = str(HOST)
            try:
                PORT = input('port?')
            except:    
                PORT = 8526
    return HOST, PORT, net
    
sercli()

if net == 1 or net == 2:
    print (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if net == 1:
    s.bind((HOST, PORT))
    s.listen(0)
    s, addr = s.accept()
    s.send('server found')
    print('Connected by', addr)
    dat = s.recv(12)
    #print repr(dat)
if net  == 2:
    s.connect((HOST, PORT))
    s.send('Client found')
    dat = s.recv(12)
    #print repr(dat)
        

print(net)
if net == 1 or net == 2:
    print (repr(dat))
pg.init() 
display_width = 800
display_height = 600
xx = [400]
yy = [300]
xx2 = ([200])
yy2 = ([100])
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
w =10
h= 10
ow=20
oh=20

ox=random.randrange(20, display_width-20) #OMPPU
oy=random.randrange(20, display_height-20)#OMPPU
if net == 1:
        dataox = str(ox).rjust(4, '0')
        dataoy = str(oy).rjust(4, '0')
        datoc=dataox+dataoy
        s.send(datoc)    
if net ==2:    
        dato = s.recv(8)
        ox = int(dato[:4])
        oy = int(dato[4:])
        

speed =4
speed2 =4
leng=10
leng2=10
xc = 0
yc = -speed
x2c = 0
y2c = -speed
x = (display_width -200)
y = (display_height -300)
x2 = (display_width -600)
y2 = (display_height -300)

if net == 2:
    x2 = (display_width -200)
    y2 = (display_height -300)
    x = (display_width -600)
    y = (display_height -300)
    
gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('liero')
clock = pg.time.Clock()
eatn = False
gameDisplay.fill(white)

def eaten():   
    ou(55,0,white)
    font = pg.font.SysFont('Sans', 25)
    text = font.render(''+str(leng2-10), True, black)
    gameDisplay.blit(text,(60,0))
    ou(455,0,white)
    font = pg.font.SysFont('Sans', 25)
    text = font.render(''+str(leng-10), True, black)
    gameDisplay.blit(text,(460,0))

def ou(ox,oy,c):
    pg.draw.rect(gameDisplay, c, (ox,oy,50,20))    


def omppu(ox,oy,c):
    pg.draw.rect(gameDisplay, c, (ox,oy,ow,oh))

def mato2(x2,y2,cs):
    pg.draw.circle(gameDisplay, cs,(x2,y2),5)     
   
def matoh(xh,yh):
    pg.draw.circle(gameDisplay, white,(xh,yh),6) 

eaten()
     
while not eatn:
          
    for event in pg.event.get():
        if event.type == pg.QUIT:
            eatn = True
            
        if event.type == pg.KEYDOWN:            
            if event.key == pg.K_LEFT:
                xc = -speed
                yc=0 
            elif event.key == pg.K_RIGHT:
                xc = +speed
                yc=0 
            elif event.key == pg.K_UP:
                yc = -speed
                xc=0                
            elif event.key == pg.K_DOWN:
                yc = +speed
                xc=0  
            elif event.key == pg.K_SPACE:
                yc = 0
                xc=0
                
            elif event.key == pg.K_a:
                x2c = -speed2
                y2c=0 
            elif event.key == pg.K_d:
                x2c = +speed2
                y2c=0 
            elif event.key == pg.K_w:
                y2c = -speed2
                x2c=0 
            elif event.key == pg.K_s:
                y2c = +speed2
                x2c=0 
            elif event.key == pg.K_e:
                y2c = 0
                x2c=0
            elif event.key == pg.K_v:
                speed -=1
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    print('')

    
        
    xh=xx[-1]
    yh=yy[-1]
    xh2=xx2[-1]
    yh2=yy2[-1]
    
    x2 += x2c
    y2 += y2c
    x += xc
    y += yc
    if net != 3:
        datax = str(x).rjust(4, '0')
        datay = str(y).rjust(4, '0')
        datc=datax+datay
        s.send(datc)    
    
        dat = s.recv(8)
        x2 = int(dat[:4])
        y2 = int(dat[4:])

    omppu(ox,oy,red)
    mato2(x,y,black)
    mato2(x2,y2,green)
    xx.insert(0,x)
    yy.insert(0,y)
    xx2.insert(0,x2)
    yy2.insert(0,y2) 
    
    if x in xx or x2 in xx2:
        if y in yy or y2 in yy2:
            ff =len(xx)-1            
            f=ff
            for fr in range(20,ff):
                if leng<20:
                    break                                 
                if xx[fr] ==x and yy[fr]==y:                
                    while leng >fr:
                        if leng<20:
                            eaten()
                            break
                        xh=xx[-1]
                        yh=yy[-1]
                        matoh(xh,yh)
                        del xx[-1]
                        del yy[-1]     
                        leng-=1
                    eaten()
                    break                   
   
            ff2 =len(xx2)-1            
            f2=ff2
            for fr2 in range(10,ff2):
                if leng2<10:
                    break                                 
                if xx2[fr2] ==x and yy2[fr2]==y:                
                    while leng2 >fr2:
                        if leng2<10:
                            eaten()
                            break
                        xh2=xx2[-1]
                        yh2=yy2[-1]
                        matoh(xh2,yh2)
                        del xx2[-1]
                        del yy2[-1]      
                        leng2-=1
                        leng+=1
                    eaten()
                    break
    if x in xx or x2 in xx2:
        if y in yy or y2 in yy2:
            ff =len(xx)-1            
            f=ff
            for fr in range(10,ff):
                if leng<10:
                    break                                 
                if xx[fr] ==x2 and yy[fr]==y2:                
                    while leng >fr:
                        if leng<10:
                            eaten()
                            break
                        xh=xx[-1]
                        yh=yy[-1]
                        matoh(xh,yh)
                        del xx[-1]
                        del yy[-1]     
                        leng-=1
                        leng2+=1
                    eaten()
                    break                   
   
            ff2 =len(xx2)-1            
            f2=ff2
            for fr2 in range(20,ff2):
                if leng2<20:
                    break                                 
                if xx2[fr2] ==x2 and yy2[fr2]==y2:                
                    while leng2 >fr2:
                        if leng2<20:
                            eaten()
                            break
                        xh2=xx2[-1]
                        yh2=yy2[-1]
                        matoh(xh2,yh2)
                        del xx2[-1]
                        del yy2[-1]       
                        leng2-=1
                    eaten()
                    break                   
    
    matoh(xh,yh)  
    matoh(xh2,yh2)        

    if len(xx) > leng:                  ######  ######
        del xx[leng]
        del yy[leng]          
        
    if len(xx2) > leng2:
        del xx2[leng2]
        del yy2[leng2] 
     
    if ox+ow+5 > x+w/2 > ox-5 and oy+oh+5 > y+h/2 > oy-5:  ###  omppu #####
        omppu(ox,oy,white)  
        leng+=20
        eaten()
        ox=random.randrange(30, display_width-30)
        oy=random.randrange(30, display_height-30)
        omppu(ox,oy,red)
        if net != 3:
            dataox = str(ox).rjust(4, '0')
            dataoy = str(oy).rjust(4, '0')
            datoc=dataox+dataoy
            s.send(datoc)    
    
        
    if ox+ow+5 > x2+w/2 > ox-5 and oy+oh+5 > y2+h/2 > oy-5: ##### omppu #####
        omppu(ox,oy,white)  
        leng2+=20
        eaten()
        ox=random.randrange(30, display_width-30)
        oy=random.randrange(30, display_height-30)
                                ###############
        if net != 3:
            dato = s.recv(8)
            ox = int(dato[:4])
            oy = int(dato[4:])
        omppu(ox,oy,red)       
    if x > display_width-30 or x < 30:    ####### reunat ######
            xc*=-1           
    if y > display_height-30 or y < 30:
            yc*=-1
    if x2 > display_width-30 or x2 < 30:
            x2c*=-1
    if y2 > display_height-30 or y2 < 30:  ################
            y2c*=-1  

    pg.display.update()
    clock.tick(60)

if net != 3:
    s.close()     
pg.quit()
quit()
