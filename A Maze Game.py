#Welcome To My Maze Game 
#You Need TO Go To Garden To Win  The GAME
#Grab Items Along The Way

























































from termcolor import colored
item=[]
def instruction():
  print("1.MOVE \n2.GRAB ITEM \n3.EXIT GAME")
  print("You Entered Into:",current_room.title())
  print("You Currently Have :- ",",".join(item))
current_room="hall"

rooms={
  "hall":{
    "up":"kitchen",
    "left":"bedroom",
    "item":"key"},
    
  "kitchen":{"down":"hall",
             "item":"food"
    
             },
  "bedroom":{"right":"hall",
             "up":"garage",
             "item":"cloths"
  },
  "garage":{"down":"bedroom",
            "item":"skateboard",
            "left":"pathway"
            },
    "pathway":{
      "right":"garage",
      "item":"monster",
      "down":"garden"
      
    },
    
    "garden":{
      "up":"pathway"
      }
    }
    
  
while True:
  instruction()
  #print("1.MOVE \n 2. GRAB ITEM \n 3.EXIT GAME")
  a=int(input("Enter The Choice "))
  if(a == 1):
    b=str(input("Which Direction Would You Like To Move Up,Down,Left,Right?"))
    b=b.lower()
    #print(b,rooms[current_room][b])
    if(b in rooms[current_room]):
      current_room=rooms[current_room][b]
      if(current_room == 'garden' and 'key' in item):
        print(colored("You Won The Game","green"))
        break
    else:
      print(colored("You Cant Enter Into That Place","cyan"))
  if(a ==2 ):
    if(rooms[current_room]['item'] == "monster" ):
      print(colored("You Lost The Game Cuz Monster Killed You ","red"))
      break
    else:
      item.append(rooms[current_room]['item'])
      print("You Found ",colored(item[-1].title(),"red"))
      
      
  if(a == 3):
    print(colored("Go To The Garden To Win","cyan"))
    