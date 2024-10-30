import json
import os

history_file = "test_upload_history.json"#поместили строку с именем в переменную history_file

def save_history(file_path, link):#пришли сюда новые двнные путь и ссылка линк
    history = []#пустой список
    if os.path.exists(history_file):#если есть файл хф то прочитать
        with open(history_file, 'r') as f:
            history=json.load(f)#читаем в json и грузим в хистори
    history.append({"file_path": os.path.basename(file_path), "file_link": link})#небыло файла то сюда где добавляем или создаем список джисон
    with open(history_file, 'w') as f:#открываем для записи
        json.dump(history, f, indent=4)#сохраняем в формате джисон все что в хистори и идем к save_history к месту вызова

def test_save_history():
    test_file_path = "test_file.txt"
    test_download_link = "https://file.io/examooo"
    # Вызов функции для тестирования
    save_history(test_file_path, test_download_link)#вызвали с новыми параметрами save_his
    # Проверка, что история была сохранена корректно
    with open("test_upload_history.json", 'r') as file:#проверяем что там есть
        history = json.load(file)#читаем из хистори
        assert len(history) == 1#если ложь то ошибка сравнивает число сообщений в файле должно быть одно те одна пара
        assert history[0]['file_path'] == test_file_path #если по ключуfile_path то что в переменнойtest_file_path то ошибки нет
        assert history[0]['file_link'] == test_download_link#то же только сам понял
    # Очистка тестовых данных
    os.remove("test_upload_history.json")# удалим тестовый файл
test_save_history()#тест пошел
