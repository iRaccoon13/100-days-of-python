def loading_screen(logo,delay):
  from time import sleep
  from os import system,name
  A = "#"
  B = " "
  for i in range(0,10):
    system('cls' if name == 'nt' else 'clear')
    Bs = 10-i
    print(logo)
    print(f"[{A*i}{B*Bs}]")
    sleep(delay/1000)