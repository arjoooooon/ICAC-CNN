## still a wip for some rzn it's giving 100% accuracy lol 
# inspired from prof dodds rf guide




import numpy as np      
import pandas as pd     


from sklearn import model_selection
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from math import sqrt


filename = "CA_LA_NORTH_CLEANED/o3_data.csv"
df_tidy = pd.read_csv(filename)      

print(f"df_tidy.shape is {df_tidy.shape}\n")
df_tidy.info() 


ROW = 0
COLUMN = 1
df_model1 = df_tidy.drop( 'datetime_local', axis=COLUMN )
df_model1 = df_model1.drop( 'year', axis=COLUMN )

COLUMNS = df_model1.columns            
print(f"COLUMNS is {COLUMNS}\n")  
print(f"COLUMNS[0] is {COLUMNS[0]}\n")


COL_INDEX = {}
for i, name in enumerate(COLUMNS):
    COL_INDEX[name] = i  


A = df_model1.to_numpy()   
A = A.astype('float64')
NUM_ROWS, NUM_COLS = A.shape

X_all = A[:,0:3]  # X (features)
y_all = A[:,3]    # y (labels)



indices = np.random.permutation(len(y_all))  # indices is a permutation-list

# we scramble both X and y, necessarily with the same permutation
X_permed = X_all[indices]              
y_permed = y_all[indices]              
print(f"The scrambled labels/species are \n {y_permed}")
print(f"The corresponding data rows are \n {X_permed[0:5]}")


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.2, random_state=42)

print(f"training with {len(y_train)} rows;  testing with {len(y_test)} rows\n" )

print(f"Held-out data... (testing data: {len(y_test)})")
print(f"y_test: {y_test}\n")
print(f"X_test (few rows): {X_test[0:5,:]}")  # 5 rows
print()
print(f"Data used for modeling... (training data: {len(y_train)})")
print(f"y_train: {y_train}\n")
print(f"X_train (few rows): {X_train[0:5,:]}")  # 5 rows



best_depth = 9 
dtree_model = tree.DecisionTreeRegressor(max_depth=best_depth)


dtree_model.fit(X_train, y_train)      


predicted_labels = dtree_model.predict(X_test)
actual_labels = y_test



def compare_labels(predicted_labels, actual_labels):
    """ a more neatly formatted comparison """
    NUM_LABELS = len(predicted_labels)
    num_correct = 0
    
    for i in range(NUM_LABELS):
        p = int(round(predicted_labels[i]))         # round protects from fp error 
        a = int(round(actual_labels[i]))
        result = "incorrect"
        if p == a:  
            result = ""       
            num_correct += 1  

     

    print()
    print("Correct:", num_correct, "out of", NUM_LABELS)
    return num_correct


predicted_labels = dtree_model.predict(X_test)
actual_labels = y_test


compare_labels(predicted_labels,actual_labels)




