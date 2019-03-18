# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GBDT
   Description :
   Author :       yinjun8
   date：          2019/2/12
-------------------------------------------------
   Change Activity:
                   2019/2/12:
-------------------------------------------------
"""
#https://www.cnblogs.com/pinard/p/6143927.html
#github: https://github.com/ljpzzz/machinelearning/blob/master/ensemble-learning/gbdt_classifier.ipynb
__author__ = 'yinjun8'
import os
os.chdir('C:\Users\yinjun8\Desktop')
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
#数据导入
##先批量生成列名
names=[]
for i in range(34):
    names.append('Var'+str(i+1))
names.append('gbflag')
df = pd.read_csv('ionosphere.data.txt',header = None,names=names)
##查看前五行数据
df.head
##查看数据有没有缺失值，异常值
df.describe()
x_columns = [x for x in df.columns if x not in 'gbflag']
X = df[x_columns]
y = df['gbflag']
#将数据集分成训练集，测试集
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1)

#GBDT
##重要参数max_depth=4,max_features=10,n_estimators=80
from sklearn.ensemble import GradientBoostingClassifier
gbdt = GradientBoostingClassifier()
gbdt.fit(X_train,y_train)
pred = gbdt.predict(X_test)
pd.crosstab(y_test,pred)

#算法评估指标
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print(classification_report(y_test, pred, digits=4))

#交叉验证（数据样本少，可以使用交叉验证方法）
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
kf = KFold(n_splits = 10)
scores = []
for train,test in kf.split(X):
    train_X,test_X,train_y,test_y = X.iloc[train],X.iloc[test],y.iloc[train],y.iloc[test]
    gbdt =  GradientBoostingClassifier(max_depth=4,max_features=9,n_estimators=100)
    gbdt.fit(train_X,train_y)
    prediced = gbdt.predict(test_X)
    print(accuracy_score(test_y,prediced))
    scores.append(accuracy_score(test_y,prediced))
##交叉验证后的平均得分
np.mean(scores)

#自动调参
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
gbdt = GradientBoostingClassifier()
cross_validation = StratifiedKFold(y,n_folds = 10)
parameter_grid = {'max_depth':[2,3,4,5],
                  'max_features':[1,3,5,7,9],
                  'n_estimators':[10,30,50,70,90,100]}
grid_search = GridSearchCV(gbdt,param_grid = parameter_grid,cv =cross_validation,
                           scoring = 'accuracy')
grid_search.fit(X,y)
#输出最高得分
grid_search.best_score_
#输出最佳参数
grid_search.best_params_