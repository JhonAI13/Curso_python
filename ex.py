from sklearn.preprocessing import StandardScaler
import numpy as np

# Criando um array de dados
X = np.array([[1, 2], [2, 3], [3, 4]])

# Instanciando o StandardScaler
scaler = StandardScaler()

# Ajustando e transformando os dados para média zero e desvio padrão unitário
X_scaled = scaler.fit_transform(X)

# Exibindo os dados escalonados
print(X_scaled)
