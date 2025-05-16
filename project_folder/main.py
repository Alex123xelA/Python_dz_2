"""
Основной модуль для загрузки данных и генерации отчетов.
"""

from db_loader import load_excel_to_pickle, select_dataframe
from generate_reports import (
    generate_text_report,
    generate_scatter_plot,
    generate_pie_chart,
    generate_bar_chart,
    generate_pivot_report,
)


def main():
    """
    Главная функция приложения.
    """
    print("Загрузка базы данных и создание справочников...")
    load_excel_to_pickle()

    df = select_dataframe()

    print(
        "\nВыберите действие:\n"
        "1. Текстовый отчет\n"
        "2. Scatter-график\n"
        "3. Круговая диаграмма\n"
        "4. Столбчатая диаграмма\n"
        "5. Сводная таблица (pivot table)"
    )

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        generate_text_report(df)
    elif choice == "2":
        generate_scatter_plot(df)
    elif choice == "3":
        generate_pie_chart(df)
    elif choice == "4":
        generate_bar_chart(df)
    elif choice == "5":
        generate_pivot_report(df)
    else:
        print("Неверный выбор. Пожалуйста, выберите вариант от 1 до 4.")


if __name__ == "__main__":
    main()
