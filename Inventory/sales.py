from PySide6.QtCharts import QChartView, QLineSeries, QPieSeries, QPieSlice, QChart, QDateTimeAxis, QValueAxis
from PySide6.QtCore import QRect, QSize, QDate, QDateTime
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
        self.period_widget.fromDateEdit.dateChanged.connect(self.period_updated)
        self.period_widget.toDateEdit.dateChanged.connect(self.period_updated)
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

        # Display empty charts at load
        self.item_sales_list_update()
        self.item_qnt_list_update()
        self.category_pie_view.setChart(self.create_pieseries())


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


        # Sort both lists alphabetically
        self.item_sales_list.sortItems()
        self.item_qnt_list.sortItems()

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


    # Updates charts when sales period dates are updated
    def period_updated(self):
        self.item_sales_list_update()
        self.item_qnt_list_update()
        self.category_pie_view.setChart(self.create_pieseries())


    # Updates item sales chart with new selections
    def item_sales_list_update(self):
        dates = self.period_widget.get_dates()
        item_names = self.get_checked_items(self.item_sales_list)
        item_sales = DatabaseManager.sales_between_dates(item_names, dates[0], dates[1])[0]
        chart = self.create_linechart(item_sales, "Sales by Day", y_mode=1)
        self.item_sales_view.setChart(chart)


    # Updates item qnt chart with new selections
    def item_qnt_list_update(self):
        dates = self.period_widget.get_dates()
        item_names = self.get_checked_items(self.item_qnt_list)
        item_sales = DatabaseManager.sales_between_dates(item_names, dates[0], dates[1])[0]
        chart = self.create_linechart(item_sales, "Quantity Sold by Day", y_mode=0)
        self.item_qnt_view.setChart(chart)


    # Returns a chart with pie slices for gross sales of each item category
    def create_pieseries(self):
        dates = self.period_widget.get_dates()
        item_names = DatabaseManager.items_between_dates(dates[0], dates[1])
        gross_category_sales = DatabaseManager.sales_between_dates(tuple(item_names), dates[0], dates[1])[1]

        chart = QChart()
        chart.setTitle("Sales by Category")
        pie = QPieSeries()
        pie.setLabelsVisible(True)

        for index, gross_sales in enumerate(gross_category_sales):
            category_name = f"Category {index + 1}"
            slice = QPieSlice(category_name, gross_sales)
            pie.append(slice)

        chart.addSeries(pie)
        return chart


    # Returns a chart with lineseries for each item in item_sales
    # y_mode determines if y_axis will display quantity sold (y_mode=0) or sales in dollars (y_mode=1)
    def create_linechart(self, item_sales, chart_title="Chart", y_mode=0):
        chart = QChart()
        chart.setTitle(chart_title)

        x_axis = QDateTimeAxis()
        x_axis.setFormat("MM/dd")
        x_axis.setTitleText("Date")
        chart.addAxis(x_axis, Qt.AlignBottom)

        y_axis = QValueAxis()
        y_axis.setTickCount(10)
        if y_mode == 0: # Display Quantity Sold
            y_axis.setLabelFormat("%i")
            y_axis.setTitleText("Quantity Sold")
        elif y_mode == 1: # Display dollar amount sold
            y_axis.setLabelFormat("%.2f")
            y_axis.setTitleText("Amount Sold ($)")
        else: # Display default y_axis
            y_axis.setLabelFormat("%i")
            y_axis.setTitleText("y_axis")
        chart.addAxis(y_axis, Qt.AlignLeft)

        sales_lineseries = self.create_lineseries(item_sales, y_mode)

        # Variable to calculate y-axis range
        max_y = 0


        for item_lineseries in sales_lineseries:
            chart.addSeries(item_lineseries)
            item_lineseries.attachAxis(x_axis)
            item_lineseries.attachAxis(y_axis)

            # Update max_y
            for point in item_lineseries.pointsVector():
                y = point.y()
                max_y = max(max_y, y)

        # Set axis ranges
        if max_y == 0:
            max_y = 1  # Default range if no data
        y_axis.setRange(0, max_y * 1.15)

        dates = self.period_widget.get_dates()
        daterange = (dates[1] - dates[0]).days
        # Dynamically adjust tick count based on daterange
        if daterange <= 10:
            x_axis.setTickCount(daterange + 1)  # Ensure a tick for each date
        elif daterange <= 50:
            x_axis.setTickCount(min(10, daterange))  # At most 10 ticks for ranges <= 50 days
        else:
            x_axis.setTickCount(10)  # Default tick count for larger ranges

        return chart


    # Returns a list of lineseries created from item_sales items
    def create_lineseries(self, item_sales, y_mode=0):
        sales_lineseries = []

        for item in item_sales:
            series = QLineSeries()
            series.setName(item['name'])

            all_zero = True

            for daily_data in item['daily_sales']:
                date = QDateTime.fromString(daily_data['date'], "yyyy-MM-dd").toMSecsSinceEpoch()
                if y_mode == 0:
                    qnt_sold = daily_data['qnt_sold']
                    series.append(date, qnt_sold)
                    if qnt_sold > 0: all_zero = False
                else:
                    gross = daily_data['qnt_sold'] * item['sale_price']
                    series.append(date, gross)
                    if gross > 0: all_zero = False

            # Ensure the series is added even if all values are zero
            if all_zero:
                series.append(QDateTime.currentDateTime().toMSecsSinceEpoch(), 0)

            sales_lineseries.append(series)

        return sales_lineseries


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
