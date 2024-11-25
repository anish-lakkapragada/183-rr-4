# %% 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data-points.csv")
plt.scatter(data['zeroes'], data['attempts'])
plt.yscale('log')
plt.title("# of attempts (Log Scale) vs. # of leading zeroes")
plt.xlabel("# of leading zeroes")
plt.ylabel("# of attempts (Log Scale)")
# %%

"""
Because this trend is roughly linear, we can create a linear regression model to 
predict the log(# of attempts) based on the # of leading zeroes.
"""
import numpy as np 
from sklearn.linear_model import LinearRegression

x = data['zeroes'].to_numpy()
y = data['attempts'].to_numpy()
y = np.log(y)

reg = LinearRegression()
reg.fit(np.expand_dims(x, -1), y)
# %%
"""
We can show the prediction curve vs. the actual data points.
"""

plt.scatter(data['zeroes'], data['attempts'], label="Data Points")
plt.plot(np.arange(0, 8), np.exp(reg.predict(np.arange(0, 8).reshape(-1, 1))), label="Predictions", color="orange")
plt.yscale('log')
plt.title("# of attempts (Log Scale) vs. # of leading zeroes")
plt.xlabel("# of leading zeroes")
plt.ylabel("# of attempts (Log Scale)")
plt.legend()

# %%
print(reg.coef_, reg.intercept_)
# %%
