import pygame
pygame.init()


win=pygame.display.set_mode((500,500))

pygame.display.set_caption("Game2: Kinja")

walkRight=[pygame.transform.scale(pygame.image.load("R"+str(x)+".png"),(64,128)) for x in range(1,11)]
walkLeft=[pygame.transform.scale(pygame.image.load("L"+str(x)+".png"),(64,128)) for x in range(1,11)]
idle=pygame.transform.scale(pygame.image.load('standing.png'),(64,128))
bg=pygame.transform.scale(pygame.image.load('bg.png'),(500,500))

clock=pygame.time.Clock()

screen_width=500
screen_height=500


class player(object):

	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.vel=5
		self.isJump=False
		self.left=False
		self.right=False
		self.walkCount=0
		self.jumpCount=10
		self.idle=True


	def draw(self,win):

		if self.walkCount+1>=30:
			self.walkCount=0

		if not(self.idle):
			if self.left:
				win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1

			elif self.right:
				win.blit(walkRight[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1

		else:
			if self.right:
				win.blit(walkRight[0],(self.x,self.y))

			else:
				win.blit(walkLeft[0],(self.x,self.y))



class projectile(object):
	def __init__(self,x,y,radius,color,facing):
		self.x=x
		self.y=y
		self.radius=radius
		self.facing=facing
		self.vel=8*facing

	def draw(win):
		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius,1) #1==filled in circle


def  redrawGameWin():
	
	#global walkCount
	#win.fill((0,0,0)) #black bg color

	win.blit(bg, (0,0)) #restore bg

	p1.draw(win)
	#pygame.draw.rect(win,(255,150,0),(x,y,width,height))
	pygame.display.update()



# main
blades=[]
p1=player(x=250,y=370,width=64,height=128)
run=True
while run:

	#pygame.time.delay(50)
	clock.tick(60)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False

	for blade in blades:
		if blade.x<500 and blade.x>0:
			blade.x += blade.vel
		else:
			

	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and p1.x>p1.vel:
		p1.x = p1.x-p1.vel
		p1.left=True
		p1.right=False
		p1.idle=False
		# if x<0:
		# 	x=0

	elif keys[pygame.K_RIGHT] and p1.x< screen_width-p1.width-p1.vel:
		p1.x= p1.x+p1.vel
		p1.left=False
		p1.right=True
		p1.idle=False
		# if x>500-width:
		# 	x=500-width

	else:
		# p1.right=False
		# p1.left=False
		p1.walkCount=0
		p1.idle=True

	if not(p1.isJump):

		# if keys[pygame.K_UP] and y>vel:
		# 	y= y-vel
		# 	# if y<0:
		# 	# 	y=0

		# if keys[pygame.K_DOWN] and y< screen_height-height-vel:
		# 	y= y+vel
		# 	# if y>500-height:
		# 	# 	y=500-height
		if keys[pygame.K_UP]:
			# p1.left=False
			# p1.right=False
			p1.walkCount=0
			p1.isJump=True

	else:
		if p1.jumpCount>=-10:
			neg=1
			if p1.jumpCount<0:
				neg=-1
			p1.y=p1.y- (p1.jumpCount**2)*0.5*neg
			p1.jumpCount=p1.jumpCount-1
			print(f'jc= {p1.jumpCount}, y = {p1.y}')

		else:
			p1.isJump=False
			p1.jumpCount=10

	redrawGameWin()


pygame.quit()