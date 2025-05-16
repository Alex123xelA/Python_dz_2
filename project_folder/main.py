"""
Основной модуль для загрузки данных и генерации отчетов.
"""

from db_loader import load_excel_to_pickle, select_dataframe
from generate_reports import (
    report_filter_by_criteria,
    plot_price_vs_quantity,
    plot_pie_chart_by_column,
    plot_bar,
)

def choose_columns_by_index(df):
    """
    Предлагает пользователю выбрать колонки по номерам.

    Parameters:
        df (pd.DataFrame): DataFrame, из которого выбираются колонки.

    Returns:
        list: Список названий выбранных колонок.
    """
    print("\nВыберите колонки по номерам через запятую:")
    for i, col in enumerate(df.columns):
        print(f"{i + 1}. {col}")

    selected_indices = input("Номера колонок: ").split(",")
    selected_columns = []

    for index in selected_indices:
        index = index.strip()
        if index.isdigit():
            idx = int(index) - 1
            if 0 <= idx < len(df.columns):
                selected_columns.append(df.columns[idx])
            else:
                print(f"[!] Индекс {index} вне диапазона.")
        else:
            print(f"[!] '{index}' — не число.")

    return selected_columns


def main():
    """
    Главная функция приложения.

    Описание:
    ----------
    1. Загружает базу данных и сохраняет её в формате .pkl.
    2. Позволяет пользователю выбрать DataFrame из сохранённых.
    3. Отображает меню с вариантами генерации отчетов:
        - Текстовый отчёт по фильтру.
        - Scatter-график.
        - Круговая диаграмма.
        - Столбчатая диаграмма.
    4. Запрашивает у пользователя нужные параметры и вызывает соответствующую функцию.
    """
    print("Загрузка базы данных и создание справочников...")
    load_excel_to_pickle()

    df = select_dataframe()

    print(
        "\nВыберите действие:\n"
        "1. Создать текстовый отчет\n"
        "2. Построить график (Scatter)\n"
        "3. Круговая диаграмма\n"
        "4. Столбчатая диаграмма"
    )

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        print("\nФильтрация:")
        for i, col in enumerate(df.columns):
            print(f"{i + 1}. {col}")
        filter_col_index = int(input("Введите номер колонки фильтра: ")) - 1
        if not (0 <= filter_col_index < len(df.columns)):
            print("Неверный номер колонки.")
            return
        filter_column = df.columns[filter_col_index]
        value = input(f"Введите значение для фильтрации по '{filter_column}': ").strip()

        selected_columns = choose_columns_by_index(df)
        report = report_filter_by_criteria(df, {filter_column: value}, selected_columns)
        print("\nРезультат отчета:\n", report)

    elif choice == "2":
        print("\nВыбор переменных для графика:")
        selected = choose_columns_by_index(df)
        if len(selected) < 2:
            print("Нужно выбрать как минимум две колонки.")
            return
        x_column, y_column = selected[:2]
        plot_price_vs_quantity(df, x_column, y_column)

    elif choice == "3":
        print("\nКруговая диаграмма — выбор колонки:")
        selected = choose_columns_by_index(df)
        if not selected:
            print("Нужно выбрать хотя бы одну колонку.")
            return
        plot_pie_chart_by_column(df, selected[0])

    elif choice == "4":
        print("\nСтолбчатая диаграмма — выбор колонки:")
        selected = choose_columns_by_index(df)
        if not selected:
            print("Нужно выбрать хотя бы одну колонку.")
            return
        plot_bar(df, selected[0])

    else:
        print("Неверный выбор. Пожалуйста, выберите вариант от 1 до 4.")


if __name__ == "__main__":
    main()
