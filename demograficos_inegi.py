# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:45:20 2019

@author: GUILLERMO IZQUIERDO

Bases de datos a nivel municipal de México
con datos poblacionales y con código postal
para alimentar modelos de ML.
"""


import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

import plotly.io as pio
import plotly.graph_objects as go

def poblacion_economicamente_activa_municipal():
    """
    NOTA
    
    FUENTE: Encuesta Intercensal 2015, INEGI.
    Nota: Los límites de confianza se calculan al 90 por ciento.
    1  La distribución porcentual de la condición de actividad económica se calcula respecto de la población de 12 años y más.
    2  La distribución porcentual se calcula respecto al total de la población económicamente activa.
    *  Municipio censado.
    **  Municipio con muestra insuficiente.
    
    """
    pea_2015 = pd.read_excel('datos/siha_2_2_4_1_agosto_2016.xlsx', encoding='utf-8', sheet_name='2015')
    columnas_pea = ['CLAVE','ESTADO','MUNICIPIO','POB_12_MAS','PEA_TOTAL','PEA_OCUPADA','PEA_DESOCUPADA','NO_PEA','NO_PEA_ESPECIFICADO']
    pea_2015_copy = pea_2015.iloc[5:-8,:].copy()
    pea_2015_copy.columns = columnas_pea
    return pea_2015_copy



def obligaciones_fiscales_municipales():
    """
    NOTA
    
    Fuente: Unidad de Coordinación con Entidades Federativas, SHCP.
    """
    obligaciones_finan_mun_2015 = pd.read_excel('datos/siha_2_2_5.xlsx', encoding='utf-8', sheet_name='1° 2015')
    columnas_obligaciones_finan_mun_2015 = ['CLAVE','ESTADO','MUNICIPIO','OB_BANCA_MUL','OB_BANCA_DESA','OB_EMISIONES_BUR',
                                            'OB_OTROS','OB_TOTAL']
    obligaciones_finan_mun_2015_copy = obligaciones_finan_mun_2015.iloc[5:-2,:].copy()
    obligaciones_finan_mun_2015_copy = obligaciones_finan_mun_2015_copy.iloc[:,:-1]
    obligaciones_finan_mun_2015_copy.columns = columnas_obligaciones_finan_mun_2015
    return obligaciones_finan_mun_2015_copy



def delitos_fuero_comun_municipal():
    """
    NOTA
    
    * En la suma anual se incluyen el total de delitos patrimoniales (abuso de confianza, daño en propiedad ajena,
     extorsión, fraude y despojo), delitos sexuales (violación), homicidios, lesiones, privación de la libertad y robo
     (en sus diversos tipos).
    
    FUENTE: Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública.
    n. d. = No disponible
    """
    delitos_fuero_comun_mun_2015 = pd.read_excel('datos/siha_2_2_4_9_dic_2015.xlsx', encoding='utf-8')
    columnas_delitos_fuero_comun_mun_2015 = ['CLAVE','ESTADO','MUNICIPIO','DELITOS_2011','DELITOS_2012','DELITOS_2013',
                                            'DELITOS_2014']
    delitos_fuero_comun_mun_2015_copy = delitos_fuero_comun_mun_2015.iloc[3:-5,:].copy()
    delitos_fuero_comun_mun_2015_copy.columns = columnas_delitos_fuero_comun_mun_2015
    return delitos_fuero_comun_mun_2015_copy
    


def alumnos_municipal():
    """
    NOTA
    
    FUENTE: Sistema Estatal y Municipal de Bases de Datos, INEGI
    
    C = Cifra no publicable, por el principio de confidencialidad de la Ley de Información Estadística y Geográfica.
    ND = No disponible
    """
    alumnos_mun_2012 = pd.read_excel('datos/siha_2_2_4_8.xlsx', encoding='utf-8')
    columnas_alumnos_mun_2012 = ['CLAVE','ESTADO','MUNICIPIO',
                                'ALUM_TOTALES_2005','PREESCOLAR_2005','PRIMARIA_2005',
                                'SECUNDARIA_2005','PROFESIONAL_T_2005','BACHILLERATO_2005',
                                'ALUM_TOTALES_2006','PREESCOLAR_2006','PRIMARIA_2006',
                                'SECUNDARIA_2006','PROFESIONAL_T_2006','BACHILLERATO_2006',
                                'ALUM_TOTALES_2007','PREESCOLAR_2007','PRIMARIA_2007',
                                'SECUNDARIA_2007','PROFESIONAL_T_2007','BACHILLERATO_2007',
                                'ALUM_TOTALES_2008','PREESCOLAR_2008','PRIMARIA_2008',
                                'SECUNDARIA_2008','PROFESIONAL_T_2008','BACHILLERATO_2008',
                                'ALUM_TOTALES_2009','PREESCOLAR_2009','PRIMARIA_2009',
                                'SECUNDARIA_2009','PROFESIONAL_T_2009','BACHILLERATO_2009',
                                'ALUM_TOTALES_2010','PREESCOLAR_2010','PRIMARIA_2010',
                                'SECUNDARIA_2010','PROFESIONAL_T_2010','BACHILLERATO_2010',
                                'ALUM_TOTALES_2011','PREESCOLAR_2011','PRIMARIA_2011',
                                'SECUNDARIA_2011','PROFESIONAL_T_2011','BACHILLERATO_2011',
                                'ALUM_TOTALES_2012','PREESCOLAR_2012','PRIMARIA_2012',
                                'SECUNDARIA_2012','PROFESIONAL_T_2012','BACHILLERATO_2012']

    alumnos_mun_2012_copy = alumnos_mun_2012.iloc[4:-5,:].copy()
    alumnos_mun_2012_copy.columns = columnas_alumnos_mun_2012
    return alumnos_mun_2012_copy
    


def viviendas_internet_municipal():
    """
    NOTA
    
    FUENTE: Resultados definitivos del Censo de Población y Vivienda 2010, INEGI.
    """
    viviendas_inter_2010 = pd.read_excel('datos/siha_2_2_4_6.xlsx', encoding='utf-8')
    columnas_viviendas_inter_2010 = ['CLAVE','ESTADO','MUNICIPIO',
                                     'VIV_HABITADAS','VIV_C_COMPUTADORA','VIVIENDAS_C_INTERNET']
    viviendas_inter_2010_copy = viviendas_inter_2010.iloc[3:-3,1:].copy()
    viviendas_inter_2010_copy.columns = columnas_viviendas_inter_2010
    return viviendas_inter_2010_copy



def medicos_municipal():
    """
    NOTA
    
    * Incluye personal adscrito al IMSS, ISSSTE, PEMEX, SEDENA, SEMAR, IMSS-Oportunidades, SSA y otras.
    Fuente: INEGI, Sistema Estatal y Municipal de Base de Datos
    """
    medicos_2012 = pd.read_excel('datos/siha_2_2_4_5.xlsx', encoding='utf-8')
    columnas_medicos_2012 = ['CLAVE','ESTADO','MUNICIPIO',
                             'MEDICOS_2005', 'MEDICOS_2006', 'MEDICOS_2007',
                             'MEDICOS_2008', 'MEDICOS_2009', 'MEDICOS_2010',
                             'MEDICOS_2011','MEDICOS_2012']
    medicos_2012_copy = medicos_2012.iloc[3:-4,:].copy()
    medicos_2012_copy.columns = columnas_medicos_2012
    return medicos_2012_copy
    


def infraestructura_educativa_municipal():  
    """
    NOTA
    
    * Comprende los niveles preescolar, primaria, secundaria, profesional técnico,
    bachillerato y superior. La información está expresada en términos de planta
    física y puede servir para el funcionamiento de varias escuelas o turnos.
    
    ND = No disponible
    FUENTE: INEGI, Sistema Estatal y Municipal de Bases de Datos
    
    """
    infra_ed_2012 = pd.read_excel('datos/siha_2_2_4_2.xlsx', encoding='utf-8')
    columnas_infra_ed_2012 = ['CLAVE','ESTADO','MUNICIPIO',
                             'PLANTELES', 'AULAS', 'BIBLIOTECAS',
                             'LABORATORIOS', 'TALLERES', 'ANEXOS']
    infra_ed_2012_copy = infra_ed_2012.iloc[3:-5,:].copy()
    infra_ed_2012_copy.columns = columnas_infra_ed_2012
    return infra_ed_2012_copy



def derechohabientes_seguridadsocial_municipal():  
    """
    NOTA
    FUENTE: Censo de población y vivienda 2010.

    1  Incluye una estimación de población a nivel nacional de 1,344,585 personas,
    correspondientes a 448,195 viviendas sin información de ocupantes.
    2  La suma de los derechohabientes en las distintas instituciones de salud puede
    ser mayor al total por aquella población que tiene derecho a este servicio en más de una institución de salud.
    3  Incluye al Sistema de Protección Social en Salud (SPSS) que coordina la Secretaría de Salud (SSA).
    4  Incluye instituciones de salud públicas o privadas.

    
    """
    derechohabiente_2010 = pd.read_excel('datos/siha_2_2_4_3.xlsx', encoding='utf-8')
    columnas_derechohabiente_2010 = ['CLAVE','ESTADO','MUNICIPIO',
                             'POB_TOTAL', 'TOTAL', 'IMSS',
                             'ISSSTE', 'ISSSTE_ESTATAL', 'PEMEX_DEF_MARIN',
                             'SEGURO_POPULAR','INST_PRIV','OTRA_INST','NO_DERECHO',
                             'NO_ESPEF_DERECHO']
    derechohabiente_2010_copy = derechohabiente_2010.iloc[4:-7,:].copy()
    derechohabiente_2010_copy.columns = columnas_derechohabiente_2010
    return derechohabiente_2010_copy

def cambiar_tipodedato(df,columna):
    temp_df = df.copy()
    temp_df[columna] = temp_df[columna].apply(lambda x: int(x))
    return temp_df


def multiple_merge_by_colum(main_df, df_list,column):
    main_df_inner = main_df.copy()
    for df_i in df_list:
        main_df_inner = pd.merge(main_df_inner,df_i, on=column,how='inner')
    return main_df_inner

def carga_codigos_postales():
    xl = pd.ExcelFile('datos/CPdescarga.xls')    
    hojas_leer = xl.sheet_names[1:]
    main_df = pd.DataFrame()
    for hoja in hojas_leer:    
        cp_catalogo = pd.read_excel('datos/CPdescarga.xls',sheet_name=hoja,dtypes={'c_estado':str,'c_mnpio':str},ignore_index=True)
        main_df = pd.concat([main_df,cp_catalogo])
    return main_df.copy()

def limpiar_codigos_postales(df):
    df_cp = df.copy() 
    df_cp['c_estado'] = df_cp['c_estado'].apply(lambda x: str(x))
    df_cp['c_mnpio'] =  df_cp['c_mnpio'].apply(lambda x: str(x))
    df_cp['c_mnpio2']  = df_cp['c_mnpio'].apply(lambda x:'00'+str(x) if len(x) == 1 else x)
    df_cp['c_mnpio3']  = df_cp['c_mnpio2'].apply(lambda x:'0'+str(x) if len(x) == 2 else x)
    df_cp['TEST']  = df_cp['c_estado'] + df_cp['c_mnpio3']
    df_cp['CLAVE'] = df_cp['TEST'].apply(lambda x: int(x))   
    return df_cp

        
def force_integer_transformation(df):
    df_copy = df.copy()
    columnas = df_copy.columns
    str_columnas = []
    for columna in columnas:
        try:
            df_copy[columna] = df_copy[columna].apply(lambda x : float(x))
        except:
            str_columnas.append(columna)
    
    for columna in str_columnas[2:]:
        df = df_copy[columna].copy()
        values = []
        for value in df:    
            try:
                values.append(float(value))
            except:
                values.append(None)
        df_copy[columna] = values
    return df_copy


def clean_numeric_super_df(super_df):
    copy_super = super_df.copy()
    string_columns = []
    for columna in copy_super.columns:    
        try:
            value = copy_super[columna].median()
            copy_super[columna] = copy_super[columna].fillna(value)
            string_columns.append(value)
        except:
            string_columns.append(columna)

    filter_numeric_columns = [y for x,y in zip(string_columns,copy_super.columns ) if isinstance(x, float)]
    cpy_filtered = copy_super[filter_numeric_columns]
    clean_super_df = cpy_filtered.drop('c_CP', axis=1)
    return clean_super_df


if __name__ == '__main__':
    

    # Leemos el archivo principal
    main_file = pd.read_csv(r'datos/Indicadores_municipales_sabana_DA.csv', encoding='utf-8')
    main_file.rename(columns={'clave_mun':'CLAVE'},inplace=True)
    
    # Leemos otros archivos
    df_poblacion_economicamente_activa_municipal = poblacion_economicamente_activa_municipal()
    df_obligaciones_fiscales_municipales = obligaciones_fiscales_municipales()
    df_delitos_fuero_comun_municipal = delitos_fuero_comun_municipal()
    df_alumnos_municipal = alumnos_municipal()
    df_viviendas_internet_municipal = viviendas_internet_municipal()
    df_medicos_municipal = medicos_municipal()
    df_infraestructura_educativa_municipal = infraestructura_educativa_municipal()
    df_derechohabientes_seguridadsocial_municipal = derechohabientes_seguridadsocial_municipal()
    
    # Creamos lista de archivos 
    lista_df = [df_poblacion_economicamente_activa_municipal,df_obligaciones_fiscales_municipales,
                df_delitos_fuero_comun_municipal,df_alumnos_municipal,df_viviendas_internet_municipal,
                df_medicos_municipal,df_infraestructura_educativa_municipal,
                df_derechohabientes_seguridadsocial_municipal]
    
    # Modificamos la lista de archivos para hacer que la CLAVE sea int
    lista_df_dtype = [force_integer_transformation(df) for df in lista_df]  
    
    # Hacemos un merge de multiples archivos
    lista_df_set_index = multiple_merge_by_colum(main_file,lista_df_dtype,'CLAVE')

    # Leemos los codigos postales
    df_cp_raw = carga_codigos_postales()
    
    # Limpiamos los codigos postales 
    df_cp = limpiar_codigos_postales(df_cp_raw)
    
    # Merge final entre nuestra base de CP y datos
    super_df = pd.merge(df_cp,lista_df_set_index, on='CLAVE', how='left')
    
    # Guardamos el dataframe en un pkl para uso futuro
    super_df = pd.read_pickle('super_df.pkl')   
  
    clean_super_df = clean_numeric_super_df(super_df)
    
    geo_df = pd.read_csv(r'datos/mx_postal_codes.csv', encoding='latin1')
    geo_df.rename(columns={'Postal Code':'d_codigo'},inplace=True)
    geo_df_dup = geo_df.drop_duplicates(subset=['d_codigo'], keep='first')
    
    len(clean_super_df.d_codigo.unique())
    
    
    clean_super_df_geo = pd.merge(clean_super_df,geo_df_dup[['d_codigo','Latitude','Longtiude']], how='left', on ='d_codigo' )
    testtttet = clean_super_df_geo.iloc[:,13:-2]
    
    
    # Creamos variable para overfittear modelo
    X = testtttet.values
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    kmeans.labels_
    y = kmeans.predict(X)

    colores = {0:'#110133',1:'#00918e',2:'#4dd599',3:'#ffdc34',4:'#FFA07A'}
    results = pd.concat([clean_super_df_geo[['d_codigo','Latitude','Longtiude']], pd.DataFrame(y)],axis=1)
    results['color'] = results[0].map(colores)
    
    mapbox_access_token = "pk.eyJ1IjoibWVtb25rZXkwMSIsImEiOiJjam51ejVxbWwxOXpnM3Zwa3h5d3Jxd2d5In0.mrAjlrVjoHFLnN8H2TzHrg"

    fig = go.Figure(go.Scattermapbox(
            lat=results['Latitude'],
            lon=results['Longtiude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color=results['color'],
            ),
            text=results['d_codigo'],
        ))
    
    fig.update_layout(
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=45,
                lon=-73
            ),
            pitch=0,
            zoom=5
        )
    )
    
    pio.write_html(fig, file='hello_world.html', auto_open=True,config={'displaylogo': False})

    
    

    
    