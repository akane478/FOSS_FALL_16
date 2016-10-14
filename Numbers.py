numbers = open('numbers', 'r')
a = 0
total = 0
average = 0
count = 0
while(a==0):
   b = numbers.readline()
   if(b==""):
       a=1
   else:
       for n in b.split():
           total = total + int(n)
           count = count + 1
average = total/count
print("Average: " + str(average))
