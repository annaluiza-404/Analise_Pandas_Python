import pandas as pd
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

#no doc original estão separados por ; / serve para tirar e ficar tipo tabela
dados=pd.read_csv(url,sep=';')


#Quais os valores médios de aluguel por tipo de imóvel + criar gráfico
def_preco_tipo=dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

def_preco_tipo.plot(kind='barh',figsize=(14,10),color='purple')



#removendo os imóveis comerciais
dados.Tipo.unique()

imoveis_comerciais=['Conjunto Comercial/Sala',
                    'Prédio Inteiro', 'Loja/Salão',
                    'Galpão/Depósito/Armazém',
                    'Casa Comercial','Terreno Padrão',
                    'Loja Shopping/ Ct Comercial',
                    'Box Garagem','Chácara',
                    'Loteamento/Condomínio','Sítio',
                    'Pousada/Chalé','Hotel','Indústria']

df=dados.query('@imoveis_comerciais not in Tipo')
def_preco_tipo=df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
def_preco_tipo.plot(kind='barh',figsize=(14,10),color='blue')



#percentual de cada tipo de imóvel na base de dados
df.Tipo.value_counts(normalize=True)
df_percentual_tipo=df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo.plot(kind='bar',figsize=(14,10),color='green',
                        xlabel='Tipos',ylabel='Percentual')

df=df.query('Tipo == "Apartamento" ')



#tratamento de valores nulos
df.isnull().sum()
df=df.fillna(0)

#removendo linhas com 0 em valores ou condominio
registros_a_remover=df.query('Valor == 0 | Condominio == 0').index
df.drop(registros_a_remover,axis=0,inplace=True)

#removendo a coluna Tipo
df.drop('Tipo',axis=1,inplace=True)



#filtro 1 - apartamentos com 1 quarto e aluguel <R$1200
selecao1=df['Quartos']==1
df[selecao1]

selecao2=df['Valor']<1200
df[selecao2]

selecao_final=(selecao1) & (selecao2)
df_1=df[selecao_final]

#filtro 2 - apartamentos com 2 quartos, aluguel <R$3000 e área>70
selecao=(df['Quartos']>=2) & (df['Valor']<3000) & (df['Area']>70)
df_2=df[selecao]



#salvando os dados
df.to_csv('dados_apartamentos.csv',index=False, sep=';')
pd.read_csv('dados_apartamentos.csv',sep=';')

df_1.to_csv('filtro_1.csv', index=False, sep=";")
pd.read_csv('filtro_1.csv',sep=';')
df_2.to_csv('filtro_2.csv', index=False, sep=";")
pd.read_csv('filtro_2.csv',sep=';')



#criando colunas numericas a partir da base de dados original
url='https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados=pd.read_csv(url,sep=';')

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']


#criando colunas categoricas
dados['Descricao']= dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + dados['Quartos'].astype(str) + ' quarto(s) ' + ' e ' + dados['Vagas'].astype(str) + 'vaga(s) de garagem'

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x>0 else "Não")
print(dados.head())

dados.to_csv('dados_completos_dev.csv',index=False,sep=';')

                    




























#pega a linha sobre o estudante de id S003 e mostra aquelas duas colunas
#print(tabela_aluno.loc[tabela_aluno['student_id']=='S003', ['hours_studied','sleep_hours']])
