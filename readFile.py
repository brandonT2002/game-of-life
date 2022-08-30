import xml.etree.ElementTree as ET
from app import Grid

class Read:
    def getContent(self,routeFile):
        tree = ET.parse(routeFile)
        root = tree.getroot()

        for patient in root:
            data = patient[0]
            print('Nombre: ',data[0].text)
            print('Edad: ',data[1].text)
            print('Periodos: ',patient[1].text)
            print('Dimensiones: ',patient[2].text)
            grid = patient[3]
            grill = Grid(int(patient[2].text))
            for cell in grid:
                print(f"F: {cell.attrib['f']}, C: {cell.attrib['c']}")
                grill.killCell(int(cell.attrib['f']),int(cell.attrib['c']))

            grill.generatePeriod(int(patient[1].text))

read = Read()
read.getContent('ArchivoEntradaV1.xml')
