import math

def metodo_newton(f,f_derivada,p0,tol,n):
  i = 1
  print("-"*88)
  print("| i |      p     |      F(p0)     |     F'(p0)      |       p-p0      |       tol      |")
  while i<=n:
    p = p0 - (f(p0)/f_derivada(p0))
    print("| {0:d} |   {1:.4f}   |     {2:.4f}     |     {3:.4f}     |      {4:.4f}     |     {5:.4f}     |".format(i, p, f(p0), f_derivada(p0), abs(f(p)), tol))
    if abs(p-p0)<tol:
      print("-"*88)
      return "\nProcedimento concluido com sucesso.\n\nResultado = {0:.5f}\n".format(p)
    else:
      i += 1
      p0 = p
  print("-"*88)
  return "\nO metódo falhou após {} iterações.\n".format(n)

exemplo_f = lambda x: x**3 +4*(x**2) - 10
exemplo_f_derivada = lambda x: 3*(x**2) + 8*x

ex_1 = lambda x: math.cos(x) - x
ex_1_derivada = lambda x: -math.sin(x) -1
print(metodo_newton(exemplo_f, exemplo_f_derivada, 1, 0.1,100))
print(metodo_newton(ex_1, ex_1_derivada, math.pi/4, 0.001, 100))


ex1_a = lambda x: math.exp(x) + 2**(-x) + 2 * math.cos(x) - 6
ex1_a_derivada = lambda x: math.exp(x) - math.log(2)*2-x-2*math.sin(x)

ex1_b = lambda x: math.exp(x) - x**2 + 3*x - 2
ex1_b_derivada = lambda x: math.exp(x) - x**2 + 3*x - 2
