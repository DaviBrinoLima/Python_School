def exec10():
   soma_primeiro= 0
   soma_segundo= 0
   soma_igual= 0


   for i in range (10,100):
      primeiro = int(i/10)
      segundo = int(i%10)


      if primeiro>segundo:
           soma_primeiro= soma_primeiro + 1

      elif primeiro<segundo:
           soma_segundo= soma_segundo + 1

      else:
           soma_igual= soma_igual+ 1


   print(f"A quantidade de números que possuem o algarismo da esquerda maior que o da direita é: {soma_primeiro}")
   print(f"A quantidade de números que possuem o algarismo da direita maior que o da esquerda é: {soma_segundo}")
   print(f"A quantidade de número que possuem os dois algarismo iguais é: {soma_igual}")   
           

if __name__== '__main__':
    exec10()