#Get - current - python-random-quote
# python-random-quote From GitHub by JAnDo
"""
from time import strftime, gmtime, localtime #using time module
dt_gmt = strftime('%A, %d %b %Y %H:%M:%S', localtime()) #By JAnDo
var="Nuevas lineas hoy: "
strLine = ""

print(strLine)
print(' {} '.format(var) + str(dt_gmt))
print(strLine)
"""

# Starts the Program

import random

def main():
  print()
  print("Keep it logically awesome JAnDo.")

  print()
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(quotes)
  #print(len(quotes))

  print("First")
  print(quotes[0])

  varLast = len(quotes) - 1

  print("Last")
  print(quotes[varLast])

  varRand = random.randint(0, varLast)

  print("Random: " + str(varRand))
  print(quotes[varRand])
  print()


if __name__== "__main__":
  main()
