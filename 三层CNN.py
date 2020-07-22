import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def get_data():
    (x_train,t_train),(x_text,t_text)=\
        load_mnist(normalize=True,flatten=True,one_hot_label=False)
    return x_text,t_text
def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network = pickle.load(f)
    return network

def sigmoid(x):
    return 1/(1+np.exp(x))

def predict():
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])
    return network
x,t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network,x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
