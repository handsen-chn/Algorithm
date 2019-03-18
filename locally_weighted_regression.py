# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     locally_weighted_regression
   Description :
   Author :       yinjun8
   date：          2019/1/30
-------------------------------------------------
   Change Activity:
                   2019/1/30:
-------------------------------------------------
"""
#https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/codes/%E5%B1%80%E9%83%A8%E5%8A%A0%E6%9D%83%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92.html
__author__ = 'yinjun8'
import os
os.chdir('C:\Users\yinjun8\Desktop')
from numpy import *


# 该函数打开一个用tab键分割的文本文件
def loadDataSet(fileName):  # general function to parse tab -delimited floats
	numFeat = len(open(fileName).readline().split('\t')) - 1  # get number of fields
	dataMat = [];
	labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat, labelMat


def standRegres(xArr, yArr):  # 该函数用来计算最佳拟合直线
	xMat = mat(xArr);
	yMat = mat(yArr).T  # 读入x和y并将它们保存到矩阵中
	xTx = xMat.T * xMat
	if linalg.det(xTx) == 0.0:  # 判断行列式是否为0，直接调用numpy的linalg线性代数的库来计算行列式
		print "This matrix is singular, cannot do inverse"
		return
	ws = xTx.I * (xMat.T * yMat)  # 行列式非0，计算系数并返回
	return ws


def lwlr(testPoint, xArr, yArr, k=1.0):  # 局部加权线性回归函数
	xMat = mat(xArr);
	yMat = mat(yArr).T
	m = shape(xMat)[0]
	weights = mat(eye((m)))  # 创建对角权重矩阵
	for j in range(m):  # next 2 lines create weights matrix遍历数据集
		diffMat = testPoint - xMat[j, :]  #
		weights[j, j] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))  # 计算每个样本点对应的权重值
	xTx = xMat.T * (weights * xMat)
	if linalg.det(xTx) == 0.0:
		print "This matrix is singular, cannot do inverse"
		return
	ws = xTx.I * (xMat.T * (weights * yMat))  # 估计最优回归系数
	return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):  # loops over all the data points and applies lwlr to each one
	m = shape(testArr)[0]
	yHat = zeros(m)
	for i in range(m):
		yHat[i] = lwlr(testArr[i], xArr, yArr, k)  # lwlrtest函数主要用于调用lwlr函数
	return yHat


def lwlrTestPlot(xArr, yArr, k=1.0):  # same thing as lwlrTest except it sorts X first
	yHat = zeros(shape(yArr))  # easier for plotting
	xCopy = mat(xArr)
	xCopy.sort(0)
	for i in range(shape(xArr)[0]):
		yHat[i] = lwlr(xCopy[i], xArr, yArr, k)
	return yHat, xCopy


if __name__ == "__main__":
	dataMat, labelMat = loadDataSet('ex0.txt')
	# print (mat(dataMat[0:2]))[:,1]
	# print (mat(labelMat[0:2])).T[:,0]
	import matplotlib.pyplot as plt  # 导入matplotlib库用于画散点图进行比较

	fig = plt.figure()
	ax = fig.add_subplot(111)  # add_subplot(111)函数也可写成add_subplot(1,1,1)，意思是将画布分布在1行1列从左到右从上到下的第一个模块
	ws = standRegres(dataMat, labelMat)  # 计算系数向量
	# print ws
	yHat = (mat(dataMat)) * ws  # 计算最优回归值
	# 以下代码是标准线性回归的散点图与最佳拟合的图像
	# ax.scatter((mat(dataMat))[:,1].flatten().A[0],(mat(labelMat)).T[:,0].flatten().A[0])#数据集散点图
	# xCopy=(mat(dataMat)).copy()
	# xCopy.sort(0)#对点按照升序排序
	# yHat=xCopy*ws#画最佳拟合直线
	# ax.plot(xCopy[:,1],yHat)
	# plt.show()
	pc = corrcoef(yHat.T, labelMat)  # 计算yHat与labelMat的相关系数，即相关矩阵
	# print pc
	# ws=lwlr(dataMat[0],dataMat,labelMat,k=1.0)
	yHat = lwlrTest(dataMat, dataMat, labelMat, 0.02)
	print yHat
	# 以下代码是局部线性回归的散点图与最佳拟合的图像
	srtInd = (mat(dataMat))[:, 1].argsort(0)
	xSort = (mat(dataMat))[srtInd][:, 0, :]
	ax.plot(xSort[:, 1], yHat[srtInd])
	ax.scatter((mat(dataMat))[:, 1].flatten().A[0], (mat(labelMat)).T.flatten().A[0], s=2, c='red')
	plt.show()


