# -*- coding: utf-8 -*-

import sys, pygame, os
from pygame.locals import*
from menu import *
from pong_pong_classes import *



class Tela():

	def minha_tela(self,width = 800,height = 680):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Pong Pong!")

		img = pygame.image.load("index.gif")
		img = pygame.transform.scale(img,(width,height))
		
		imgPosition = (0,30)
		grupo = "Maickon e Clarisse"
		menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
               [('Start Game', 1, None),
                ('Top Score',2, None),
                ('Modo',3, None),
				('Sobre',4, None),
                ('Exit',5, None)])
		menu.set_center(True, True)
		menu.set_alignment('center', 'center')
		state = 0
		prev_state = 1
		rect_list = []
		screen.blit(img,imgPosition)
		pygame.event.set_blocked(pygame.MOUSEMOTION)
		while 1:
			
			integrantes = font.render("Integrantes: %s" %(grupo),True,red)
			if prev_state != state:
				pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
				prev_state = state
			e = pygame.event.wait()
			
			if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
				if state == 0:
					rect_list, state = menu.update(e, state)
				elif state == 1:
					tela = Tela()
					tela.game()
					state = 0
				elif state == 2:
					tela = Tela()
					tela.score_geral()
					state = 0
				elif state == 3:
					tela = Tela()
					tela.option()
					state = 0
				elif state == 4:
					tela = Tela()
					print "sobre"
					state = 0
				else:
					print 'Exit!'
					pygame.quit()
					sys.exit()

			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			screen.blit(integrantes, [20,20])	
			pygame.display.update(rect_list)
			pygame.display.flip()
			

	def game(self,BALL_SPEED = [13,13],TEXT_NIVEL = "NIVEL: Facil",fase_nome = "Fase 1",fase_backgraund = "fase_extra_spaco_2.png",fase = 1,pts = 0):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("PONG PONG")
		font = pygame.font.Font(None,35)
		ball = Bola([80,80],pts,'Lose',BALL_SPEED,TEXT_NIVEL)
		barra_1 = Barra([150,650])

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						barra_1.direction = -1
					if event.key == pygame.K_RIGHT:
						barra_1.direction = 1
		

			if barra_1.rect.colliderect(ball.rect): 		
	# AQUI O ATRIBUTO pt DA CLASSE BOLA AUMENTA EM MAIS 1 TODA VEZ QUE ELA FOR REBATIDA
				ball.pt = ball.pt+100
				if ball.pt >= 500 and fase == 1:#fase 2
					tela = Tela()
					tela.gerenciador_de_fases(1)
				elif ball.pt > 600 and fase == 2:#fase 3
					tela = Tela()
					tela.gerenciador_de_fases(2)
				elif ball.pt > 700 and fase == 3:#fase 4
					tela = Tela()
					tela.gerenciador_de_fases(3)
				elif ball.pt > 800 and fase == 4:#fase 5
					tela = Tela()
					tela.gerenciador_de_fases(4)
				elif ball.pt > 900 and fase == 5:#fase 6
					tela = Tela()
					tela.gerenciador_de_fases(5)
				elif ball.pt > 1000 and fase == 6:#fase 7
					tela = Tela()
					tela.gerenciador_de_fases(6)
				elif ball.pt > 1200 and fase == 7:#fase 8
					tela = Tela()
					tela.gerenciador_de_fases(7)
				elif ball.pt > 1400 and fase == 8:#fase 9
					tela = Tela()
					tela.gerenciador_de_fases(8)
				elif ball.pt > 1600 and fase == 9:#fase 10
					tela = Tela()
					tela.gerenciador_de_fases(9)
				elif ball.pt > 1800 and fase == 10:#fase 11
					tela = Tela()
					tela.gerenciador_de_fases(10)
				elif ball.pt > 2000 and fase == 11:#fase 12
					tela = Tela()
					tela.gerenciador_de_fases(11)
				elif ball.pt > 3000 and fase == 12:#fase 13
					tela = Tela()
					tela.gerenciador_de_fases(12)
				elif ball.pt > 1500 and fase == 13:#fase extra 1
					tela = Tela()
					tela.gerenciador_de_fases(13)
				elif ball.pt > 3000 and fase == 14:#fase extra 2
					tela = Tela()
					tela.gerenciador_de_fases(14)
				elif ball.pt > 4500 and fase == 15:#fase extra 3
					tela = Tela()
					tela.gerenciador_de_fases(15)
				elif ball.pt > 6000 and fase == 16:#fase extra 4
					tela = Tela()
					tela.gerenciador_de_fases(16)
				elif ball.pt > 7500 and fase == 17:#fase extra 5
					tela = Tela()
					tela.gerenciador_de_fases(17)
				elif ball.pt > 10000 and fase == 18:#fase extra aquario
					tela = Tela()
					tela.gerenciador_de_fases(18)

				if ball.speed[1] > 0:
					ball.speed[1] = -ball.speed[1]

	# CONFIGURA A PONTUAÇAO PARA APARECER NA TELA           		
			textScore = font.render("Score: %d" %(ball.pt),True,white)
			textNivel = font.render("%s" %(ball.textNivel),True,white)
			textFase  = font.render("%s" %(fase_nome),True,white)
			ball.update()
			barra_1.update()
		
			img = pygame.image.load(fase_backgraund)
			img = pygame.transform.scale(img,(width,height))
		
			imgPosition = (0,0)
			screen.blit(ball.image, ball.rect)
			screen.blit(barra_1.image, barra_1.rect)
	# screen.blit(textScore, [20,20])	O BLIT COLOCA O QUE ESTA DENTRO DE textScore NA TELA POSICIONADO NA 
	# POSIÇAO 20,20 DENTRO DA TELA VERDE
			screen.blit(textScore, [20,20])	
			screen.blit(textNivel, [200,20])
			screen.blit(textFase, [620,20])
	
			if ball.textLose != '':
				screen.blit(ball.textLose, [400,340])	
				score_total = open("score_geral","w")
				score_total.write("Melhor pontuação: %i ponts"%(GRAVA_PTS)) 				
				score_total.close()							
				tela = Tela()
				tela.tela_lose()
			
			pygame.display.flip()
			screen.blit(img,imgPosition)

	def tela_lose(self):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("You Lose!")
		img = pygame.image.load("lose.gif")
		img = pygame.transform.scale(img,(width,height))
		lose = "VOCE PERDEU !"
		voltar = "Aperte qualquer tecla para retornar ao menu principal..."
				
		imgPosition = (0,0)
		screen.blit(img,imgPosition)
		lose_msg = font.render("%s" %(lose),True,red)
		volta = font.render("%s" %(voltar),True,red)
		for event in pygame.event.get():
	
			if event.type == pygame.K_KP_ENTER or pygame.K_BACKSPACE:
				tela = Tela()
				tela.minha_tela()
		
		screen.blit(volta, [80,250])
		screen.blit(lose_msg, [320,290])
		pygame.display.flip()
		

	def score_geral(self):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Melhor pontuacao!")
		img = pygame.image.load("lose.gif")
		img = pygame.transform.scale(img,(width,height))
		
		arq_score = open("score_geral")
		lido = arq_score.read() 							
		record = "Top Recordes !"
				
		imgPosition = (0,0)
		screen.blit(img,imgPosition)
		record_msg = font.render("%s" %(record),True,red)
		arq_lido = font.render("%s" %(lido),True,red)
		for event in pygame.event.get():
	
			if event.type == pygame.K_KP_ENTER or pygame.K_BACKSPACE:
				tela = Tela()
				tela.minha_tela()
		
		screen.blit(arq_lido, [20,20])
		screen.blit(record_msg, [20,60])
		pygame.display.flip()

	def option(self,width = 800,height = 680):
		screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Dificuldade!")
		img = pygame.image.load("index.gif")
		img = pygame.transform.scale(img,(width,height))
		
		imgPosition = (0,30)

		opcoes = "Escolha um modo de jogo..."
		menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
               [('Facil',1, None),
                ('Normal',2, None),
                ('Desafiador',3, None),
                ('Dificil',4, None),
				('Epico',5, None),
				('Voltar',6, None),])
		menu.set_center(True, True)
		menu.set_alignment('center', 'center')
		state = 0
		prev_state = 1
		rect_list = []
		screen.blit(img,imgPosition)
		pygame.event.set_blocked(pygame.MOUSEMOTION)
		while 1:
			dificuldade = font.render("%s" %(opcoes),True,red)
			if prev_state != state:
				pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
				prev_state = state
			e = pygame.event.wait()

			if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
				if state == 0:
					rect_list, state = menu.update(e, state)
				elif state == 1:
					game_lento = Tela()
					game_lento.game([13,13],"NIVEL: Facil",fase = 0)
					state = 0				
				elif state == 2:
					game_lento = Tela()
					game_lento.game([15,15],"NIVEL: Normal",fase = 0)
					state = 0
				elif state == 3:
					game_lento = Tela()
					game_lento.game([17,17],"NIVEL: Desafiador",fase = 0)
					state = 0
				elif state == 4:
					game_lento = Tela()
					game_lento.game([20,20],"NIVEL: Dificil",fase = 0)
					state = 0
				elif state == 5:
					game_lento = Tela()
					game_lento.game([25,25],"NIVEL: Epico (sem chance ! rsrs)",fase = 0)
					state = 0
				elif state == 6:
					tela = Tela()
					tela.minha_tela()
					state = 0
				else:
					print 'Exit!'
					pygame.quit()
					sys.exit()

			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			screen.blit(dificuldade, [20,20])	
			pygame.display.update(rect_list)
			pygame.display.flip()
	
	def gerenciador_de_fases(self,fase):
		if fase == 1:
			pygame.time.wait(1000)
			fase_2 = Tela()
			fase_2.game([13,13],"NIVEL: Facil","Fase 2","fase_1.png",fase = 2)		

		elif fase == 2:			
			pygame.time.wait(1000)
			fase_3 = Tela()
			fase_3.game([13,13],"NIVEL: Facil","Fase 3","fase_2.png",fase = 3)

		elif fase == 3:			
			pygame.time.wait(1000)
			fase_4 = Tela()
			fase_4.game([15,15],"NIVEL: Normal","Fase 4","fase_3.png",fase = 4)

		elif fase == 4:
			pygame.time.wait(1000)
			fase_5 = Tela()
			fase_5.game([15,15],"NIVEL: Normal","Fase 5","fase_4.png",fase = 5)

		elif fase == 5:
			pygame.time.wait(1000)
			fase_6 = Tela()
			fase_6.game([15,15],"NIVEL: Normal","Fase 6","fase_5.png",fase = 6)		

		elif fase == 6:
			pygame.time.wait(1000)
			fase_7 = Tela()
			fase_7.game([17,17],"NIVEL: Desafiador","Fase 7","fase_6.png",fase = 7)

		elif fase == 7:
			pygame.time.wait(1000)
			fase_8 = Tela()
			fase_8.game([17,17],"NIVEL: Desafiador","Fase 8","fase_7.png",fase = 8)

		elif fase == 8:
			pygame.time.wait(1000)
			fase_9 = Tela()
			fase_9.game([17,17],"NIVEL: Desafiador","Fase 9","fase_8.png",fase = 9)

		elif fase == 9:
			pygame.time.wait(1000)
			fase_10 = Tela()
			fase_10.game([17,17],"NIVEL: Desafiador","Fase 10","fase_9.png",fase = 10)		

		elif fase == 10:
			pygame.time.wait(1000)
			fase_11 = Tela()
			fase_11.game([20,20],"NIVEL: Dificil","Fase 11","fase_10.png",fase = 11)

		elif fase == 11:
			pygame.time.wait(1000)
			fase_12 = Tela()
			fase_12.game([20,20],"NIVEL: Dificil","Fase 12","fase_12.gif",fase = 12)

		elif fase == 12:
			pygame.time.wait(1000)
			fase_13 = Tela()
			fase_13.game([25,25],"NIVEL: Epico","Penultima Fase","fase_13.gif",fase = 13)

		elif fase == 13:
			pygame.time.wait(1000)
			fase_14 = Tela()	
			fase_14.game([25,25],"NIVEL: Epico","Ultima Fase","fase_14.gif",fase = 14)

		elif fase == 14:
			pygame.time.wait(1000)			
			fase_15 = Tela()
			fase_15.game([20,20],"NIVEL: Dificil","Fase Extra 1","bg_fase_extra_1.gif",fase = 15)		

		elif fase == 15:
			pygame.time.wait(1000)
			fase_16 = Tela()
			fase_16.game([20,20],"NIVEL: Dificil","Fase Extra 2","bg_fase_extra_2.gif",fase = 16)

		elif fase == 16:
			pygame.time.wait(1000)
			fase_17 = Tela()
			fase_17.game([25,25],"NIVEL: Epico","Fase Extra 3","bg_fase_extra_3.gif",fase = 17)

		elif fase == 17:
			pygame.time.wait(1000)
			fase_18 = Tela()
			fase_18.game([25,25],"NIVEL: Epico","Fase Extra 4","bg_fase_extra_4.gif",fase = 18)

		elif fase == 18:		
			pygame.time.wait(1000)
			fase_19 = Tela()
			fase_19.game([25,25],"NIVEL: Epico","Fase Extra 5","bg_fase_extra_5.gif",fase = 19)


def main():
	tela = Tela()
	tela.minha_tela()
	
	

if __name__ == "__main__":
	main()
