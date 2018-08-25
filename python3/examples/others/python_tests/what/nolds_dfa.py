import nolds
import numpy as np


matrix = np.random.random(1000)

# rwalk = np.cumsum(matrix)
# __import__('pprint').pprint(rwalk)
# __import__("pprint").pprint(matrix)

h = nolds.dfa(matrix, nvals=range(4, 60), debug_plot=False, debug_data=False)

H = nolds.sampen(matrix, debug_plot=False)

print(f"Entropy: {H}")
print(f"Hurst: {h}")
