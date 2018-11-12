# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ten_classical_sort
   Description :
   Author :       yinjun8
   date：          2018/11/12
-------------------------------------------------
   Change Activity:
                   2018/11/12:
-------------------------------------------------
"""
__author__ = 'yinjun8'

class ten_classical_sort:
	def bubble_sort(self,arr):
		'''冒泡排序
		:param arr: list or array
		:return: sort ascending
		'''
		arr_length = len(arr)
		for i in range(arr_length-1):
			#print i
			for j in range(arr_length-1-i):
				#print j
				if arr[j] > arr[j+1]:
					temp = arr[j+1]
					arr[j+1] = arr[j]
					arr[j] = temp
		return arr

