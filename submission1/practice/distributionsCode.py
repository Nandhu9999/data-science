import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = sum( np.random.binomial(12, 0.2, 20_000) == 4 ) / 20_000
print(x)

print( sum( np.random.binomial(9, 0.1, 20_000) == 2 ) / 20_000 )

a = pd.Series( np.random.binomial( 12, 0.2, 20_000 )).value_counts().index
b = pd.Series( np.random.binomial( 12, 0.2, 20_000 )).value_counts().values
plt.bar(a,b)
plt.show()