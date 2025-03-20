import pandas as pd
import sys
#chamando as tabelas
tabela0 = pd.read_csv('previsao_melt_total_v20250318_h0_r2.csv')
tabela0_pivot = pd.pivot_table(tabela0, values = 'Casos', index = 'Semana', columns = 'Município')
resultado = pd.DataFrame()
resultado["S1"] = tabela0_pivot.loc['2025-03-23'] - tabela0_pivot.loc['2025-03-16']
resultado["S2"] = tabela0_pivot.loc['2025-03-30'] - tabela0_pivot.loc['2025-03-23']
resultado_transposto = resultado.T
print(f"\nResultado:\n{resultado}\n")
resultado.to_csv("resultado.csv")
sys.exit()
resultado = pd.DataFrame(resultado, index = "Município", columns = "S1")
resultado1 = pd.DataFrame(resultado1, index = "Município", columns = "S2")
novo = resultado.merge(resultado1)
print(f"\nPrimeiro Resultado:\n{resultado}\n")
print(f"\nSegundo Resultado:\n{resultado1}\n")
print(f"\nNovo Resultado:\n{novo}\n")
sys.exit()


print(resultado)


