<div align="center"> 
  <h1>Inception </h1>



   

 
</div>
<div align="center"> 
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white">
  
 
 </div> 

## About:
It is a machine learning model which can play car and bike driving game and can be used as a reference for self driving vehicle.



## Models:
**Model-1:** This model uses *Canny Edge Detection* technique to detect edges and then by using the slopes of the detected edges lines the model take left or right turn depending upon the whether slope is negative or positive. *OpenCV* and Basic *If-else* condition is used in this model.I played this model on GTA-5.

**Model-2:** This model uses the deep learning technique *Convolutional Neural Networks(CNN)* to learn driving.With the help of *OpenCV*  i created a custom dataset by driving car for several minutes and then train that custom dataset to the neural networks.Used *Tensorflow* for neural networks.

## Description:
**data_collect.py**-Used to create custom data.<br>
**grabscreen.py**-Used to detect the screen.<br>
**motion.py**-Used for motion detection.<br>
**neural.py**-File where Neural network is written.<br>
**train_data.py**-Used to train model with custom dataset.<br>
**test_data.py**-Used to test the trained model.<br>
**directkeys.py**-Used to map keys according to Direct-X framework.<br>
**getkeys.py**-Used to detect input keys by using Windows API.<br>


## How to Use:
* First clone the repository
* Install the requirements.txt file<br>
* **Model-1:**
* Run main.py file to play.<br>
* **Model-2:**
* Run data_collect to create custom dataset.
* Run train_data to train the data.
* Run test_data to play it on any car driving game.
* For pausing the model press P.


## Requirements:
* CPU-Atleast Quadcore or Octacore.
* GPU-Dedicated, with as much memory as possible.
* RAM: at least 16 or 32 GB.

## Recommendations:
* Use in games which has W,A,S,D Keys as controls.(You can change code to play with desired controls).
* Create custom data for atleast 25-30 min.The accuracy depends totally on how much you train the model.
* In neural.py there are different types of neural networks you can be use to train(must try and check accuracy).

## Sample:
<div align="left">
<h5>Edge Detection:</h5>
<img src="https://github.com/Dynamic-Vector/Inception/blob/master/res/edge%20detection.gif" width=100% height=400>
<h5>Model-1:</h5>
<img src="https://github.com/Dynamic-Vector/Inception/blob/master/res/v1.gif" width=100% height=400>
<div align="left">
<h5>Model-2:</h5>
<img src="https://github.com/Dynamic-Vector/Inception/blob/master/res/cnn_V2.gif" width=100% height=400>
</div>

## Support
⭐ **Please Star  and share the project. Thanks!** ❤️ 
