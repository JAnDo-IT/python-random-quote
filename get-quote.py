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

  varResp0 = input("Wish to add extra line to the file y/n?: ")
  varResp=varResp0.upper()
  print("Resp: " + varResp)
  

  varFilename = "quotes.txt"

  global varLast
  global varExtNum
  global quotes

  varLast = 0
  varExtNum = 0
  quotes = []

  def readJFile():
    global varLast
    global varExtNum
    global quotes
    f = open(varFilename)
    #quotes = f.readlines() #Keeps \n
    quotes = f.read().splitlines()  #Eliminates \n
    varLast = len(quotes) - 1
    varExtNum = len(quotes)
    f.close()


  if varResp == "Y":
    #varExtNum = readJFile()
    readJFile()
    f = open(varFilename, 'a+')
    print()
    varExtraLine = "Python-random-quote, line: " + str(varExtNum) +  "\n"
    f.write(varExtraLine)

    print("{}".format(varExtraLine))
    f.close()
    # varExtNum = readJFile()

  else:
    print("No extra line")

  #varExtNum = readJFile()
  readJFile()

  print()

  print(quotes)
  print()
  print("Number of lines: " + str(len(quotes)))
  print()

  print("First")
  print(quotes[0])

  print("Last: " + str(varLast))
  print(quotes[varLast])

  varRand = random.randint(0, varLast)

  print("Random: " + str(varRand))
  print(quotes[varRand])
  print()


if __name__== "__main__":
  main()
