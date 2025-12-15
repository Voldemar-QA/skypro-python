from todo_api import TodoApi

url = "https://todo-app-sky.herokuapp.com/"
api = TodoApi(url)


def test_create_task():
    name = "Посадить сорок розовых кустов"
    task = api.create_task(name)
    assert task["title"] == name


def test_rename_task():
    name = "Old name"
    old_task = api.create_task(name)
    id = old_task["id"]
    new_name = "New name"
    new_task = api.rename_task(new_name, id)
    assert new_task["title"] == new_name


def test_delete_task():
    name = "Task to delete"
    task_to_delete = api.create_task(name)
    id = task_to_delete["id"]
    result = api.delete_task(id)
    assert result == "todo was deleted"


def test_get_list():
    name = "New task"
    api.create_task(name)
    api.create_task(name)
    api.create_task(name)
    list = api.get_list()
    assert len(list) > 0


def test_get_task():
    name = "Mission impossible"
    task_to_be = api.create_task(name)
    id = task_to_be["id"]
    task_as_is = api.get_task(id)
    assert task_as_is["title"] == name


def test_done():
    name = "Accomplished"
    task = api.create_task(name)
    id = task["id"]
    api.done(id)
    task_done = api.get_task(id)
    assert task_done["completed"] is True


def test_undone():
    name = "Not finished"
    task = api.create_task(name)
    id = task["id"]
    api.undone(id)
    task_undone = api.get_task(id)
    assert task_undone["completed"] is False
