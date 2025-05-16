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


def load_excel_to_pickle(excel_path: str = "DZ_1.xlsx", output_dir: str = "./data/") -> None:
    """
    Загружает все листы Excel-файла (кроме первого) и сохраняет каждый как .pkl-файл.

    Проверяет, существует ли файл и содержит ли он нужные листы данных.

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
        Если в Excel-файле только один лист (обычно описание проекта).
    """
    if not os.path.exists(excel_path):
        raise FileNotFoundError(
            f"[Ошибка] Файл '{excel_path}' не найден. Убедитесь, что файл существует."
        )

    xl = pd.ExcelFile(excel_path)
    sheet_names = xl.sheet_names

    if len(sheet_names) <= 1:
        raise ValueError(
            "[Ошибка] Файл содержит только один лист (вероятно, описание проекта). "
            "Для загрузки справочников необходимо минимум два листа."
        )

    sheets_to_process = sheet_names[1:]  # Пропустить первый лист
    os.makedirs(output_dir, exist_ok=True)

    print("[Инфо] Найденные листы для обработки:")
    for sheet in sheets_to_process:
        print(f" - {sheet}")

    for sheet in sheets_to_process:
        df = xl.parse(sheet)
        df.columns = df.columns.str.strip()
        file_path = os.path.join(output_dir, f"{sheet}.pkl")
        df.to_pickle(file_path)
        print(f"[✓] Сохранено: {sheet}.pkl")


if __name__ == "__main__":
    load_excel_to_pickle()
