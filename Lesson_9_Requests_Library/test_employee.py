import pytest
from employee_api import EmplApi

url = "http://5.101.50.27:8000"
api = EmplApi(url)
empl_id_db = 10


def test_create_empl():
    name = "QA Paradise"
    description = "Add employee here"
    result = api.create_company(name, description)
    comp_id = result["id"]

    fst_name = api.random_name()
    lst_name = api.random_name()
    mid_name = api.random_name()
    new_email = api.random_email()
    new_phone = api.random_phone()
    birth = api.random_date()
    new_empl = api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    assert new_empl["first_name"] == fst_name
    assert new_empl["last_name"] == lst_name
    assert new_empl["middle_name"] == mid_name
    assert new_empl["email"] == new_email
    assert new_empl["phone"] == new_phone
    assert new_empl["birthdate"] == birth
    assert new_empl["is_active"] is True

    del_comp = api.delete_company(comp_id)
    assert del_comp["detail"] == "Компания успешно удалена"


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_create_empl_neg():
    name = "Dead Souls Ltd"
    description = "Consulting"
    result = api.create_company(name, description)
    comp_id = result["id"]

    fst_name = api.random_name()
    lst_name = api.random_name()
    mid_name = api.random_name()
    new_email = api.random_email()
    new_phone = api.random_phone()
    birth = api.random_date()
    new_empl = api.create_empl([])

    assert new_empl["first_name"] == fst_name
    assert new_empl["last_name"] == lst_name
    assert new_empl["middle_name"] == mid_name
    assert new_empl["email"] == new_email
    assert new_empl["phone"] == new_phone
    assert new_empl["birthdate"] == birth
    assert new_empl["is_active"] is True

    del_comp = api.delete_company(comp_id)
    assert del_comp["detail"] == "Компания успешно удалена"


def test_get_empl_list():
    name = "QA Paradise"
    description = "Add employee here"
    result = api.create_company(name, description)
    comp_id = result["id"]

    fst_name = api.random_name()
    fst_name1 = fst_name
    lst_name = api.random_name()
    lst_name1 = lst_name
    mid_name = api.random_name()
    mid_name1 = mid_name
    new_email = api.random_email()
    new_email1 = new_email
    new_phone = api.random_phone()
    new_phone1 = new_phone
    birth = api.random_date()
    birth1 = birth
    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    fst_name = api.random_name()
    fst_name2 = fst_name
    lst_name = api.random_name()
    lst_name2 = lst_name
    mid_name = api.random_name()
    mid_name2 = mid_name
    new_email = api.random_email()
    new_email2 = new_email
    new_phone = api.random_phone()
    new_phone2 = new_phone
    birth = api.random_date()
    birth2 = birth
    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    fst_name = api.random_name()
    fst_name3 = fst_name
    lst_name = api.random_name()
    lst_name3 = lst_name
    mid_name = api.random_name()
    mid_name3 = mid_name
    new_email = api.random_email()
    new_email3 = new_email
    new_phone = api.random_phone()
    new_phone3 = new_phone
    birth = api.random_date()
    birth3 = birth
    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    result = api.get_empl_list(comp_id)
    # print(result)

    assert result[0]["first_name"] == fst_name1
    assert result[0]["last_name"] == lst_name1
    assert result[0]["middle_name"] == mid_name1
    assert result[0]["email"] == new_email1
    assert result[0]["phone"] == new_phone1
    assert result[0]["birthdate"] == birth1

    assert result[1]["first_name"] == fst_name2
    assert result[1]["last_name"] == lst_name2
    assert result[1]["middle_name"] == mid_name2
    assert result[1]["email"] == new_email2
    assert result[1]["phone"] == new_phone2
    assert result[1]["birthdate"] == birth2

    assert result[2]["first_name"] == fst_name3
    assert result[2]["last_name"] == lst_name3
    assert result[2]["middle_name"] == mid_name3
    assert result[2]["email"] == new_email3
    assert result[2]["phone"] == new_phone3
    assert result[2]["birthdate"] == birth3

    del_comp = api.delete_company(comp_id)
    assert del_comp["detail"] == "Компания успешно удалена"


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_get_empl_list_neg():
    name = "Noid"
    description = "Company without ID"
    result = api.create_company(name, description)
    comp_id = None

    fst_name = api.random_name()
    fst_name1 = fst_name
    lst_name = api.random_name()
    mid_name = api.random_name()
    new_email = api.random_email()
    new_email1 = new_email
    new_phone = api.random_phone()
    birth = api.random_date()

    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    fst_name = api.random_name()
    lst_name = api.random_name()
    lst_name2 = lst_name
    mid_name = api.random_name()
    new_email = api.random_email()
    new_phone = api.random_phone()
    new_phone2 = new_phone
    birth = api.random_date()
    api.create_empl(
        comp_id, fst_name, lst_name, mid_name, new_email, new_phone, birth)

    result = api.get_empl_list(comp_id)

    assert result[0]["first_name"] == fst_name1
    assert result[0]["email"] == new_email1
    assert result[1]["last_name"] == lst_name2
    assert result[1]["phone"] == new_phone2

    api.delete_company(comp_id)


def test_edit_empl():
    empl_id = empl_id_db
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


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_edit_empl_no_id():
    empl_id = None
    new_email = api.random_email()
    api.edit_empl(empl_id, new_email)
    edited = api.get_empl_ind(empl_id)
    assert edited["email"] == new_email


@pytest.mark.negative_test
@pytest.mark.xfail(strict=False)
def test_edit_empl_no_token():
    empl_id = empl_id_db
    new_phone = api.random_phone()
    api.edit_empl_no_token(empl_id, new_phone)
    edited = api.get_empl_ind(empl_id)
    assert edited["phone"] == new_phone


def test_get_empl_ind():
    empl_id = empl_id_db
    old = api.get_empl_ind(empl_id)

    new_email = api.random_email()
    new_phone = api.random_phone()
    status = api.random_status()
    api.edit_empl(empl_id, new_email, new_phone, status)
    edited = api.get_empl_ind(empl_id)

    assert edited["first_name"] == old["first_name"]
    assert edited["last_name"] == old["last_name"]
    assert edited["email"] == new_email
    assert edited["phone"] == new_phone
    assert edited["birthdate"] == old["birthdate"]
    assert edited["is_active"] == status


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
def test_get_empl_ind_neg():
    empl_id = None
    old = api.get_empl_ind(empl_id)

    new_email = api.random_email()
    api.edit_empl(empl_id, new_email)
    edited = api.get_empl_ind(empl_id)

    assert edited["first_name"] == old["first_name"]
    assert edited["email"] == new_email
