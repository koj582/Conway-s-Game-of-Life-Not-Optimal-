import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()
running = True
taille = 10
compteur = 0
font2 = pygame.font.SysFont('didot.ttc', 40)
img2 = font2.render('Clicgauche:placer ; Clicdroit:effacer ; a:commencer ; z:arrêter ; espace:toutenlever ; flèches:cases ', True, (62, 237, 232))

color1 = (128,122,122)
color2 = (209,207,207)

cellules = [ [0,0,color1,0] for i in range(1001000)]


ecart = 66
ok2 = 0   
adjacent = 0
pos_x = 0
pos_y = 0         

commence = 0
while running:
    #pour quitter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('grey')

   
    #zoom 
    ok3 = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        taille = taille + 1
        
    if keys[pygame.K_UP]:
        taille = taille - 1
        
   
    

    gauche, milieu, droite = pygame.mouse.get_pressed()
    
   
    
    #mise en place des carrés
    
    
    i = 0
    for x in range (0, 1280, 11):   
        for y in range(0,720, 11):
            
            
            cellules[i][0] = x 
            cellules[i][1] = y 
            
            pygame.draw.rect(screen, cellules[i][2] , (x, y, taille, taille))
            i += 1
    ok = 0
    if gauche:
        a, o = pygame.mouse.get_pos() 
        for i in range(0,len(cellules)):
            if cellules[i][0] > a  and cellules[i][1] > o  and ok == 0 :
                cellules[i - ecart - 1][2] = color2
                ok = 1
                
              
    if droite:
        a, o = pygame.mouse.get_pos() 
        for i in range(0,len(cellules)):
            if cellules[i][0] > a  and cellules[i][1] > o  and ok == 0 :
                cellules[i - ecart - 1][2] = color1
                ok = 1
               

    if keys[pygame.K_SPACE]:
        for i in range(len(cellules)):
            if cellules[i][2] == color2:
                cellules[i][2] = color1
    if keys[pygame.K_a]:
        commence = 1
    if keys[pygame.K_z]:
        commence = 0
    if commence  == 1 :
        for i in range(100000):
                adjacent = 0
                if cellules[i + ecart][2] == color2 :
                    adjacent += 1
                if cellules[i - ecart ][2] == color2:
                    adjacent += 1
                if cellules[i + ecart - 1][2] == color2:
                    adjacent += 1
                if cellules[i + ecart + 1][2] == color2:
                    adjacent += 1
                if cellules[i - ecart  + 1][2] == color2:
                    adjacent += 1
                if cellules[i - ecart - 1][2] == color2:
                    adjacent += 1
                if cellules[i + 1][2] == color2:
                    adjacent += 1
                if cellules[i - 1][2] == color2:
                    adjacent += 1
                    
                
                
                cellules[i][3] = adjacent 
        for i in range(100000):
            if cellules[i][2] == color1:
                if cellules[i][3] == 3:
                    cellules[i][2] = color2
            if cellules[i][2] == color2:
                if cellules[i][3] != 2 and cellules[i][3] != 3:
                    cellules[i][2] = color1
        
    
    
    """for i in range (0, 1280, taille + 1 + taille //10):
       for j in range(0,720,taille+ 1 + taille // 10):
        
        color = 'white'
        carrx = i
        carry = j
        if gauche:
            x, y = pygame.mouse.get_pos() 
            
            if x > carrx :
                color = 'black'
                active[i] = i
        if i in active :
            color = 'black'
            

        pygame.draw.rect(screen, color , (carrx,carry, taille, taille))"""

    screen.blit(img2,(0,0))
    pygame.display.flip()
    clock.tick(200)
pygame.quit()