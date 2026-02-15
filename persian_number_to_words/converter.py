from typing import Union, Literal, Optional
from .models import NumberResult
from .utils import normalize_input, format_number
from .constants import *

LangType = Literal["fa", "en"]


def _three_digit_to_words(n: int, lang: LangType):
    if lang == "fa":
        ONES, TEENS, TENS, HUNDREDS = ONES_FA, TEENS_FA, TENS_FA, HUNDREDS_FA
        joiner = " و "
    else:
        ONES, TEENS, TENS, HUNDREDS = ONES_EN, TEENS_EN, TENS_EN, HUNDREDS_EN
        joiner = " "

    words = []
    hundreds = n // 100
    tens_units = n % 100

    if hundreds:
        words.append(HUNDREDS[hundreds])

    if 10 <= tens_units <= 19:
        words.append(TEENS[tens_units])
    else:
        tens = tens_units // 10
        units = tens_units % 10
        if tens:
            words.append(TENS[tens])
        if units:
            words.append(ONES[units])

    return joiner.join(words)


def number_to_words(
    number: Union[int, float, str],
    lang: LangType = "fa",
    currency: Optional[str] = None,
    mode: Literal["normal", "financial"] = "normal",
) -> NumberResult:

    number = normalize_input(number)
    formatted = format_number(number)

    negative = False
    if number < 0:
        negative = True
        number = abs(number)

    integer_part = int(number)
    decimal_part = round(number - integer_part, 2)

    SCALES = SCALES_FA if lang == "fa" else SCALES_EN
    joiner = " و " if lang == "fa" else " "

    parts = []
    scale_index = 0

    while integer_part > 0:
        chunk = integer_part % 1000
        if chunk:
            words = _three_digit_to_words(chunk, lang)
            scale = SCALES[scale_index]
            parts.append(f"{words} {scale}".strip())
        integer_part //= 1000
        scale_index += 1

    words = joiner.join(reversed(parts)) if parts else ("صفر" if lang=="fa" else "zero")

    # financial mode
    if mode == "financial" and decimal_part:
        decimal_value = int(round(decimal_part * 100))
        decimal_words = _three_digit_to_words(decimal_value, lang)

        if lang == "fa":
            words = f"{words} {currency or ''} و {decimal_words} ریال"
        else:
            words = f"{words} {currency or ''} and {decimal_words} cents"
    else:
        if decimal_part:
            decimal_digits = str(decimal_part).split(".")[1]
            if lang == "fa":
                decimal_words = " ".join(ONES_FA[int(d)] for d in decimal_digits)
                words += f" ممیز {decimal_words}"
            else:
                decimal_words = " ".join(ONES_EN[int(d)] for d in decimal_digits)
                words += f" point {decimal_words}"

    if currency and mode != "financial":
        words += f" {currency}"

    if negative:
        words = ("منفی " if lang=="fa" else "minus ") + words

    return NumberResult(
        formatted=formatted,
        words=words.strip(),
        language=lang,
        currency=currency,
    )
