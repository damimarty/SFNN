#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

import random

class Connexion(object):
	def __init__(self, From = None, To = None, w = None):
		"""blah"""
		self.From = From
		self.To = To
		if w is None: self.w = random.random() * 2.0 - 1.0
		else: self.w = w

	def setW(self, w = None):
		if w is None: self.w = random.random() * 2.0 - 1.0
		else: self.w = w

	def getW(self):
		return self.w

	def setFrom(self, From):
		self.From = From

	def setTo(self, To):
		self.To = To

	def getFrom(self):
		return self.From

	def getTo(self):
		return self.To
