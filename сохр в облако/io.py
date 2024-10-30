from tkinter import *
import pyperclip
from tkinter import filedialog  as fd
from tkinter import messagebox as mb
import os
import json
import requests
from tkinter import ttk
history_file="upload_history.json"#создаем имя для файла загрузок
def show_history():
    if not os.path.exists (history_file):
        mb.showinfo("История загрузок","У вас нет истории загрузок")
        return
    history_window=Toplevel(window)
    history_window.title("История загрузок")
    my_box=Listbox(history_window,width=50,height=20)
    my_box.grid(row=0,column=0,padx=(10,0),pady=10)

    my_links = Listbox(history_window, width=50, height=20)
    my_links.grid(row=0, column=1, padx=(0, 10), pady=10)

    with open(history_file, 'r') as f:
        history=json.load(f)#список словарей в json
        for i in history:
            my_box.insert(END, i['file_path'])#забираем из json значение по ключю File_path
            my_links.insert(END, i['file_link'])#забираем из json значение по ключю File_link

 


def save_history(file_path,link):
     history=[]#пустой список
     if os.path.exists(history_file):#проверяем есть ли хистори файл
         with open(history_file, 'r') as file:#открываем history_file в json
             history=json.load(file)#загружаем файил и преоьразовываем json в пайтон и закр файл

     history.append({"file_path":os.path.basename(file_path), "file_link":link})#добавили новую инфу в history список причем в file_path только имя файла не весь путь тк basename использ

     with open(history_file, 'w') as file:# открываем файл для записи
         json.dump(history,file, indent=4)# сохраняем новую инфу там словарь в формат json

def upload():
    try:
        filepath=fd.askopenfilename()#получим путь к файлу для его загрузки
        if filepath:#если не пустая то выполнить ниже
            files={"file":open(filepath,'rb')}#откр файл для чтения по байтно для отправкив сеть 'rb' - Открывает файл в бинарном режиме только для чтения. Указатель файла помещается в начале файла. Это режим "по умолчанию".
            response=requests.post('https://file.io/',files=files)#ответ на запрос post закрытый вид запрса с отправкой данных(строка URL,путь к отправляемому файлу)
            response.raise_for_status()#для обработки в исключении если будет ошибка при запросе статуса
            if response.status_code==200:#Объект requests.Response модуля requests содержит всю информацию ответа сервера на HTTP-запрос requests.get(), requests.post() и т.д.,если все гуд то поехали далее
                print(response.headers)# возвратит заголовок сервера
                s=response.json()#возвратит ответ в виде json
                link=response.json()['link']#сохранияем ссылку в переменную линк, из файла json по ключу 'link'
                if link:#если есть что то в link то поехали
                    e.delete(0,END)#очищаем энтри от говна
                    e.insert(0, link)#вставляем в энтри то что в link
                    pyperclip.copy(link)  #копир ссылку в буфер обмена link ссылка на скачивание
                    save_history(filepath,link)#вызываем функцию сохранения в файл JSON и  параметы у нас другие он сам догадывается по местам

                    mb.showinfo("скопировано",f"ссылка{link}скопирована в буфер обмена")

                else:
                    raise ValueError("Нет ссылки")
    except ValueError as ve:
                mb.showerror("Ошибка", f"Произошла ошибка: {ve}")
    except Exception as err:
                mb.showerror("Ошибка", f"Произошла ошибка: {err}")





window=Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x500")

but=ttk.Button(text="Загрузить", command=upload)
but.pack(pady=10)

his_button=ttk.Button(text="Показать историю", command=show_history)
his_button.pack()

e=Entry()
e.pack()

window.mainloop()
