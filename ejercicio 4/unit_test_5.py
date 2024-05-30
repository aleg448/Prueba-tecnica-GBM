from keras.models import Sequential
from keras.layers import Dense
from model import create_model

def test_model_architecture():
    model = create_model()
    #2 caused we added "ReLu" and "softmax"
    assert len(model.layers) == 2, "Incorrect number of layers in the model"
    assert model.input_shape == (None, 3), "Incorrect input shape of the model"

if __name__ == '__main__':
    test_model_architecture()
    print("You have a pretty code cathedral!!!")