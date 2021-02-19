# NYC Car Accident Predictor
![traffic](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/traffic.jpg?raw=true)

**Davida Rosenstrauch**

February 2021

# Business Problem
Car accidents are one of the leading causes of death and injury in the United States. They also require significant resources from police departments, EMT services, and hospitals. Being able to accurately predict the number of car accidents within a given area on a given day would help individuals assess their level of risk when going out on the road and help these institutions properly prepare and allocate resources.

# Data
Data was collected from the NYC Open Data Motor Vehicle Collisions dataset and supplemented by the Nominatim reverse geocoding API. This API provided address information for each accident location based on its GPS coordinates. The entire dataset consists of 1.75 million car accidents in New York City between July 1, 2012 and January 29, 2021.

# Methods
Time series models were performed independently on each borough, appraoched in order of accident frequency. The baseline model for each borough was an ARIMA model, supplemented by ARIMAX, SARIMA, and SARIMAX models, and finally with a Facebook Prophet model. Predictions of the best-performing models in each borough were deployed on a Streamlit dashboard for public use.

# Pandemic Impacts
![full_line](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/full_line.png?raw=true)

As we can see in the above visualization of our entire dataset, the COVID-19 pandemic has had a huge impact on car accident frequency in New York City, starting in march of 2020. In order to understand how to make as accurate predictions as possible following this anamalous year, I conducted research in three key areas, which yielded the following information. Sources are included at the end of this README.

### 1. COVID-19 Projections
Since car accidents are negatively correlated with COVID cases, looking at COVID case projections can give us insight regarding accident count.

- Several models predict a plateau of cumulative COVID deaths by June, with a linear trend until then.

- Several models predict approximaely 80% poulation COVID immunity in NYC by June, with a linear trend until then.

### 2. Transportation Projections

Since more accidents occur with more cars on the road, looking at projections relating to traffic patterns and transportation in general will impact our own as well.

- NYC has planned 40% service cuts for its subway and bus service by 2022. It is expected that more people will drive as compared with pre-COVID transportation patterns, but this plan in cuts could also be indicative of fewer people traveling on a daily basis overall.

- There has been a rise in pedestrian streets, which has removed cars from downtown neighborhoods. These are expected to stay indefinitely, and could impact the number of cars on the road in more urban areas of NYC.

### 3. Workforce Projections

As more people return to working in offices, the number of cars on the road will increase.

- 77% of office employees are currently working from home at least 1 day per week. 55% expect to continue doing so indefinitely.

- Estimates show that 10-20% of the US workforce could work from home indefinitely.

## The Plan
While it is impossible to predict exactly what will happen over the coming months, based on the above information the plan to create as accurate an accident count prediction as possible is:

1. The time series model will be based on pre-COVID data.
2. Predictions will be aplied starting on July 1, 2021.
3. Predictions based on pre-COVID data will be diminished by 25%.
4. Between the end of the current dataset, January 2021, and the time series model starting in July, predictions will be applied linearly as a connection.

This method was used for all five boroughs, except Staten Island. As we will see, Staten Island's accident data was much less affected by the pandemic than the other boroughs' and is almsost back to pre-COVID numbers. Therefore, I similarly predicted results based on pre-COVID data, but applied them starting on February 28, 2021 and without diminishing them as I did for the other boroughs.

# Exploratory Data Analysis

### Where Do Accidents Occur?
Viewing borough-specific data in both bar-chart and time-based form shows that Brooklyn and Queens are the boroughs with the most car accidents, and Staten Island with the fewest:

![borough_bar](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/borough_bar.png?raw=true)

![borough_line](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/borough_line.png?raw=true)

Mean daily accident frequencies of the ten zip codes with the most car accidents are represented below. Unsurprisingly given its standing in overall borough accidents, Brooklyn is the most-represented borough:

![zipcodes](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/zipcodes.png?raw=true)

### When Do Accidents Occur?
Based on the below, we see that accidents are more likely to occur during the week, on non-holidays, and in the spring. Lower accident rates in the winter may be due to fewer people on the road.

![seasons](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/seasons.png?raw=true)

![weekday](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/weekday.png?raw=true)

![holiday](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/holiday.png?raw=true)


# Results
The first three boroughs examined, Brooklyn, Queens, and Manhattan, had most success with Facebook Prophet models. All had an RMSE-to-accident-range ratio of 9-10%, indicating that predictions were wrong by an average of 9-10% of total accident range. The Bronx performed best with an ARIMA model, also with a 9% RMSE-to-accident-range ratio, and Staten Island performed best with a SARIMAX model, which has a 6% RMSE-to-accident ratio. Details for each model are listed below:

### Brooklyn Predictions:
- Facebook Prophet model
- RMSE: 24.44
- RMSE-to-range-ratio: 9%

![Bkln_model](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/Bkln_model.png?raw=true)

### Queens Predictions:
- Facebook Prophet model
- RMSE: 26.62
- RMSE-to-range-ratio: 10%

![Qns_model](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/Qns_model.png?raw=true)

### Manhattan Predictions:
- Facebook Prophet model
- RMSE: 19.05
- RMSE-to-range-ratio: 9%

![Man_model](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/Man_model.png?raw=true)

### Bronx Predictions:
- ARIMA model
- RMSE: 18.63
- RMSE-to-range ratio: 9%

![Bx_model](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/Bx_model.png?raw=true)

### Staten Island Predictions:
- SARIMAX model
- RMSE: 2.06
- RMSE-to-range ratio: 6%

![SI_model](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/SI_model.png?raw=true)


## Streamlit Dashboard
I created a user-friendly [Streamlit dashboard](http://192.168.0.11:8501/.) for public use, with the option to view historical and predicted data by borough and/or date. A demo is included below: 
![streamlit](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/streamlit.gif?raw=true)


# Recommendations
For institutions:
- Increase crash-related resources in time periods with most accidents, for example during the spring.
- Save resources in time period with fewer accidents, for example on holidays and weekends.
- Increase crash-related resources in zip codes with most accidents.

For individuals:
If your timing is flexible, avoid hours of peak accident frequency.
  
# Next Steps
- Try other modeling types, such as neural networks
- Predict number of accidents by zip code
- Predict number of injuries
- Incorporate weather data
- Adjust model as pandemic-related updates occur 


# Source Material
### Data Source:
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

### Sources for COVID-19 Strategy: 
https://www.cdc.gov/coronavirus/2019-ncov/downloads/covid-data/Consolidated-Forecasts-Incident-Cumulative-Deaths-2021-02-01.pdf

https://covid19.healthdata.org/united-states-of-america?view=total-deaths&tab=trend

https://analytics-tools.shinyapps.io/covid19simulator04/

https://covid19-projections.com/path-to-herd-immunity/

https://www.theatlantic.com/ideas/archive/2020/12/the-2021-post-pandemic-prediction-palooza/617332/

https://www.govtech.com/analytics/Has-COVID-19-Forever-Changed-Rush-Hour-Traffic-Patterns.html

