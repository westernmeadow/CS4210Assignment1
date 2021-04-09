#-------------------------------------------------------------------------
# AUTHOR: Wesley Kwan
# FILENAME: decision_tree
# SPECIFICATION: ID3 algorithm for contact lens data
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for instance in db:
    transform = []
    for attribute in range(len(instance)-1):
        if instance[attribute] in ('Young', 'Myope', 'No', 'Reduced'):
            transform.append(1)
        elif instance[attribute] in ('Prepresbyopic', 'Hypermetrope', 'Yes', 'Normal'):
            transform.append(2)
        else:
            transform.append(3)
    X.append(transform)
print(X)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for instance in db:
    if instance[len(instance)-1] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)
        
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


