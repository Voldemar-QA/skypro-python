from sqlalchemy import create_engine
from sqlalchemy import text


class EmplTable:
    scripts = {
        "select all": text("select * from employee"),
        "select from company": text(
            "select * from employee where company_id =:comp_id"),
        "select only active": text(
            "select * from employee where \"is_active\" = true"),
        "select empl by id": text(
            "select * from employee where id =:select_id"),
        "get empl max id": text(
            "select MAX(\"id\") from employee"),
        "delete empl by id": text(
            "delete from employee where id =:id_to_delete"),
        "insert new empl": text(
            """
            insert into employee(
                "is_active",
                "create_timestamp",
                "change_timestamp",
                "first_name",
                "last_name",
                "phone",
                "email",
                "birthdate",
                "company_id"
            )
            values (
                True,
                now(),
                now(),
                :name1,
                :name2,
                :tel,
                :mailto,
                :birthday,
                :compid
            )
            """
        ),
    }

    def __init__(self, connection_string):
        self.dbe = create_engine(connection_string)

    def get_employees(self):
        return self.dbe.execute(self.scripts["select all"]).fetchall()

    def get_empl_list(self, comp_id):
        with self.dbe.begin() as conn:
            return conn.execute(
                self.scripts["select from company"], {"comp_id": comp_id}
                ).fetchall()

    def get_active_employees(self):
        return self.dbe.execute(self.scripts["select only active"]).fetchall()

    def create_empl(
        self,
        fst_name,
        lst_name,
        new_phone,
        new_email,
        birth,
        comp_id
    ):
        self.dbe.execute(
            self.scripts["insert new empl"],
            name1=fst_name,
            name2=lst_name,
            tel=new_phone,
            mailto=new_email,
            birthday=birth,
            compid=comp_id,
        )

    def get_empl_max_id(self):
        return self.dbe.execute(
            self.scripts["get empl max id"]).fetchall()[0][0]

    def get_employee_by_id(self, id):
        return self.dbe.execute(
            self.scripts["select empl by id"], select_id=id).fetchone()

    def delete_empl(self, id):
        self.dbe.execute(
            self.scripts["delete empl by id"], id_to_delete=id)
