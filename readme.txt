-> source code: ai.py
-> Features used: maximum and minimum price along with charges1 and charges2
-> models used: 
# model = Perceptron()
# model = svm.SVC()
# KNeighborsClassifier(n_neighbors=10)
# model = GaussianNB()

   KNeighborsClassifier is used which gives more closer results with just above features
   While training 60% data is used to train and rest 40% data is used for predictions from train.csv and got 78.2% accuracy
-> Removal of redund rows with '0' in missing coordinates are used in training as well as pridictions are used