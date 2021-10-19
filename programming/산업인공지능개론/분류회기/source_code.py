import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from matplotlib import pyplot as plt

dataset = pd.read_csv('autonomus_driving_issue_01.csv')
x = dataset.iloc[:, [7, 7]].values # 입력 
y = dataset.iloc[:, 6].values # 출력

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.88, random_state = 0)

print ('xtrain : ', xtrain)
print ('ytrain : ', ytrain)
print ('xtest : ', xtest)
print ('ytest : ', ytest)

IssueID = dataset.iloc[:, 1]
CarNum = dataset.iloc[:, 2].values 
IStart = dataset.iloc[:, 3].values 
IEnd = dataset.iloc[:, 4].values 
Priority = dataset.iloc[:, 5].values 
Frequency = dataset.iloc[:, 6].values # 출력
wSum = dataset.iloc[:, 7].values # 입력 

Hit = [0,0,0,0,0]
HitCnt = 0

print('1. 기본 데이터를 선형 회기 모델로 학습')
print(' ')

plt.scatter(wSum, y) # 데이터 위치의 산포도 출력 
plt.title("Linear Regression")
plt.xlabel("Issue wSum")
plt.ylabel("Frequency")
#plt.axis([0, 450, 0, 7])

model = LinearRegression( )
model.fit(xtrain, ytrain) # 모델 학습
y_pred = model.predict(xtest) # 예측값 계산
#정확도 측정
score = model.score(xtrain, ytrain)    #score(x_train,y_train)
print('score : ', score)

# 회귀선 그리기
plt.plot(xtest, y_pred, color='r')
plt.show( )

print(' ')
print('2. x값 200 가중치, y값 invert 하여 원하는 값으로 학습 될 수 있도록 수정')
print(' ')

plt.scatter(wSum, y) # 데이터 위치의 산포도 출력 
plt.title("Linear Regression")
plt.xlabel("Issue wSum")
plt.ylabel("Frequency")
#plt.axis([0, 450, 0, 7])

for i in range(0,len(ytrain)):#len(y)
  ytrain[i] = max((ytrain)) - ytrain[i] # Y값 대칭 이동값으로 변경, 
  # X값 200값 이동하여, Frequence 4 이상 wSum 350 이상 으로 학습 되도록 가중치 적용
  xtrain[i] = xtrain[i] + 200   

model = LinearRegression( )
model.fit(xtrain, ytrain) # 모델 학습
y_pred = model.predict(xtest) # 예측값 계산
#정확도 측정
score = model.score(xtrain, ytrain)    #score(x_train,y_train)
print('score : ', score)

# 회귀선 그리기
plt.plot(xtest, y_pred, color='r')
plt.show( )

# 중요 이슈 도출 정보 출력
for i in range(0,len(wSum)):
    if wSum[i] > 300 and Frequency[i] > 4:       
        Hit[HitCnt] = i
        HitCnt += 1    
    print('Num:', i, 'IssueID:', IssueID[i], 'CarNum:', CarNum[i])

HitCnt = 0
print('----- [ 도출된 이슈 ] -----')

for i in range(0,len(Hit)):
    if Hit[HitCnt] > 0:
        print('Num:', Hit[HitCnt], 'IssueID:', IssueID[Hit[HitCnt]], 'CarNum:', 
              CarNum[Hit[HitCnt]], 'Frequency:', Frequency[Hit[HitCnt]], 'wSum:', wSum[Hit[HitCnt]])
    HitCnt += 1
print(' ')