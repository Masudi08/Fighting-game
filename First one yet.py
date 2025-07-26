import pygame
import random
import time
pygame.init()
win=pygame.display.set_mode((1280,720))
pygame.display.set_caption("NO HARD FEELINGS😁😁")
pygame.mixer.music.load("pedal_point_loop.mp3")
bg_Front=pygame.image.load("FRONT.png").convert_alpha()
bg_front=pygame.transform.scale(bg_Front,(1280,720))
walkright=[pygame.image.load("BattingGirl_Walk1.png").convert_alpha(),pygame.image.load("BattingGirl_Walk2.png").convert_alpha(),pygame.image.load("BattingGirl_Walk3.png").convert_alpha(),pygame.image.load("BattingGirl_Walk4.png").convert_alpha(),pygame.image.load("BattingGirl_Walk5.png").convert_alpha(),pygame.image.load("BattingGirl_Walk6.png").convert_alpha()]
walkleft=[pygame.transform.flip(frame,True,False)for frame in walkright]
standright=pygame.image.load("BattingGirl_idle1.png")
standleft=pygame.transform.flip(standright,True,False)
jumpright=[pygame.image.load("BattingGirl_Jump1.png"),pygame.image.load("BattingGirl_Jump2.png"),pygame.image.load("BattingGirl_Jump3.png"),pygame.image.load("BattingGirl_Jump4.png"),pygame.image.load("BattingGirl_Jump5.png"),pygame.image.load("BattingGirl_Jump6.png"),pygame.image.load("BattingGirl_Jump7.png"),pygame.image.load("BattingGirl_Jump8.png")]
jumpleft=[pygame.transform.flip(frame,True,False) for frame in jumpright]
punchright=[pygame.image.load("BattingGirl_attack03.png"),pygame.image.load("BattingGirl_attack01.png"),pygame.image.load("BattingGirl_attack02.png"),pygame.image.load("BattingGirl_attack03.png"),pygame.image.load("BattingGirl_attack04.png"),pygame.image.load("BattingGirl_attack05.png"),pygame.image.load("BattingGirl_attack06.png"),pygame.image.load("BattingGirl_attack07.png"),pygame.image.load("BattingGirl_attack08.png")]
punchleft=[pygame.transform.flip(frame,True,False) for frame in punchright]
kickright=[pygame.image.load("BattingGirl_attack09.png"),pygame.image.load("BattingGirl_attack10.png"),pygame.image.load("BattingGirl_attack11.png"),pygame.image.load("BattingGirl_attack12.png"),pygame.image.load("BattingGirl_attack13.png"),pygame.image.load("BattingGirl_attack14.png")]
kickleft=[pygame.transform.flip(frame,True,False) for frame in kickright]
batright=[pygame.image.load("BattingGirl_attack15.png"),pygame.image.load("BattingGirl_attack16.png"),pygame.image.load("BattingGirl_attack17.png"),pygame.image.load("BattingGirl_attack18.png"),pygame.image.load("BattingGirl_attack19.png"),pygame.image.load("BattingGirl_attack20.png"),pygame.image.load("BattingGirl_attack21.png"),pygame.image.load("BattingGirl_attack22.png"),pygame.image.load("BattingGirl_attack23.png"),pygame.image.load("BattingGirl_attack24.png"),pygame.image.load("BattingGirl_attack25.png")]
batleft=[pygame.transform.flip(frame,True,False) for frame in batright]
bg_Back=pygame.image.load("BACK.png").convert_alpha()
bg_back=pygame.transform.scale(bg_Back,(1280,720))
bg_Middle=pygame.image.load("MIDDLE.png").convert_alpha()
bg_middle=pygame.transform.scale(bg_Middle,(1280,720))
bg_Light=pygame.image.load("LIGHT.png").convert_alpha()
bg_light=pygame.transform.scale(bg_Light,(1280,720))

