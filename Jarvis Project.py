import RPi.GPIO as GPIO
import sys, pygame, time, math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
freq = 100
pwm1 = GPIO.PWM(20, freq) #left
pwm2 = GPIO.PWM(21, freq) #right
dc = 30 
pwm1.start(dc)
pwm2.start(dc)
pygame.init()
size = width, height = 480, 300
screen = pygame.display.set_mode(size)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
freq1 = 70
pwm3 = GPIO.PWM(19, freq1)
pwm4 = GPIO.PWM(26, freq1)
dc1 = 100

def check(place):
	if place[0] >= 0 and place[0] < 210:
		if place[1] >= 0 and place[1] < 120:
			return 1
		if place[1] >= 120 and place[1] <= 180:
			return 2
		if place[1] > 180 and place[1] <= 300:
			return 3
	if place[0] >= 210 and place[0] <= 270:
		if place[1] >= 0 and place[1] < 120:
			return 4
		if place[1] >= 120 and place[1] <= 180:
			return 5
		if place[1] > 180 and place[1] <= 300:
			return 6
	if place[0] > 270 and place[0] < 480:
		if place[1] >= 0 and place[1] < 120:
			return 7
		if place[1] >= 120 and place[1] <= 180:
			return 8
		if place[1] > 180 and place[1] <= 300:
			return 9
	
		
def straight_short():
	pwm1.ChangeDutyCycle(90)
	pwm2.ChangeDutyCycle(76)
	time.sleep(3)

def straight_long():
	pwm1.ChangeDutyCycle(90)
	pwm2.ChangeDutyCycle(76)	
	time.sleep(6)

def circle(side):
	start = time.time()
	if side == 'right':
		pwm1.ChangeDutyCycle(90)
		pwm2.ChangeDutyCycle(50)
		pwm4.start(dc1)
		while (time.time() - start) < 7.7:
			pwm4.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm4.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm4.ChangeDutyCycle(0)
	elif side == 'left':
		pwm1.ChangeDutyCycle(50)
		pwm2.ChangeDutyCycle(96)
		pwm3.start(dc1)
		while (time.time() - start) < 8.1:
			pwm3.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm3.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm3.ChangeDutyCycle(0)
def uturn(side):
	straight_short()
	start = time.time()
	if side == 'right':
		pwm1.ChangeDutyCycle(78)
		pwm2.ChangeDutyCycle(40)
		pwm4.start(dc1)
		while (time.time() - start) < 5:
			pwm4.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm4.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm4.ChangeDutyCycle(0)
	elif side == 'left':
		pwm1.ChangeDutyCycle(40)
		pwm2.ChangeDutyCycle(91)
		pwm3.start(dc1)
		while (time.time() - start) < 4.5:
			pwm3.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm3.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm3.ChangeDutyCycle(0)
	straight_short()

def turn(side):
	straight_short()
	start = time.time()
	if side == 'right':
		pwm1.ChangeDutyCycle(85)
		pwm2.ChangeDutyCycle(32)
		pwm4.start(dc1)
		while (time.time() - start) < 2.2:
			pwm4.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm4.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm4.ChangeDutyCycle(0)
	elif side == 'left':
		pwm1.ChangeDutyCycle(30)
		pwm2.ChangeDutyCycle(91)
		pwm3.start(dc1)
		while (time.time() - start) < 1.9:
			pwm3.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm3.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm3.ChangeDutyCycle(0)
	straight_short()

def smooth_turn(side):
	start = time.time()
	if side == 'right':
		pwm1.ChangeDutyCycle(85)
		pwm2.ChangeDutyCycle(68)
		pwm4.start(dc1)
		while (time.time() - start) < 7:
			pwm4.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm4.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm4.ChangeDutyCycle(0)
	elif side == 'left':
		pwm1.ChangeDutyCycle(75)
		pwm2.ChangeDutyCycle(85)
		pwm3.start(dc1)
		while (time.time() - start) < 7:
			pwm3.ChangeDutyCycle(100)
			time.sleep(0.05)
			pwm3.ChangeDutyCycle(0)
			time.sleep(0.05)
		pwm3.ChangeDutyCycle(0)

