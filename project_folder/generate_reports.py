import pandas as pd
import matplotlib.pyplot as plt

def report_filter_by_criteria(df, criteria: dict, columns: list):
    """
    Фильтрует DataFrame по заданным критериям и возвращает выбранные столбцы.
    """
    mask = pd.Series(True, index=df.index)
    for key, val in criteria.items():
        mask &= (df[key] == val)
    return df.loc[mask, columns]

def plot_price_vs_quantity(df, x, y):
    """
    Строит scatter-график для двух переменных.
    """
    df.plot.scatter(x=x, y=y)
    plt.title(f"{y} от {x}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
