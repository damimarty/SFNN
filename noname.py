# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  9 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 599,366 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_but_1gen = wx.Button( self, wx.ID_ANY, u"Do 1 generation", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_but_1gen, 1, wx.ALL, 5 )
		
		self.m_but_100gen = wx.Button( self, wx.ID_ANY, u"Do 100 generations", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_but_100gen, 0, wx.ALL, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_sliderNeurones = wx.Slider( self, wx.ID_ANY, 25, 5, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer4.Add( self.m_sliderNeurones, 0, wx.ALL, 5 )
		
		self.m_nbNeurones = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		gSizer4.Add( self.m_nbNeurones, 0, wx.ALL, 5 )
		
		self.m_sliderConnexions = wx.Slider( self, wx.ID_ANY, 25, 5, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer4.Add( self.m_sliderConnexions, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 30,-1 ), 0 )
		gSizer4.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.displayFitness = wx.Button( self, wx.ID_ANY, u"Display Fitnesses", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.displayFitness, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_but_1gen.Bind( wx.EVT_BUTTON, self.run1Generation )
		self.m_but_100gen.Bind( wx.EVT_BUTTON, self.run100Generation )
		self.displayFitness.Bind( wx.EVT_BUTTON, self.displayFitnesses )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def run1Generation( self, event ):
		event.Skip()
	
	def run100Generation( self, event ):
		event.Skip()
	
	def displayFitnesses( self, event ):
		event.Skip()
	

