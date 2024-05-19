from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xg

heart_disease = fetch_ucirepo(id=45)

dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0)*1

X = dados.drop(columns='doenca')
y = dados.doenca

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,random_state=432, stratify=y)

modelo = xg.XGBClassifier(objetive='binary:logistic')
modelo.fit(X_train,Y_train)
preds = modelo.predict(X_test)

acuracia = accuracy_score(Y_test, preds)

print(f'A acurácia do modelo é {acuracia:.2%}')
