def reverse(n):
    out=0
    a=n
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if a==out:
        return("palindrome number")
    else:
        return("not a palindrome")
n=int(input("enter the number:"))
print(reverse(n))
