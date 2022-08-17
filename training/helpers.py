import numpy as np

# test array
x = np.random.rand(3)*10
print(x)

# after transformation
normalized_x = x/np.linalg.norm(x)
print(normalized_x)

# inverse transformation
inverse_transformed = normalized_x * np.linalg.norm(x)
print(inverse_transformed)

assert x.sum() == inverse_transformed.sum()
