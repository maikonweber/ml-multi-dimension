from sklearn.model_selection import train_test_split
from numpy import random
SEED = 123143
random.seed(SEED)

def train_test(v1, v2):
    treino_x, teste_x, treino_y, teste_y = train_test_split(v1, v2, test_size=0.3)
    return {
        'treino_x' : treino_x,
        'teste_x' : teste_x,
        'treino_y' : treino_y,
        'teste_y' : teste_y
    }

