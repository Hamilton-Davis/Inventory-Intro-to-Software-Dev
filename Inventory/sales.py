from PySide6.QtCharts import QChartView, QLineSeries, QChart
from PySide6.QtCore import QRect, QSize, QDate
from PySide6.QtGui import QIcon, Qt, QFont, QFontMetrics
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QSpacerItem, QSizePolicy,
                               QLabel, QDateEdit, QListWidgetItem)

from tablereader import DatabaseManager
from datetime import datetime


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
        self.item_sales_list.itemChanged.connect(self.item_sales_list_update)

        self.item_qnt_view = QChartView()
        self.item_qnt_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.item_graph_layout.addWidget(self.item_qnt_view)

        self.item_qnt_list = QListWidget() # List of options for quantity graph
        self.item_qnt_list.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.item_graph_layout.addWidget(self.item_qnt_list)
        self.item_qnt_list.itemChanged.connect(self.item_qnt_list_update)

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
        self.item_sales_list.clear()
        self.item_qnt_list.clear()
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


    def get_checked_items(self, list):
        checked_items = []
        for row in range(list.count()):
            item = list.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(item.text())  # Get the text of the checked item
        return checked_items

    # Updates item sales chart with new selections
    def item_sales_list_update(self):
        dates = self.period_widget.get_dates()
        item_names = self.get_checked_items(self.item_sales_list)
        item_sales = DatabaseManager.sales_between_dates(item_names, dates[0], dates[1])
        chart = self.create_linechart(item_sales)
        self.item_sales_view.setChart(chart)


    # Updates item qnt chart with new selections
    def item_qnt_list_update(self):
        dates = self.period_widget.get_dates()
        item_names = self.get_checked_items(self.item_qnt_list)
        item_sales = DatabaseManager.sales_between_dates(item_names, dates[0], dates[1])
        chart = self.create_linechart(item_sales)
        self.item_qnt_view.setChart(chart)

    # Create and return a QChart with sales data plotted
    def create_linechart(self, item_sales):
        chart = QChart()

        # Iterate over the item sales and plot data
        for day_sales in item_sales:
            date_str = day_sales['date']
            date = datetime.strptime(date_str, "%Y-%m-%d")
            sales_data = day_sales['sales_data']

            # Create a QLineSeries for each item in sales_data
            for item in sales_data:
                item_name = item[0]
                item_sales = item[2]  # Assuming index 2 holds the sales data for this item

                # Find the series for the item or create a new one if it doesn't exist
                series = self.get_lineseries(chart, item_name)

                # Add data to the series
                # Each point is (x, y) where x is the date timestamp and y is the sales quantity
                series.append(date.timestamp(), item_sales)

        # Set up chart
        chart.createDefaultAxes()
        chart.setTitle("Sales Data Over Time")
        return chart

    def get_lineseries(self, chart, item_name):
        """Find or create a QLineSeries for the given item name."""
        # Try to find an existing series for the item
        for series in chart.series():
            if series.name() == item_name:
                return series

        # If not found, create a new series
        new_series = QLineSeries()
        new_series.setName(item_name)
        chart.addSeries(new_series)
        return new_series


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

    # Returns a tuple of datetime dates in format (from_date, to_date)
    def get_dates(self):
        from_date = datetime.strptime(self.fromDateEdit.text(), "%Y-%m-%d").date()
        to_date = datetime.strptime(self.toDateEdit.text(), "%Y-%m-%d").date()
        return from_date, to_date
