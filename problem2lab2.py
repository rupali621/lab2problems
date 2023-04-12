#defined inputs
number=float(input("starting number of organisms"))
average=int(input("average daily percentage increase"))
days=int(input("enter the number of days to display final data:"))
#declaring outputs
print("approximate day"," ","population")
print("........................................")
print("1","  ",number)
#concept of loop
for i in range(1, 10):
  a=number+(number*(average/100))
  number=a
  print(i+1, "",a)
