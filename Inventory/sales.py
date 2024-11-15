from PySide6.QtCharts import QChartView, QLineSeries, QChart
from PySide6.QtCore import QRect, QSize, QDate
from PySide6.QtGui import QIcon, Qt, QFont, QFontMetrics
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QSpacerItem, QSizePolicy,
                               QLabel, QDateEdit, QListWidgetItem)

from tablereader import DatabaseManager


class SalesScreen(QWidget):
    def __init__(self, switch_to_home, switch_to_sales_log):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create navigation layout
        self.nav_layout = QHBoxLayout()
        icon = QIcon()
        icon.addFile(u"../Inventory/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_button = QPushButton(icon, "Home", self)
        self.home_button.setGeometry(QRect(10, 20, 80, 26))
        self.home_button.clicked.connect(switch_to_home)
        self.nav_layout.addWidget(self.home_button)

        spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.nav_layout.addItem(spacer)

        self.period_widget = SalesPeriodWidget(switch_to_sales_log)
        self.nav_layout.addWidget(self.period_widget)
        self.main_layout.addLayout(self.nav_layout)

        # Create item graphs layout
        self.item_graph_layout = QHBoxLayout()
        self.item_sales_view = QChartView()
        self.item_sales_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.item_graph_layout.addWidget(self.item_sales_view)

        self.item_sales_list = QListWidget() # List of options for sales graph
        self.item_sales_list.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_graph_layout.addWidget(self.item_sales_list)

        self.item_qnt_view = QChartView()
        self.item_qnt_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.item_graph_layout.addWidget(self.item_qnt_view)

        self.item_qnt_list = QListWidget() # List of options for quantity graph
        self.item_qnt_list.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_graph_layout.addWidget(self.item_qnt_list)

        self.setup_lists()
        self.main_layout.addLayout(self.item_graph_layout)

        # Create category sales graph layout
        self.category_graph_layout = QHBoxLayout()
        left_spacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.category_graph_layout.addItem(left_spacer)

        self.category_pie_view = QChartView()
        self.category_pie_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.category_graph_layout.addWidget(self.category_pie_view)

        right_spacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.category_graph_layout.addItem(right_spacer)
        self.main_layout.addLayout(self.category_graph_layout)



    # Adds checkboxes with item names to both item option lists
    def setup_lists(self):
        dates = self.period_widget.get_dates()
        item_names = DatabaseManager.items_between_dates(dates[0], dates[1])

        # Set up font and font metrics
        item_font = QFont()
        item_font.setPointSize(10)
        font_metrics = QFontMetrics(item_font)
        max_width = 0

        # Add item names to lists and calculate max width
        for list_index in range(2):
            for name in item_names:
                # Create list item with checkbox and specified font
                list_item = QListWidgetItem(name)
                list_item.setFlags(list_item.flags() & ~Qt.ItemIsEditable | Qt.ItemIsUserCheckable)
                list_item.setCheckState(Qt.Unchecked)
                list_item.setFont(item_font)

                # Calculate width of text and update max_width if it's larger
                max_width = max(max_width, font_metrics.horizontalAdvance(name))

                # Add item to the appropriate list
                if list_index == 0:
                    self.item_sales_list.addItem(list_item)
                else:
                    self.item_qnt_list.addItem(list_item)

        # Set the fixed width for both lists based on max_width
        self.item_sales_list.setFixedWidth(max_width + 50)
        self.item_qnt_list.setFixedWidth(max_width + 50)


    # Updates item sales chart with new selections
    def item_sales_list_update(self):
        # GET SALES DATA FROM FILE MANAGEMENT
        item_sales = [] # Assume list is in format [ [item1] [item2] ...], each item being a sublist

        # Create chart with line series for each item
        chart = QChart()
        for item in item_sales:
            # Add sales for
            series = QLineSeries()
            for sales_point in item:
                series.append(sales_point)
            chart.addSeries(series)

        self.item_sales_view.setChart(chart)


class SalesPeriodWidget(QWidget):
    def __init__(self,  switch_to_sales_log):
        super().__init__()
        self.layout = QHBoxLayout()
        self.label = QLabel("Sales Period:")
        self.layout.addWidget(self.label)

        self.fromDateEdit = QDateEdit()
        self.fromDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.fromDateEdit.setCalendarPopup(True)
        self.layout.addWidget(self.fromDateEdit)
        self.toDateEdit = QDateEdit()
        self.toDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.toDateEdit.setCalendarPopup(True)
        self.setup_dates()
        self.layout.addWidget(self.toDateEdit)

        icon = QIcon()
        icon.addFile(u"icons/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.log_sales_button = QPushButton(icon, "Log Sales", self)
        self.log_sales_button.clicked.connect(switch_to_sales_log)
        self.layout.addWidget(self.log_sales_button)
        self.setLayout(self.layout)

    # Set fromDate and toDate to span a set number of days
    # Default 7 days
    def setup_dates(self, timespan=7):
        current_date = QDate.currentDate()
        self.toDateEdit.setDate(current_date)
        self.fromDateEdit.setDate(current_date.addDays(-timespan))

    # Returns a tuple of (from_date, to_date) in string format "yyyy-MM-dd"
    def get_dates(self):
        from_date = self.fromDateEdit.date().toString("yyyy-MM-dd")
        to_date = self.toDateEdit.date().toString("yyyy-MM-dd")
        return from_date, to_date
