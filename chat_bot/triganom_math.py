import sympy as sp
import random
import numpy as np

def trig_equation_cos_gen(SIZE=100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.Symbol('x')
    
    eq = a * sp.cos(x)**2 + b * sp.cos(x) + c
    eq = sp.Eq(eq, 0)
    solutions = sp.solve(eq, x)
    
    # Фильтруем решения, оставляя только действительные
    if b**2-4*a*c < 0:
        real_solutions = []
    else:
        real_solutions = [s for s in solutions if np.isreal(s)]
    
    return {"raw_data": [a, b, c], "solutions": real_solutions}

def trig_equation_sin_gen(SIZE=100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.Symbol('x')
    
    eq = a * sp.sin(x)**2 + b * sp.sin(x) + c
    eq = sp.Eq(eq, 0)
    solutions = sp.solve(eq, x)
    
    # Фильтруем решения, оставляя только действительные
    if b**2-4*a*c < 0:
        real_solutions = []
    else:
        real_solutions = [s for s in solutions if np.isreal(s)]
    
    return {"raw_data": [a, b, c], "solutions": real_solutions}

def trig_equation_tan_gen(SIZE=100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.Symbol('x')
    
    eq = a * sp.tan(x)**2 + b * sp.tan(x) + c
    eq = sp.Eq(eq, 0)
    solutions = sp.solve(eq, x)
    
    # Фильтруем решения, оставляя только действительные
    if b**2-4*a*c < 0:
        real_solutions = []
    else:
        real_solutions = [s for s in solutions if np.isreal(s)]
    
    return {"raw_data": [a, b, c], "solutions": real_solutions}

def trig_equation_cot_gen(SIZE=100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.Symbol('x')
    
    eq = a * sp.cot(x)**2 + b * sp.cot(x) + c
    eq = sp.Eq(eq, 0)
    solutions = sp.solve(eq, x)
    
    # Фильтруем решения, оставляя только действительные
    if b**2-4*a*c < 0:
        real_solutions = []
    else:
        real_solutions = [s for s in solutions if np.isreal(s)]
    
    return {"raw_data": [a, b, c], "solutions": real_solutions}

def log_equation_gen(SIZE=100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = sp.Symbol('x')
    eq = sp.log(x**2 - a*x, 2) - b
    eq = sp.Eq(eq, c)
    
    # Находим решения численно
    try:
        solutions = sp.solve(eq, x)
    except ValueError:
        solutions = []
    
    real_solutions = [s for s in solutions if np.isreal(s)]
    return {"raw_data": [a, b, c], "solutions": real_solutions}

# Дебаг
result = trig_equation_tan_gen()
print(f"Уравнение: {result['raw_data'][0]}cos^2(x) + {result['raw_data'][1]}cos(x) + {result['raw_data'][2]} = 0")
print(f"Решения: {result['solutions']}")

#result = log_equation_gen()
#print(f"Уравнение: log2(x^2 - {result['raw_data'][0]}x) = {result['raw_data'][1]}")
#print(f"Решения: {result['solutions']}")

