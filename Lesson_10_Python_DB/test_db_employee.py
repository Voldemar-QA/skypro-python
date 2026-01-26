import pytest
from class_company_table import CompanyTable
from class_employee_api import EmplApi
from class_employee_db import EmplTable

dbc = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")
api = EmplApi("http://5.101.50.27:8000")
dbe = EmplTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


def test_db_connection():
    tables = dbc.get_table_names()
    assert 'employee' in tables


# Test API method [GET] /employee/list/{company_id}
def test_get_empl_list():
    name = "QA Paradise"
    description = "Add employee here"
    dbc.create_comp(name, description)
    comp_id = dbc.get_comp_max_id()

    for x in range(3):
        employee = {
            "fst_name": api.random_name(),
            "lst_name": api.random_name(),
            "phone": api.random_phone(),
            "email": api.random_email(),
            "birth": api.random_date()
        }
        dbe.create_empl(
            employee["fst_name"],
            employee["lst_name"],
            employee["phone"],
            employee["email"],
            employee["birth"],
            comp_id
        )
    api_result = api.get_empl_list(comp_id)
    db_result = dbe.get_empl_list(comp_id)
    assert len(api_result) == len(db_result)

    for _ in range(3):
        max_id = dbe.get_empl_max_id()
        dbe.delete_empl(max_id)
        row = dbe.get_employee_by_id(max_id)
        assert row is None

    dbc.delete_comp(comp_id)
    max_id = dbc.get_comp_max_id()
    deleted_company = dbc.get_company_by_id(comp_id)
    assert max_id != comp_id
    assert deleted_company is None


# Test SQL command INSERT for DB and
# API method [GET] /employee/info/{employee_id}
def test_insert():
    list = dbe.get_employees()
    len_before = len(list)

    dbc.create_comp("QA Paradise", "Add employee here")
    comp_id = dbc.get_comp_max_id()

    fst_name = api.random_name()
    lst_name = api.random_name()
    new_phone = api.random_phone()
    new_email = api.random_email()
    birth = api.random_date()

    dbe.create_empl(
        fst_name, lst_name, new_phone, new_email, birth, comp_id)

    list = dbe.get_employees()
    len_after = len(list)

    max_id = dbe.get_empl_max_id()
    row = dbe.get_employee_by_id(max_id)
    resp = api.get_empl_ind(max_id)

    assert row is not None
    assert len_after - len_before == 1
    assert resp["is_active"] is True
    assert resp["first_name"] == fst_name
    assert resp["last_name"] == lst_name
    assert resp["middle_name"] is None
    assert resp["phone"] == new_phone
    assert resp["email"] == new_email
    assert resp["birthdate"] == birth.strftime("%Y-%m-%d")
    assert row["birthdate"] == birth

    dbe.delete_empl(max_id)
    row = dbe.get_employee_by_id(max_id)
    assert row is None
    list = dbe.get_employees()
    len_after = len(list)
    assert len_after - len_before == 0

    dbc.delete_comp(comp_id)
    del_comp = dbc.get_company_by_id(comp_id)
    assert del_comp is None


# Test API method [POST] /employee/create
def test_create_empl():
    list = dbe.get_employees()
    len_before = len(list)

    dbc.create_comp("QAPI", "POST new employee here")
    comp_id = dbc.get_comp_max_id()

    fst_name = api.random_name()
    lst_name = api.random_name()
    mid_name = api.random_name()
    new_email = api.random_email()
    new_phone = api.random_phone()
    birth = api.random_date()

    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    list = dbe.get_employees()
    len_after = len(list)
    assert len_after - len_before == 1

    max_id = dbe.get_empl_max_id()
    row = dbe.get_employee_by_id(max_id)
    assert row is not None
    assert row["is_active"] is True
    assert row["first_name"] == fst_name
    assert row["last_name"] == lst_name
    assert row["middle_name"] == mid_name
    assert row["email"] == new_email
    assert row["phone"] == new_phone
    assert row["birthdate"] == birth

    dbe.delete_empl(max_id)
    row = dbe.get_employee_by_id(max_id)
    assert row is None
    list = dbe.get_employees()
    len_after = len(list)
    assert len_after - len_before == 0

    dbc.delete_comp(comp_id)
    del_comp = dbc.get_company_by_id(comp_id)
    assert del_comp is None


