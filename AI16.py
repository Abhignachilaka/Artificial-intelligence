import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.biases_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.biases_output = np.zeros((1, output_size))
    def forward(self, inputs):
        self.hidden_activation = sigmoid(np.dot(inputs, self.weights_input_hidden) + self.biases_hidden)
        self.output = sigmoid(np.dot(self.hidden_activation, self.weights_hidden_output) + self.biases_output)
        return self.output
    def train(self, inputs, targets, learning_rate=0.1, epochs=10000):
        for epoch in range(epochs):
            self.forward(inputs)
            error = targets - self.output
            output_delta = error * sigmoid_derivative(self.output)
            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * sigmoid_derivative(self.hidden_activation)
            self.weights_hidden_output += self.hidden_activation.T.dot(output_delta) * learning_rate
            self.biases_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.biases_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")
if __name__ == "__main__":
    input_size = 2
    hidden_size = 4
    output_size = 1
    nn = NeuralNetwork(input_size, hidden_size, output_size)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])
    nn.train(inputs, targets)
    predictions = nn.forward(inputs)
    print("\nFinal Predictions:")
    print(predictions)
