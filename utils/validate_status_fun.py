def validate_status(status):

    lst_status = ['новая', 'в процессе', 'выполнено']

    for st in lst_status:
        if st == status.strip():
            return True

    return False