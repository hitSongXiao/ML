import matplotlib.pyplot as plt
import numpy as np
import math
import os
m = 9  # 阶数
num = 100  # 训练数据个数
test_num = 100 #测试数据个数
l = math.e**(-20)


def draw(A, B, W):
    X = np.linspace(0, 1, 100)
    X_test = np.random.random_sample(test_num,)
    Y_test = np.sin(X_test*2*np.pi) + np.random.normal(0,0.1,test_num)
    plt.subplot(121)
    plt.title("Best fit without regular terms")
   # plt.text(1,0.6,"loss = " + loss(X_test,Y_test,W), fontsize = 20)
    plt.plot(X, answer(X, W), label="y = f(w,x)")
    plt.plot(X, np.sin(X*np.pi*2), label="y=sin(2x)")
    plt.scatter(A, B, color="red", s=15, label="train")
    plt.scatter(X_test,Y_test, color = "green", s = 15, label = "test")
    plt.legend()
    plt.show()


def opti(X, Y):
    X_T = X.transpose()
    XTX = np.dot(X_T, X)
    oppo = np.linalg.inv(XTX)
    XTY = np.dot(X_T, Y)
    return np.dot(oppo, XTY)


def opti_reg(X, Y):
    X_T = X.transpose()
    XTX = np.dot(X_T, X)
    oppo = np.linalg.inv(XTX+(np.eye(m+1))*l)
    XTY = np.dot(X_T, Y)
    return np.dot(oppo, XTY)


def loss(X_test,Y_test,W):
    X = np.linspace(1, 1, num)
    for i in range(m):
        X = np.vstack([X, X_test**(i+1)])
    X = X.transpose()
    Y2 = np.dot(X, W)
    L = Y_test-Y2
    return np.dot(L.transpose(), L)


def answer(x, W):
    X = np.linspace(1, 1, x.size)
    for i in range(m):
        X = np.vstack([X, x**(i+1)])
    X = X.transpose()
    return np.dot(X, W)


x = np.linspace(0, 1, num)
X = np.linspace(1, 1, num)
for i in range(m):
    X = np.vstack([X, x**(i+1)])
X = X.transpose()
Y = np.sin(x*2*np.pi) + np.random.normal(0, 0.1, (x.size,))  # 添加噪声的Y
W = opti_reg(X, Y)
print(W)
draw(x, Y, W)
