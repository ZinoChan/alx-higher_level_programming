#!/usr/bin/python3
"""Defines peak-finding algorithm"""


def find_peak(list_of_integers):
	"""Return the peak"""
	if list_of_integers == []:
		return None
	start, end = 0, len(list_of_integers) - 1
	while start < end:
		mid = start + (end - start) // 2
		if list_of_integers[mid] > list_of_integers[mid + 1]:
			end = mid
		else:
			start = mid + 1
	return start


