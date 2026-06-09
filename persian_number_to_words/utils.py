from decimal import Decimal


def normalize_input(number):
    if isinstance(number, str):
        number = number.replace(",", "").replace("٬", "")
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        english_digits = "0123456789"
        trans = str.maketrans(persian_digits, english_digits)
        number = number.translate(trans)
        return Decimal(number) if "." in number else int(number)

    if isinstance(number, float):
        return Decimal(str(number))

    return number


def format_number(number):
    if isinstance(number, Decimal):
        text = format(number, "f")
        integer, _, decimal = text.partition(".")
        integer = f"{int(integer):,}"
        return f"{integer}.{decimal}" if decimal else integer

    if isinstance(number, float):
        integer, _, decimal = str(number).partition(".")
        integer = f"{int(integer):,}"
        return f"{integer}.{decimal}" if decimal else integer

    return f"{int(number):,}"
