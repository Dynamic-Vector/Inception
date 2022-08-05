<div align="center"> 
  <h1>Inception </h1>



   

 
</div>
<div align="center"> 
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
  
 
 </div> 

## About:
It is a machine learning model which can autoplay any car driving game and can be used as a reference for autonomous driving.



## Models:
**Model-1:** This model uses *Canny Edge Detection* technique to detect edges and then by using the slopes of the detected edges lines the model take left or right turn depending upon the weather slope is negative or positive. *OpenCV* and Basic *If-else* condition is used in this model.I played this model on GTA-5.

**Model-2:** This model uses the deep learning technique *Convolutional Neural Networks(CNN)* to learn driving.With the help of *OpenCV*  i created a custom dataset by driving car for several minutes and then train that custom dataset to the neural networks.Used *Tensorflow* for neural networks.

## Description:
data_collect.py-Used to create custom data.<br>
directkeys.py-Used to map keys according to Direct-X framework.<br>
getkeys.py-Used to detect input keys by using Windows API.<br>
motion.py-Used for motion detection.<br>
neural.py-File where Neural network is written.<br>
train_data.py-Used to train model with custom dataset.<br>
test_data.py-Used to test the trained model.<br>

## How to Use:
* First clone the repository
* Install the requirements.txt file
* Run data_collect to create custom dataset.
* Run train_data to train the data.
* Run test_data to play it on any car driving game.

## Requirements:
* CPU-Atleast Quadcore or Octacore.
* GPU-Dedicated, with as much memory as possible.
* RAM: at least 16 or 32 GB.

## Recommendations:
* Create custom data for atleast 25-30 min.The accuracy depends totally on how much you train the model.
* Use in games which has W,A,S,D Keys as controls.(You can change code to play with desired controls).
* For pausing the the model press P.

## Sample:











## Support
⭐ **Please Star  and share the project. Thanks!** ❤️ 
