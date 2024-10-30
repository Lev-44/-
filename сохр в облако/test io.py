import os
import json

history_file="test_save_history.json"#создаем  файл тестовый


def save_history(file_path, link):
    history = []  # пустой список
    if os.path.exists(history_file):  # проверяем есть ли хистори файл
        with open(history_file, "r") as file:  # открываем history_file в json
            history = json.load(file)  # загружаем файил и преоьразовываем json в пайтон и закр файл

    history.append({"file_path": os.path.basename(file_path),"file_link": link})  # добавили новую инфу в history список причем в file_path только имя файла не весь путь тк basename использ

    with open(history_file, "w") as file:  # открываем файл для записи
        json.dump(history, file, indent=4)  # сохраняем новую инфу там словарь в формат json

def test_save_history():
    test_file_path="test_file.txt"
    test_file_link="https://file.io/nwqfgxchqg"
    
    save_history(test_file_path, test_file_link)
    with open ("test_save_history.json","r") as f:
        history= json.load(f)
        assert len (history)==1
        assert history[0]['file_path'] == test_file_path
        assert history[0]['file_link'] == test_file_link
    os.remove("test_save_history.json")
test_save_history()