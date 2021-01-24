import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

txtdir = r''
results = pd.read_csv(txtdir, header=None, sep='\s+')

PR_results = results.iloc[:, 8:10]

plt.subplot(1, 2, 1)
# plt.figure(1)
plt.plot(PR_results.iloc[:, 0])
# plt.show()
# plt.figure(2)
plt.subplot(1, 2, 2)
plt.plot(PR_results.iloc[:, 1])
plt.show()

print(PR_results)