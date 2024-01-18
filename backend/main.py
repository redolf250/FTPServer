import qtawesome as qta
from icons.icons import *
from packages.pyside import *
from packages.built_in import *
from packages.ui_import import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.label.setPixmap(QPixmap.fromImage(self.resource_path('icon.ico')))
        # self.ui.label.setScaledContents(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_dashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard))
        self.ui.btn_statistics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.statistics))
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))

        # self.ui.btn_home.setIcon(qta.icon("fa5s.home",color='#FFFFFF',options=[{
        #         'scale_factor': 1.5,}]))

        self.profileImage(self.resource_path("image.jpg"))
        self.ui.userName.setText("redolf230")
        icon = QIcon()
        QSize(30,30)
        
        self.ui.btn_home.setIcon(QIcon("D:\\Python\\learning\\FTPServer\\Application\\resource\\asset\\home.svg"))

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path
    
    def mask_image(self,imgdata, imgtype ='jpeg', size = 160):
        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)
        imgsize = min(image.width(), image.height())
        rect = QRect((image.width() - imgsize) / 2,(image.height() - imgsize) / 2,imgsize,imgsize,)
        image = image.copy(rect)
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)
        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio,Qt.SmoothTransformation)
        return pm

    def profileImage(self,path):
        imgdata = open(path,'rb').read()
        pixmap =self.mask_image(imgdata)
        self.ui.profile.setPixmap(pixmap)    

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()   


if __name__ == '__main__':
    try:
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(application.exec_())
    except Exception as e:
        print(e)