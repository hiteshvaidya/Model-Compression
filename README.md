# Model-Compression
This is my final year project of Bachelor of Engineering. Its still incomplete though. I am trying to replicate the research paper "Deep Compression" by Song Han et. al. This paper received best paper award in ICLR 2016.

# Overview
The original code by the author (Song Han) is in caffe. I tried using caffe. But caffe is waste of time. So I decided to implement the code in tensorflow. Even in tensorflow some things are difficult to implement. I am still figuring out some ways to completely implement the idea. I am sorry but I didn't get time to properly add comments to the code. So you might find it difficult to understand the code. But its not that difficult I assure you. I will soon add proper comments and algorithm in this repo. I started just the 'pruning' part of the paper. For 'Quantization' part you may refer to the tensorflow link I have provided in the Resources section.

# Resources
1) Deep Compression research paper - https://arxiv.org/abs/1510.00149
2) Video Explaining the paper by its author - https://youtu.be/vouEMwDNopQ
3) Github repository of the author - https://github.com/hiteshvaidya/Deep-Compression-AlexNet
4) A short video explaining model compression - https://www.youtube.com/shared?ci=1ivgFE--PBY (Ignore the DSD and part)
5) How to use Alexnet in Tensorflow - https://kratzert.github.io/2017/02/24/finetuning-alexnet-with-tensorflow.html
6) Quantization of Neural Network by using native Tensorflow operations - https://www.tensorflow.org/performance/quantization
7) Video explaining how to build the neural network which I am using - https://youtu.be/qVwm-9P609I

# Dependencies
* python
* numpy
* tensorflow
* future
* pickle

# Usage
I have provided implementation of two algorithms for pruning. They are: `reduce.py` and `mnist_cnn_<>.py`

1) `run reduce.py`
Reduce folder contains reduce.py and the screenshot of the output. run `python reduce.py` in terminal and the program would run. `weights.csv` file contains a small list of weights and the output of neurons in the format `weight x output_of_neuron`
weights.csv can be updated according to your choice. This algorithm however works for just a single neuron and not an entire neural network.<br />
__LOGIC:__
It uses the logic of subset selection/0-1 knapsack

2) `run mnist_cnn_1.0.py`
This program is a small convolutional neural network with three hidden layers. At last it saves all the variables using tf.Saver(). Also, I have tried to pickle all the weights for further use.
For now you can ignore `minst_cnn_1.2.py`. It reuses the variables stored by `mnist_cnn_1.0.py`. The code is not complete.<br />
**LOGIC:**
The logic behind this program is straight from the Deep Compression research paper. When you get a trained neural network i.e. `mnist_cnn_1.0.py` you remove the edges from it by using a threshold value. Now what exactly do you do in the program to remove the edges? well according to me, I have converted the weight values of such edges to 'NaN'. This is so that it does not change its value in the future when the neural network is retrained (given in the paper). If you just assign zero to these pruned edges, the retraining process might either regenerate the pruned edges or run with a low accuracy.
But even by turning them to 'NaN' I don't know how successful the neural network be after retraining. Because 'NaN'*<any_number> = 'NaN'. So if matrix multiplication while retraining makes other weights as 'NaN' then the neural network would collapse. But all these things would be clear only when the program is actually tested.<br />
PS: The code to make the weight values 'NaN' can be found in `test.py`
