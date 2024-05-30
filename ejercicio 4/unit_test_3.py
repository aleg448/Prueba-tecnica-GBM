import pandas as pd
from model import load_data, preprocess_data

def test_data_preprocessing():
    data = load_data('Prueba-tecnica-GBM\\ejercicio 4\\data_customer_classification 1.xlsx')
    data = preprocess_data(data)
    assert 'trans_date_norm' in data.columns, "Missing 'trans_date_norm' column"
    assert data['trans_date_norm'].min() >= 0, "Normalized date should be larher than or equal to 0"
    assert data['trans_date_norm'].max() <= 1, "Normalized date should be less than or equal to 1"

if __name__ == '__main__':
    test_data_preprocessing()
    print("Weird dates succesfully normalized!!!")