#code developed to udemy's course: Data Science and Machine Learning
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv("Ecommerce Customers")

#Comparar colunas e verificar se a correlação faz sentido
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)

#verificando a regressão linear
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)

#treinando
x = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.4, random_state=11)

lr = LinearRegression()

lr.fit(xtrain,ytrain)
pred = lr.predict(xtest)

#avaliando
print('MAE:', metrics.mean_absolute_error(ytest, pred))
print('MSE:', metrics.mean_squared_error(ytest, pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(ytest, pred)))

#coeficientes
coeff = pd.DataFrame(lr.coef_,  x.columns)
coeff.columns = ['Coeffecient']
print(coeff)