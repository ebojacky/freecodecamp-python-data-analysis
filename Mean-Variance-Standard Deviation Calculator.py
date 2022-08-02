
import pprint
import numpy as np


def calculate(mylist):

    if len(mylist) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        my_array = np.array(mylist)
        my_array = my_array.reshape(3, 3)

        return {
            'mean': [my_array.mean(axis=0).tolist(), my_array.mean(axis=1).tolist(), my_array.mean().tolist()],
            'variance': [my_array.var(axis=0).tolist(), my_array.var(axis=1).tolist(), my_array.var().tolist()],
            'standard deviation': [my_array.std(axis=0).tolist(), my_array.std(axis=1).tolist(), my_array.std().tolist()],
            'max': [my_array.max(axis=0).tolist(), my_array.max(axis=1).tolist(), my_array.max().tolist()],
            'min': [my_array.min(axis=0).tolist(), my_array.min(axis=1).tolist(), my_array.min().tolist()],
            'sum': [my_array.sum(axis=0).tolist(), my_array.sum(axis=1).tolist(), my_array.sum().tolist()]
        }


ans = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
pprint.pprint(ans)
