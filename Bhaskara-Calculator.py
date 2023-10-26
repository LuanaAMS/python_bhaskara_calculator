import IPython.display
from IPython.display import clear_output as clear


#Calcula a raiz de Delta
def rdelta(delta):
  delta = delta ** (1/2)
  return delta

#Calcula X1 e X2
def recipe(a,b,delta):
  x0 = (-b+(delta))/(2*a)
  x1 = (-b-(delta))/(2*a)
  return [x0, x1]

#Retorna os resultados
def result(x0,x1):
    if (x0>0 and x1<0):
      print("O primeiro resultado é " + str(x0))
      print("O Segundo resultado é NEGATIVO, e é " + str(x1))
    else:
      if (x0<0 and x1>0):
        print("O primeiro resultado é NEGATIVO, e é " + str(x0))
        print("O Segundo resultado é " + str(x1))
      else:
        if (x0>0 and x1>0):
          print("O primeiro resultado é " + str(x0))
          print("O Segundo resultado é " + str(x1))
        else:
          print("O primeiro resultado é NEGATIVO, e é " + str(x0))
          print("O Segundo resultado é NEGATIVO, e é " + str(x1))


print("Calculo de fórmula de Bhaskara \n")

#Recebe os valores de A,B e C
a=int(input("Digite o valor de A \n"))
print("")
b=int(input("Digite o valor de B \n"))
print("")
c=int(input("Digite o valor de C \n"))

clear()

#Calcula Delta
delta = (b ** 2) - a * c * 4

#Verifica se Delta tem um valor real para puxar os resultados
if (delta>0):
  print("Sua equação tem dois resultados reais \n")
  delta = rdelta(delta)
  x = recipe(a,b,delta)
  result(x[0], x[1])
else:
  if (delta==0):
    print("Sua equação tem apenas um resultado real \n")
    delta = rdelta(delta)
    x = recipe(a,b,delta)
    result(x[0], x[1])
  else:
     print("Sua equação não possui um resultado real \n")