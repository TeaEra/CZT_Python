# -*- coding: utf-8 -*-

# 2014/8/19
# Author: Vince CHEN

from PyQt4 import QtGui
from PyQt4 import QtCore
import pandas as pd
import os

################################################################################
# Already copied;


try:
    _from_utf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _from_utf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

################################################################################
# TODO: ready for refactor;


class AllDataForTest(object):
    """
    All prepared data:
      - header info for 3 tabs;
      - model data for tab 0;
      - updated model data for tab 0;
    """

    @staticmethod
    def get_header_info0():
        return [
            "期初权益", "当前权益", "可用资金", "平仓盈亏",
            "持仓盈亏", "总盈亏", "持仓保证金", "资金风险率"
        ]

    @staticmethod
    def get_header_info1():
        return [
            "成交编号", "合约", "买卖", "开平", "成交价格",
            "成交手数", "成交时间", "报单编号", "成交类型", "投保", "交易所"
        ]

    @staticmethod
    def get_header_info2():
        return [
            "文华码", "合约名称", "涨幅%", "开盘", "最高", "最低",
            "最新", "涨跌", "买价", "买量", "卖价", "卖量", "现量",
            "增仓", "成交量", "持仓量", "日增仓", "结算", "昨结算", "昨收"
        ]

    @staticmethod
    def get_model_data0():
        return [
            ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
            ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
            ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'],
            ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'],
            ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'],
            ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'],
            ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'],
            ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
            ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8']
        ]

    @staticmethod
    def get_updated_model_data0():
        return [
            ['a1u', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
            ['b1', 'b2u', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
            ['c1', 'c2', 'c3u', 'c4', 'c5', 'c6', 'c7', 'c8'],
            ['d1', 'd2', 'd3', 'd4u', 'd5', 'd6', 'd7', 'd8'],
            ['e1', 'e2', 'e3', 'e4', 'e5u', 'e6', 'e7', 'e8'],
            ['f1', 'f2', 'f3', 'f4', 'f5', 'f6u', 'f7', 'f8'],
            ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7u', 'g8'],
            ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8u'],
            ['i1u', 'i2u', 'i3', 'i4u', 'i5', 'i6', 'i7', 'i8u']
        ]

################################################################################
# TODO: ready for refactor;


class UtilForTest(object):
    """
    Some prepared functions;
    """

    # Clear content data;
    @staticmethod
    def clean_data(model):
        model.removeRows(0, model.rowCount())

    # Assign content data;
    @staticmethod
    def assign_data(model, data):
        for eachRow in data:
            each_row_items = \
                [QtGui.QStandardItem(QtCore.QString(_from_utf8(str(item))))
                 for item in eachRow]
            model.appendRow(each_row_items)

    # Assign header info;
    @staticmethod
    def assign_header_info(model, header_info):
        for i in range(len(header_info)):
            model.setHeaderData(
                i, QtCore.Qt.Horizontal,
                QtCore.QVariant(_from_utf8(str(header_info[i])))
            )

    # Fore: yellow;
    # Back: black;
    @staticmethod
    def assign_data_with_color(model):
        for i in range(model.rowCount()):
            for j in range(model.columnCount()):
                model.setData(model.index(i, j), QtGui.QColor(QtCore.Qt.black),
                              QtCore.Qt.BackgroundRole)
                model.setData(model.index(i, j), QtGui.QColor(QtCore.Qt.yellow),
                              QtCore.Qt.ForegroundRole)

    # Fore: black;
    # Back: red;
    @staticmethod
    def update_data(model, updated_data):
        for i in range(len(updated_data)):
            for j in range(len(updated_data[0])):
                if model.item(i, j).text()\
                        .compare(
                            QtCore.QString(_from_utf8(str(updated_data[i][j])))
                        ) != 0:
                    model.setData(
                        model.index(i, j),
                        QtCore.QVariant(_from_utf8(str(updated_data[i][j])))
                    )
                    model.setData(
                        model.index(i, j),
                        QtGui.QColor(QtCore.Qt.red), QtCore.Qt.BackgroundRole
                    )
                    model.setData(
                        model.index(i, j),
                        QtGui.QColor(QtCore.Qt.black), QtCore.Qt.ForegroundRole
                    )

    @staticmethod
    def csv2frame(file_name):
        """
        读取CSV文件到DataFrame
        """
        try:
            print "*******", file_name
            data = pd.read_csv(file_name, index_col=0, parse_dates=True)
            data['islong'] = False if file_name.endswith("_.csv") else True
            assert data.index.is_unique
        except Exception, e:
            print u"**Warning: File \"%s\" doesn't exist!"%file_name
            data = None
        return data

    # Get the k-line data by file-path;
    @staticmethod
    def get_k_line_data_by_path(path):
        return UtilForTest.csv2frame(os.path.abspath(path))

    # Get minimum & maximum of price for y-axis;
    @staticmethod
    def get_min_and_max_price(k_line_data):
        if len(k_line_data) <= 0:
            return 0, 0
        first_entry = k_line_data.ix[k_line_data.index[0]]
        first_list = list()
        first_list.append(float(first_entry['open']))
        first_list.append(float(first_entry['close']))
        first_list.append(float(first_entry['high']))
        first_list.append(float(first_entry['low']))
        the_min = min(first_list)
        the_max = max(first_list)
        for eachIndex in k_line_data.index:
            each_entry = k_line_data.ix[eachIndex]
            temp_list = list()
            temp_list.append(float(each_entry['open']))
            temp_list.append(float(each_entry['close']))
            temp_list.append(float(each_entry['high']))
            temp_list.append(float(each_entry['low']))
            temp_min = min(temp_list)
            temp_max = max(temp_list)
            if temp_min < the_min:
                the_min = temp_min
            if temp_max > the_max:
                the_max = temp_max
        return the_min, the_max

################################################################################
# Status: OK;


class KLineSizeSetter(QtGui.QWidget):
    """
    """

    def __init__(self, size_min=1, size_max=500, curr_value=1):
        super(KLineSizeSetter, self).__init__()
        #
        main_grid_layout = QtGui.QGridLayout(self)
        #
        label_size = QtGui.QLabel(_from_utf8("K-Line size: "))
        spin_box_size = QtGui.QSpinBox()
        #
        main_grid_layout.addWidget(label_size, 0, 0, 1, 1)
        main_grid_layout.addWidget(spin_box_size, 1, 0, 1, 1)
        #
        spin_box_size.setMinimum(size_min)
        spin_box_size.setMaximum(size_max)
        spin_box_size.setValue(curr_value)
        #
        self._spin_box_size = spin_box_size

    def get_spin_box_size(self):
        return self._spin_box_size

    def get_spin_box_size_value(self):
        return self._spin_box_size.value()

    def set_size_min(self, size_min):
        self._spin_box_size.setMinimum(size_min)

    def set_size_max(self, size_max):
        self._spin_box_size.setMaximum(size_max)

    def set_curr_value(self, curr_value):
        self._spin_box_size.setValue(curr_value)


class IndexRangeSelector(QtGui.QWidget):
    """
    """

    def __init__(self, from_index=0, to_index=1):
        super(IndexRangeSelector, self).__init__()
        #
        #self.setFixedWidth(150)
        #self.setFixedHeight(100)
        #
        main_grid_layout = QtGui.QGridLayout(self)
        #
        label_from = QtGui.QLabel(_from_utf8("From"))
        label_to = QtGui.QLabel(_from_utf8("To"))
        spin_box_from = QtGui.QSpinBox()
        spin_box_to = QtGui.QSpinBox()
        #
        main_grid_layout.addWidget(label_from, 0, 0, 1, 1)
        main_grid_layout.addWidget(spin_box_from, 0, 1, 1, 1)
        main_grid_layout.addWidget(label_to, 1, 0, 1, 1)
        main_grid_layout.addWidget(spin_box_to, 1, 1, 1, 1)
        #
        spin_box_from.setMinimum(from_index + 1)
        spin_box_from.setMaximum(to_index + 1)
        spin_box_to.setMinimum(from_index + 1)
        spin_box_to.setMaximum(to_index + 1)
        #
        self._spin_box_from = spin_box_from
        self._spin_box_to = spin_box_to

    def get_spin_box_from(self):
        return self._spin_box_from

    def get_spin_box_to(self):
        return self._spin_box_to

    def get_from_value(self):
        return self._spin_box_from.value()

    def get_to_value(self):
        return self._spin_box_to.value()

    def set_from_value(self, from_value):
        self._spin_box_from.setValue(from_value)

    def set_to_value(self, to_value):
        self._spin_box_to.setValue(to_value)

################################################################################
# TODO: for test; to be removed;


class BlankArea(QtGui.QWidget):

    def __init__(self):
        super(BlankArea, self).__init__()
        #
        self_palette = QtGui.QPalette()
        self_palette.setColor(
            QtGui.QPalette.Background, QtGui.QColor(255, 0, 0)
        )
        self.setPalette(self_palette)
        self._pix_map = QtGui.QPixmap(self.size())
        self.refresh_pix_map()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.drawPixmap(0, 0, self._pix_map)
        painter.end()

    def refresh_pix_map(self):
        self._pix_map.fill(self, 0, 0)
        #
        self.update()


class InfoArea(QtGui.QWidget):

    def __init__(self):
        super(InfoArea, self).__init__()
        # About size;
        #self.setMinimumWidth(100)
        #self.setMinimumHeight(600)
        #
        self_palette = QtGui.QPalette()
        self_palette.setColor(
            QtGui.QPalette.Background, QtGui.QColor(0, 0, 255)
        )
        self.setPalette(self_palette)
        self.pix_map = QtGui.QPixmap(self.size())
        self.refresh_pix_map()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.drawPixmap(0, 0, self.pix_map)
        painter.end()

    def refresh_pix_map(self):
        self.pix_map.fill(self, 0, 0)
        #
        self.update()

################################################################################
# Status: OK


class PixMapSettings(object):
    """
    PixMapSettings
    """

    def __init__(self):
        super(PixMapSettings, self).__init__()
        self._settings = {}
        #
        self.init_settings()

    def init_settings(self):
        """
        Initialize settings;

        :return: nothing
        """
        # The size of pix_map:
        self._settings['pix_map_max_width'] = 30000.0
        self._settings['pix_map_max_height'] = 800.0
        # The margins:
        self._settings['pix_map_margin_top'] = 0.0
        self._settings['pix_map_margin_right'] = 0.0
        self._settings['pix_map_margin_bottom'] = 0.0
        self._settings['pix_map_margin_left'] = 0.0
        # The size of window:
        self._settings['window_width'] = 1000.0
        self._settings['window_height'] = 600.0
        # The x step:
        self._settings['pix_map_x_step_width'] = 50.0
        # To calculate pix_map_x_step_size:
        self.calc_settings_about_x()
        # To calculate pix_map_y_range:
        self.calc_pix_map_y_range()

    def calc_settings_about_x(self):
        """
        According to:
          - pix_map_max_width
          - pix_map_margin_left
          - pix_map_margin_right
          - pix_map_x_step_width
        Results:
          - pix_map_x_step_size
          - pix_map_x_history_size
          - pix_map_x_reserve_size
          - pix_map_k_line_rect_width

        :return: nothing
        """
        temp_total_width = \
            self._settings['pix_map_max_width'] \
            - self._settings['pix_map_margin_left'] \
            - self._settings['pix_map_margin_right'] \
            - self._settings['pix_map_x_step_width']
        temp_total_size = \
            int(
                temp_total_width
                / self._settings['pix_map_x_step_width']
            )
        self._settings['pix_map_x_step_size'] = \
            temp_total_size
        self._settings['pix_map_x_history_size'] = \
            temp_total_size - 1
        self._settings['pix_map_x_reserve_size'] = 1
        rect_step_ratio = 0.8
        self._settings['pix_map_k_line_rect_width'] = \
            rect_step_ratio * self._settings['pix_map_x_step_width']

    def calc_pix_map_y_range(self):
        """
        According to:
          - pix_map_max_height
          - pix_map_margin_top
          - pix_map_margin_bottom
        Results:
          - pix_map_y_range

        :return: nothing
        """
        self._settings['pix_map_y_range'] = \
            self._settings['pix_map_max_height'] \
            - self._settings['pix_map_margin_top'] \
            - self._settings['pix_map_margin_bottom']

    def get_settings(self):
        """
        Getter of _settings;

        :return: self._settings
        """
        return self._settings

    def set_margins(
            self, margin_top=0, margin_right=0, margin_bottom=0, margin_left=0):
        """

        :param margin_top: top margin
        :param margin_right: right margin
        :param margin_bottom: bottom margin
        :param margin_left: left margin
        :return: nothing
        """
        # TODO: exception raise?
        self._settings['pix_map_margin_top'] = 1.0 * margin_top
        self._settings['pix_map_margin_right'] = 1.0 * margin_right
        self._settings['pix_map_margin_bottom'] = 1.0 * margin_bottom
        self._settings['pix_map_margin_left'] = 1.0 * margin_left
        #
        self.calc_settings_about_x()
        self.calc_pix_map_y_range()

    def set_pix_map_size(self, max_width=30000, max_height=600):
        """

        :param max_width
        :param max_height
        :return: nothing
        """
        if max_width <= 0 or max_height <= 0:
            raise MaxSizeInvalidException()
        else:
            self._settings['pix_map_max_width'] = 1.0 * max_width
            self._settings['pix_map_max_height'] = 1.0 * max_height
            self.calc_settings_about_x()
            self.calc_pix_map_y_range()

    def set_pix_map_x_step_width(self, pix_map_x_step_width):
        if pix_map_x_step_width <= 0:
            raise XStepWidthInvalidException()
        else:
            self._settings['pix_map_x_step_width'] = \
                1.0 * pix_map_x_step_width
            self.calc_settings_about_x()

    def set_window_size(self, window_width=1000, window_height=600):
        if window_width <= 0 or window_height <= 0:
            raise WindowSizeInvalidException
        else:
            self._settings['window_width'] = 1.0 * window_width
            self._settings['window_height'] = 1.0 * window_height

    def get_pix_map_max_width(self):
        """
        Getter for 'pix_map_max_width'
        """
        return self._settings['pix_map_max_width']

    def get_pix_map_x_step_width(self):
        """
        Getter for 'pix_map_x_step_width'
        """
        return self._settings['pix_map_x_step_width']

################################################################################
# Status: OK


class MaxSizeInvalidException(Exception):
    """
    Exception: MaxSizeInvalidException
    """

    def __init__(self, msg="Max size is invalid."):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)


class XStepWidthInvalidException(Exception):
    """
    Exception: XStepWidthInvalidException
    """

    def __init__(self, msg="X step width is invalid."):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)


