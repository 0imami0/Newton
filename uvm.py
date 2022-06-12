import sympy as sp
from math import *

def NewtonRaphson(x0,tol,n):
	x = sp.symbols('x') 
	f = input('digite la funcion')
	df = sp.diff(f) 
	f = sp.lambdify(x,f)
	df = sp.lambdify(x,df)

	for k in range(n):
		x1=x0-f(x0)/df(x0)
		if(abs(x1-x0)<tol):
			print('x', k+1, '=', x1,'es la raiz')
			return
		x0=x1
		print('x',k+1,'=', x1)


NewtonRaphson(3.5, 0.0005, 3)

# 0.95*x**3-5.9*x**2+10.9*x-6
