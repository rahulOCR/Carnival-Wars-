import csv
import random
import sys
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import os
# model = Perceptron()
# model = svm.SVC()
model = KNeighborsClassifier(n_neighbors=10)
# model = GaussianNB()

def write_csv(data,p):
    fname = 'predictions.csv'
    fields = ['Product_id','Selling_Price']
    rows = []
    for i in range(len(data)):
        rows.append([data[i]['Product_id'],p[i]])
    with open(fname, 'w',newline="") as csvfile:  
      
        csvwriter = csv.writer(csvfile)  
        
    
        csvwriter.writerow(fields)  
        
     
        csvwriter.writerows(rows)
        print("File saved to "+os.getcwd())

def train_csv(file):
    data = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)

        
        for row in reader:
            try:
                data.append({'Product_id':row[0],'evidence':[float(cell) for cell in row[12:14]],'label':row[14]})
            except ValueError:
                continue
        return data

def test_csv(file):
    data = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                data.append({'Product_id':row[0],'evidence':[float(cell) for cell in row[12:14]]})
            except ValueError:
                x = []
                for i in range(12,14):
                    if row[i] =='':
                        x.append(float(0))
                    else:
                        x.append(float(row[i]))
                data.append({'Product_id':row[0],'evidence':x})
        return data
if len(sys.argv) < 3:
    print('help:\n python ai.py testfile.csv trainfile.csv')
    exit()
else:
    tf = sys.argv[1]
    trf = sys.argv[2]
    test = test_csv(tf)
    train = train_csv(trf)

    X_training = [row["evidence"] for row in train]
    y_training = [row["label"] for row in train]
    model.fit(X_training, y_training)

    X_testing = [row["evidence"] for row in test]

    predictions = model.predict(X_testing)


    print(predictions[:10])
    print(f"Results for model {type(model).__name__}")
    write_csv(test,predictions)
    # accracy testing of train.csv dataset
    '''correct = 0
    incorrect = 0
    total = 0
    for actual, predicted in zip(y_testing, predictions):
        total += 1
        if actual == predicted:
            correct += 1
        else:
            incorrect += 1

    
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    print(f"Accuracy: {100 * correct / total:.2f}%")'''

