user_respond = 0

def begin_story():
  print("You bumped to a random man dressed in black, told you to take the fancy dragon ring?. What do you do?")
  print("choose your dicision by the given number")
  user_respond = int(input("1. Don't take the ring. \n2. Take the ring from him.\n3. Why would you give me this ring?"))
  the_ring (user_respond)
    
def the_ring(user_respond):
  if (user_respond == 2):
   take_the_ring()
  elif (user_respond == 1):
   do_not_take_the_ring()
  elif (user_respond == 3):
    ask_question()
  else:
    failed_to_respond()
    
  return user_respond

def take_the_ring():
  print("You took the offer from him but he handed you a folded note you looked at it looked back up but he vanished in a sec. While panicking you try to think.")
  user_respond = int(input("1. Read the note that's folded. \n2. Try to pinch your self to check if you're dreaming. \n3. Throw the ring away"))
  ring(user_respond) 

def ring(user_respond):
  if (user_respond == 1):
    read_note()
  elif (user_respond ==2):
    pinch()
  elif (user_respond == 3):
    throw_ring()
  else:
    failed_to_respond()
    

def read_note():
  print("You had open the note it says to put it on and meet at a certain place in the forest in a old amusement park and you knew it had shut down 10 years ago.")
  user_respond = int(input("1. Go to the location. \n2. Put on the ring."))
  l(user_respond)
  
def l(user_respond):
  if (user_respond == 1):
    location()
  elif (user_respond == 2):
    p_o_t_r()
  else:
    failed_to_respond()
  
  return user_respond
  
def pinch():
  print("You pinched yourself but you found yourself not dreaming. So you are holding the folded note and the ring")
  user_respond = int(input("1. Open the folded note. \n2. Look at the ring."))
  o_p(user_respond)

def o_p(user_respond):
  if(user_respond == 1):
    read_note()
  elif (user_respond == 2):
    look_at_ring()
  else:
    failed_to_respond()
      
  return user_respond()
  
def throw_ring():
  print("You threw the ring but it just happend to shine bright and you seem to get close but the ring attached to finger right away")
  user_respond = int(input("1. Try to take it off. \n2. Read the note you had in your hand."))
  strug(user_respond)
  
def  strug(user_respond):
  if (user_respond == 1):
   t_off()
  elif (user_respond == 2):
   note()
  else:
    failed_to_respond()  
    
def t_off():
  print("You tried to take it off, but you struggled to take it off couldn't do much.")
  user_respond = int(input("1. Read the note from your hand."))
  re_n(user_respond)
  
def re_n(user_respond):
  if (user_respond == 1):
    note()
  else:
    failed_to_respond()
    
def do_not_take_the_ring():
  print("You refused the ring, but the man handed the ring back to you with a folded note and vanished before your eyes.")
  user_respond  = int(input("1. Read the folded note. \n2. Throw away the ring."))
  refused (user_respond)

def refused (user_respond):
  if (user_respond == 1):
   read_note()
  elif(user_respond == 2):
   throw_ring()
  else:
    failed_to_respond()
  
  return user_respond()
    
def ask_question():
  print("He aproches to you by your ear and says you need this and hands you the ring. Walks away and vanishes leaving something in the floor")
  user_respond = int(input("1. Pick up that something \n2. Take a look at the ring."))
  pick (user_respond)
  
def pick(user_respond):
  if (user_respond == 1):
   p_u_t_s()
  elif(user_respond == 2):
   look_at_ring()
  else:
    failed_to_respond()
  
  return user_respond()
  
def p_u_t_s():
  print("You get closer to it and you pick up that note.")
  user_respond = int(input("1. Open the folded note. \n2. Look at the ring."))
  n_o_r (user_respond)
  
def n_o_r(user_respond):
  if (user_respond == 1):
   read_note()
  elif(user_respond == 2):
   look_at_ring()
  else:
    failed_to_respond()
  
  return user_respond()  

def look_at_ring():
  print("You took a closer looked at a detailed dragon wrapped around the ring. That had all gold with dragon's eyes in small sparkling red stones.")
  user_respond = int(input("1. Put on the ring.\n2. Open the the folded note."))
  t_r (user_respond)
  
def t_r(user_respond):
  if(user_respond == 1):
   p_o_t_r()
  elif(user_respond == 2):
   read_note()
  else:
    failed_to_respond()
    
def note():
  print("You had open the note it says to put it on and meet at a certain place in the forest in a old amusement park and you knew it had shut down 5 years ago.")
  user_respond = int(input("1. Go to the location."))
  go_location(user_respond)

def go_location(user_respond):
  if(user_respond ==1):
    location()
  else:
    failed_to_respond()

def location():
  print("You had gone to the forest that seemed to had taken you a long time but you had known this place and it started to get dark but had proceed to go to the location.")
  user_respond = int(input("1. Enter the amusement park.\n2. Take a look around."))
  amusement(user_respond)
  
def amusement(user_respond):
  if(user_respond == 1):
   enter_amu()
  elif(user_respond == 2):
   look()
  else:
    failed_to_respond() 

def p_o_t_r():
  print("You had put on the ring and it had shined bright and had tighten on your finger since it was a little loose.")
  user_respond = int(input("1. Try to take off the ring. \n2. Read the note"))
  ring_a(user_respond)
  
def ring_a(user_respond):
  if(user_respond == 1):
   tr_off()
  elif(user_respond == 2):
   note()
  else:
    failed_to_respond() 
    
def tr_off():
  print ("Tried to take it off but just stayed stuck couldn't do much.")
  user_respond = int(input("1. Go to the location."))
  g(user_respond)
  
def g(user_respond):
  if(user_respond == 1):
    location()
  else:
    failed_to_respond()
    
def enter_amu():
  print("You entered the amusement park had all different rides they were all rusted, fadded and teared apart. That plants grew around some of the rides.")
  user_respond = int(input("1. Take a look around \n2. Enter a small building"))
  lt(user_respond)
  
def lt(user_respond):
  if(user_respond == 1):
   look()
  elif(user_respond == 2):
    ent_build()
  else:
    failed_to_respond

def ent_build():
  print("You had entered to the old small building but onece you entered it had smelt kind of bad and the door behind you had slammed on you. You had seen a man standing in a small distance.")
  user_respond = int(input("1. Try to escape.\n2. Ask a question."))
  a_q(user_respond)
  
def a_q(user_respond):
  if(user_respond == 1):
    esc()
  elif(user_respond == 2):
    as_qu()
  else:
    failed_to_respond()
      
def esc():
  print("You tried to find an object around you to break out and you did find a sharp object and broke out a window, but as you tried to escape but the dragon from the ring seem to move and grew at snake size and started to strangle you. Then you died. The End")

def as_qu():
  print("What am I doing here.What is this ring for? You had a lot of quetions but you had to just say a couple. But then he had said you are the chosen one. The End")
  
  
def look():
  print("You took a look around but everything was crashed down, signs and some of the rides too.You thought about how it looked in the past since it was your favorite amusement park when you were younger.")
  user_respond = int(input("1. Enter a small building"))
  en_bu(user_respond)
  
def en_bu(user_respond):
  if(user_respond ==1 ):
    ent_build()
  else:
    failed_to_respond()


    
def failed_to_respond():
  print("Try again click by the given number.")
  return begin_story()
  
  
begin_story()
