import joblib
db=joblib.load("2nd.pk1")
db
db.predict([[9]])
db.coef_
db.intercept_