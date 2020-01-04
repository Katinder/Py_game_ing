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
x=250
y=370
width=64
height=128
vel=5

isJump=False
jumpCount=10
left=False
right=False
walkCount=0

def  redrawGameWin():
	global walkCount

	#win.fill((0,0,0)) #black bg color

	win.blit(bg, (0,0)) #restore bg

	if walkCount+1>=30:
		walkCount=0

	if left:
		win.blit(walkLeft[walkCount//3],(x,y))
		walkCount+=1

	elif right:
		win.blit(walkRight[walkCount//3],(x,y))
		walkCount+=1

	else:
		win.blit(idle,(x,y))

	#pygame.draw.rect(win,(255,150,0),(x,y,width,height))
	pygame.display.update()



# main
run=True
while run:

	#pygame.time.delay(50)
	clock.tick(60)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False

	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x>vel:
		x = x-vel
		left=True
		right=False
		# if x<0:
		# 	x=0

	elif keys[pygame.K_RIGHT] and x< screen_width-width-vel:
		x= x+vel
		left=False
		right=True
		# if x>500-width:
		# 	x=500-width

	else:
		right=False
		left=False
		walkCount=0

	if not(isJump):

		# if keys[pygame.K_UP] and y>vel:
		# 	y= y-vel
		# 	# if y<0:
		# 	# 	y=0

		# if keys[pygame.K_DOWN] and y< screen_height-height-vel:
		# 	y= y+vel
		# 	# if y>500-height:
		# 	# 	y=500-height
		if keys[pygame.K_UP]:
			left=False
			right=False
			walkCount=0
			isJump=True

	else:
		if jumpCount>=-10:
			neg=1
			if jumpCount<0:
				neg=-1
			y=y- (jumpCount**2)*0.5*neg
			jumpCount=jumpCount-1
			print(f'jc= {jumpCount}, y = {y}')

		else:
			isJump=False
			jumpCount=10

	redrawGameWin()


pygame.quit()