from database.code.models.code_model import Code


def validation_code(valid_code: str) -> bool:
    code = Code.select().where(Code.code == valid_code)

    if code:
        Code.delete().where(Code.code == valid_code).execute()
        return True
    else:
        return False


async def delete_code(code_id: int):
    qry = Code.delete_by_id(code_id)
    qry.execute()
