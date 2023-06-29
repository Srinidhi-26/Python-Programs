def pallindrome(n):
    n = n.lower()
    return n == n[::-1]


n = input('enter string')
v = pallindrome(n)

if v :
    print('pallindrome')
else:
    print('not pallindrome')