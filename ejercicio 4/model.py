#load pandas to the rescue (sklearn 2)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
#functions for unit tests
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

def preprocess_data(data):
    data['trans_date'] = pd.to_datetime(data['trans_date'], format='%d-%b-%y')
    data['trans_date_norm'] = (data['trans_date'] - data['trans_date'].min()) / (data['trans_date'].max() - data['trans_date'].min())
    return data

def calculate_features(data):
    customer_data = data.groupby("customer_id").agg({"trans_date_norm": "mean", "tran_amount": ["mean", "max"]})
    customer_data.columns = ["avg_trans_date", "avg_amount", "max_amount"]
    customer_data = customer_data.reset_index()
    customer_data["category"] = pd.qcut(customer_data["avg_amount"], q=3, labels=[0, 1, 2])
    customer_data["category"] = customer_data["category"].astype(int)
    return customer_data

def create_model():
    model = Sequential()
    model.add(Dense(8, activation="relu", input_shape=(3,)))
    model.add(Dense(3, activation="softmax"))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def train_model(model, X_train, y_train, epochs=50, batch_size=32):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

def evaluate_model(model, X_test, y_test):
    loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
    return loss, accuracy  
#dunder to run the funcs
if __name__ == '__main__':  
    #load data
    data = load_data('Prueba-tecnica-GBM\\ejercicio 4\\data_customer_classification 1.xlsx')
    print(data.head())
    #normalize trans date
    data = preprocess_data(data)
    print(data[['trans_date', 'trans_date_norm']].head())
    #Calculate features
    #add useful features
    #label data
    customer_data = calculate_features(data)
    print(customer_data.head())
    #split features
    X = customer_data[["avg_trans_date", "avg_amount", "max_amount"]]
    y = customer_data["category"]
    print(X.head())
    print(y.head())
    #split in sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=420)

    #Normalize/scale? the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    #numpy not pandas >:3
    print(X_train_scaled[:5])
    print(X_test_scaled[:5])
    #build model
    model = create_model()
    model.summary()
    #train
    train_model(model, X_train_scaled, y_train)
    #evaluate loss and accuracy, verbose to track run
    loss, accuracy = evaluate_model(model, X_test_scaled, y_test)
    print(f"Loss: {loss:.4f}")
    print(f"Accuracy: {accuracy:.4f}")
    #profits