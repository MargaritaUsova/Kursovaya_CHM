from sympy import Function, Symbol, simplify, Derivative, Subs, factorial, collect, expand, symbols, solve
t = Symbol('t') #независимая переменная t и h
h = Symbol('h') 
y = Function('y')(t) #функция от переменной t
#разложение функции с шагом h по ф. Тейлора вплоть до производной порядка count
def u(step, count):
    res = y
    for i in range(1, count+1):
        res += (step)**i * Derivative(y,(t,i))/factorial(i)
    return res
a, b, c, d, e, f, g, k, l, m, n, o, p, v,r, z, t = symbols('a, b, c, d, e, f, g, k, l, m, n, o, p, v,r, z, t')
res = Derivative(y,(t,2)) + (a * u(-h, 17) + b * y + c * u(h, 17) + d * u(2*h, 17) 
                             + e * u( 3*h, 17)+f*u(4*h, 17)+g*u(5*h, 17)+k*u(6*h, 17)+l*u(7*h, 17)
                             +m*u(8*h, 17)+n*u(9*h, 17)+o*u(10*h, 17)+p*u(11*h, 17)+v*u(12*h, 17)
                             +r*u(13*h, 17)+z*u(14*h, 17)+t*u(15*h, 17)) / h**2
res_=collect(expand(res, h), h)
print(res_)
simplify(res_.coeff(h,3))

q = solve([res_.coeff(h, -2),res_.coeff(h,-1), res_.coeff(h,0), res_.coeff(h,1), res_.coeff(h,2)], a, b, c, d, e)
print(q)

#порядок аппроксимаций 

res_.subs([(a, q[a]), (b, q[b]), (c, q[c]), (d, q[d]), (e, q[e])])
