#!/usr/bin/python3
# Made By Sina Meysami
# Black-Notepad v1.0
#


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import qdarktheme
import qtmodern.styles
import qtmodern.windows
import sys,platform

width = 1000
height = 700


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        qdarktheme.setup_theme("dark")
        self.file = False
        self.file_path = ""
        self.n_line = True
        self.setWindowTitle("Notepad - New File")
        self.setWindowIcon(QIcon("black-notepad-icon.ico"))
        self.setGeometry(500,150,width,height)
    
        
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        
        self.text = QTextEdit(self)
        self.text.setFont(font)
        self.setCentralWidget(self.text)
        self.set_theme()
        self.key_shortcut()
        self.menu()
        
    def menu(self):
        self.menu_ = self.menuBar()
        self.file = self.menu_.addMenu("&File")
        self.edit = self.menu_.addMenu("&Edit")
        self.font = self.menu_.addMenu("&Font")
        self.theme = self.menu_.addMenu("&Theme")
        self.view = self.menu_.addMenu("&View")
        self.help = self.menu_.addMenu("&Help")
        
        self.file.addAction(QIcon("new_file.png"),"New File",self.new_file)
        self.file.addAction(QIcon("open_file.png"),"Open File",self.open_file)
        self.file.addAction(QIcon("save_file.png"),"Save File",self.save_file)
        self.file.addAction(QIcon("save_as.jpg"),"Save As",self.save_as)
        self.file.addAction(QIcon("star.png"),"Star",self.star_file)
        self.file.addAction(QIcon("bookmark.png"),"Bookmark",self.bookmark)
        self.file.addSeparator()
        self.file.addAction(QIcon("printer.ico"),"Print",self.print_dialog)
        self.file.addSeparator()
        self.file.addAction(QIcon("exit_icon.png"),"&Exit",self.close)
        self.font.addAction("Set Font",self.font_dialog)
        self.font.addAction("Set Font Size",self.font_size)
        self.font.addAction("Set Font Color",self.font_color)
        self.theme.addAction("Light",self.light)
        self.theme.addAction("Dark",self.dark)
        self.theme.addAction("Matrix",self.matrix)
        self.theme.addAction("Sky",self.sky)
        self.theme.addAction("Bee",self.bee)
        
        self.edit.addAction("Undo",self.text.undo)
        self.edit.addAction("Redo",self.text.redo)
        self.edit.addSeparator()
        self.edit.addAction("Cut",self.text.cut)
        self.edit.addAction("Copy",self.copy_text)
        self.edit.addAction("Paste",self.text.paste)
        self.edit.addSeparator()
        self.edit.addAction("Select All",self.text.selectAll)
        self.edit.addAction("Clear All",self.text.clear)
        self.view.addAction("Fullscreen",self.showFullScreen)
        self.view.addAction("Normal",self.showNormal)
        self.view.addAction("Minimize",self.showMinimized)
        self.help.addAction("Help",self.help_)
        self.help.addAction("About",self.about_)
        self.help.addAction("Donate",self.donate)
        self.help.addSeparator()
        self.help.addAction("Send Feedback",self.send_feedback)
        self.statusbar_()
        self.set_toolbar()
        
    def key_shortcut(self):
        exit_key = QShortcut(QKeySequence("Ctrl+Q"),self)
        exit_key.activated.connect(self.close)
        exit_key_2 = QShortcut(QKeySequence("Ctrl+E"),self)
        exit_key_2.activated.connect(self.close)
        open_key = QShortcut(QKeySequence("Ctrl+O"),self)
        open_key.activated.connect(self.open_file)
        save_key = QShortcut(QKeySequence("Ctrl+S"),self)
        save_key.activated.connect(self.save_file)
        save_as_key = QShortcut(QKeySequence("Ctrl+Shift+S"),self)
        save_as_key.activated.connect(self.save_as)
        help_key = QShortcut(QKeySequence("Ctrl+H"),self)
        help_key.activated.connect(self.help_)
        bookmark_key = QShortcut(QKeySequence("Ctrl+B"),self)
        bookmark_key.activated.connect(self.bookmark)
        
        
    def set_toolbar(self):
        tools = QToolBar()
        tools.setMovable(False)
        self.addToolBar(tools)
        tools.addAction(QIcon("new_file.png"),"New File",self.new_file)
        tools.addAction(QIcon("open_file.png"),"Open File",self.open_file)
        tools.addAction(QIcon("save_file.png"),"Save File",self.save_file)
        tools.addAction(QIcon("save_as.jpg"),"Save As",self.save_as)
        tools.addAction(QIcon("star.png"),"Star",self.star_file)
        tools.addAction(QIcon("help_icon.png"),"Help",self.help_)
        tools.addAction(QIcon("exit_icon.png"),"Exit",self.close)
    def undo(self):
        self.text.undo()
    def redo(self):
        self.text.redo()
    def copy(self):
        self.text.copy()
    def paste(self):
        self.text.paste()
    def cut(self):
        self.text.cut()
    def star_file(self):
        try:
            if self.n_line == True:
                file_path = self.file_path
                if file_path != "" and file_path != " ":
                    file = open(f"bookmark.txt","a")
                    file.write(f"{file_path}")
                    file.close()
                    self.n_line = False
                    print(True)
                else:
                    pass
            else:
                    file_path = self.file_path
                    if file_path != "" and file_path != " ":
                        file = open(f"bookmark.txt","a")
                        file.write(f"\n{file_path}")
                        file.close()
                        print(False)
                    else:
                        pass
        except:
            pass
    def bookmark(self):
        try:
            dlg = QMainWindow(self)
            dlg.setWindowTitle("Black-Notepad/Bookmarks")
            dlg.setWindowIcon(QIcon("black-notepad-icon.ico"))
            dlg.setGeometry(700,300,500,400)
            dlg.setFixedSize(500,400)
            self.mylist = QListWidget(dlg)
            self.mylist.resize(500,380)
            self.mylist.itemDoubleClicked.connect(self.open_file_list)
            dlg.setCentralWidget(self.mylist)
            file = open("bookmark.txt","r").readlines()
            for item in file:
                item = item.strip()
                self.mylist.addItem(item)
            
        
            menu = QMenuBar(dlg)
            dlg.setMenuBar(menu)
            options = menu.addMenu("Options")
            options.addAction("Clear All",self.clear_bookmark)
            options.addSeparator()
            options.addAction("Close",dlg.close)
        
            dlg.show()
        except (Exception,) as err:
            print(err)
            pass
    def open_file_list(self,item):
       item_ = item.text()
       file_text = open(item_,"r").read()
       self.text.setText(file_text)
    def clear_bookmark(self):
        file = open("bookmark.txt","w")
        file.write("")
        file.close()
        self.mylist.clear()
        self.n_line = True
    def new_file(self):
        self.text.clear()
        self.file = False
        self.file_path = ""
        self.setWindowTitle("Notepad - nodocument")
    
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*)", options=options)
        self.file_path = fileName
        self.setWindowTitle(f"Notepad - {self.file_path}")
        if self.file_path != "":
            self.file = True
        if fileName:
            f = open(fileName,"r",encoding="UTF-8").read()
            self.text.setText(f)
    
    def save_file(self):
        if self.file == True:
            try:
                file = open(self.file_path,'w',encoding="UTF-8")
                text = self.text.toPlainText()
                file.write(text)
            except:
                pass
        else:
            try:
                
                name = QFileDialog.getSaveFileName(self, 'Save File')
                self.file_path = name[0]
                self.setWindowTitle(f"Notepad - {name[0]}")
                file = open(self.file_path,'w',encoding="UTF-8")
                text = self.text.toPlainText()
                file.write(text)
            
                file.close()
                if self.file_path != "":
                    self.file = True
            except (Exception,FileNotFoundError,):
                self.file = False
    def save_as(self):
        try:
            name = QFileDialog.getSaveFileName(self, 'Save As')
            self.setWindowTitle(f"Notepad - {name[0]}")
                
            file = open(name[0],'w',encoding="UTF-8")
            text = self.text.toPlainText()
            file.write(text)
            file.close()
            
            if name[0] != "":
                self.file = True
        except (Exception,FileNotFoundError,):
            self.file = False
    def print_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        print_dlg = QPrintPreviewDialog(printer,self)
        print_dlg.paintRequested.connect(self.print_preview)
        print_dlg.exec_()
    def print_preview(self,printer):
        self.text.print_(printer)
    def help_(self):
        width = 500
        height = 400
        text = """Developer: Sina Meysami
Version: v1.0
Ctrl + Q = QUIT
Ctrl + E = QUIT
Ctrl + P = Print
Ctrl + O = Open File
Ctrl + S = Save File
Ctrl + Shift + S = Save As
Ctrl + H = Help
Ctrl + B = Bookmark
"""
        dlg = QDialog()
        dlg.setWindowTitle("Black-Notepad/Help")
        dlg.setWindowIcon(QIcon("black-notepad-icon.ico"))
        
        dlg.setGeometry(600,300,width,height)
        t = QTextEdit(dlg)
        t.setReadOnly(True)
        t.setText(text)
        t.resize(width,height)
        
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        t.setFont(font)
        res = dlg.exec_()
    def about_(self):
        width = 500
        height = 400
        text = """Developer: Sina Meysami
Version: v1.0

Instagram: https://instagram.com/sina.coder
Telegram: https://t.me/sina_python
Twitter: https://twitter.com/Sinameysami
Github: https://github.com/mrprogrammer2938
Weblog: sinameysami.blogfa.com
"""
        dlg = QDialog()
        dlg.setWindowTitle("Black-Notepad/About")
        dlg.setWindowIcon(QIcon("black-notepad-icon.ico"))
        dlg.setGeometry(600,300,width,height)
        t = QTextEdit(dlg)
        t.setReadOnly(True)
        t.setText(text)
        t.resize(width,height)
        
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        t.setFont(font)
        res = dlg.exec_()
        
    def donate(self):
        #webbrowser.open_new_tab("https://google.com")
        pass
    def send_feedback(self):
        #webbrowser.open_new_tab("")
        pass
    def font_dialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)
            
    def font_size(self):
        dlg = QDialog()
        dlg.setWindowTitle("Set Font Size")
        dlg.setWindowIcon(QIcon("black-notepad-icon.ico"))
        dlg.setFixedSize(122,64)
        
        self.spinbox = QSpinBox(dlg)
        self.spinbox.resize(121,22)
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(72)
        self.spinbox.valueChanged.connect(self.set_font_size)
        
        set_btn = QPushButton("Set",dlg)
        set_btn.setGeometry(0,20,121,24)
        set_btn.clicked.connect(self.set_font_size)
        
        close_btn = QPushButton("Close",dlg)
        close_btn.setGeometry(0,40,121,24)
        close_btn.clicked.connect(dlg.close)
        
        rev = dlg.exec_()
    def set_font_size(self):
        self.text.selectAll()
        self.text.setFontPointSize(self.spinbox.value())
    def font_color(self):
        font_color = QColorDialog().getColor()
        self.text.selectAll()
        self.text.setTextColor(font_color)
    # ----- Theme -----
    def set_theme(self):
        f = open("theme.txt","r").read()
        if f == "light":
            self.light()
        elif f == "dark":
            self.dark()
        elif f == "matrix":
            self.matrix()
        elif f == "sky":
            self.sky()
        elif f == "bee":
            self.bee()
    def light(self):
        qtmodern.styles.light(QApplication.instance())   
        self.text.setStyleSheet("""
QTextEdit {
    color: #000;
    background-color: #fff;
    
}
                                
""")                     
        f = open("theme.txt","w")
        f.write("light")
        f.close()
    def dark(self):
        qtmodern.styles.dark(QApplication.instance())
        self.text.setStyleSheet("""
QTextEdit {
    color: white;
    background-color: black;
    
}
                                
""")
        f = open("theme.txt","w")
        f.write("dark")
        f.close()
    def matrix(self):
        qtmodern.styles.dark(QApplication.instance()) 
        self.text.setStyleSheet("""
QTextEdit {
    color: lightgreen;
    background-color: black;    
        
}
                                
""")
        f = open("theme.txt","w")
        f.write("matrix")
        f.close()
    def sky(self):
        qtmodern.styles.light(QApplication.instance()) 
        self.text.setStyleSheet("""
QTextEdit {
    color: lightblue;
    background-color: blue;
    
}
                                
""")
        f = open("theme.txt","w")
        f.write("sky")
        f.close()
    def bee(self):
        qtmodern.styles.dark(QApplication.instance()) 
        self.text.setStyleSheet("""
QTextEdit {
    color: yellow;
    background-color: #000;    
}                          
""")
        f = open("theme.txt","w")
        f.write("bee")
        f.close()
    def copy_text(self):
        self.text.selectAll()
        self.text.copy()
    def statusbar_(self):
        status = QStatusBar(self)
        status.showMessage(f"Black-Notepad  {self.file_path}")
        self.setStatusBar(status)
    def get_error(self):
        error = QErrorMessage(self)
        error.showMessage("Error, Please Try Again!")
        error.show()
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Black-Notepad")
    app.setApplicationDisplayName("Black-Software")
    app.setApplicationVersion("v1.0")
    win = Window()
    win.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    # Black Notepad v2.0
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        main()
    else:
        print("Sorry Please Run This App On Windows,Linux Or Mac OS!")
        sys.exit()
