from PySide6.QtCore import QRunnable, Slot, Signal, QObject
import traceback
import sys

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
       super(Worker, self).__init__()
       self.__fn = fn
       self.__args = args
       self.__kwargs = kwargs
       self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            result = self.__fn(*self.__args, **self.__kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


