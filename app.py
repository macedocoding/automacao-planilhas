import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./custo_nivel.csv', sep=';', skipinitialspace=True)

# Limpar os pontos da coluna NIVEL
df['NIVEL'] = df['NIVEL'].str.replace('.', '')

# Converter NIVEL para inteiro
df['NIVEL'] = df['NIVEL'].astype(int)

# Função para encontrar o componente pai
def encontrar_pai(row, df):
    nivel_atual = row['NIVEL']
    if nivel_atual == 0:
        return None
    # Encontra o componente do nível imediatamente superior
    pai = df[df['NIVEL'] == nivel_atual - 1].iloc[-1]['COMPONENTE']
    return pai

# Criar nova estrutura
resultado = []

# Iterar sobre o DataFrame
for i, row in df.iterrows():
    pai = encontrar_pai(row, df[:i+1])
    if pai is not None:
        resultado.append({
            'Nivel': pai,
            'Subnivel': row['COMPONENTE']
        })

# Criar DataFrame final
df_resultado = pd.DataFrame(resultado)
df_resultado.to_csv('resultado.csv')
