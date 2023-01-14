from sklearn.ensemble import RandomForestClassifier

def random_forest(estimators, train):
    classificador = RandomForestClassifier(n_estimators = 100)
    print('Fit')
    a = train['treino_x']
    b = train['treino_y']
    c = train['teste_x']
    d = train['teste_y']
    print('teste', a)
    
    classificador.fit(a, b)
    score = classificador.score(c, d)

    return score
