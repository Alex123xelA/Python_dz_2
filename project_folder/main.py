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
        "Выберите действие:\n"
        "1. Создать текстовый отчет\n"
        "2. Построить график\n"
        "3. Круговая диаграмма\n"
        "4. Столбчатая диаграмма"
    )

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        column = input("Введите колонку фильтра: ").strip()
        value = input("Введите значение: ").strip()
        selected_columns = input("Введите через запятую нужные колонки: ").split(", ")
        selected_columns = [col.strip() for col in selected_columns]
        report = report_filter_by_criteria(df, {column: value}, selected_columns)
        print("\nРезультат отчета:\n", report)

    elif choice == "2":
        x_column = input("Введите X (независимая переменная): ").strip()
        y_column = input("Введите Y (зависимая переменная): ").strip()
        plot_price_vs_quantity(df, x_column, y_column)

    elif choice == "3":
        column = input("Введите имя колонки для круговой диаграммы: ").strip()
        plot_pie_chart_by_column(df, column)

    elif choice == "4":
        column = input("Введите название колонки для отображения в столбчатой диаграмме: ").strip()
        plot_bar(df, column)

    else:
        print("Неверный выбор. Пожалуйста, выберите вариант от 1 до 4.")


if __name__ == "__main__":
    main()
