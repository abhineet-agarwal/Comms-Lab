#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: Admin
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class first_third(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "first_third")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.two = two = 1
        self.three = three = 1
        self.one = one = 1
        self.four = four = 1
        self.five = five = 1

        ##################################################
        # Blocks
        ##################################################
        self._two_range = Range(0.1, 10, 0.1, 1, 200)
        self._two_win = RangeWidget(self._two_range, self.set_two, 'two', "counter_slider", float)
        self.top_grid_layout.addWidget(self._two_win)
        self._three_range = Range(0.1, 10, 0.1, 1, 200)
        self._three_win = RangeWidget(self._three_range, self.set_three, 'three', "counter_slider", float)
        self.top_grid_layout.addWidget(self._three_win)
        self._one_range = Range(0.1, 10, 0.1, 1, 200)
        self._one_win = RangeWidget(self._one_range, self.set_one, 'k1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._one_win)
        self._four_range = Range(0.1, 10, 0.1, 1, 200)
        self._four_win = RangeWidget(self._four_range, self.set_four, 'four', "counter_slider", float)
        self.top_grid_layout.addWidget(self._four_win)
        self._five_range = Range(0.1, 10, 0.1, 1, 200)
        self._five_win = RangeWidget(self._five_range, self.set_five, 'five', "counter_slider", float)
        self.top_grid_layout.addWidget(self._five_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\Admin\\Downloads\\Bach.wav', True)
        self.blocks_multiply_const_vxx_5 = blocks.multiply_const_ff(four)
        self.blocks_multiply_const_vxx_4 = blocks.multiply_const_ff(two)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(five)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(three)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(one)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_4 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                6000,
                9000,
                30,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                500,
                3000,
                30,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                9000,
                15000,
                30,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                3000,
                6000,
                30,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                20,
                500,
                30,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.band_pass_filter_3, 0), (self.blocks_multiply_const_vxx_4, 0))
        self.connect((self.band_pass_filter_4, 0), (self.blocks_multiply_const_vxx_5, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_5, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_3, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "first_third")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_two(self):
        return self.two

    def set_two(self, two):
        self.two = two
        self.blocks_multiply_const_vxx_4.set_k(self.two)

    def get_three(self):
        return self.three

    def set_three(self, three):
        self.three = three
        self.blocks_multiply_const_vxx_1.set_k(self.three)

    def get_one(self):
        return self.one

    def set_one(self, one):
        self.one = one
        self.blocks_multiply_const_vxx_0.set_k(self.one)

    def get_four(self):
        return self.four

    def set_four(self, four):
        self.four = four
        self.blocks_multiply_const_vxx_5.set_k(self.four)

    def get_five(self):
        return self.five

    def set_five(self, five):
        self.five = five
        self.blocks_multiply_const_vxx_3.set_k(self.five)





def main(top_block_cls=first_third, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