class WindowSizeInvalidException(Exception):
    """
    Exception: WindowSizeInvalidException
    """

    def __init__(self, msg="Window size is invalid"):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)

################################################################################


class RectLikeLine(object):

    def __init__(self):
        super(RectLikeLine, self).__init__()
        #
        self._line = QtCore.QLineF()
        self._pen_width = 0.0

    def set_line_with_pen_width(self, x1, y1, x2, y2, pen_width):
        """
        :param x1
        :param y1
        :param x2
        :param y2
        :param pen_width
        """
        self._line.setLine(x1, y1 - pen_width/2.0, x2, y2 - pen_width/2.0)

    def get_line(self):
        """
        :return self._line
        """
        return self._line

    def get_pen_width(self):
        """
        :return self._pen_width
        """
        return self._pen_width

################################################################################
# TODO: still need refactoring;


class KLine(QtGui.QWidget):
    """
    Class: KLine
    """

    def __init__(
        self, pix_map_settings
    ):
        super(KLine, self).__init__()
        #
        # Init the instance variables:
        self._k_line_data = None
        self._k_line_data_index = None
        #self.k_line_data_size = None
        self.pix_map = None
        self._is_loaded = False
        #
        # Get settings:
        self._settings = pix_map_settings.get_settings()
        # Background and foreground:
        self_palette = QtGui.QPalette()
        self_palette.setColor(
            QtGui.QPalette.Background, QtGui.QColor(0, 0, 0)
        )
        self_palette.setColor(
            QtGui.QPalette.Foreground, QtGui.QColor(255, 0, 0)
        )
        self.setPalette(self_palette)
        # Init pix map:
        self.start_index = 0
        self._curr_x_offset = 0
        self._curr_y_offset = 0
        self._curr_k_line_size = 20
        self._curr_width = \
            self._curr_k_line_size * self._settings['pix_map_x_step_width']
        self._curr_height = self.height()
        self.pix_map = QtGui.QPixmap(
            self._settings['pix_map_max_width'],
            self._settings['pix_map_max_height']
        )
        self.the_max = 0.0
        self.the_min = 0.0
        # TODO: should adapt to actions like update and append;
        self._curr_the_max = 0.0
        self._curr_the_min = 0.0
        # TODO: this is counted manually by now, should be dynamic;
        self._curr_k_line_index = 0
        self._valid_k_line_data = None
        #
        self.temp_layout = QtGui.QGridLayout()
        self.temp_layout.addWidget(
            QtGui.QLabel(
                "Please click the 'Load data file' "
                + "from menu bar 'K-Line'"
            ),
            0, 1, 1, 1
        )
        self.setLayout(self.temp_layout)

    # TODO: for test; to be removed;
    def get_data(self):
        return self._k_line_data

    def get_curr_width(self):
        return self._curr_width

    def init_pix_map(self):
        self.pix_map.fill(self, 0, 0)
        pix_map_painter = QtGui.QPainter(self.pix_map)
        pix_map_painter.initFrom(self)
        #
        self.init_k_lines_on_pix_map(pix_map_painter)
        #
        self.update()

    def init_k_lines_on_pix_map(self, painter):
        #
        pix_map_margin_top = self._settings['pix_map_margin_top']
        pix_map_margin_left = self._settings['pix_map_margin_left']
        pix_map_x_history_size = \
            self._settings['pix_map_x_history_size']
        #
        temp_k_line_data = \
            self._k_line_data[
                self.start_index: self.start_index + pix_map_x_history_size]
        self._valid_k_line_data = temp_k_line_data
        #
        the_min, the_max = UtilForTest.get_min_and_max_price(temp_k_line_data)
        the_min -= 5.0
        the_max += 5.0
        self.the_min = the_min
        self.the_max = the_max
        #
        self.draw_k_lines(
            painter,
            temp_k_line_data,
            pix_map_margin_left, pix_map_margin_top,
            the_max, the_min)

    def draw_k_lines(
            self, painter,
            temp_k_line_data,
            x_from, y_from,
            the_max, the_min
    ):
        #
        pix_map_x_step_width = self._settings['pix_map_x_step_width']
        pix_map_k_line_rect_width = \
            self._settings['pix_map_k_line_rect_width']
        y_range = self._settings['pix_map_y_range']
        #
        k_line_rectangles_red = []
        k_line_rectangles_white = []
        k_line_lines_red = []
        k_line_lines_white = []
        k_line_rect_like_lines_red = []
        k_line_rect_like_lines_white = []
        #
        for i in list(xrange(len(temp_k_line_data))):
            #
            # Current row:
            curr_data = temp_k_line_data.ix[i]
            #
            # Open price:
            open_price = curr_data["open"]
            #
            # Close price:
            close_price = curr_data["close"]
            #
            # High price:
            high_price = curr_data["high"]
            #
            # Low price:
            low_price = curr_data["low"]
            #
            x_start = \
                x_from + pix_map_x_step_width * (i + 1) \
                - pix_map_k_line_rect_width / 2
            y_start = \
                y_from \
                + abs(max(open_price, close_price) - the_max) \
                / (the_max - the_min) * y_range
            y_height = \
                abs(
                    max(open_price, close_price) - min(open_price, close_price)
                ) \
                / (the_max - the_min) * y_range
            #
            curr_rect = QtCore.QRectF()
            curr_rect_like_line = RectLikeLine()
            #
            # High enough: rect
            if y_height >= 5:
                curr_rect.setRect(
                    x_start, y_start, pix_map_k_line_rect_width, y_height
                )
            #
            # Otherwise: line instead of rect
            else:
                curr_rect_like_line.set_line_with_pen_width(
                    x_start, y_start,
                    x_start + pix_map_k_line_rect_width, y_start,
                    y_height
                )
            #
            # The high & low price line:
            curr_line = QtCore.QLineF(
                x_from + pix_map_x_step_width * (i + 1),
                y_from
                + abs(high_price - the_max) / (the_max - the_min) * y_range,
                x_from + pix_map_x_step_width * (i + 1),
                y_from
                + abs(low_price - the_max) / (the_max - the_min) * y_range
            )
            #
            # Red:
            if close_price > open_price:
                painter.fillRect(curr_rect, QtCore.Qt.red)
                k_line_rectangles_red.append(curr_rect)
                k_line_lines_red.append(curr_line)
                k_line_rect_like_lines_red.append(curr_rect_like_line)
            #
            # White:
            else:
                painter.fillRect(curr_rect, QtCore.Qt.white)
                k_line_rectangles_white.append(curr_rect)
                k_line_lines_white.append(curr_line)
                k_line_rect_like_lines_white.append(curr_rect_like_line)
        #
        # Red pen & white pen;
        pen_red = QtGui.QPen(QtCore.Qt.red)
        painter.setPen(pen_red)
        painter.drawRects(k_line_rectangles_red)
        painter.drawLines(k_line_lines_red)
        pen_white = QtGui.QPen(QtCore.Qt.white)
        painter.setPen(pen_white)
        painter.drawRects(k_line_rectangles_white)
        painter.drawLines(k_line_lines_white)
        #
        pen_red_for_rect_like_line = QtGui.QPen(QtCore.Qt.red)
        for each_rect_like_line in k_line_rect_like_lines_red:
            pen_red_for_rect_like_line.setWidth(
                each_rect_like_line.get_pen_width()
            )
            painter.setPen(pen_red_for_rect_like_line)
            painter.drawLine(
                each_rect_like_line.get_line()
            )
        pen_white_for_rect_like_line = QtGui.QPen(QtCore.Qt.white)
        for each_rect_like_line in k_line_rect_like_lines_white:
            pen_white_for_rect_like_line.setWidth(
                each_rect_like_line.get_pen_width()
            )
            painter.setPen(pen_white_for_rect_like_line)
            painter.drawLine(
                each_rect_like_line.get_line()
            )
        #

    def paintEvent(self, event):
        #
        if self._is_loaded:
            painter = QtGui.QPainter(self)
            painter.begin(self)
            temp_the_min, temp_the_max = \
                UtilForTest.get_min_and_max_price(
                    self._valid_k_line_data[
                        self._curr_k_line_index:
                        self._curr_k_line_index + self._curr_k_line_size
                    ]
                )
            self._curr_y_offset = \
                self._settings['pix_map_margin_top'] \
                + abs(temp_the_max - self.the_max) \
                / (self.the_max - self.the_min) \
                * self._settings['pix_map_y_range'] \
                - 5
            self._curr_height = \
                (temp_the_max - temp_the_min) / (self.the_max - self.the_min) \
                * self._settings['pix_map_y_range'] \
                + 10
            painter.drawPixmap(
                0.0, 0.0,
                self.width(), self.height(),
                self.pix_map,
                self._curr_x_offset, self._curr_y_offset,
                self._curr_width
                + self._settings['pix_map_x_step_width'] / 2.0 + 1,
                self._curr_height
            )
            painter.end()

    def refresh_pix_map(self, x_offset):
        #
        self._curr_x_offset = x_offset
        # TODO: rough calculation;
        self._curr_k_line_index = \
            int((x_offset - self._settings['pix_map_margin_left']) / 50.0)
        self.update()

    # Update last datum:
    def update_the_last_k_line(self, the_last_datum):
        #
        y_range = self._settings['pix_map_y_range']
        pix_map_margin_top = self._settings['pix_map_margin_top']
        pix_map_margin_left = self._settings['pix_map_margin_left']
        pix_map_x_step_width = self._settings['pix_map_x_step_width']
        pix_map_x_history_size = \
            self._settings['pix_map_x_history_size']
        pix_map_k_line_rect_width = \
            self._settings['pix_map_k_line_rect_width']
        #
        pix_map_painter = QtGui.QPainter(self.pix_map)
        pix_map_painter.initFrom(self)
        #
        open_price = the_last_datum['open']
        close_price = the_last_datum['close']
        high_price = the_last_datum['high']
        low_price = the_last_datum['low']
        #
        x_start = \
            pix_map_margin_left \
            + pix_map_x_step_width * pix_map_x_history_size
        # TODO: now just make the assumption, price is in the y_range;
        # TODO: thus self.the_min & self.the_max is valid;
        y_start = \
            pix_map_margin_top \
            + abs(max(open_price, close_price) - self.the_max) \
            / (self.the_max - self.the_min) * y_range
        y_height = \
            abs(
                max(open_price, close_price) - min(open_price, close_price)
            ) \
            / (self.the_max - self.the_min) * y_range
        #
        # To erase rectangle:
        #   extend to +1 and -1 to avoid potential erasing problem;
        erase_rect = QtCore.QRectF(
            x_start - pix_map_k_line_rect_width/2 - 1, 0,
            pix_map_k_line_rect_width+2, self._settings['pix_map_max_height']
        )
        pix_map_painter.eraseRect(erase_rect)
        #
        # To draw the new rectangle:
        new_rect = QtCore.QRectF(
            x_start - pix_map_k_line_rect_width/2, y_start,
            pix_map_k_line_rect_width, y_height)
        new_line = QtCore.QLineF(
            x_start,
            pix_map_margin_top
            + abs(high_price - self.the_max) / (self.the_max - self.the_min)
            * y_range,
            x_start,
            pix_map_margin_top
            + abs(low_price - self.the_max) / (self.the_max - self.the_min)
            * y_range
        )
        #
        if close_price > open_price:
            red_pen = QtGui.QPen(QtCore.Qt.red)
            pix_map_painter.setPen(red_pen)
            pix_map_painter.fillRect(new_rect, QtCore.Qt.red)
            pix_map_painter.drawRect(new_rect)
            pix_map_painter.drawLine(new_line)
        else:
            white_pen = QtGui.QPen(QtCore.Qt.white)
            pix_map_painter.setPen(white_pen)
            pix_map_painter.fillRect(new_rect, QtCore.Qt.white)
            pix_map_painter.drawRect(new_rect)
            pix_map_painter.drawLine(new_line)
        #
        # TODO: modify self._valid_k_line_data to adapt to the new data;
        self._valid_k_line_data.ix[-1] = the_last_datum
        #
        self.update()

    # Append a new k-line:
    def append_one_k_line(self, new_k_line_datum):
        #
        pix_map_painter = QtGui.QPainter(self.pix_map)
        pix_map_painter.initFrom(self)
        x_from = \
            self._settings['pix_map_margin_left'] \
            + self._settings['pix_map_x_step_width']\
            * self._settings['pix_map_x_history_size']
        y_from = \
            self._settings['pix_map_margin_top']
        # TODO: now just make the assumption, price is in the y_range;
        # TODO: thus self.the_min & self.the_max is valid;
        self.draw_k_lines(
            pix_map_painter,
            new_k_line_datum,
            x_from, y_from,
            self.the_max, self.the_min

        )
        #
        # TODO: adaptive!
        concatenated_temp_data = \
            pd.concat([self._valid_k_line_data, new_k_line_datum])
        self._valid_k_line_data = concatenated_temp_data
        #
        self.update()

    def get_curr_x_offset(self):
        return self._curr_x_offset

    def get_curr_k_line_size(self):
        return self._curr_k_line_size

    def set_curr_k_line_size(self, curr_k_line_size):
        self._curr_k_line_size = curr_k_line_size

    def set_curr_width(self, curr_width):
        """
        Setter for 'self._curr_width';
        """
        self._curr_width = curr_width

    def load_data_from_file(self, data_file):
        """
        Load k-line data from given file;
        """
        # About k-line data:
        self._k_line_data = UtilForTest.get_k_line_data_by_path(data_file)
        self._k_line_data_index = self._k_line_data.index
        #self.k_line_data_size = len(self._k_line_data)
        self.pix_map = QtGui.QPixmap(
            self._settings['pix_map_max_width'],
            self._settings['pix_map_max_height']
        )
        self._is_loaded = True
        #
        for i in reversed(range(self.temp_layout.count())):
            self.temp_layout.itemAt(i).widget().setParent(None)
        #
        self.init_pix_map()

    def load_k_line(self):
        file_dialog = QtGui.QFileDialog(self)
        file_dialog.setWindowTitle("Load data file")
        file_dialog.setNameFilter("Data files (*.csv)")
        file_dialog.show()
        if file_dialog.exec_():  # Click 'Open' will return 1;
            data_file = file_dialog.selectedFiles()[0]
            print(">>> Selected file: " + data_file)
            self.load_data_from_file(data_file)

