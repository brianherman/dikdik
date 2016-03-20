from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime

class MainWindow:
    def fill_item(self, item, value):
        item.setExpanded(True)
        if type(value) is dict:
            for (key, val) in sorted(value.iteritems()):
                child = QTreeWidgetItem()
                child.setText(0, unicode(key))
                item.addChild(child)
                fill_item(child, val)
        elif type(value) is list:
            beginlist = QTreeWidgetItem()
            beginlist.setText(0,'[')
            item.addChild(beginlist)
            for val in value:
                child = QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:
                    child.setText(0, '{')
                    fill_item(child, val)
                    enddict = QTreeWidgetItem()
                    enddict.setText(0, '}')
                    item.addChild(enddict)
                elif type(val) is list:
                    child.setText(0, '[')
                    fill_item(child, val)
                    endlist = QTreeWidgetItem()
                    endlist.setText(0, ']')
                    item.addChild(endlist)

                else:

                    child.setText(0, str(type(val))+ ' '+ unicode(val))
                child.setExpanded(True)
            endlist = QTreeWidgetItem()
            endlist.setText(0, ']')
            item.addChild(endlist)
        else:
            child = QTreeWidgetItem()
            child.setText(0, unicode(value))
            item.addChild(child)


    def fill_widget(self, widget, value):
        widget.clear()
        fill_item(widget.invisibleRootItem(), value)\
    def show(self,args):
        """Entry point for the application script"""
        dictionary = {}

        app = QApplication(sys.argv)


        widget = QTreeWidget()
        fill_widget(widget, data)
        widget.show()
        sys.exit(app.exec_())