def stop():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)


data = []
prev_time = time.time()
bgcolor = 0, 0, 0
linecolor = 255, 255, 255
linecolor1 = 65, 105, 225
pygame.mouse.set_pos(10, 140)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			x = pos[0]
			y = pos[1]
			now_time = time.time()
			place = check(pos)
			data.append(place)
			pygame.draw.line(screen, linecolor1, (210, 0),(210, 300))
			pygame.draw.line(screen, linecolor1, (270, 0),(270, 300))
			pygame.draw.line(screen, linecolor1, (0, 120),(480, 120))
			pygame.draw.line(screen, linecolor1, (0, 180),(480, 180))
			pygame.draw.line(screen, linecolor, (x, y - 7), (x, y + 7))
			pygame.draw.line(screen, linecolor, (x - 7, y), (x + 7, y))
			pygame.display.flip()
			if (now_time - prev_time) > 5:
				screen.fill(bgcolor)
				prev_time = now_time
				pygame.mixer.init()
				pygame.mixer.music.load("/home/pi/Desktop/a.mp3")
				pygame.mixer.music.play()
				sh = 0; l = 0; u = 0; c = 0; sm = 0; t = 0
				c_1 = True; c_2 = True; c_3 = True; c_4 = True; c_5 = True; c_6 = True; c_7 = True; c_8 = True; c_9 = True
				right = False
				cir_dir1 = 0
				cir_dir2 = 0
				length = (len(data) - 1)
				for i in range(length):
					if data[i] == 1:
						if c_1 == True:
							sm = sm + 1
							c = c + 1
							u = u + 1
							c_1 = False
					elif data[i] == 2:
						if c_2 == True:
							sh = sh + 1
							l = l + 1
							t = t + 1
							sm = sm + 1
							c = c + 1
							c_2 = False
					elif data[i] == 3:
						if c_3 == True:
							sm = sm + 1
							c = c + 1
							u = u + 1
							c_3 = False
					elif data[i] == 4:
						if c_4 == True:
							t = t + 1
							c = c + 1
							sm = sm + 1
							u = u  + 1
							cir_dir1 = i
							c_4 = False
					elif data[i] == 5:
						if c_5 == True:
							sh = sh + 1
							l = l + 1
							t = t + 1
							sm = sm + 1
							u = u + 1
							c_5 = False
					elif data[i] == 6:
						if c_6 == True:
							u = u + 1
							t = t + 1
							c = c + 1
							cir_dir2 = i
							right = True
							c_6 = False
					elif data[i] == 7:
						if c_7 == True:
							u = u + 1
							t = t + 1
							sm = sm + 1
							c = c + 1
							c_7 = False
					elif data[i] == 8:
						if c_8 == True:
							l = l + 1
							t = t + 1
							c = c + 1
							u = u + 1
							c_8 = False
					elif data[i] == 9:
						if c_9 == True:
							u = u + 1
							t = t + 1
							sm = sm + 1
							c = c + 1
							right = True
							c_9 = False
				if c == 8:
					if cir_dir1 < cir_dir2:
						circle('right')
					else:
						circle('left')
				elif u == 5 or u == 7:
					if cir_dir1 < cir_dir2:
						uturn('right')
					else:
						uturn('left')
				elif sm == 4:
					if right == True:
						smooth_turn('right')
					else:
						smooth_turn('left')
				elif t == 4:
					if right == True:
						turn('right')
					else:
						turn('left')
				elif l == 3:
					straight_long()
				elif t == 3:
					if right == True:
						turn('right')
					else: 
						turn('left')
				elif sm == 3:
					if right == True:
						smooth_turn('right')
					else:
						smooth_turn('left')
				elif sh == 2:
					straight_short()
				else:
					stop()				
				stop()
				pygame.mixer.music.stop()
				pygame.mixer.stop()
				pygame.mixer.quit()
				data = []
                             
GPIO.cleanup()