################################################################################


class KLineContainer(QtGui.QMainWindow):
    """
    """

    def __init__(self, pix_map_settings):
        super(KLineContainer, self).__init__()
        #
        self._pix_map_settings = pix_map_settings
        #
        main_splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        left_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        right_splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        #
        main_splitter.addWidget(left_splitter)
        main_splitter.addWidget(right_splitter)
        main_splitter.setSizes(
            [self.width()*0.8, self.width()*0.2]
        )
        #
        k_line = KLine(
            pix_map_settings
        )
        k_line_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        k_line_slider.setEnabled(False)
        left_splitter.addWidget(k_line)
        left_splitter.addWidget(k_line_slider)
        left_splitter.setSizes(
            [self.height()*0.9, self.height()*0.1]
        )
        #
        info_area = InfoArea()
        index_range_selector = IndexRangeSelector()
        k_line_size_setter = KLineSizeSetter()
        index_range_selector.setEnabled(False)
        k_line_size_setter.setEnabled(False)
        QtCore.QObject.connect(
            k_line_size_setter.get_spin_box_size(),
            QtCore.SIGNAL("valueChanged(int)"), self.refresh_k_line_size
        )
        right_splitter.addWidget(info_area)
        right_splitter.addWidget(index_range_selector)
        right_splitter.addWidget(k_line_size_setter)
        right_splitter.setSizes(
            [self.height()*0.8, self.height()*0.1, self.height()*0.1]
        )
        #
        self.setCentralWidget(main_splitter)
        #
        max_offset = \
            pix_map_settings.get_pix_map_max_width() - k_line.get_curr_width()
        k_line_slider.setMinimum(0)
        k_line_slider.setMaximum(max_offset)
        k_line_slider.setPageStep(pix_map_settings.get_pix_map_x_step_width())
        QtCore.QObject.connect(
            k_line_slider,
            QtCore.SIGNAL("valueChanged(int)"), self.slide_to_offset
        )
        #
        self._k_line = k_line
        self._max_offset = max_offset
        self._k_line_slider = k_line_slider
        self._k_line_size_setter = k_line_size_setter

    def slide_to_offset(self, x_offset):
        self._k_line.refresh_pix_map(x_offset)
        self._k_line_slider.setValue(x_offset)

    def refresh_k_line_size(self, k_line_size):
        self._k_line.set_curr_width(
            k_line_size * self._pix_map_settings.get_pix_map_x_step_width()
        )
        self._k_line.set_curr_k_line_size(k_line_size)
        self._k_line.update()

    def get_k_line(self):
        return self._k_line

    def get_max_offset(self):
        return self._max_offset

    def get_k_line_slider(self):
        return self._k_line_slider

    def load_k_line(self):
        self._k_line.load_k_line()
        #
        self._k_line_size_setter.set_size_min(1)
        self._k_line_size_setter.set_size_max(1000)
        self._k_line_size_setter.set_curr_value(
            self._k_line.get_curr_k_line_size()
        )
        self._k_line_size_setter.setEnabled(True)
        #
        self.slide_to_offset(self._max_offset)
        self._k_line_slider.setEnabled(True)

