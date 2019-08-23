
def is_number(value):
    for num in value:
        if((num>='a' and num<='z') or(num>='A' and num<='Z')):
            return False
        else:
            return True
def validatePhone(value):
    if len(value)<11 or len(value)>13:
        return False
    if not is_number(value):
        return False
    else:
        return True



