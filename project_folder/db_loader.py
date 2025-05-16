import os
import pandas as pd

def select_dataframe() -> pd.DataFrame:
    """
    Позволяет пользователю выбрать один из доступных .pkl-файлов в папке ./data
    и загружает соответствующий DataFrame.

    Returns
    -------
    pd.DataFrame
        Загруженный DataFrame с очищенными названиями колонок.
    """
    files = [f for f in os.listdir("./data") if f.endswith(".pkl")]
    if not files:
        raise FileNotFoundError("Нет доступных .pkl файлов в папке ./data")

    print("Доступные справочники:")
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")

    index = int(input("Выберите справочник по номеру: ")) - 1
    if not (0 <= index < len(files)):
        raise IndexError("Некорректный номер справочника")

    df = pd.read_pickle(os.path.join("./data", files[index]))
    df.columns = df.columns.str.strip()
    print("Колонки:", df.columns.tolist())
    return df


def load_excel_to_pickle(excel_path: str = 'DZ_2.xlsx', output_dir: str = './data/') -> None:
    """
    Загружает все листы Excel-файла (кроме первого) и сохраняет каждый как .pkl-файл.

    Производит следующие проверки:
    - Файл существует.
    - В файле больше одного листа (первый — описание проекта).
    - Листы не пустые (должны содержать как заголовки, так и данные).

    Parameters
    ----------
    excel_path : str
        Путь к Excel-файлу (по умолчанию 'DZ_2.xlsx').

    output_dir : str
        Каталог для сохранения .pkl файлов (по умолчанию './data/').

    Raises
    ------
    FileNotFoundError
        Если указанный Excel-файл не найден.

    ValueError
        Если в файле только один лист или все листы (кроме первого) пустые.
    """
    if not os.path.isfile(excel_path):
        raise FileNotFoundError(f"[Ошибка] Файл '{excel_path}' не найден. Убедитесь, что он находится в нужной папке.")

    xl = pd.ExcelFile(excel_path)
    sheet_names = xl.sheet_names

    if len(sheet_names) <= 1:
        raise ValueError("[Ошибка] В Excel-файле только один лист (возможно, описание проекта). "
                         "Необходимо как минимум два листа, чтобы загрузить данные.")

    sheets_to_process = sheet_names[1:]  # Пропустить первый лист
    valid_sheets = []

    for sheet in sheets_to_process:
        df = xl.parse(sheet)
        if df.empty or df.dropna(how='all').shape[0] <= 1:
            print(f"[Предупреждение] Лист '{sheet}' пропущен: он пустой или содержит только заголовки.")
            continue
        valid_sheets.append((sheet, df))

    if not valid_sheets:
        raise ValueError("[Ошибка] Все листы (кроме первого) пустые или содержат только заголовки. "
                         "Нет данных для сохранения.")

    os.makedirs(output_dir, exist_ok=True)

    print("[Инфо] Загружаются следующие листы:")
    for sheet, df in valid_sheets:
        df.columns = df.columns.str.strip()
        file_path = os.path.join(output_dir, f'{sheet}.pkl')
        df.to_pickle(file_path)
        print(f"[✓] Сохранено: {sheet}.pkl")


if __name__ == "__main__":
    load_excel_to_pickle()
