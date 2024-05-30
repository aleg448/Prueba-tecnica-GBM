import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from model import load_data, preprocess_data, calculate_features, create_model, train_model, evaluate_model
#todo el modelo sardineado
def test_model_evaluation():
    data = load_data('Prueba-tecnica-GBM\\ejercicio 4\\data_customer_classification 1.xlsx')
    data = preprocess_data(data)
    customer_data = calculate_features(data)
    X = customer_data[["avg_trans_date", "avg_amount", "max_amount"]]
    y = customer_data["category"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=420)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = create_model()
    train_model(model, X_train_scaled, y_train)
    loss, accuracy = evaluate_model(model, X_test_scaled, y_test)
    assert accuracy >= 0.8, "Model accuracy is too low"
    assert loss <= 0.5, "Model loss is too high"
    print(f"Loss: {loss:.4f}")
    print(f"Accuracy: {accuracy:.4f}")

if __name__ == '__main__':
    test_model_evaluation()
    print("It runs!, It works!, but at what cost?")
