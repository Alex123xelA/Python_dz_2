import pandas as pd
import os

def select_dataframe():
    files = [f for f in os.listdir("./data") if f.endswith(".pkl")]
    print("Доступные справочники:")
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")
    index = int(input("Выберите справочник по номеру: ")) - 1
    df = pd.read_pickle(os.path.join("./data", files[index]))
    df.columns = df.columns.str.strip()
    print("Колонки:", df.columns.tolist())
    return df

def load_excel_to_pickle(excel_path='DZ_2.xlsx', output_dir='./data/'):
    """
    Загружает все листы Excel-файла (кроме первого), сохраняет как pickle-файлы.

    Parameters
    ----------
    excel_path : str
        Путь к Excel-файлу.
    output_dir : str
        Каталог для сохранения .pkl файлов.
    """
    os.makedirs(output_dir, exist_ok=True)
    xl = pd.ExcelFile(excel_path)
    for sheet in xl.sheet_names[1:]:  # Пропустить первый лист с описанием
        df = xl.parse(sheet)
        df.to_pickle(os.path.join(output_dir, f'{sheet}.pkl'))
        print(f"[✓] Сохранено: {sheet}.pkl")
    df.columns = df.columns.str.strip()

if __name__ == "__main__":
    load_excel_to_pickle()
