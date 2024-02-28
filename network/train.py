from dataset.mnist import load_mnist
import numpy as np
from network.gradient_simplenet import Net

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=True)

train_loss_list = []

hyper_params = {
    "epoch": 10,
    "train_size": x_train.shape[0],
    "batch_size": 128,
    "learning_rate": 1e-2,
}
network = Net(input_size=784, hidden_size=64, output_size=10)   # net 생성

for i in range(hyper_params["epoch"]):  # epoch만큼 학습을 돌린다
    mask = np.random.choice(hyper_params["train_size"], hyper_params["batch_size"]) # 배치를 생성(train_size에서 batch_size만큼 수를 뽑음)
    x_batch = x_train[mask]
    t_batch = t_train[mask]

    grad = network.numerical_gradient(x_batch, t_batch)
    for key in grad.keys():     # grad.keys = W1, b1, W2, b2
        network.parameter[key] -= hyper_params["learning_rate"] * grad[key]     # 각각의 파라미터들에 대해서 갱신
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    print(f"Epoch: {i}, Loss: {loss}")
