# Write code for algorithm 1 below

def count_down(n):
   
   if n==0:
      return
   
   else:
      print(n)
      count_down(n-1)


n=8
count_down(n)