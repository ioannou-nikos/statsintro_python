# -*- coding: utf-8 -*-

def main_2_5_1():
    """
    This is the code from 2.5.1 section
    :return: 
    """
    import numpy as np
    import pandas as pd

    t = np.arange(0, 10, 0.1)
    x = np.sin(t)
    y = np.cos(t)

    df = pd.DataFrame({'Time': t, 'x': x, 'y': y})

    print(df.iloc[4:10, [0, 2]])
    print(df.values)
    print(df.iloc[2])

    # Grouping. Example of tv wathcing
    import matplotlib.pyplot as plt
    data = pd.DataFrame({
        'Gender': ['f', 'f', 'm', 'f', 'm',
                   'm', 'f', 'm', 'f', 'm', 'm'],
        'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,
               5.1, 3.9, 3.7, 2.1, 4.3]
    })

    # Group the data
    grouped = data.groupby('Gender')

    # Do some overview statistics
    print(grouped.describe())


    # Plot the data
    grouped.boxplot()
    plt.show()

    # Get the groups as dataframes
    df_female = grouped.get_group('f')

    # Get the corresponding numpy-array
    values_female = grouped.get_group('f').values


def main_2_6():
    """
    Statsmodels. Tools for statistical modeling
    :return: 
    """
    import numpy as np
    import pandas as pd
    import statsmodels.formula.api as sm

    # Generate a noisy line, and save the data in a pandas-DataFrame
    x = np.arange(100)
    y = 0.5*x - 20 + np.random.randn(len(x))
    df = pd.DataFrame({'x': x, 'y': y})

    # Fit a linear model, using the "formula" language
    # added by the package "patsy"
    model = sm.ols('y~x', data=df).fit()
    print(model.summary())


def main_2_7():
    """
    Seaborn. Data Visualization
    :return: 
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    x = np.linspace(1, 7, 50)
    y = 3 + 2*x + 1.5*np.random.randn(len(x))
    df = pd.DataFrame({'xData': x, 'yData': y})
    sns.regplot('xData', 'yData', data=df)
    plt.show()


if __name__ == '__main__':
    main_2_7()