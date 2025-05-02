import pandas as pd
import os

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

if __name__ == "__main__":
    load_excel_to_pickle()
