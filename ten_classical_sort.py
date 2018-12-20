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
import numpy as np
# 排序的相关概念
# 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
# 不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
# 时间复杂度：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
# 空间复杂度：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。
class ten_classical_sort:
	def bubble_sort(self,arr):
		'''冒泡排序
		冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
		走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
		这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
		:param arr: list or array
		:return: sort ascending
		'''
		arr_length = len(arr)
		for i in range(arr_length - 1):
			#print i
			for j in range(arr_length-1-i):
				#print j
				if arr[j] > arr[j+1]:#相邻元素两两比较
					temp = arr[j+1]#元素交换
					arr[j+1] = arr[j]
					arr[j] = temp
		return arr
	def selection_sort(self,arr):
		'''选择排序
		选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：
		首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
		然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
		以此类推，直到所有元素均排序完毕。
		:param arr:
		:return:
		'''
		arr_length = len(arr)
		for i in range(arr_length-1):
			min_index = i
			for j in range(i+1,arr_length):
				if arr[j]<arr[min_index]:
					min_index = j
			temp = arr[i]
			arr[i] = arr[min_index]
			arr[min_index] = temp
		return arr
	def insertion_sort(self,arr):
		'''插入排序
		插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。
		它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
		:param arr:
		:return:
		'''
		arr_length = len(arr)
		for i in range(1,arr_length):
			pre_index = i-1
			current = arr[i]
			while (pre_index >= 0 and arr[pre_index] > current):
				arr[pre_index+1] = arr[pre_index]
				pre_index = pre_index-1
			arr[pre_index+1] = current
		return arr
	def shell_sort(self,arr):
		def _gapInsertionSort(arr, start, gap):
			for i in range(start + gap, len(arr), gap):
				currentvalue = arr[i]
				position = i
				while position >= gap and arr[position - gap] > currentvalue:
					arr[position] = arr[position - gap]
					position = position - gap
				arr[position] = currentvalue
		sublistcount = len(arr) // 2
		while sublistcount > 0:
			for startposition in range(sublistcount):
				_gapInsertionSort(arr, startposition, sublistcount)
			print("After increments of size", sublistcount,
			      "The list is", arr)
			sublistcount = sublistcount // 2
		# arr_length = len(arr)
		# gap = 1
		# while(gap<arr_length/3):
		# 	gap = gap*3+1
		# while(gap>0):
		# 	gap = int(np.floor(gap/3))
		# 	for i in range(gap,arr_length):
		# 		temp = arr[i]
		# 		for j in range(i-gap,0,gap):
		# 			if arr[j]>temp:
		# 				arr[j+gap] = arr[j]
		# 			arr[j+gap] = temp
		return arr

if __name__ == '__main__':
	a=ten_classical_sort()
	a.bubble_sort([8,9,1,7,2,3,5,4,6,0])
	# a.selection_sort([8,9,1,7,2,3,5,4,6,0])
	# a.insertion_sort([8,9,1,7,2,3,5,4,6,0])
	# a.shell_sort([8,9,1,7,2,3,5,4,6,0])