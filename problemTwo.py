// Problem Two
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
// find the sum of the even-valued terms.
l = [2]
f = {0:1, 1:2}
for i in range(1000):
  f[i+2] = f[i] + f[i+1]
  if( f[i+2] > 4000000 ):
    break
  if( f[i+2] % 2 == 0 ):
    l.append(f[i+2])

print(sum(l))
