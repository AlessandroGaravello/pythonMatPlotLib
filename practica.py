import pandas as pd
import matplotlib.pyplot as plt
#consume los datos del archivo inversiones
#almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
#gráfico de dispersión de los totales de superficie por TIPUSSOL
#gráfico de barras de la supeficie media de los 10 primeros NOM_ENS
#gráfico circular de las superficie de 10 NOM_ENS

def consumirHistograma():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','SUPERFICIE','TIPUSSOL']]#convertir datos en Dataframe
    #print(df)
    df.SUPERFICIE.plot.hist()
    plt.show()
consumirHistograma()

def consumirDispersion():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','SUPERFICIE','TIPUSSOL','CODI_TIPUSSOL']]#convertir datos en Dataframe
    #print(df)
    df.plot.scatter(x='SUPERFICIE',y='CODI_TIPUSSOL',alpha=0.2)
    plt.show()
consumirDispersion()

