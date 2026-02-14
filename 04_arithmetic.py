print(5/2)  # 2.5
print(5**2) # power -> 25 

i=2
i+=2
print(i) # 4

# operator precedance 
# BODMAS rule
print( 2 + 3 * 9 )  #29

print( 3 > 2 )  # True
print( 3 == 3 ) # True
print( 3 != 3 ) # False

print( 2>3 or 2>1 ) #True
print( 2>3 and 2>1 ) #False
print( not 2>3 ) #True


a,b=2,3
txt="@"
print(a*txt*b) # @@@@@@ 6 times

a,b="2",3
txt="@"
print((a+txt)*b) # 2@2@2@

#division operator
a=1
b=2
c=1/2
print(c) # 0.5
print(1//2) #0  # int div --> floor(a/b)
                # floor : closest val which is lesser than or equal to float val
                # 0.1 -> 0  , 5.2 -> 5  , 7.99 -> 7 , 11.2 -> 11
                # -5.2 -> -6 , -5.0 -> 5.0, 2 -> 2

# reminder 

# numinator % denominator
# + % + => +
# - % - => +
# + % - => -
# - % + => +

