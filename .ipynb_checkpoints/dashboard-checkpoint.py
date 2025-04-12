import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QTextEdit, QGridLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RefinedDroneDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intelligent Drone Surveillance Dashboard")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background-color: #111827; color: white;")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        # Left Panel
        left_layout = QVBoxLayout()
        title_label = QLabel("🛡️ Intelligent Drone Surveillance")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))

        self.upload_label = QLabel("No file selected")
        self.upload_button = QPushButton("Browse...")
        self.upload_button.clicked.connect(self.browse_file)
        self.upload_button.setStyleSheet("background-color: #1f2937; color: white; padding: 8px;")

        upload_box = QVBoxLayout()
        upload_box.addWidget(self.upload_label)
        upload_box.addWidget(self.upload_button)

        upload_frame = QWidget()
        upload_frame.setLayout(upload_box)
        upload_frame.setStyleSheet("border: 1px solid #374151; padding: 15px; border-radius: 10px;")

        summary_label = QLabel("📝 Generated Summary")
        self.summary_text = QTextEdit()
        self.summary_text.setPlaceholderText("Lorem ipsum dolor sit amet...")
        self.summary_text.setStyleSheet("background-color: #1f2937;")

        report_label = QLabel("📄 Detailed Report")
        self.report_text = QTextEdit()
        self.report_text.setPlaceholderText("Lorem ipsum dolor sit amet...")
        self.report_text.setStyleSheet("background-color: #1f2937;")

        download_btn = QPushButton("Download PDF")
        download_btn.setStyleSheet("background-color: #3b82f6; color: white; padding: 10px;")

        left_layout.addWidget(title_label)
        left_layout.addWidget(upload_frame)
        left_layout.addSpacing(20)
        left_layout.addWidget(summary_label)
        left_layout.addWidget(self.summary_text)
        left_layout.addWidget(report_label)
        left_layout.addWidget(self.report_text)
        left_layout.addWidget(download_btn)

        # Right Panel
        right_layout = QVBoxLayout()
        dashboard_title = QLabel("📊 Dashboard")
        dashboard_title.setFont(QFont("Arial", 16, QFont.Bold))

        grid = QGridLayout()
        grid.setSpacing(20)

        metrics = [
            ("🛸", "Hours Flown", "12.3"),
            ("🛢️", "Fuel Capacity", "100.0"),
            ("⛽", "Remaining Fuel", "65.7"),
            ("🗺️", "Explored Area", "45.8"),
            ("📸", "Captured Images", "234"),
        ]

        for i, (icon, label, value) in enumerate(metrics):
            icon_label = QLabel(icon)
            icon_label.setFont(QFont("Arial", 36))  # Enlarged icons

            metric_label = QLabel(label)
            metric_label.setFont(QFont("Arial", 14, QFont.Bold))  # Bold label

            value_label = QLabel(value)
            value_label.setFont(QFont("Arial", 20, QFont.Bold))
            value_label.setStyleSheet("color: #60a5fa;")

            row_layout = QVBoxLayout()
            row_layout.setAlignment(Qt.AlignCenter)
            row_layout.addWidget(icon_label)
            row_layout.addWidget(metric_label)
            row_layout.addWidget(value_label)

            cell = QWidget()
            cell.setLayout(row_layout)
            cell.setStyleSheet("background-color: #1f2937; padding: 20px; border-radius: 10px;")
            grid.addWidget(cell, i // 2, i % 2)

        dashboard_widget = QWidget()
        dashboard_widget.setLayout(grid)

        right_layout.addWidget(dashboard_title)
        right_layout.addWidget(dashboard_widget)

        # Final Layout Merge
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 2)

        self.setLayout(main_layout)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_name:
            self.upload_label.setText(file_name.split("/")[-1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = RefinedDroneDashboard()
    dashboard.show()
    sys.exit(app.exec_())
