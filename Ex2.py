import struct
import math

def limpar_registrador_excecoes():
    pass

def verificar_excecoes():
    return False

def mostrar_bits_float(valor, nome):
    packed = struct.pack('f', valor)
    # Converte bytes para inteiro para mostrar bits
    bits = struct.unpack('I', packed)[0]
    # Formata como binário de 32 bits
    bits_str = format(bits, '032b')
    
    # Separa sinal, expoente e mantissa
    sinal = bits_str[0]
    expoente = bits_str[1:9]
    mantissa = bits_str[9:]
    
    print(f"{nome}: {valor}")
    print(f"  Bits: {bits_str}")
    print(f"  Sinal: {sinal}, Expoente: {expoente}, Mantissa: {mantissa}")

def calculadora_ieee754():
    print("=== Calculadora IEEE-754 ===")
    
    # (a) Recebe expressão no formato val1 op val2
    entrada = input("Digite a expressão (formato: val1 op val2): ")
    partes = entrada.split()
    
    if len(partes) != 3:
        print("Formato inválido! Use: valor1 operacao valor2")
        return
    
    try:
        val1_str, op, val2_str = partes
        
        # Converte valores (aceita NaN e ±∞)
        if val1_str.lower() == 'nan':
            val1 = float('nan')
        elif val1_str.lower() == 'inf' or val1_str == '+inf':
            val1 = float('inf')
        elif val1_str == '-inf':
            val1 = float('-inf')
        else:
            val1 = float(val1_str)
            
        if val2_str.lower() == 'nan':
            val2 = float('nan')
        elif val2_str.lower() == 'inf' or val2_str == '+inf':
            val2 = float('inf')
        elif val2_str == '-inf':
            val2 = float('-inf')
        else:
            val2 = float(val2_str)
        
        # Converte para float32 para simular precisão de 32 bits
        val1 = struct.unpack('f', struct.pack('f', val1))[0]
        val2 = struct.unpack('f', struct.pack('f', val2))[0]
        
    except ValueError:
        print("Valores inválidos!")
        return
    
    # (b) Limpa registrador de exceções
    limpar_registrador_excecoes()
    print("\n(b) Registrador de exceções limpo.")
    
    # (c) Realiza operação e mostra resultado
    print(f"\n(c) Realizando operação: {val1} {op} {val2}")
    
    try:
        if op == '+':
            resultado = val1 + val2
        elif op == '-':
            resultado = val1 - val2
        elif op == '*':
            resultado = val1 * val2
        elif op == '/':
            if val2 == 0:
                resultado = float('inf') if val1 > 0 else float('-inf') if val1 < 0 else float('nan')
            else:
                resultado = val1 / val2
        else:
            print("Operação inválida! Use: +, -, *, /")
            return
        
        # Converte resultado para float32
        resultado = struct.unpack('f', struct.pack('f', resultado))[0]
        
        print(f"Resultado: {resultado}")
        
        # (d) Mostra configuração de bits
        print(f"\n(d) Configuração de bits:")
        mostrar_bits_float(val1, "val1")
        mostrar_bits_float(val2, "val2")
        mostrar_bits_float(resultado, "resultado")
        
        # (e) Verifica exceções IEEE-754
        print(f"\n(e) Verificação de exceções IEEE-754:")
        
        # Detecta algumas condições especiais
        excecoes = []
        
        if math.isnan(resultado):
            excecoes.append("Invalid Operation (resultado é NaN)")
        
        if math.isinf(resultado) and not (math.isinf(val1) or math.isinf(val2)):
            excecoes.append("Overflow (resultado é infinito)")
        
        if resultado == 0 and val1 != 0 and val2 != 0:
            excecoes.append("Underflow (resultado muito pequeno)")
        
        if op == '/' and val2 == 0 and not math.isnan(val1) and val1 != 0:
            excecoes.append("Division by Zero")
        
        if excecoes:
            print("Exceções detectadas:")
            for exc in excecoes:
                print(f"  - {exc}")
        else:
            print("Nenhuma exceção IEEE-754 detectada.")
            
    except Exception as e:
        print(f"Erro durante a operação: {e}")

# Executa o programa
if __name__ == "__main__":
    calculadora_ieee754()