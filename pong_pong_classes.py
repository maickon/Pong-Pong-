# -*- coding: utf-8 -*-

import sys, pygame, os
from pygame.locals import*

pygame.init()

width = 800
height = 680
font = pygame.font.Font(None,35)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue  = (0,0,255)
red   = (255, 0,0)
gray  = (128,128,128)
black = (0,0,0)


class  Barra(pygame.sprite.Sprite):
	def __init__(self,startpos):
		pygame.sprite.Sprite.__init__(self)
		self.direction = 1
		self.image, self.rect = load_image("barra_horizontal.jpg")
		self.rect.centerx = startpos[1]
		self.rect.centery = startpos[1]

	def update(self):
		self.rect.move_ip((self.direction*16,0))
		#Este if e elif verifica quando a barra colide com o lado direito e esquerdo da tela		
		if self.rect.left < 0:
			self.direction = 1
		elif self.rect.right > width:
			self.direction = -1


class Bola(pygame.sprite.Sprite):
# NA CLASSE BOLA EU COLOQUEI UM ATRIBUTO CHAMADO pt (LINHA 47)
# QUANDO UMA BOLA E CRIADA ESTE ATRIBUTO SE INICIALIZA COM 0, OU SEJA 0 PONTOS
# POREM A PROPRIA CLASSE BOLA ATUALIZA A POSIÇAO DA BOLA QUANDO A BARRA NAO A REBATE 
# DESSA FORMA TODA VEZ QUE A POSIÇAO DA BOLA FOR REINICIADA, SUA PONTUAÇAO ZERA
# pygame.time.wait(300) SIGNIFICA QUE O PROGRAMA VAI PARAR POR ALGUNS SEGUNDOS
	def __init__(self,startpos,pt,textLose,BALL_SPEED,textNivel):
		pygame.sprite.Sprite.__init__(self)
		self.speed = BALL_SPEED
		self.carregar_img(BALL_SPEED)
		self.rect.centerx = startpos[1]
		self.rect.centery = startpos[1]
		self.init_pos = startpos
		self.pt = 0
		self.textLose = ''
		self.textNivel = textNivel
		

	def carregar_img(self,BALL_SPEED):
		if BALL_SPEED == [13,13]:
			img = self.image,self.rect = load_image("cold_ball.gif")
		if BALL_SPEED == [15,15]:
			img = self.image,self.rect = load_image("ball.gif")
		if BALL_SPEED == [17,17]:
			img = self.image,self.rect = load_image("dark_ball.gif")
		if BALL_SPEED == [20,20]:
			img = self.image,self.rect = load_image("light_ball.gif")
		if BALL_SPEED == [25,25]:
			img = self.image,self.rect = load_image("fire_ball.gif")	
		return img
	"""
		def speed(self,BALL_SPEED = [13,13]):
			if BALL_SPEED == [13,13]:
				 img = load_image("cold_ball.gif")
			if BALL_SPEED == [15,15]:
				img = load_image("ball.gif")
			if BALL_SPEED == [17,17]:
				img = load_image("dark_ball.gif")
			if BALL_SPEED == [20,20]:
				img = load_image("light_ball.gif")
			if BALL_SPEED == [25,25]:
				img = load_image("fire_ball.gif")
			return img
	
	"""	


	def update(self):
		self.rect.move_ip(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]	
		if self.rect.top < 0:
			self.speed[1] =  -self.speed[1]
		if self.rect.bottom > height:
			self.pt = 0
			pygame.time.wait(1000)
			self.textLose = font.render("YOU LOSE",True,red)	
			self.rect.centerx = self.init_pos[1]
			self.rect.centery = self.init_pos[1]



def load_image(name):
	fullname = os.path.join("images",name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error,message:
		print "Nao carregou a imagem !",fullname
		raise SystemExit,message
	return image, image.get_rect()




