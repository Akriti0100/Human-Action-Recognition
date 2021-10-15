  <h1 align="center">
  <br>
  <img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/Jogging.gif" alt="Action" width="200">
  <br>
  HUMAN ACTION RECOGNITION
  <br>
</h1>

<!--<h3 align="center">Visit Website: <a href="https://akriti.pythonanywhere.com/" target="_blank"> antidote.com </a></h3>-->

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-3.8.1-blue)
![Version](https://img.shields.io/badge/version-1.0.0-orange)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-%20GPL--3.0%20-blue)](https://github.com/Akriti0100/Antidote/blob/main/LICENSE.md)

<div align="justify">
<!-- # ?? Project overview -->

> Computers are getting better at solving complex problems due to the advances in computer vision. This project uses deep learning for Video Recognition - given a set of labelled videos, train a model so that it can give a label/prediction for a new video. Here, the label might represent what is being performed in the video, or what the video is about. The aim of this project is to create a model that can identify the basic human actions like running, jogging, 
walking, clapping, hand-waving and boxing.
</div>

<p align="center">
  <a href="#project-scope">Project Scope</a> •
  <a href="#data-analysis">Data Analysis</a> •
  <a href="#model-used">Model Used</a> •
  <a href="#input-output-screenshots">I/O Screenshots</a> •
  <a href="#methodology-flowchart">Methodology Flowchart</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

<div align="justify">
  
## Project Scope

There are potentially a lot of applications of video recognition :

* Real-time tracking of an object
  - This includes tracking the location of an object (like a vehicle) or a person from the video recorded by a CCTV.
* Learning the patterns involved in the movement of humans
  - Training a model which can learn how humans perform different activities like walking, running etc. would help in proper functioning of mechanisms in autonomous robots.

</div>

<div align="justify">
  
## DATA ANALYSIS

* The video dataset contains six types of human actions `(boxing, handclapping, handwaving, jogging, running and walking)` performed multiple times by 6 different subjects in 4 different scenarios 
  - outdoors
  - outdoors with scale variation
  - outdoors with different clothes
  - indoors
* The videos are captured at a frame rate of 25fps and each frame is down-sampled to the resolution of 160x120 pixels. 
  - Loading each video in a NumPy array yields the shape of video in the form of a tuple 
      - (No. of Videos, No. of frames, height, width, channels)
  - Each video consists of 3 channels i.e. R(red), G(green), B(blue)
* The dataset contains 144 videos – 24 videos for each of the 6 categories mentioned above.

</div>

<div align="justify">

## Model Used

* Convolutional Neural Network [Refer: <a href="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/ActionRec/actions/model.json">`model.json`</a> for implementation and <a href="https://drive.google.com/file/d/1-9qVHM-f3FWYir2KCwPUUE0Tar5Ll_mi/view?usp=sharing">`Model.weights.best.hdf5` </a> for weights of the model]
  - CNNs are best suited for the task of image recognition. The importance of these networks is that it encodes the content of an image that can be flattened into 1-dimensional array.
  - The Convolutional layers are responsible for generating feature maps using kernels which find patterns in different regions of the image. These feature maps can be stacked into a 3-d array thus increasing the depth of the input image.
  - These layers are followed by the Pooling layers, that reduce the spatial dimensions of the output obtained from the convolutional layers.
  - This model resulted in an accuracy of `54.17 %` on the test dataset using 'nadam' optimizer.
  

```
  - The CNN model used in this project is depicted below. 
  - Multiple convolutional and pooling layers are stacked together.
  - These are followed by some fully-connected layers, where the last layer is the output layer. 
  - Output layer contains 6 neurons (one for each category).The network gives the probability corresponding to each class.
  
```
<img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/cnn_model.png" alt="Model" width="500" height="600">
<br><br>
<p>The training and validation loss graph of the above sequential CNN model is as shown below:</p>
<img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/modelLoss.png" alt="Loss" width="500">
 
</div>

<!--<div align="justify">-->
 
<!-- # ?? Project overview -->
<!--## Project Scope

> Everything today is moving towards digitalization. This platform designed will increase the efficiency of the hospitals and bring the specialists from the nooks and corners of the country available at a single platform. 
>
> It will help overcome the challenge of increased drop rate in the regular patient visits and also help patients to consult the doctors in case of emergency situations by fixing an appointment without the need to visit the hospital. 
>
> This would also help to overcome the problem of deficiency of human resources in the health sector which is prevalent at several levels such as between regions, between rural and urban areas and between private and public sectors. It's a platform to consult the health care specialists in the respective fields thus, bridging the gap between different sections of the society. 
>
> Apart from these, it aims to reduce the challenges faced by people who are looking online for health information regarding diseases, diagnosis and different treatments.
 
</div>-->

<div align="justify">
 
## Input-Output Screenshots
 
![screenshot](https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/Input-Output%20Screenshots.gif)
  
For details, you may also refer the <a href="https://github.com/Akriti0100/Human-Action-Recognition/tree/main/Input-Output%20Screenshots">`Input - Output Screenshots`</a> folder.

</div>

<div align="justify">
 
## Methodology Flowchart
 
<img src="https://github.com/Akriti0100/Human-Action-Recognition/blob/main/images/WorkFlow.jpg" alt="Flowchart">

</div>

<div align="justify">
 
## How To Use

To clone and run this application, you’ll need `Git` installed on your computer. <br>
From your command line:

```
# Clone this repository
$ git clone https://github.com/Akriti0100/Human-Action-Recognition.git

# Create a virtual environment
$ python3 -m venv <environment-name>

# Activate the virtual environment
$ <environment-name>/bin/activate

# Install dependencies
$ pip3 install -r requirements.txt

# Go into the repository
$ cd ActionRec

# Run the app
$ python manage.py runserver
```

</div>

<div align="justify">
 
## License
 
This project is free and open-source software licensed under the `GPL-3.0 License`.

</div>
