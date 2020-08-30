n = int(input())
if(n%2 == 0):
    no_of_even = int(n/2)
    no_of_odd = int(n/2)
else:
    no_of_even = (n-1) // 2
    no_of_odd = n - no_of_even
print(no_of_even*(no_of_even+1) - no_of_odd*no_of_odd)