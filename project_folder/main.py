from db_loader import load_excel_to_pickle, select_dataframe
from generate_reports import *

def main():
    print("Загрузка базы данных и создание справочников...")
    load_excel_to_pickle()

    df = select_dataframe()

    print("Выберите действие:\n1. Создать текстовый отчет\n2. Построить график\n3. Круговая диаграмма")
    choice = input("Ваш выбор: ")

    if choice == "1":
        col = input("Введите колонку фильтра: ")
        val = input("Введите значение: ")
        selected_cols = input("Введите через запятую нужные колонки: ").split(", ")
        report = report_filter_by_criteria(df, {col: val}, selected_cols)
        print(report)

    elif choice == "2":
        x = input("Введите X (независимая переменная): ")
        y = input("Введите Y (зависимая переменная): ")
        plot_price_vs_quantity(df, x, y)

    elif choice == "3":
        col = input("Введите имя колонки для круговой диаграммы: ")
        plot_pie_chart_by_column(df, col)

if __name__ == "__main__":
    main()
