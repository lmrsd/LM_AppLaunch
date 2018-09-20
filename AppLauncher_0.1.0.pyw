from PySide import QtGui,QtCore
from functools import partial
import sys,ctypes,os

class AppBtn(QtGui.QPushButton):
	def __init__(self,*args):
		super(AppBtn, self).__init__(*args)
		self.img = ""
		self.path = ""
		self.setFixedSize(55, 55)
		self.setStyleSheet("QPushButton{ border: 0px solid  rgb(80,80,80);}"
			"QPushButton:hover{ border: 5px solid  rgb(120,120,120);}"
			"QPushButton:pressed{ border: 5px solid  rgb(24,161,173);}")
		
	def __delete__(self, instance):
		print "deleted in descriptor object"
		del self.value

class MyMainWindows(QtGui.QWidget):
	def __init__(self,*args):
		super(MyMainWindows, self).__init__(*args)
		self.layout = QtGui.QGridLayout(self)
		self.setStyleSheet("background-color: rgb(80,80,80);")
		self.uiRoot = os.path.dirname(os.path.realpath(__file__))
		# Get Screen Size
		user32 = ctypes.windll.user32
		self.ScreenWidth = user32.GetSystemMetrics(0)
		# Set Init Layout Attribute
		self.width = 350
		self.height = 10
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)
		#Place Windows
		self.resize( self.width, self.height )
		self.move( (self.ScreenWidth/2) - (self.width/2), 0)

	def appBtnConnections (self):
		for i in range (self.layout.count()):
			widget = self.layout.itemAt(i).widget()
			if isinstance(widget, QtGui.QPushButton):
				widget.clicked.connect(partial(self.appBtnPressed, widget))
				#Put icon
				icon = QtGui.QIcon(widget.img)
				widget.setIconSize(QtCore.QSize(50, 50))   
				widget.setIcon(icon)

	def lookLayout (self):
		print (self.layout.columnCount())
		print (self.layout.columnCount())
		print (self.layout.verticalSpacing())
		for i in range (self.layout.count()):
			widget = self.layout.itemAt(i).widget()
			widget.resize(0,0)
			widget.setMaximumSize(0,0)
			widget.setFixedSize(0,0)
			print widget.size()


	def appBtnAdd(self):
		#3dsmax
		btn3dsmax = AppBtn()
		btn3dsmax.img = os.path.normpath( self.uiRoot + '\\ui\\3ds.png')
		btn3dsmax.path = "C:\\Program Files\\Autodesk\\3ds Max 2017\\3dsmax.exe"
		#Zbrush
		btnZbrush = AppBtn()
		btnZbrush.img = os.path.normpath( self.uiRoot + '\\ui\\zbrush.png')
		btnZbrush.path = "C:\\Program Files\\Pixologic\\ZBrush 4R8\\ZBrush.exe"
		#Substance Painter
		btnSubPaint = AppBtn()
		btnSubPaint.img = os.path.normpath( self.uiRoot + '\\ui\\subspainter.png')
		btnSubPaint.path = "C:\\Program Files\\Allegorithmic\\Substance Painter\\Substance Painter.exe"
		#Substance Designer
		btnSubDesi = AppBtn()
		btnSubDesi.img = os.path.normpath( self.uiRoot + '\\ui\\subsdesigner.png')
		btnSubDesi.path = "C:\\Program Files\\Allegorithmic\\Substance Designer\\Substance Designer.exe"
		# Mari
		btnMari = AppBtn()
		btnMari.img = os.path.normpath( self.uiRoot + '\\ui\\mari.png')
		btnMari.path = "C:\\Program Files\\Mari4.0v4\\Bundle\\bin\\Mari4.0v4.exe"
		#Marvelous
		btnMarvelous = AppBtn()
		btnMarvelous.img = os.path.normpath( self.uiRoot + '\\ui\\marvelous.png')
		btnMarvelous.path = "C:\\Program Files\\Marvelous Designer 7 Enterprise\\MarvelousDesigner7_Enterprise_x64.exe"
		#Photoshop
		btnPhotoshop = AppBtn()
		btnPhotoshop.img = os.path.normpath( self.uiRoot + '\\ui\\photoshop.png')
		btnPhotoshop.path = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2018\\Photoshop.exe"
		#After Effect
		btnAE = AppBtn()
		btnAE.img = os.path.normpath( self.uiRoot + '\\ui\\Ae.png')
		btnAE.path = "C:\\Program Files\\Adobe\\Adobe After Effects CC 2018\\Support Files\\AfterFX.exe"
		#DjvVeiw
		btnDjv = AppBtn()
		btnDjv.img = os.path.normpath( self.uiRoot + '\\ui\\djv.png')
		btnDjv.path = "C:\\Program Files\\djv-1.1.0-Windows-64\\bin\\djv_view.exe"
		#PureRef
		btnPureRef = AppBtn()
		btnPureRef.img = os.path.normpath( self.uiRoot + '\\ui\\pureref.png')
		btnPureRef.path = "C:\\Program Files\\PureRef\\PureRef.exe"
		#slack
		btnSlack = AppBtn()
		btnSlack.img = os.path.normpath( self.uiRoot + '\\ui\\slack.png')
		btnSlack.path = "C:\\Users\\user\\AppData\\Local\\slack\\app-3.3.1\\slack.exe"
		#ftrack
		btnFtrack = AppBtn()
		btnFtrack.img = os.path.normpath( self.uiRoot + '\\ui\\frtack.png')
		btnFtrack.path = "https://capsule-studio.ftrackapp.com/"
		#Doc Capsule
		btnDoc = AppBtn()
		btnDoc.img = os.path.normpath( self.uiRoot + '\\ui\\doc.png')
		btnDoc.path = "https://192.168.0.100:8081/dokuwiki/doku.php?id=start"
		#Doc Chrome
		btnChrome = AppBtn()
		btnChrome.img = os.path.normpath( self.uiRoot + '\\ui\\chrome.png')
		btnChrome.path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
		#
		self.layout.addWidget(btn3dsmax, 0, 0, 1, 1)
		self.layout.addWidget(btnZbrush, 0, 1, 1, 1)
		self.layout.addWidget(btnSubPaint, 0, 2 ,1 ,1)
		self.layout.addWidget(btnSubDesi, 0, 3 ,1 ,1)
		self.layout.addWidget(btnMari, 1, 0, 1 ,1) 
		self.layout.addWidget(btnMarvelous, 1, 1, 1 ,1)
		self.layout.addWidget(btnPhotoshop, 1, 2, 1, 1)
		self.layout.addWidget(btnAE, 1, 3, 1, 1)
		self.layout.addWidget(btnDjv, 2, 0, 1, 1)
		self.layout.addWidget(btnPureRef, 2, 1, 1, 1)
		self.layout.addWidget(btnSlack, 2, 2, 1, 1)
		self.layout.addWidget(btnFtrack, 2, 3, 1, 1)
		self.layout.addWidget(btnDoc, 3, 0, 1, 1)
		self.layout.addWidget(btnChrome, 3, 1, 1, 1)
		# Make connection function
		self.appBtnConnections()

	def appBtnRemove(self):
		for i in reversed(range(self.layout.count())): 
			self.layout.itemAt(i).widget().setParent(None)
		self.resize(self.width,self.height)
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)

	def appBtnPressed(self,buton):
		print buton.path
		print buton.img
		os.startfile(buton.path)
		print buton.text()

	#Mouse Over Widget
	def enterEvent(self, event):
		print "Mouse Entered"
		self.appBtnAdd()
		self.resize( self.width ,350)
		self.setStyleSheet("background-color: rgb(30,30,30);")
		return super(MyMainWindows, self).enterEvent(event)

	#Mouse Leave Widget
	def leaveEvent(self, event):
		print "Mouse Left"
		self.appBtnRemove()
		self.resize(self.width,self.height)
		self.setStyleSheet("background-color: rgb(80,80,80);")
		
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