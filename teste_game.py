def speed(BALL_SPEED):
		if BALL_SPEED == [13,13]:
			 #img = load_image("cold_ball.gif")
			img = 'spped 1'
		if BALL_SPEED == [15,15]:
			#img = load_image("ball.gif")
			img = 'spped 2'
		if BALL_SPEED == [17,17]:
			#img = load_image("dark_ball.gif")
			img = 'spped 3'
		if BALL_SPEED == [20,20]:
			#img = load_image("light_ball.gif")
			img = 'spped 4'
		if BALL_SPEED == [25,25]:
			#img = load_image("fire_ball.gif")
			img = 'spped 5'
		return img


print speed([13,13])


