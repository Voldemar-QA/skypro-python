import requests
import uuid
import random
import string
from datetime import date, timedelta


class EmplApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='ginny', password='batbogey'):
        creds = {
            'username': user,
            'password': password
            }
        resp = requests.post(self.url + "/auth/login", json=creds)
        return resp.json()["user_token"]

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        print(resp.url)
        return resp.json()

    def create_company(self, name, description=""):
        company = {
            'name': name,
            'description': description
            }
        resp = requests.post(self.url + "/company/create", json=company)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def delete_company(self, comp_id):
        client_token = self.get_token()
        url_with_token = f"{
            self.url}/company/{comp_id}?client_token={client_token}"
        resp = requests.delete(url_with_token)
        return resp.json()

    def random_name(self, length=9):
        return ''.join(random.choices(
            string.ascii_lowercase, k=length)).capitalize()

    def random_email(self):
        return f"user_{uuid.uuid4()}@example.com"

    def random_phone(self, length=10):
        return ''.join(random.choices(string.digits, k=length))

    def random_birth(self, start_year=1950, end_year=2005):
        start = date(start_year, 1, 1)
        end = date(end_year, 12, 31)
        return (start + timedelta(
            days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

    def random_date(self):
        year = random.randint(1950, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return date(year, month, day)

    def random_status(self):
        return random.choice([True, False])

    def create_empl(
            self, comp_id, fst_name, lst_name, mid_name, new_email, new_phone,
            birth
            ):
        body = {
            'first_name': fst_name,
            'last_name': lst_name,
            'middle_name': mid_name,
            'company_id': comp_id,
            'email': new_email,
            'phone': new_phone,
            'birthdate': birth.strftime("%Y-%m-%d"),
            'is_active': True
            }
        resp = requests.post(self.url + "/employee/create", json=body)
        resp.raise_for_status()
        return resp.json()

    def get_empl_list(self, comp_id):
        resp = requests.get(self.url + '/employee/list/' + str(comp_id))
        return resp.json()

    def get_empl_ind(self, empl_id):
        resp = requests.get(self.url + '/employee/info/' + str(empl_id))
        return resp.json()

    def edit_empl(self, empl_id, new_email, new_phone, status):
        user_token = self.get_token()
        url_with_token = f"{
            self.url}/employee/change/{empl_id}?client_token={user_token}"
        update = {
            "email": new_email,
            "phone": new_phone,
            "is_active": status
            }
        resp = requests.patch(url_with_token, json=update)
        return resp.json()

    def edit_empl_no_token(self, empl_id, new_phone):
        user_token = None
        url_with_token = f"{
            self.url}/employee/change/{empl_id}?client_token={user_token}"
        update = {
            "phone": new_phone
            }
        resp = requests.patch(url_with_token, json=update)
        return resp.json()
