import pandas as pd
from model import load_data, preprocess_data, calculate_features

def test_feature_calculation():
    data = load_data('Prueba-tecnica-GBM\\ejercicio 4\\data_customer_classification 1.xlsx')
    data = preprocess_data(data)
    customer_data = calculate_features(data)
    assert 'avg_trans_date' in customer_data.columns, "Missing 'avg_trans_date' feature"
    assert 'avg_amount' in customer_data.columns, "Missing 'avg_amount' feature"
    assert 'max_amount' in customer_data.columns, "Missing 'max_amount' feature"

if __name__ == '__main__':
    test_feature_calculation()
    print("Features are A-ok!!!")