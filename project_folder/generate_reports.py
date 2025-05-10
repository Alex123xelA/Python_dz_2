import pandas as pd
import matplotlib.pyplot as plt

def report_filter_by_criteria(df, criteria: dict, columns: list) -> pd.DataFrame:
    """
    Фильтрует DataFrame по заданным критериям и возвращает выбранные столбцы.

    Parameters:
        df (pd.DataFrame): Исходный DataFrame.
        criteria (dict): Словарь фильтров (ключ — имя столбца, значение — значение для фильтрации).
        columns (list): Список столбцов, которые нужно вернуть.

    Returns:
        pd.DataFrame: Отфильтрованный DataFrame с выбранными столбцами.
    """
    mask = pd.Series(True, index=df.index)
    for key, val in criteria.items():
        mask &= (df[key] == val)
    return df.loc[mask, columns]


def plot_price_vs_quantity(df: pd.DataFrame, x: str, y: str) -> None:
    """
    Строит scatter-график для двух переменных.

    Parameters:
        df (pd.DataFrame): Исходный DataFrame.
        x (str): Название столбца для оси X.
        y (str): Название столбца для оси Y.
    """
    df.plot.scatter(x=x, y=y)
    plt.title(f"{y} от {x}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_pie_chart_by_column(df: pd.DataFrame, column_name: str) -> None:
    """
    Строит круговую диаграмму по значениям в выбранной колонке.

    Parameters:
        df (pd.DataFrame): Исходный DataFrame.
        column_name (str): Название столбца, по которому строится диаграмма.
    """
    if column_name not in df.columns:
        print(f"Колонка '{column_name}' не найдена.")
        return

    value_counts = df[column_name].value_counts()
    if value_counts.empty:
        print(f"Нет данных для колонки '{column_name}'.")
        return

    plt.figure(figsize=(8, 8))
    value_counts.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=360,
        shadow=True
    )
    plt.title(f'Распределение по колонке: {column_name}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()


def plot_bar(df: pd.DataFrame, column_name: str) -> None:
    """
    Строит столбчатую диаграмму по количеству вхождений значений в колонке.

    Parameters:
        df (pd.DataFrame): Исходный DataFrame.
        column_name (str): Название столбца, по которому строится диаграмма.
    """
    if column_name not in df.columns:
        print(f"Колонка '{column_name}' не найдена.")
        return

    value_counts = df[column_name].value_counts()
    if value_counts.empty:
        print(f"Нет данных для колонки '{column_name}'.")
        return

    value_counts.plot.bar()
    plt.yticks(range(0, max(value_counts) + 1))
    plt.tight_layout()
    plt.title(
        f'Распределение количества по колонке: {column_name}',
        fontsize=14
    )
    plt.show()
