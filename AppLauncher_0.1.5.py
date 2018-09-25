from PySide import QtGui,QtCore
from functools import partial
import sys,ctypes,os,json

class AppBtn(QtGui.QPushButton):
	"""
	Main class of the button
	"""
	def __init__(self,*args):
		super(AppBtn, self).__init__(*args)
		self.img = ""
		self.path = ""
		self.btnMatchColor = ""
		self.btnNoMatchColor = ""
		self.btnClickColor = ""
		self.appSettings = {}
		self.btnSize = 10
		
		self.setStyleSheet("QPushButton{ border: 0px solid  rgb(80,80,80);}"
			"QPushButton:pressed{ border: 5px solid  "+ self.btnClickColor +";}")

	def enterEvent (self,event):
		if os.path.isfile(self.path) :
			self.setStyleSheet ("QPushButton:hover{ border: 5px solid  "+ self.btnMatchColor +";}")
		else:
			self.setStyleSheet ("QPushButton:hover{ border: 5px solid "+ self.btnNoMatchColor+";}")

class MyMainWindows(QtGui.QWidget):
	"""
	Main widget of the launcher
	"""
	def __init__(self,*args):
		super(MyMainWindows, self).__init__(*args)
		self.layout = QtGui.QGridLayout(self)
		self.uiRoot = os.path.dirname(os.path.realpath(__file__))
		self.appList = self.uiRoot + "\\bin\\apps_list.json"
		self.appSettings = self.uiRoot + "\\bin\\app_settings.json"
		# Init app from settings
		self.applySettings()
		# Get Screen Size & Place Windows
		user32 = ctypes.windll.user32
		self.ScreenWidth = user32.GetSystemMetrics(0)
		self.resize( self.width, self.height )
		self.move( (self.ScreenWidth/2) - (self.width/2), 0)

	def applySettings (self) :
		"""
		Init ui settings from the file : self.appSettings = self.uiRoot + "\\bin\\app_settings.json"
		"""
		settingsFile = open(self.appSettings, "r")
		settingsData = json.load(settingsFile)

		for settings in settingsData['AppSettings'] : 
				self.width = settings['Width']
				self.height = settings['Height']
				self.maxCol = settings['maxCol']
				self.hoverColor = settings['backgroundHoverColor']
				self.backgroundColor = settings['backgroundColor']
				self.appbtnMatchColor = settings['ButtonHoverMatchColor']
				self.appbtnNoMatchColor = settings['ButtonHoverNoMatchColor']
				self.appbtnClickColor = settings['ButtonClickColor']
				self.appbtnSize = settings['ButtonSize']
				self.layout.setSpacing(settings['mainSpacing'])
				self.layout.setContentsMargins(settings['mainContentMargin'], settings['mainContentMargin'], settings['mainContentMargin'], settings['mainContentMargin'])
				self.setStyleSheet("background-color: " + settings['backgroundColor'] + ";")

	def appBtnConnections (self):
		"""
		Add function appBtnPressed to each Button when left clicked
		Add Icon to each button
		"""
		for i in range (self.layout.count()):
			widget = self.layout.itemAt(i).widget()
			if isinstance(widget, QtGui.QPushButton):
				widget.clicked.connect(partial(self.appBtnPressed, widget))

	def appBtnAdd(self):
		"""
		Add all btn to layout 
		"""
		row = 0
		col = 0
		appsFile = open(self.appList, "r")
		appsData = json.load(appsFile)

		def createBtn(row,col):
			btn = AppBtn()
			btn.btnMatchColor = self.appbtnMatchColor
			btn.btnNoMatchColor = self.appbtnNoMatchColor
			btn.btnClickColor = self.appbtnClickColor
			btn.setFixedSize(self.appbtnSize, self.appbtnSize)
			btn.img = os.path.normpath( self.uiRoot + '\\ui\\' + app['App Thumbnail'])
			if not os.path.isfile(btn.img) :
				btn.img = os.path.normpath( self.uiRoot + '\\ui\\' + 'default.png')
			btn.path = app['App Path']

			icon = QtGui.QIcon(btn.img)
			btn.setIconSize(QtCore.QSize(50, 50))   
			btn.setIcon(icon)
			self.layout.addWidget(btn, row, col, 1, 1)
			
		for app in appsData['AppsList'] :
			if col < (self.maxCol-1) :
				createBtn(row,col)
				col += 1

			else :
				createBtn(row,col)
				col = 0
				row += 1

		self.appBtnConnections()

	def appBtnRemove(self):
		"""
		"""
		for i in reversed(range(self.layout.count())): 
			self.layout.itemAt(i).widget().setParent(None)
		self.resize(self.width,self.height)

	def appBtnPressed(self,buton):
		"""
		"""
		if os.path.isfile(buton.path) :
			os.startfile(buton.path)
			self.appBtnRemove()
			self.resize(self.width,self.height)
		else :
			self.appBtnRemove()
			self.resize(self.width,self.height)
			print "Sorry the path doesn't exists..."
		print buton.text()

	#Mouse Over Widget
	def enterEvent(self, event):
		#print "Mouse Entered"
		self.appBtnAdd()
		self.resize( self.width ,350)
		self.setStyleSheet("background-color: "+ self.hoverColor +";")
		return super(MyMainWindows, self).enterEvent(event)

	#Mouse Leave Widget
	def leaveEvent(self, event):
		#print "Mouse Left"
		self.appBtnRemove()
		self.resize(self.width,self.height)
		self.setStyleSheet("background-color:" + self.backgroundColor + ";")
		return super(MyMainWindows, self).enterEvent(event)

	#Mouse Event function
	
	def mousePressEvent(self, event):
		if event.type() == QtCore.QEvent.MouseButtonPress:
			if event.button() == QtCore.Qt.MiddleButton:
				# Right Click event handler
				#print "middle = closing !!!"
				self.close()
				return
			elif event.button() == QtCore.Qt.LeftButton:
				# Left Click event handler
				#print "left"
				return
			elif event.button() == QtCore.Qt.RightButton:
				# Left Click event handler
				#print "right"
				return
	
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mw = MyMainWindows()
	mw.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
	mw.show()
	app.exec_()