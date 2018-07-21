import csv
import numpy as np
import scipy.stats

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

c_diff_array = np.array([row['c_diff'] for row in wordsim_concreteness_combined])
wordsim_array = np.array([row['Human (mean)'] for row in wordsim_concreteness_combined])
corr = np.corrcoef(c_diff_array, wordsim_array)
ttest = scipy.stats.ttest_ind(c_diff_array, wordsim_array)
print(c_diff_array)
print(wordsim_array)
print(corr)
print(ttest)
