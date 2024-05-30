import pandas as pd
from model import load_data

def test_data_loading():
    data = load_data('Prueba-tecnica-GBM\\ejercicio 4\\data_customer_classification 1.xlsx')
    assert len(data) > 0, "Data loading failed"
    assert 'customer_id' in data.columns, "Missing 'customer_id' column"
    assert 'trans_date' in data.columns, "Missing 'trans_date' column"
    assert 'tran_amount' in data.columns, "Missing 'tran_amount' column"

if __name__ == '__main__':
    test_data_loading()
    print("Your data loaded correctly!!")