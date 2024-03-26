import math

def sign(x):
    return math.copysign(1,x)

def newton(fname,fpname,x0,tolx,tolf,nmax):
    xk = []
    #Prima iterazione
    fx0 = fname(x0)
    d = fx0 / fpname(x0)
    x1 = x0 - d
    fx1 = fname(x1)
    xk.append(x1)
    numit = 1
    #Ciclo iterativo per le successive.
    while numit < nmax and abs(fx1) > tolf and abs(d) >= tolx*abs(x1):
        x0 = x1
        fx0 = fname(x0)
        d = fx0 / fpname(x0)
        x1 = x0-d
        fx1 = fname(x1)
        numit = numit + 1
        xk.append(x1)
    
    if numit == nmax:
        print("Iterazioni massime raggiunte")
    
    return x1,numit,xk

def bisezione(fname,a,b,tol):
    fa = fname(a)
    fb = fname(b)
    if sign(fa) * sign(fb) >= 0:
        print("Metodo di bisezione non applicabile.")
        return None,None,None
    maxit = math.ceil(math.log2((b-a)/tol) - 1)
    centers = []
    numit = 0
    while b-a > tol:
        xk = a + (b-a) / 2
        centers.append(xk)
        numit = numit + 1
        fxk = fname(xk)
        if fxk == 0:
            return xk,numit,centers
        if sign(fa) * sign(fxk) > 0:
            a = xk
            fa = fxk
        elif sign(fb) * sign(fxk) > 0:
            b = xk
            fb = fxk
    return xk,numit,centers