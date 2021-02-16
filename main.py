import pyautogui
import random

pyautogui.FAILSAFE = False
PETS_Y_INDEX = 150 #Changes between 150 and 175 if they add speedchat phrases
SPEEDCHAT = (85, 70)
PETS = 125, PETS_Y_INDEX
OFFSET = 25
TRICKS = 310, PETS_Y_INDEX
JUMP = (390, PETS_Y_INDEX)

# index 0 for jump, ...
def do_trick(index):
  speedchat()
  move_to(PETS)
  move_to(TRICKS)
  move_to(JUMP) #always move to jump first to properly highlight
  move_and_click((JUMP[0], JUMP[1] + index * OFFSET))

def speedchat():
  move_to(SPEEDCHAT)
  pyautogui.click()


def get_duration():
  global x
  x = random.random() * 1.5 + .25
  return x


def move_to(cursor):
  pyautogui.moveTo(cursor, duration=get_duration())


def move_and_click(cursor):
  move_to(cursor)
  pyautogui.click()


def say_something():
  speedchat()
  if random.randint(0, 1): say_hello()
  else: say_pet()

def say_hello():
  hello_pos = (PETS[0], PETS[1] + OFFSET)
  move_to(hello_pos)
  say_random(hello_pos)


def say_pet():
  move_to(PETS)
  say_random(PETS)


def say_random(pos):
  move_to((pos[0] + 185, pos[1]))
  move_and_click((pos[0] + 185, pos[1] + random.randint(1, 5) * OFFSET))


for i in range(0, 308):
  do_trick(2)
  say_something()
  #if random.randint(0, 1): say_something()
  print(str(x) + " " + str(i))
