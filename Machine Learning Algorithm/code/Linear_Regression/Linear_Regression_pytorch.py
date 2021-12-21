import torch
import numpy as np
import torch.utils.data as Data
from torch import nn, optim
from torch.nn import init


class LinearNet(nn.Module):
    def __init__(self, num_inputs):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(num_inputs, 1)

    def forward(self, x):
        y = self.linear(x)
        return y


def main():
    # y = x_1 * w_1 + x_2 * w_2 + b
    num_inputs = 2
    num_examples = 1000
    true_w = [2, -3.4]
    true_b = 4.2
    features = torch.tensor(
        np.random.normal(0, 1, (num_examples, num_inputs)),
        dtype=torch.float
    )
    labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b + torch.tensor(
        np.random.normal(0, 0.01, size=(num_examples,)),
        dtype=torch.float
    )
    print(labels.shape)

    batch_size = 10
    dataset = Data.TensorDataset(features, labels)
    date_iter = Data.DataLoader(dataset, batch_size, shuffle=True)
    for X, y in date_iter:
        print(X, y)
        print(X.shape)
        print(y.shape)
        break

    # net = LinearNet(num_inputs)
    net = nn.Sequential(
        nn.Linear(num_inputs, 1)
    )
    print(net)
    for param in net.parameters():
        print(param)

    # model parameters initialize
    init.normal_(net[0].weight, mean=0, std=0.01)
    init.constant_(net[0].bias, val=0)

    loss = nn.MSELoss()

    optimizer = optim.SGD(net.parameters(), lr=0.03)
    print(optimizer)

    num_epochs = 3
    for epoch in range(num_epochs):
        for X, y in date_iter:
            output = net(X)
            l = loss(output, y.view(-1, 1))
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        print(f'epoch {epoch + 1}, loss: {l.item()}')

    dense = net[0]
    print(true_w, dense.weight)
    print(true_b, dense.bias)


if __name__ == '__main__':
    main()
