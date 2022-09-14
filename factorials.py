# declare any variables
user_int = 0
f = 1  

user_int = int(input("Enter a non-negative integer: "))

if user_int > 0:
    for n in range(1, user_int+1):
        
        f = f * n

        print(str(f))
