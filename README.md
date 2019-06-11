# Chicago Crime Dataset Analysis

The assignment explores and analysis the different types of crimes found in the City of Chicago. We try and predict the crime rates for the years 2019-2024 using linear regression. We use time-series graphs to see the frequence of crimes from the years 2001-2018 as well as the crime rates for each hour in the day. We make the use of data clustering to see which crimes are more likely to occur in the City of Chicago based on the zip code. 

## Dataset

We used the dataset found [here](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data) to perform our analysis. This dataset is not included in this repository as it is a couple of GBs. Smaller datasets have been included to run the specific programs in each directory. These datasets have been cleaned and preprocessed. 

## Preparation

Each program is to be used with python3 and makes use of the following libraries: 

```python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy import stats
```

## Demo

For demo purposes, a toy example has been provided. To invoke, 

```bash
cd Testing_Folder
make
```
and the prediction of total crimes for the years 2019-2024 will appear. 

## Explanation

Each directory has its own program corresponding to what type of analysis we are performing. 

For each of the programs we used, we created smaller datasets to obtain the data we needed so we would not have to use the entire dataset. This made programs run much quicker and more effectively. 

The SQL queries can be found under the SQL directory. 

## Authors and Acknowledgment

The following people have contributed greatly towards the making of this project: 

- Mehrad Amin
- Jonathan Peng
- Paul Rodriguez

## License

[MIT](https://github.com/pauljrodriguezcs/Chicago_Crime_Analysis/blob/master/LICENSE)