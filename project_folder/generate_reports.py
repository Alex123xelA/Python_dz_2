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

def plot_pie_chart_by_column(df, column_name):
    """
    Строит круговую диаграмму по любой выбранной колонке.
    """
    if column_name not in df.columns:
        print(f"Колонка '{column_name}' не найдена.")
        return

    value_counts = df[column_name].value_counts()
    if value_counts.empty:
        print(f"Нет данных для колонки '{column_name}'.")
        return

    plt.figure(figsize=(8, 8))
    value_counts.plot(kind='pie', autopct='%1.1f%%', startangle=360, shadow=True)
    plt.title(f'Распределение по колонке: {column_name}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
