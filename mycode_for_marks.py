import pandas
db = pandas.read_csv('marks.csv')
db
y = db["marks"]
x = db['hrs']
x.shape
type(x)
x = x.values
type(x)
x = x.reshape(4,1)
type(x)
x.shape
x
from sklearn.linear_model import LinearRegression
mind = LinearRegression()
mind.fit( x,  y)
mind.predict([[ 6 ]] )