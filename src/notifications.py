# START v0.3.0

# LibrarZzz! / FileZzz!
#-----------------------------------------------------------------------------------#
from PySide6.QtGui import QPixmap
import math
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QApplication,
    QGraphicsOpacityEffect
)
from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    QTimer,
    QPoint,
    QParallelAnimationGroup,
    QElapsedTimer,
    QVariantAnimation,
    Slot,
    Qt
)

from setting import Setting

#-----------------------------------------------------------------------------------#

# ClasseZzz!
#-----------------------------------------------------------------------------------#
class Notification(QWidget) :
    def __init__(self):
        super().__init__()

        #self.setup_window()
        #self.setup_ui()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.image = QLabel(self)

        self.opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)

        

    def set_image(self, img_path):
        pixmap = QPixmap(img_path)

        pixmap = pixmap.scaled(
            300,
            340,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.image.setPixmap(pixmap)
        self.resize(pixmap.size())

    def show_notif(self) :
        canshow = Setting.load()
        if not canshow["notification"] : return
        
        screen_size = QApplication.primaryScreen().availableGeometry()

        endx = screen_size.width() - self.width() -20
        endy = screen_size.height() - self.height()-20

        starty = screen_size.bottom() + self.height()

        self.move(endx, starty)

        self.show()

        self.slide_in(endx, endy)

    def slide_in(self, endx,endy) :
        self.animat = QPropertyAnimation(self, b"pos")

        self.animat.setDuration(400)

        self.animat.setStartValue(self.pos())

        self.animat.setEndValue(QPoint(endx, endy))
        
        curve = QEasingCurve(QEasingCurve.OutBack)
        curve.setOvershoot(0.6)
        self.animat.setEasingCurve(curve)

        self.animat.finished.connect(self.on_slide_finished)


        self.fade = QPropertyAnimation(self.opacity, b"opacity")
        self.fade.setDuration(350)
        self.fade.setStartValue(0.0)
        self.fade.setEndValue(1.0)
        self.fade.setEasingCurve(QEasingCurve.OutCubic)

        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.animat)
        self.group.addAnimation(self.fade)

        self.group.start()

    def slide_out(self):

        if hasattr(self, "float_anim"):
            self.float_anim.stop()

        screen = QApplication.primaryScreen().availableGeometry()

        endy = screen.bottom() + self.height()

        self.animat = QPropertyAnimation(self, b"pos")

        self.animat.setDuration(400)

        self.animat.setStartValue(self.pos())

        self.animat.setEndValue(QPoint(self.x(), endy))

        self.animat.setEasingCurve(QEasingCurve.InBack)

        self.animat.finished.connect(self.close)


        self.fade = QPropertyAnimation(self.opacity, b"opacity")
        self.fade.setDuration(1000)
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)

        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.animat)
        self.group.addAnimation(self.fade)

        self.group.start()
        
    def setup_window(self) :

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setup_ui(self) :

        self.container = QFrame(self)

        self.container.setStyleSheet("""QFrame{background-color:#2B2D31; border-radius:16px;}""")

    def on_slide_finished(self):

        self.base_pos = self.pos()

        self.start_floating()

        QTimer.singleShot(2620, self.slide_out)

    def start_floating(self):

        self.timer = QElapsedTimer()
        self.timer.start()

        self.float_anim = QVariantAnimation(self)

        self.float_anim.setStartValue(0.0)
        self.float_anim.setEndValue(1.0)

        self.float_anim.setDuration(1000)

        self.float_anim.setLoopCount(-1)

        self.float_anim.valueChanged.connect(self.update_floating)

        self.float_anim.start()
    
    def update_floating(self, _):

        t = self.timer.elapsed() / 1000.0

        offset = math.sin(t * 4.0) * 6

        self.move(self.base_pos.x(), int(self.base_pos.y() + offset))

    @Slot(str)
    def show_image_notification(self, img_path):
        self.set_image(img_path)
        self.show_notif()

#-----------------------------------------------------------------------------------#

# the END
