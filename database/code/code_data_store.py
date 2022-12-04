import datetime

from database.code.models.code_model import Code


def validation_code(valid_code: str) -> bool:
    code_list = Code.select().where(Code.code == valid_code)

    if code_list:
        code = code_list[0]
        date = datetime.datetime.now()

        if code.use_count > 0:
            if code.validity_period >= date:
                use_count = code.use_count - 1
                Code.update({Code.use_count: use_count}).where(Code.id == code.id).execute()
                return True
            else:
                return False
        else:
            return False
    else:
        return False


async def delete_code(code_id: int):
    qry = Code.delete_by_id(code_id)
    qry.execute()
