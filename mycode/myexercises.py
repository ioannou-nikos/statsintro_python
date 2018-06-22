# -*- coding: utf-8 -*-


def ex_2_1_1():
    import pandas as pd
    df = pd.read_csv('../ipynb/Data/data_kaplan/swim100m.csv', header=0)
    print(df.head(5))


def ex_2_1_2():
    import pandas as pd
    df = pd.read_excel('../ipynb/Data/data_others/Table 2.8 Waist loss.xls')
    print(df.tail(5))


def ex_2_1_3():
    from zipfile import ZipFile
    from urllib.request import urlopen
    import pandas as pd
    import io

    URL = 'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'

    # get the zip archive
    GLM_archive = urlopen(URL).read()

    # make the archive available as a byte stream
    zipdata = io.BytesIO()
    zipdata.write(GLM_archive)

    # extract the requested file from the archive, as a pandas XLS-file
    myzipfile = ZipFile(zipdata)
    xlsfile = myzipfile.open(r'GLM_data/Table 2.8 Waist loss.xls')

    # read the xls-file into Python, using pandas, and return the extracted data
    xls = pd.ExcelFile(xlsfile)
    df = xls.parse('Sheet1', skiprows=2)

    # print the first 5 rows
    print(df.head(5))


def ex_2_2_1():
    import numpy as np
    import pandas as pd
    import os

    x = np.arange(0, 10, 0.001)
    y = np.sin(x * 1.5)
    z = np.cos(x * 1.5)
    df = pd.DataFrame({
        'Time': x,
        'YVals': y,
        'ZVals': z
    })

    print(df.head())

    df[['YVals', 'ZVals']][10:15].to_csv('out.txt')

    print(os.path.abspath(os.curdir))


if "__main__" == __name__:
    ex_2_2_1()