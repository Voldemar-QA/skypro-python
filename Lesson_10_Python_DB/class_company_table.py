from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text


class CompanyTable:
    scripts = {
        "insert new comp": text(
            """
            insert into company(
                "is_active",
                "create_timestamp",
                "change_timestamp",
                "name",
                "description"
            )
            values (
                True,
                now(),
                now(),
                :new_name,
                :new_descr
            )
            """
        ),
        "get comp max id": text(
            "select MAX(\"id\") from company where deleted_at is null"),
        "select comp by id": text(
            """
            select * from company
            where id =:select_id and deleted_at is null
            """
        ),
        "delete comp by id": text(
            """
            delete from company
            where id = :id_to_delete and deleted_at is null
            """
        ),
    }

    def __init__(self, connection_string):
        self.dbc = create_engine(connection_string)

    def get_table_names(self):
        inspector = inspect(self.dbc)
        return inspector.get_table_names()

    def create_comp(self, name, descr):
        self.dbc.execute(
            self.scripts["insert new comp"], new_name=name, new_descr=descr)

    def get_comp_max_id(self):
        return self.dbc.execute(
            self.scripts["get comp max id"]).fetchall()[0][0]

    def get_company_by_id(self, id):
        return self.dbc.execute(
            self.scripts["select comp by id"], select_id=id).fetchone()

    def delete_comp(self, id):
        self.dbc.execute(self.scripts["delete comp by id"], id_to_delete=id)
