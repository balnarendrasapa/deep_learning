# Introduction 

### Classification

<center><img src="https://github.com/balnarendrasapa/deep_learning/assets/61614290/e8cbed55-caca-4181-a6cc-f623f1efd507" width="400"></img></center>

<br />

- Artificial Intelligence: Algorithm that mimicks the behaviour of human beings.
- Machine Learning: an algorithm that is able to learn from data to improve their performance at some task with experience
- Representation Learning: Learning how to represent the data. Representation learning, also known as feature learning, automatically extracts meaningful data representations to enhance machine learning tasks like classification and clustering. It eliminates the need for extensive manual feature engineering, advancing the field significantly.Examples of representation learning techniques include autoencoders, convolutional neural networks (CNNs) for image data, recurrent neural networks (RNNs) for sequential data, word embeddings (e.g., Word2Vec and GloVe) for natural language processing, and many others.
- Deep learning: Deep learning is a subfield of machine learning that focuses on the use of artificial neural networks, particularly deep neural networks, to model and solve complex tasks.

### Learning types

- Supervised learning : Training data includes desired outputs
- Unsupervised learning : Training data doesnot include desired outputs
- Weakly or Semi-supervised learning : Training data includes few outputs
- Reinforcement learning : Rewards from sequence of actions.

## Deep Learning

- Hierarchical Compositionality: we can make complex functions. Machine learning algorithms may not be able to capture the relationship in data because of their inability to handle complex nature of the data.
- End to End learning: there is no need for domain knowledge. things like feature extraction etc are handled inside the deep net itself. all we need to is to input the data to the trained model and we get the output.

<center><img src="https://github.com/balnarendrasapa/deep_learning/assets/61614290/40ab182b-765c-4e75-8f50-3b542e035052" width="600"></img></center>

- Shallow Model: Shallow models often require handcrafted feature engineering, where domain-specific knowledge is used to create relevant input features.
- Deep Model: Deep models can automatically learn relevant features from raw data, reducing the need for manual feature engineering. They can discover and extract features at different levels of abstraction.

<center><img src="https://github.com/balnarendrasapa/deep_learning/assets/61614290/0faa701f-163f-4969-aca9-cf7c0e845cc6" width="600"></img></center>


- feature extraction and classification are combined together inside the deep net

### Performance of Machine learning and Deep learning

<center><img src="https://github.com/balnarendrasapa/deep_learning/assets/61614290/0e815d15-f8a4-41f1-8cb7-4f4f6478b1db" width="600"></img></center>

- As the size of the data increases, the performance of the deep learning model increases.
- This is due to the fact that machine learning algorithms fail to capture the complex relationship in data.
- For smaller data, the performance of the machine learning algorithms is higher than deep learning. this is due to overfitting of the data in deep learning. Also there is not enough data so that deep net may not generalize enough. which results in decreased accuracy
- The performance increases, in the case of deep learning, due to the ability of the deep learning to capture the complex relationship with ability of hierarchical compositionality.

### Problems with Deep learning

- All interesting problems are non-convex in nature.

> Convex functions: imagine a parabola `y = x^2`. Now lets pick to points on the curve and connect them. in this parabola, the line segment always lies above the graph. this property is called chord property

> Concave functions: imagine a parabola `y = -x^2`. Now lets pick to points on the curve and connect them. in this parabola, the line segment always lies below the graph.

> Non-convex functions have regions of both convexity and concavity, making them generally irregular and challenging to optimize, while non-concave functions are specifically those non-convex functions that do not have concave regions.

- Lack of interpretability: Hard to track down what is failing. in end to end systems, it is hard to know why things are not working

### XOR Problem

- The XOR problem is a classic problem in the field of artificial intelligence and deep learning. It serves as a simple yet illustrative example to highlight the limitations of linear models and the power of neural networks, particularly multi-layered networks.

- The XOR (exclusive OR) problem is defined as follows:

Input: You have two binary inputs, usually denoted as A and B, which can each take on values of 0 or 1.
Output: The goal is to predict the XOR of these two inputs. The XOR operation returns 1 if the inputs are different (e.g., 0 XOR 1 = 1 or 1 XOR 0 = 1) and 0 if the inputs are the same (e.g., 0 XOR 0 = 0 or 1 XOR 1 = 0).
The XOR function is not linearly separable, which means you cannot draw a straight line to separate the 0s from the 1s in a two-dimensional space of inputs A and B. Linear models, such as logistic regression or single-layer perceptrons, fail to solve the XOR problem because they can only model linear relationships.

- However, the XOR problem can be successfully solved using deep neural networks. Deep learning models, specifically multi-layered feedforward neural networks, can learn complex non-linear relationships between inputs and outputs. In the case of XOR, a two-layer neural network (one hidden layer between the input and output layers) can solve the problem effectively.
