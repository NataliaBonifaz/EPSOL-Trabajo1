#Se importan las librerias requeridas para la ejecución de la clase
import pandas as pd
import numpy as np
import os
import csv

#Se importa el .py de las interfaces gráficas
from Scripts.App_V2.Main_Window import *


#Se declara el .py de la clase de la ventana a utilizar
# y de la clase que procesa la información
from Scripts.App_V2.GraphicsMenu import *
from Scripts.App_V2.Graphic_Data import *

#Clase de la pantalla principal
class MainEpsolApp (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        
        #Variable que almacenará los archivos a utilizar en el programa
        self.files = None
        #Path del folder inicial
        self.initial_dir = "../"
        # Variable que almacenará el merge de los archivos cargados
        self.data = None

        
        #Listeners de los botones de la interfaz principal
        self.ui.load_file_button.clicked.connect(self.loadFiles)
        self.ui.download_file_button.clicked.connect(self.download)
        self.ui.graphic_button.clicked.connect(self.availableGraphics)
        self.ui.report_button.clicked.connect(self.generateReport)
        self.ui.menuHelp.triggered.connect(self.info)
        self.show()

    #Declaracion de métodos relacionados a los botones de la interfaz principal

    #Método para cargar los datos a procesas   
    def loadFiles(self):
        self.files = QFileDialog.getOpenFileNames(self, "Abrir Archivos", self.initial_dir, "CSV Files (*.csv)") 
        if self.files[0]:
            graph = Graphic_Data()
            self.data = graph.merge(self.files[0])
            

    #Metodo que descarga el csv de la informacion procesada
    def download(self):
        print(self.data)
        self.download = pd.DataFrame(self.data)
        self.download.to_csv('numeros2.csv', header=True, index=False)


    #Metodo que muestra el menu de las gráficas disponibles
    def availableGraphics(self):
        if self.files:
            if self.files[0]:
                #Se crea una instancia de GraphicsMenu
                self.menu = GraphicsMenu()
                #Se manda el merge que se genera con los datos cargados
                self.menu.cargarData(data=self.data)
                #Se establecen las opciones de gráficas que estan disponibles
                #A partir de los archivos cargados
                self.menu.activarOpciones()
                #Se muestra interfaz
                self.menu.show()
               
            else:
                #Se muestra señal de emergencia
                self.warning()
        else:
            #Se muestra señal de emergencia
            self.warning()
    
    #Metodo que genera el reporte de gráficas
    def generateReport(self):
        print("")
    
    #Metodo que miestra información de desarrollo
    def info(self):
        QMessageBox.about(self, "Informacion del programa",
                          "Programa Diseñado por:\nErick Rodriguez Orduña y\nCarlos " +
                          "Ramirez Rendon" + "\nPara: EPSOL SA de CV")

    #Metodo que muestra el mensaje de advertencia sobre datos inexistentes
    def warning(self):
        QMessageBox.warning(self, "Advertencia!", "No existen archivos cargados", buttons=QMessageBox.Ok)


#Main
if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    app = QtWidgets.QApplication(sys.argv)
    my_app = MainEpsolApp()
    sys.exit(app.exec_())