# NYC Car Accident Predictor
![traffic](https://github.com/Davida1014/NYC-Car-Accident-Predictor/blob/main/Images/traffic.jpg?raw=true)

Davida Rosenstrauch

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
-Numerous models predicta plateau of cumulative COVID deaths by June, with a linear trend until then.
-Numerous models predict approximaely 80% poulation COVID immunity in NYC by June, with a linear trend until then.

# Exploratory Data Analysis
# Methods
# Results
# Recommendations
# Next Steps
# Source Material
