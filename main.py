from invoice_UI import Ui_Invoice
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import pandas as pd


def tax_id():
    list_tax = []
    with open("tax_ID.txt", "r") as f:
        for i in f:
            list_tax.append(i.strip())
    return list_tax

class window_controller(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Invoice()
        self.ui.setupUi(self)
        self.ui.tax_text.addItems(tax_id())
        self.act()
    def act(self):
        self.ui.open.clicked.connect(self.open_path)
        self.ui.save.clicked.connect(self.save_path)
        self.ui.start.clicked.connect(self.run)
    def open_path(self):
        filename, filetype = QFileDialog.getOpenFileName(self,"選擇待查資料","D:\Python\電子發票\電子發票\發票明細CSV檔","CSV File(*.csv);;Excel File(*.xlsx)")# start path
        self.ui.open_text.setText(filename)
    def save_path(self):
        folder = QFileDialog.getExistingDirectory(self,"選擇結果生成路徑","D:\Python\電子發票\電子發票")# start path
        self.ui.save_text.setText(folder)
    def output(self, command = '\u2713 Successful'):
        if command != '\u2713 Successful':
            self.ui.output_text.setStyleSheet("QLabel{color: red;}")
            command = "\u2715 " + command
        else:
            self.ui.output_text.setStyleSheet("QLabel{color: green;}")
        self.ui.output_text.setText(command)
    def run(self):
        tax_text = self.ui.tax_text.currentText()
        invoice_b_text = self.ui.invoice_b_num.toPlainText()
        invoice_e_text = self.ui.invoice_e_num.toPlainText()
        open_text = self.ui.open_text.toPlainText()
        save_text = self.ui.save_text.toPlainText()
        # 欄位輸入值為空時的判斷顯示語句
        if len(invoice_b_text) != 10:
            self.output('發票起號錯誤')
            return
        if len(invoice_e_text) != 10 or invoice_e_text[:2].upper() != invoice_b_text[:2].upper() or int(invoice_e_text[2:]) <= int(invoice_b_text[2:]):
            self.output('發票訖號錯誤')
            return
        if open_text == '':
            self.output('資料來源未選擇')
            return
        if save_text == '':
            self.output('儲存位置未選擇')
            return
        # 讀取csv檔案
        df = pd.read_csv(open_text)
        try:
            df_taxs = df['銷售人統編']
            # 確認整個欄位的'銷售人統編'是否一致
            tax_check = []
            for tax in df_taxs:
                if tax not in tax_check:
                    tax_check.append(tax)
            # 確認檔案內所有統編是否一致
            if len(tax_check) > 1:
                self.output('檔案內有多個統編，請重新選擇檔案')
                return
            # 確認所選擇的統編和檔案內的是否一致
            if tax_check[0] != int(tax_text):
                self.output('檔案內統編與所選不一致，請重新確認')
                return
            else:
                self.output()
        except KeyError:
            self.output('格式不匹配，請確認檔案內容是否正確')
        except Exception as e:
            self.output(e)
        # 讀取發票開頭字母
        inv_title = invoice_b_text[:2].upper()
        inv_b = int(invoice_b_text[2:])
        inv_e = int(invoice_e_text[2:])
        inv_nums = []
        df_inv = df['發票起號']
        for inv in df_inv:
            # 判斷是否為所選擇的發票開頭
            if inv[:2].upper() == inv_title:
                if inv_b < int(inv[2:]) < inv_e:
                    inv_nums.append(inv[2:])
        inv_nums.sort()
        print(inv_nums)