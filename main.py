from package.req_raw import req_raw
from package.train_ import train_test
from package.random_forest import random_forest
from sklearn.preprocessing import LabelEncoder
from plot.violin import violin_plot
import matplotlib.pyplot as plt 

import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/reducao-dimensionalidade/master/data-set/exames.csv'

def main():
    print('Main Fuction')
    csv = req_raw(url) 
    
    isnull = csv.isnull().sum()
    
    # le = LabelEncoder()
    
    # csv['diagnostico'] = le.fit_transform(csv['diagnostico'])
    exames = csv.drop(columns=["id", "diagnostico"])
    print(csv.head())
    
    v1 = csv.drop(columns='exame_33')
    dig = csv.get('diagnostico')
    # dig['diagnostico'] = pd.to_numeric(dig['diagnostico'], errors='coerce')

    dados_plot = pd.concat([dig, v1], axis=1)
    dados_plot = pd.melt(dados_plot, id_vars='diagnostico', value_name='valores', var_name='exames')
   
    # dados_plot.head()

    # plt.figure(figsize=(10, 10))
    violin_plot('exames', 'valores', 'diagnostico', dados_plot)
    
    # print(exames)
    # print(dig)
    # train = train_test(v1, dig)
    # for t in train:
    #   print(t)


    # score = random_forest(100, train)
    # print(score)
    #  classficator.fit(train['treino_x'], train['treino_y'])


main()