import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

# Veri setinizi buraya yapıştırın veya dosya yolu belirtin
data = """
age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,class
39,State-gov,77516,Bachelors,13,Married-civ-spouse,Adm-clerical,Wife,White,Female,2174,0,40,United-States,<=50K
50,Self-emp-not-inc,83311,Bachelors,13,Divorced,Exec-managerial,Not-in-family,White,Male,0,0,13,United-States,<=50K
38,Private,215646,HS-grad,9,Married-civ-spouse,Handlers-cleaners,Wife,White,Female,0,0,40,United-States,<=50K
53,Private,234721,11th,7,Divorced,Handlers-cleaners,Not-in-family,Black,Female,0,0,40,United-States,<=50K
28,Private,338409,Bachelors,13,Divorced,Prof-specialty,Unmarried,Asian-Pac-Islander,Male,0,0,40,Cambodia,<=50K
"""

# Reading data as a file using StringIO

df = pd.read_csv(StringIO(data))

# draw line chart based on "age" property
plt.plot(df['age'], marker='o', linestyle='-', color='skyblue')
plt.title('Line Chart by Age')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()