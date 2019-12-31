# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:45:20 2019

@author: izqui
"""

import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

"""
# Helix equation
t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])
pio.write_html(fig, file='test.html', auto_open=True,config={'displaylogo': False})
"""







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
    pea_2015 = pd.read_excel('siha_2_2_4_1_agosto_2016.xlsx', encoding='utf-8', sheet_name='2015')
    columnas_pea = ['CLAVE','ESTADO','MUNICIPIO','POB_12_MAS','PEA_TOTAL','PEA_OCUPADA','PEA_DESOCUPADA','NO_PEA','NO_PEA_ESPECIFICADO']
    pea_2015_copy = pea_2015.iloc[5:-8,:].copy()
    pea_2015_copy.columns = columnas_pea
    return pea_2015_copy



def obligaciones_fiscales_municipales():
    """
    NOTA
    
    Fuente: Unidad de Coordinación con Entidades Federativas, SHCP.
    """
    obligaciones_finan_mun_2015 = pd.read_excel('siha_2_2_5.xlsx', encoding='utf-8', sheet_name='1° 2015')
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
    delitos_fuero_comun_mun_2015 = pd.read_excel('siha_2_2_4_9_dic_2015.xlsx', encoding='utf-8')
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
    alumnos_mun_2012 = pd.read_excel('siha_2_2_4_8.xlsx', encoding='utf-8')
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
    viviendas_inter_2010 = pd.read_excel('siha_2_2_4_6.xlsx', encoding='utf-8')
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
    medicos_2012 = pd.read_excel('siha_2_2_4_5.xlsx', encoding='utf-8')
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
    infra_ed_2012 = pd.read_excel('siha_2_2_4_2.xlsx', encoding='utf-8')
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
    derechohabiente_2010 = pd.read_excel('siha_2_2_4_3.xlsx', encoding='utf-8')
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
    xl = pd.ExcelFile('CPdescarga.xls')    
    hojas_leer = xl.sheet_names[1:]
    main_df = pd.DataFrame()
    for hoja in hojas_leer:    
        cp_catalogo = pd.read_excel('CPdescarga.xls',sheet_name=hoja,dtypes={'c_estado':str,'c_mnpio':str},ignore_index=True)
        main_df = pd.concat([main_df,cp_catalogo])
    return main_df.copy()


def 

if __name__ == '__main__':
    
    
    main_file = pd.read_csv('Indicadores_municipales_sabana_DA.csv', encoding='utf-8')
    main_file.rename(columns={'clave_mun':'CLAVE'},inplace=True)
    
    df_poblacion_economicamente_activa_municipal = poblacion_economicamente_activa_municipal()
    df_obligaciones_fiscales_municipales = obligaciones_fiscales_municipales()
    df_delitos_fuero_comun_municipal = delitos_fuero_comun_municipal()
    df_alumnos_municipal = alumnos_municipal()
    df_viviendas_internet_municipal = viviendas_internet_municipal()
    df_medicos_municipal = medicos_municipal()
    df_infraestructura_educativa_municipal = infraestructura_educativa_municipal()
    df_derechohabientes_seguridadsocial_municipal = derechohabientes_seguridadsocial_municipal()
    
    
    lista_df = [df_poblacion_economicamente_activa_municipal,df_obligaciones_fiscales_municipales,
                df_delitos_fuero_comun_municipal,df_alumnos_municipal,df_viviendas_internet_municipal,
                df_medicos_municipal,df_infraestructura_educativa_municipal,
                df_derechohabientes_seguridadsocial_municipal]
    
    
    lista_df_dtype = [cambiar_tipodedato(df,'CLAVE') for df in lista_df]
    
    lista_df_set_index = multiple_merge_by_colum(main_file,lista_df_dtype,'CLAVE')

    test = lista_df_set_index[:20]

    df_cp = carga_codigos_postales()
    
    
    
    df_cp['c_estado'] = df_cp['c_estado'].apply(lambda x: str(x))
    df_cp['c_mnpio'] =  df_cp['c_mnpio'].apply(lambda x: str(x))
    
    
    
    df_cp['TEST'] = df_cp['c_estado'] + df_cp['c_mnpio']
    
    for idx in range(len(df_cp)):
        df_cp['CLAVE'] = df_cp['c_estado'].iloc[idx] + df_cp['c_mnpio'].iloc[idx]
        
    df_cp['CLAVE'] = df_cp['CLAVE'].apply(lambda x: int(x))    






