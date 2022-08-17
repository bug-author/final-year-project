# Motion forecasting for vehicles

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
![unnamed](https://user-images.githubusercontent.com/48406637/185078356-cd2689e3-82af-4fcb-92e2-bece10b747a5.png)

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

![unnamed (2)](https://user-images.githubusercontent.com/48406637/185089492-2d211069-d33d-4f1c-8c49-43fef81c4a3c.png)

![unnamed (3)](https://user-images.githubusercontent.com/48406637/185089441-16ddf296-1b9e-4ed8-a589-02b7a99eb116.png)


- Vehicle speeds are in in the form of a time series range. 
- Some of the vehicles have peaks when the trip is initialized, and this needs to be taken care of. *This is because it is a difficult task for time series regression algorithms to predict and generalize peaks in the data, especially when there are no seasonality trends in the data and it is completely random.* 
- There should be some stationarity checks applied to this time series data for getting more insights before starting the development of the model. These tests are a part of the next phase in the pipeline.






### Algorithm
## Results
