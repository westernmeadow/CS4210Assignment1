#-------------------------------------------------------------------------
# AUTHOR: Wesley Kwan
# FILENAME: find_s
# SPECIFICATION: find-S algorithm for contact lens data
# FOR: CS 4200- Assignment #1
# TIME SPENT: 45 mins
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
index = 0
while (db[index][num_attributes] != 'Yes'):
    index+=1;
hypothesis = db[index][0:num_attributes]

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
for instance in db:
    if instance[num_attributes] == 'Yes':
        for attribute in range(num_attributes):
            if instance[attribute] != hypothesis[attribute]:
                hypothesis[attribute] = '0'
            attribute+=1

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)