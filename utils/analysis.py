import csv
import numpy as np
import scipy.stats
from matplotlib import pyplot as plt
from numpy.polynomial.polynomial import polyfit

concreteness = {}
with open('wordsim_concreteness.txt') as f:
    for row in csv.DictReader(f, fieldnames=['word', 'concreteness']):
        concreteness[row['word']] = row['concreteness']

wordsim_concreteness_combined = []
with open('combined.csv') as f:
    wordsim_dict_reader = csv.DictReader(f)
    for i, row in enumerate(wordsim_dict_reader):
        if row['Word 1'] in concreteness and row['Word 2'] in concreteness:
            row['Concreteness 1'] = float(concreteness[row['Word 1']])
            row['Concreteness 2'] = float(concreteness[row['Word 2']])
            row['c_diff'] = abs(row['Concreteness 1'] - row['Concreteness 2'])
            row['Human (mean)'] = float(row['Human (mean)'])
            wordsim_concreteness_combined.append(row)

x = np.array([row['Human (mean)'] for row in wordsim_concreteness_combined])
ymin = np.array([min([row['Concreteness 1'], row['Concreteness 2']]) for row in wordsim_concreteness_combined if row['c_diff'] < 1])
ymax = np.array([max([row['Concreteness 1'], row['Concreteness 2']]) for row in wordsim_concreteness_combined if row['c_diff'] < 1])
plt.vlines(x, ymin, ymax)
plt.xlabel('Word similarity')
plt.ylabel('Concreteness min/max')
plt.xlim([0, 10])
plt.ylim([0, 5])
plt.show()

'''c_diff_array = np.array([row['c_diff'] for row in wordsim_concreteness_combined])
r = scipy.stats.pearsonr(x, c_diff_array)
b, m = polyfit(x, c_diff_array, 1)
plt.scatter(x, c_diff_array)
plt.plot(x, b + m * x, 'r-')
plt.xlabel('Word similarity (0 to 10)')
plt.ylabel('Difference in concreteness rating (0 to 5)')
plt.show()
print(r)'''