class Fighter:
    def __init__(self,x,y,vel):
        self.x=x
        self.y=y
        self.vel=vel
        self.walkcount=0
        self.left=False
        self.right=False
        self.facing="right"
        self.jumpcount=10
        self.jump=False
        self.jumpingcount=0
        self.start_jump=y
        self.punch=False
        self.punchcount=0
        self.kick=False
        self.kickcount=0
        self.bat=False
        self.battingtime=0
        self.battingcount=0
        self.hit=False
        self.hitboxright=[self.x+25,self.y+23,30,70]
        self.hitboxleft=[self.x+40,self.y+23,30,70]
    def draw(self):
        if self.facing=='right':
            pygame.draw.rect(win,(255,255,255),(self.x+25,self.y+23,30,70))
        else:
            pygame.draw.rect(win,(255,255,255),(self.x+40,self.y+23,30,70))
        if self.jumpingcount>=32:
                self.jumpingcount=0
        if self.walkcount>=24:
            self.walkcount=0
        if self.kickcount>=18:
            self.kickcount=0
        if self.punchcount>=18:
            self.punchcount=0
        if self.battingcount>=44:
            self.battingcount=0
        elif self.punch==True and self.facing=="right":
            win.blit(punchright[self.punchcount//3],(self.x,self.y))
            if  enemy.x-self.hitboxright[0]-10+self.hitboxright[2]<70 and self.punch==True:
                self.hitboxright[0]=enemy.hitbox[0]
            self.punchcount+=1
        elif self.punch==True and self.facing=="left":
            win.blit(punchleft[self.punchcount//3],(self.x,self.y))
            if self.x-enemy.x+enemy.hitbox[2]<70 and self.punch==True:
                self.hitboxleft[0]=enemy.hitbox[0]+enemy.hitbox[2]
            self.punchcount+=1
        elif self.kick==True and self.facing=="right":
            win.blit(kickright[self.kickcount//3],(self.x,self.y))
            if enemy.x-self.hitboxright[0]-10+self.hitboxright[2]<70 and self.kick==True:
                self.hitboxright[0]=enemy.hitbox[0]
            self.kickcount+=1
        elif self.kick==True and self.facing=="left":
            win.blit(kickleft[self.kickcount//3],(self.x,self.y))
            if self.x-enemy.x+enemy.hitbox[2]<70 and self.kick==True:
                self.hitboxleft[0]=enemy.hitbox[0]+enemy.hitbox[2]
            self.kickcount+=1
        elif self.bat==True and self.facing=="right":
            win.blit(batright[self.battingcount//4],(self.x,self.y))
            if self.x+self.hitboxright[2]-enemy.x<70 and self.bat==True:
                while time.time()-fighter.battingtime>battingcooldown:
                    self.hitboxright[0]=enemy.hitbox[0]
                    fighter.battingtime=time.time()
                
            self.battingcount+=1
        elif self.bat==True and self.facing=="left":
            win.blit(batleft[self.battingcount//4],(self.x,self.y))
            if self.x-enemy.x+enemy.hitbox[2]<70 and self.bat==True:
                while time.time()-fighter.battingtime>battingcooldown:
                    self.hitboxleft[0]=enemy.hitbox[0]+enemy.hitbox[2]
                    fighter.battingtime=time.time()
                
            self.battingcount+=1
        elif self.left:
            win.blit(walkleft[self.walkcount//4],(self.x,self.y))
            self.walkcount+=1
        elif self.right:
            win.blit(walkright[self.walkcount//4],(self.x,self.y))
            self.walkcount+=1
        elif self.jump==True and self.facing=="right":
            win.blit(jumpright[self.jumpingcount//4],(self.x,self.y))    
            self.jumpingcount+=1
        elif self.jump==True and self.facing=="left":
            win.blit(jumpleft[self.jumpingcount//4],(self.x,self.y))
            self.jumpingcount+=1
        
        else:
            if self.facing=="right":
                win.blit(standright,(self.x,self.y))
            else:
                win.blit(standleft,(self.x,self.y))
            self.hitboxright[0]=self.x+25
            enemy.hitbox[0]=enemy.x
            self.hitboxleft[0]=self.x+40

enemy_Attackright=[pygame.image.load("Attack__000.png").convert_alpha(),pygame.image.load("Attack__001.png").convert_alpha(),pygame.image.load("Attack__002.png").convert_alpha(),pygame.image.load("Attack__003.png").convert_alpha(),pygame.image.load("Attack__004.png").convert_alpha(),pygame.image.load("Attack__005.png").convert_alpha(),pygame.image.load("Attack__006.png").convert_alpha(),pygame.image.load("Attack__007.png").convert_alpha(),pygame.image.load("Attack__008.png").convert_alpha(),pygame.image.load("Attack__009.png").convert_alpha()]
enemy_attackright=[pygame.transform.scale(frame,(50,70)) for frame in enemy_Attackright]
enemy_attackleft=[pygame.transform.flip(frame,True,False) for frame in enemy_attackright]
enemy_Idleright=[pygame.image.load("Idle__000.png").convert_alpha(),pygame.image.load("Idle__001.png").convert_alpha(),pygame.image.load("Idle__002.png").convert_alpha(),pygame.image.load("Idle__003.png").convert_alpha(),pygame.image.load("Idle__004.png").convert_alpha(),pygame.image.load("Idle__005.png").convert_alpha(),pygame.image.load("Idle__006.png").convert_alpha(),pygame.image.load("Idle__007.png").convert_alpha(),pygame.image.load("Idle__008.png").convert_alpha(),pygame.image.load("Idle__009.png").convert_alpha()]
enemy_idleright=[pygame.transform.scale(frame,(50,70)) for frame in enemy_Idleright]
enemy_idleleft=[pygame.transform.flip(frame,True,False) for frame in enemy_idleright]
enemy_Run=[pygame.image.load("Run__000.png").convert_alpha(),pygame.image.load("Run__001.png").convert_alpha(),pygame.image.load("Run__002.png").convert_alpha(),pygame.image.load("Run__003.png").convert_alpha(),pygame.image.load("Run__004.png").convert_alpha(),pygame.image.load("Run__005.png").convert_alpha(),pygame.image.load("Run__006.png").convert_alpha(),pygame.image.load("Run__007.png").convert_alpha(),pygame.image.load("Run__008.png").convert_alpha(),pygame.image.load("Run__009.png").convert_alpha(),]
enemy_run=[pygame.transform.scale(frame,(30,70))for frame in enemy_Run]
enemy_runleft=[pygame.transform.flip(frame,True,False) for frame in enemy_run]
jumpAttack_right=[pygame.image.load("Jump_Attack__000.png").convert_alpha(),pygame.image.load("Jump_Attack__001.png").convert_alpha(),pygame.image.load("Jump_Attack__002.png").convert_alpha(),pygame.image.load("Jump_Attack__003.png").convert_alpha(),pygame.image.load("Jump_Attack__004.png").convert_alpha(),pygame.image.load("Jump_Attack__005.png").convert_alpha(),pygame.image.load("Jump_Attack__006.png").convert_alpha(),pygame.image.load("Jump_Attack__007.png").convert_alpha(),pygame.image.load("Jump_Attack__008.png").convert_alpha(),pygame.image.load("Jump_Attack__009.png").convert_alpha()]
jumpattack_right=[pygame.transform.scale(frame,(30,70))for frame in jumpAttack_right]
jumpattack_left=[pygame.transform.flip(frame,True,False)for frame in jumpattack_right]
class Enemy:
    def __init__(self,x,y,vel):
        self.y=y
        self.x=x
        self.vel=vel
        self.attack=False
        self.attack_count=0
        self.idle=True
        self.idlecount=0
        self.facing="right"
        self.run=False
        self.runcount=0
        self.jumpattack=False
        self.jumpcount=10
        self.jumpattackcount=0
        self.startjump=self.y
        self.currentattack=None
        self.attacktime=0
        self.isjumping=False
        self.hit=False
        self.health=20
        self.hitbox=[self.x,self.y,45,70]
    

    def draw_enemy(self):
        pygame.draw.rect(win,(255,255,255),(self.x,self.y,45,70))
        if self.attack_count>=40:
            self.attack=False
            self.currentattack=None
            self.attack_count=0
        if self.idlecount>=40:
            self.idlecount=0
        if self.runcount>=40:
            self.runcount=0
        if self.jumpattackcount>=40:
            self.jumpattack=False
            self.isjumping=False
            self.currentattack=None
            self.y=self.startjump
            self.jumpattackcount=0

        if self.attack==True and self.facing=="right":
            win.blit(enemy_attackright[self.attack_count//4],(self.x,self.y))
            self.attack_count+=1
        elif self.attack==True and self.facing=="left":
            win.blit(enemy_attackleft[self.attack_count//4],(self.x,self.y))
            self.attack_count+=1
        elif self.jumpattack==True and self.facing=="right":
            self.jump()
            win.blit(jumpattack_right[self.jumpattackcount//4],(self.x,self.y))
            self.jumpattackcount+=1
        elif self.jumpattack==True and self.facing=="left":
            self.jump()
            win.blit(jumpattack_left[self.jumpattackcount//4],(self.x,self.y))
            self.jumpattackcount+=1
        elif self.run==True and self.facing=="right":
            win.blit(enemy_run[self.runcount//4],(self.x,self.y)) 
            self.runcount+=1
        elif self.run==True and self.facing=="left":
            win.blit(enemy_runleft[self.runcount//4],(self.x,self.y)) 
            self.runcount+=1
        else:
            if self.idle==True and self.facing=="right":
                win.blit(enemy_idleright[self.idlecount//4],(self.x,self.y))
                self.idlecount+=1
            elif self.idle==True and self.facing=="left":
                win.blit(enemy_idleleft[self.idlecount//4],(self.x,self.y))  
                self.idlecount+=1
    def jump(self):
        if self.isjumping==True:
            if self.jumpcount>-10:
                neg=1
                if self.jumpcount<1:
                    neg=-1
                self.y-=(enemy.jumpcount**2*0.5)*neg
                self.jumpcount-=1
            else:
                self.jumpcount=10
                self.y=enemy.startjump
        

    


running=True
def update_display():
    win.blit(bg_back,(0,0))
    win.blit(bg_middle,(0,0))
    win.blit(bg_front,(0,0)) 
    win.blit(bg_light,(0,0))
    fighter.draw()
    enemy.draw_enemy()
    pygame.display.update()
clock=pygame.time.Clock()  
fighter=Fighter(50,620,3)
enemy=Enemy(800,645,1)
pygame.mixer.music.play(-1)
attackcooldown=2
battingcooldown=2
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    key=pygame.key.get_pressed()

    if key[pygame.K_a] :
        fighter.left=True
        fighter.right=False
        fighter.facing="left"
        if fighter.x>fighter.vel:
            fighter.x-=fighter.vel
            if key[pygame.K_RSHIFT]:
                fighter.x-=6
    elif key[pygame.K_d]:
        fighter.right=True
        fighter.left=False
        fighter.facing="right"
        if fighter.x<1280-fighter.vel-walkright[0].get_width():
            fighter.x+=fighter.vel
            if key[pygame.K_RSHIFT]:
                fighter.x+=6
    else:
        fighter.left=False
        fighter.right=False


    if key[pygame.K_SPACE] and not fighter.jump:
        fighter.left=False
        fighter.right=False
        fighter.jump=True
    
    if fighter.jump==True:
        if fighter.jumpcount>-10:
            neg=1
            if fighter.jumpcount<0:
                neg=-1
            fighter.y-=(fighter.jumpcount**2//2)*neg
            fighter.jumpcount-=1
        else:
            fighter.y=fighter.start_jump
            fighter.jumpingcount=0
            fighter.jumpcount=10
            fighter.jump=False 
    if key[pygame.K_p]:
        fighter.punch=True
    elif key[pygame.K_k]:
        fighter.kick=True
    elif key[pygame.K_o]:
        while time.time()-fighter.battingtime>battingcooldown:
            fighter.bat=True
            fighter.battingtime=time.time()
    else:
        fighter.punch=False
        fighter.kick=False
        fighter.bat=False 

    if fighter.facing=="right" and fighter.x+fighter.hitboxright[2]-enemy.x<40:
        if fighter.hitboxright[0]==enemy.hitbox[0]:
            print('Hit')
            enemy.health-=1
            enemy.hit=True
    elif fighter.facing=="left" and fighter.hitboxleft[0]==enemy.hitbox[0]+enemy.hitbox[2]:
        print("hit")
        enemy.health-=1
        enemy.hit=True
    else:
        enemy.hit=False

   
    enemy.attack = False
    enemy.run = False
    enemy.idle = False
    enemy.jumpattack = False

    distance_x = abs(fighter.x - enemy.x)
  
    if fighter.x < enemy.x:
        enemy.facing = "left"
    else:
        enemy.facing = "right"

    attack_range = 70 
    if enemy.currentattack==None:
        if distance_x < attack_range and time.time()-enemy.attacktime>attackcooldown:
            enemy.currentattack=random.choice(["normal","jumpattack"])
            if enemy.currentattack=="normal":
                enemy.attack=True
                enemy.attackcount=0
            elif enemy.currentattack=="jumpattack":
                enemy.jumpattack=True
                enemy.jumpattackcount=0
                enemy.isjumping=True
            enemy.attacktime=time.time()
            enemy.idle=False
            enemy.run=False
        elif distance_x > 70: 
            enemy.run = True
            if fighter.x < enemy.x:
                enemy.x -= enemy.vel
            else:
                enemy.x += enemy.vel
        else: 
            enemy.idle = True
        
    else:
        if enemy.currentattack=="normal":
            enemy.attack=True
        if enemy.currentattack=="jumpattack":
            enemy.jumpattack=True
    update_display()
pygame.quit()