# Test API method [PATCH] /employee/change/{employee_id}
def test_edit_empl():
    comp_id = dbc.get_comp_max_id()
    employee = {
        "fst_name": api.random_name(),
        "lst_name": api.random_name(),
        "phone": api.random_phone(),
        "email": api.random_email(),
        "birth": api.random_date()
    }
    dbe.create_empl(
        employee["fst_name"],
        employee["lst_name"],
        employee["phone"],
        employee["email"],
        employee["birth"],
        comp_id
    )
    empl_id = dbe.get_empl_max_id()
    old = api.get_empl_ind(empl_id)

    new_email = api.random_email()
    new_phone = api.random_phone()
    status = api.random_status()

    api.edit_empl(empl_id, new_email, new_phone, status)
    edited = api.get_empl_ind(empl_id)

    assert old["email"] != edited["email"]
    assert old["phone"] != edited["phone"]
    assert edited["email"] == new_email
    assert edited["phone"] == new_phone
    assert edited["is_active"] == status

    dbe.delete_empl(empl_id)
    row = dbe.get_employee_by_id(empl_id)
    assert row is None


# Test Active-Inactive
def test_inactivate():
    comp_id = dbc.get_comp_max_id()
    employee = {
        "fst_name": api.random_name(),
        "lst_name": api.random_name(),
        "phone": api.random_phone(),
        "email": api.random_email(),
        "birth": api.random_date()
    }
    dbe.create_empl(
        employee["fst_name"],
        employee["lst_name"],
        employee["phone"],
        employee["email"],
        employee["birth"],
        comp_id
    )
    empl_id = dbe.get_empl_max_id()
    api.edit_empl(empl_id, employee["email"], employee["phone"], False)
    inactive_empl = dbe.get_employee_by_id(empl_id)
    active_list = dbe.get_active_employees()
    assert inactive_empl not in active_list

    dbe.delete_empl(empl_id)
    row = dbe.get_employee_by_id(empl_id)
    assert row is None


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
def test_create_empl_neg():
    comp_id = dbc.get_comp_max_id()
    dbe.create_empl([], comp_id)
    api_result = api.get_empl_list(comp_id)
    db_result = dbe.get_empl_list(comp_id)
    assert len(api_result) == len(db_result)


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_get_empl_list_neg():
    dbc.create_comp("Noid", "Try to get employees without id")
    comp_id = dbc.get_comp_max_id()

    for x in range(3):
        employee = {
            "fst_name": api.random_name(),
            "lst_name": api.random_name(),
            "phone": api.random_phone(),
            "email": api.random_email(),
            "birth": api.random_date()
        }
        dbe.create_empl(
            employee["fst_name"],
            employee["lst_name"],
            employee["phone"],
            employee["email"],
            employee["birth"],
            comp_id
        )
    rows = api.get_empl_list([])

    for x in range(3):
        empl_max_id = dbe.get_empl_max_id()
        dbe.delete_empl(empl_max_id)
        empl = dbe.get_employee_by_id(empl_max_id)
        assert empl is None

    dbc.delete_comp(comp_id)
    comp_max_id = dbc.get_comp_max_id()
    assert comp_max_id != comp_id

    assert len(rows) == 3


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
def test_edit_empl_no_id():
    comp_id = dbc.get_comp_max_id()
    employee = {
        "fst_name": api.random_name(),
        "lst_name": api.random_name(),
        "phone": api.random_phone(),
        "email": api.random_email(),
        "birth": api.random_date()
    }
    dbe.create_empl(
        employee["fst_name"],
        employee["lst_name"],
        employee["phone"],
        employee["email"],
        employee["birth"],
        comp_id
    )
    max_id = dbe.get_empl_max_id()
    old = dbe.get_employee_by_id(max_id)

    empl_id = None
    new_email = api.random_email()
    new_phone = api.random_phone()
    status = api.random_status()
    api.edit_empl(empl_id, new_email, new_phone, status)

    max_id = dbe.get_empl_max_id()
    edited = dbe.get_employee_by_id(max_id)

    assert old == edited

    dbe.delete_empl(max_id)
    row = dbe.get_employee_by_id(max_id)
    assert row is None


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_edit_empl_no_token():
    comp_id = dbc.get_comp_max_id()
    employee = {
        "fst_name": api.random_name(),
        "lst_name": api.random_name(),
        "phone": api.random_phone(),
        "email": api.random_email(),
        "birth": api.random_date()
    }
    dbe.create_empl(
        employee["fst_name"],
        employee["lst_name"],
        employee["phone"],
        employee["email"],
        employee["birth"],
        comp_id
    )
    empl_id = dbe.get_empl_max_id()
    new_phone = api.random_phone()
    api.edit_empl_no_token(empl_id, new_phone)

    edited = dbe.get_employee_by_id(empl_id)
    dbe.delete_empl(empl_id)
    row = dbe.get_employee_by_id(empl_id)
    assert row is None
    assert edited["phone"] == new_phone
