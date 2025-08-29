import numpy as np
import math

def polinomio(x):
    """Define o polinômio p(x) = 6x^5 + 18x^3 - 34x^2 - 493x + 1431"""
    return 6*x**5 + 18*x**3 - 34*x**2 - 493*x + 1431

def cota_cauchy(coeficientes):
    """
    Calcula a cota de Cauchy para as raízes do polinômio
    Fórmula: R = 1 + max(|a_{n-1}|, |a_{n-2}|, ..., |a_0|) / |a_n|
    onde a_n é o coeficiente do termo de maior grau
    """
    # coeficientes = [a_n, a_{n-1}, ..., a_1, a_0] (do maior para o menor grau)
    a_n = abs(coeficientes[0])  # coeficiente do termo de maior grau
    outros_coef = [abs(c) for c in coeficientes[1:]]  # outros coeficientes
    
    if a_n == 0:
        return float('inf')
    
    max_outros = max(outros_coef) if outros_coef else 0
    cota = 1 + max_outros / a_n
    
    return cota

def cota_lagrange(coeficientes):
    """
    Calcula a cota de Lagrange para as raízes do polinômio
    Fórmula mais refinada que a de Cauchy
    R = max(|a_k|^(1/(n-k))) para k = 0, 1, ..., n-1
    onde a_k são os coeficientes negativos divididos por |a_n|
    """
    n = len(coeficientes) - 1  # grau do polinômio
    a_n = coeficientes[0]  # coeficiente do termo de maior grau
    
    if a_n == 0:
        return float('inf')
    
    max_valor = 0
    
    for k in range(1, len(coeficientes)):
        if coeficientes[k] != 0:
            # Se o coeficiente tem sinal oposto ao coeficiente principal
            if (a_n > 0 and coeficientes[k] < 0) or (a_n < 0 and coeficientes[k] > 0):
                valor = (abs(coeficientes[k]) / abs(a_n)) ** (1 / (n - k + 1))
                max_valor = max(max_valor, valor)
    
    return max_valor if max_valor > 0 else 1

def cota_fujiwara(coeficientes):
    """
    Calcula a cota de Fujiwara (mais precisa)
    É uma versão refinada da cota de Cauchy
    """
    n = len(coeficientes) - 1
    a_n = abs(coeficientes[0])
    
    if a_n == 0:
        return float('inf')
    
    # Encontra o maior k tal que a_k != 0
    k_max = 0
    for i in range(1, len(coeficientes)):
        if coeficientes[i] != 0:
            k_max = i
            break
    
    if k_max == 0:
        return 0
    
    # Calcula a cota de Fujiwara
    soma = sum(abs(coeficientes[i]) for i in range(k_max, len(coeficientes)))
    cota = 2 * (soma / a_n) ** (1 / (n - k_max + 1))
    
    return cota

def main():
    print("=== Calculadora de Cotas para Raízes de Polinômios ===")
    print("Polinômio: p(x) = 6x⁵ + 18x³ - 34x² - 493x + 1431")
    
    # Coeficientes do polinômio (do maior grau para o menor)
    # p(x) = 6x^5 + 0x^4 + 18x^3 - 34x^2 - 493x + 1431
    coeficientes = [6, 0, 18, -34, -493, 1431]
    
    print(f"\nCoeficientes: {coeficientes}")
    
    # Calcula as cotas
    print("\n=== RESULTADOS ===")
    
    cota_c = cota_cauchy(coeficientes)
    print(f"Cota de Cauchy: {cota_c:.6f}")
    
    cota_l = cota_lagrange(coeficientes)
    print(f"Cota de Lagrange: {cota_l:.6f}")
    
    cota_f = cota_fujiwara(coeficientes)
    print(f"Cota de Fujiwara: {cota_f:.6f}")
    
    print(f"\nInterpretação:")
    print(f"- Todas as raízes estão no círculo |z| ≤ {min(cota_c, cota_l, cota_f):.6f}")
    print(f"- A cota mais precisa é: {min(cota_c, cota_l, cota_f):.6f}")
    
    # Opcional: encontrar raízes numericamente para comparação
    print(f"\n=== VERIFICAÇÃO (Raízes Numéricas) ===")
    try:
        raizes = np.roots(coeficientes)
        print("Raízes encontradas numericamente:")
        for i, raiz in enumerate(raizes):
            modulo = abs(raiz)
            print(f"  Raiz {i+1}: {raiz:.6f}, |raiz| = {modulo:.6f}")
        
        max_modulo = max(abs(raiz) for raiz in raizes)
        print(f"\nMaior módulo das raízes: {max_modulo:.6f}")
        
    except Exception as e:
        print(f"Erro ao calcular raízes numericamente: {e}")

if __name__ == "__main__":
    main()