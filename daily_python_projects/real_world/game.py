import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QTimer, QRect

# Game Constants
WIDTH, HEIGHT = 400, 500
PLAYER_SIZE = 30
LASER_WIDTH, LASER_HEIGHT = 20, 40
LASER_SPEED = 5
LASER_INTERVAL = 1000  # New laser every 1000ms

class LaserDodger(QWidget):
    def __init__(self):
        super().__init__()

        # Game window setup
        self.setWindowTitle("Laser Dodger")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setStyleSheet("background-color: black;")

        # Player setup
        self.player_x = WIDTH // 2 - PLAYER_SIZE // 2
        self.player_y = HEIGHT - 60
        self.lasers = []

        # Game Over Label
        self.game_over_label = QLabel("GAME OVER", self)
        self.game_over_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        self.game_over_label.setGeometry(WIDTH // 2 - 70, HEIGHT // 2 - 20, 140, 40)
        self.game_over_label.setVisible(False)

        # Timer for lasers
        self.laser_timer = QTimer(self)
        self.laser_timer.timeout.connect(self.spawn_laser)
        self.laser_timer.start(LASER_INTERVAL)

        # Timer for movement
        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.update_game)
        self.move_timer.start(50)

    def paintEvent(self, event):
        """Draw player and lasers"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw player (green circle)
        painter.setBrush(QColor(0, 255, 0))
        painter.drawEllipse(self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE)

        # Draw lasers (red rectangles)
        painter.setBrush(QColor(255, 0, 0))
        for laser in self.lasers:
            painter.drawRect(laser)

    def keyPressEvent(self, event):
        """Move player with arrow keys"""
        if event.key() == Qt.Key.Key_Left and self.player_x > 10:
            self.player_x -= 20
        elif event.key() == Qt.Key.Key_Right and self.player_x < WIDTH - PLAYER_SIZE - 10:
            self.player_x += 20
        self.update()

    def spawn_laser(self):
        """Create a new falling laser"""
        x = random.randint(10, WIDTH - LASER_WIDTH - 10)
        self.lasers.append(QRect(x, 10, LASER_WIDTH, LASER_HEIGHT))

    def update_game(self):
        """Move lasers down and check collisions"""
        for laser in self.lasers:
            laser.moveTop(laser.top() + LASER_SPEED)

        # Check collision
        if self.check_collision():
            self.game_over()

        self.update()

    def check_collision(self):
        """Detect if a laser hits the player"""
        player_rect = QRect(self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE)
        for laser in self.lasers:
            if player_rect.intersects(laser):
                return True
        return False

    def game_over(self):
        """End the game"""
        self.laser_timer.stop()
        self.move_timer.stop()
        self.game_over_label.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = LaserDodger()
    game.show()
    sys.exit(app.exec())