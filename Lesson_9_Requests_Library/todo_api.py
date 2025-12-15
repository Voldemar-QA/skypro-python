import requests


class TodoApi:

    def __init__(self, url):
        self.url = url

    # Создание
    def create_task(self, name):
        payload = {'title': name}
        resp = requests.post(self.url, json=payload)
        return resp.json()

    # Переименование
    def rename_task(self, new_name, id):
        payload = {'title': new_name}
        resp = requests.patch(self.url + str(id), json=payload)
        return resp.json()

    # Удаление
    def delete_task(self, id):
        resp = requests.delete(self.url + str(id))
        print("RESPONSE:", resp.json())
        return resp.json()

    # Получение списка
    def get_list(self):
        list = requests.get(self.url)
        return list.json()

    # Получение конкретной задачи из списка
    def get_task(self, id):
        task = requests.get(self.url + str(id))
        return task.json()

    # Отметка задачи «Выполнена»
    def done(self, id):
        status = {'completed': True}
        mark_done = requests.patch(self.url + str(id), json=status)
        # print("STATUS:", mark_done.status_code)
        # print("RESPONSE:", mark_done.json())
        return mark_done.json()

    # Снятие отметки «Выполнена»
    def undone(self, id):
        status = {'completed': False}
        mark_undone = requests.patch(self.url + str(id), json=status)
        return mark_undone.json()