################################################################################
# TODO: my refactoring main form;


class MainForm(QtGui.QWidget):
    """
    Class: MainWidget
    """

    def __init__(self):
        super(MainForm, self).__init__()
        #
        self._k_line_container = None
        #
        self.init_main_form()

    def init_main_form(self):
        #
        # Size of MainForm:
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        #
        # Layout for MainForm:
        main_form_grid_layout = QtGui.QGridLayout(self)
        main_form_grid_layout.setContentsMargins(5, 0, 5, 5)
        #
        # Tab-widget:
        tab_widget = QtGui.QTabWidget(self)
        tab_widget.setTabPosition(QtGui.QTabWidget.South)
        #
        # Tab 'K-Line':
        tab_k_line = QtGui.QWidget()
        tab_k_line_grid_layout = QtGui.QGridLayout(tab_k_line)
        tab_widget.addTab(tab_k_line, _from_utf8(""))
        pix_map_settings = PixMapSettings()
        k_line_container = KLineContainer(pix_map_settings)
        #
        self._k_line_container = k_line_container
        #
        tab_k_line_grid_layout.addWidget(
            k_line_container,
            0, 0, 1, 1
        )
        #
        # Tab 'None':
        tab_none = QtGui.QWidget()
        tab_none_grid_layout = QtGui.QGridLayout(tab_none)
        tab_widget.addTab(tab_none, _from_utf8(""))
        #
        # Set tab text for all tabs:
        self.setWindowTitle(
            _translate("Form", "TE-K-Line", None)
        )
        tab_widget.setTabText(
            tab_widget.indexOf(tab_k_line),
            _translate("Form", "K-Line", None)
        )
        tab_widget.setTabText(
            tab_widget.indexOf(tab_none),
            _translate("Form", "None", None)
        )
        #
        # Menu_bar for tab 'K-Line':
        tab_k_line_menu_bar = QtGui.QMenuBar(tab_widget)
        menu_k_line = tab_k_line_menu_bar.addMenu("K-Line")
        menu_none = tab_k_line_menu_bar.addMenu("None")
        #
        # Menu 'menu_k_line':
        action_update = menu_k_line.addAction("Update last k-line")
        action_append = menu_k_line.addAction("Append one k-line")
        QtCore.QObject.connect(
            action_update,
            QtCore.SIGNAL("triggered()"), self.update_k_line
        )
        QtCore.QObject.connect(
            action_append,
            QtCore.SIGNAL("triggered()"), self.append_k_line
        )
        menu_k_line.addSeparator()
        action_load = menu_k_line.addAction("Load data file")
        QtCore.QObject.connect(
            action_load,
            QtCore.SIGNAL("triggered()"), self.load_k_line
        )
        #
        # Add tab_widget & tab_k_line_menu_bar:
        main_form_grid_layout.addWidget(tab_widget, 1, 0, 1, 1)
        main_form_grid_layout.addWidget(tab_k_line_menu_bar, 0, 0, 1, 1)

    def update_k_line(self):
        self._k_line_container.get_k_line().update_the_last_k_line(
            self._k_line_container.get_k_line().get_data().ix[0]
        )
        self._k_line_container.get_k_line_slider().setValue(
            self._k_line_container.get_max_offset()
        )
        self._k_line_container.slide_to_offset(
            self._k_line_container.get_max_offset()
        )

    def append_k_line(self):
        self._k_line_container.get_k_line().append_one_k_line(
            self._k_line_container.get_k_line().get_data()[0:1]
        )
        self._k_line_container.get_k_line_slider().setValue(
            self._k_line_container.get_max_offset()
        )
        self._k_line_container.slide_to_offset(
            self._k_line_container.get_max_offset()
        )

    def load_k_line(self):
        self._k_line_container.load_k_line()

################################################################################
# Main portal:
if __name__ == "__main__":
    print(">>> Main portal")
    #
    import sys
    app = QtGui.QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())