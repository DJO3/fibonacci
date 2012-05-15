## Creates a list of fibonacci numbers and returns nth term in fibonacci

def f1(n):
    assert type(n) == int and n >  0
    terms = [0,1]
    i = 2
    while i<=n:
        terms.append(terms[-1]+terms[-2])
        i = i + 1
        print (i-1), '=', terms
    print  "Digit #%s within Fibonacci is " %n + str(terms[-2]) 

## Recursively produces corresponding nth term in fibonacci

def f2(n):
    assert type(n) == int and n >  0
    if n <= 1:
        print "Digit #%s within Fibonacci is" %n, n-1
    else:
        n = n -1
        print "Digit #%s within Fibonacci is " %(n+1) + str(d(n))

def d(n):
    if n <= 1:
        return n
    else:
        return (d(n-1) + d(n-2))

## Tests whether or not f1(n) and f2(n) are equivalent

def qa(n):
    assert type(n) == int and n >  0
    if f1(n) == f2(n):
        print True
    else:
        print False
