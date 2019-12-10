#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
import Thefirst  # module dialog_test_ui.py
from PyQt5.QtCore import *  # for Qt.ApplicationModal

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 因为使用Qt Designer设计的ui是默认继承自object类，不提供show()显示方法，
    # 所以我们需要生成一个QDialog对象来重载我们设计的Ui_Dialog类，从而达到显示效果。
    MainDialog = QDialog()  # 创建一个主窗体（必须要有一个主窗体）
    myDialog = Thefirst.Ui_Dialog()  # 创建对话框
    myDialog.setupUi(MainDialog)  # 将对话框依附于主窗体
    # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
    # MainDialog.setWindowModality(Qt.ApplicationModal)
    MainDialog.show()

    sys.exit(app.exec_())