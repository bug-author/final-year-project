# Motion forecasting for vehicles

## A note about file structure
- `prelude/` introductory work
- `api/` A FastAPI api for serving dataset
- `training/` code (noteboks and helper scripts) for training the model
- `clustering` code for second phase i.e. optimal cluster formation
---
- Presentation slides can be found [here](https://docs.google.com/presentation/d/1_vtB7uUEUL9otgZAAquNeakVFEcEkK-RATCQOFo6aog/edit?usp=sharing)

## Block Diagram 
![unnamed (0)](https://user-images.githubusercontent.com/48406637/185078662-91299f99-64fb-4d9a-a4de-9c7666c83de2.png)


## Problem Statement
Vehicular networks enable vehicles to communicate with each other and with roadside infrastructure. These smart vehicles are constrained in terms of computational capacity. Task offloading is a technique to perform computation intensive tasks in a coordinated manner by sharing the task load.

We have proposed an efficient technique for task offloading to reduce average computation time and the probability of failed task computations.

In summary, this project revolves around:
- Lack of computational capacity in smart vehicles
- Latency issues with cloud
- Task offloading decisions 





## Data Pipeline

<div align="center">

 ![unnamed](https://user-images.githubusercontent.com/48406637/185078356-cd2689e3-82af-4fcb-92e2-bece10b747a5.png)

</div>


### Data
- Dataset is generated using the [SUMO](https://www.eclipse.org/sumo/) traffic simulator.
- Different variants from the dataset are served through an API developed with FastAPI on Heroku.

----

### Exploratory Data Analysis
Obersvations and suggestions for position data
![unnamed (1)](https://user-images.githubusercontent.com/48406637/185089507-4b04bc10-26ff-417b-9dd7-48727b39284a.png)

- Vehicle positions are almost purely linear data. 
- A correlation was speculated between the positions of some vehicles in the network duing dataset generation, the EDA phase supported this speculation. 
- Positions start from 0 for each vehicle and are in the range of a continuous real interval different for each vehicle. 

These observation hint towards using suitable standardization or normalization techniques since Deep Learning models work better on standardized data.

Obersvations and suggestions for speed data

<br/>

![unnamed (2)](https://user-images.githubusercontent.com/48406637/185089492-2d211069-d33d-4f1c-8c49-43fef81c4a3c.png)

![unnamed (3)](https://user-images.githubusercontent.com/48406637/185089441-16ddf296-1b9e-4ed8-a589-02b7a99eb116.png)


- Vehicle speeds are in in the form of a time series range. 
- Some of the vehicles have peaks when the trip is initialized, and this needs to be taken care of. *This is because it is a difficult task for time series regression algorithms to predict and generalize peaks in the data, especially when there are no seasonality trends in the data and it is completely random.* 
- There should be some stationarity checks applied to this time series data for getting more insights before starting the development of the model. These tests are a part of the next phase in the pipeline.

----
### Data Preprocessing
Before applying some preprocessing techniques, some tests were performed to get detailed insights. Stationarity checks were ran on the dataset.

Observations
- Standard deviation is constant and therefore the variance is constant which should be the case for a time series to be stationary. 
- However, some vehicles violated the condition of test statistics by having a value lesser than the critical values. 

![unnamed (4)](https://user-images.githubusercontent.com/48406637/185091383-2c872dc1-6f74-4849-ba2c-bf1d3fc3a538.png)

<div align="center">
 
![unnamed (5)](https://user-images.githubusercontent.com/48406637/185091406-f6a0335e-923c-4aa6-852f-6614adf94595.png)

</div>
 
Therefore, the data failed the stationarity test and needed to be made stationary before training.

- Lag1 Differencing was applied to the dataset to make it stationary.
- Vector normalization was also applied to the training data

![unnamed (6)](https://user-images.githubusercontent.com/48406637/185091423-f2687926-7611-426b-a51a-ce55d38b2ec4.png)

---
### Data Splitting
- Data is splitted as: 85% train - 15% test
- Data is also shaped as *(number_of_time_steps, number_of_features)* in order for it to train on Sequential DL Models (RNN, LSTM, GRU)

---
### Model Development
- The models is developed using Keras
- After comparing the several models that were developed, the model with best results (Dropout Regularized LSTM) was chosen

<div align="center">
 
![image](https://user-images.githubusercontent.com/48406637/185092722-f9435ea1-be30-4a58-b8c3-c8d6cf897527.png)

 </div>

- Architecture of chosen model


<div align="center">
 
![unnamed (7)](https://user-images.githubusercontent.com/48406637/185092551-855b085e-c240-4ffe-a339-94ce9bd52bf6.png)

 </div>
 
--- 
### Clustering
- The forecasts from the model are given to the clustering algorithm which figures out the optimal cluster formation for a given test vehicle and constraints.

---
### Data Preprocessing
- The speed values are quantized upto 3 decimal places.

---
### Feature Engineering
Vehicle Positions were dropped from the training data because of these observations.

- Position data is always linearly increasing while the speed data is a time series. 
- The dataset simulated by SUMO was set to output readings every one second so we can easily derive the positions after forecasting. 
 
#### This decision also reduces the neural network computation since there would now be 20 features for training instead of 40 in a 20 vehicle network.
---
### Mean Computation Time Calculation
This phase is explained in the Algorithm section.


### Algorithm

![image](https://user-images.githubusercontent.com/48406637/185940611-d17e214b-fc83-4e3e-b736-16c59b64e6aa.png)

---

![image](https://user-images.githubusercontent.com/48406637/185940972-692df289-db2a-49da-971e-10abf521c0e8.png)

## Results
<p float="left">

 <img src=https://user-images.githubusercontent.com/48406637/185941529-3109114a-83a2-47f6-95ea-dd5ddc4664f2.png width=500px/>

<img src=https://user-images.githubusercontent.com/48406637/185941425-bcdc3e8d-5eb9-4b41-a06c-fe12f86746d8.png width=500px/>

</p>
