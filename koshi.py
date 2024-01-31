a,b = map(int,input().split())
if (a+b)/2 > pow(a*b,1/2):
  print(">")
elif (a+b)/2 < pow(a*b,1/2):
  print("<")
else:
  print("=")