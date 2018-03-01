from sklearn.tree import DecisionTreeClassifier

features = [
    [140, 1, ],
    [130, 1, ],
    [150, 0, ],
    [170, 0, ],
]

labels = [ 0, 0, 1, 1, ]

clasifier = DecisionTreeClassifier()
clasifier = clasifier.fit(features, labels)

user_input: str = input("write a 2 number separated by white space (e.g. \"160 0\") describing weight (in gram) and feels (0 for bumpy and 1 for smooth): ")
sample = [ int(x) for x in user_input.split() ]

prediction = clasifier.predict([sample])
if prediction[0] == 1:
    print("it is an apple")
else:
    print("it is an orange")
