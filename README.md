# 📦 Persian Number To Words

یک کتابخانه ساده و قدرتمند برای تبدیل اعداد فارسی و انگلیسی به حروف، با پشتیبانی از اعداد بسیار بزرگ، اعشار و حالت مالی.

---

## ✨ ویژگی‌های اصلی

* ✅ پشتیبانی از `int`، `float` و `str`
* ✅ تبدیل عدد فارسی و انگلیسی به حروف
* ✅ پشتیبانی از عدد با طول نامحدود (بدون محدودیت در تعداد رقم‌ها)
* ✅ سازگار با زبان فارسی 🇮🇷 و انگلیسی 🇬🇧
* ✅ حالت مالی برای نمایش واحد پول و ارقام اعشاری
* ✅ خروجی ساخت‌یافته با `NumberResult`
* ✅ جداسازی رقم‌ها با کاما در خروجی فرمت‌شده
* ✅ پشتیبانی از CLI
* ✅ مناسب برای API، Django و FastAPI

---

## 📥 نصب

### نصب از PyPI

```bash
pip install persian-number-to-words
```

### نصب در حالت توسعه

```bash
git clone https://github.com/p7deli/persian-number-to-words.git
cd persian-number-to-words
pip install -e .
```

---

## 🚀 استفاده سریع

```python
from persian_number_to_words import number_to_words

result = number_to_words(123456)
print(result.formatted)
# 123,456
print(result.words)
# صد و بیست و سه هزار و چهارصد و پنجاه و شش
```

---

## 📌 ساختار خروجی

تابع `number_to_words` یک شیء `NumberResult` برمی‌گرداند:

```python
NumberResult(
    formatted="123,456",
    words="صد و بیست و سه هزار و چهارصد و پنجاه و شش",
    language="fa",
    currency=None
)
```

## دسترسی به مقادیر

```python
result.formatted
result.words
result.language
result.currency
```

## تبدیل به دیکشنری

```python
result.to_dict()
```

---

## 🔢 ورودی‌های پشتیبانی‌شده

این کتابخانه می‌تواند انواع ورودی زیر را بخواند و به حروف تبدیل کند:

* اعداد صحیح
* اعداد اعشاری
* رشته عددی انگلیسی
* رشته عددی فارسی
* اعداد بزرگ با تعداد رقم نامحدود

### نمونه‌ها

```python
number_to_words(1000)
number_to_words(1234.56)
number_to_words("123456")
number_to_words("1,234,567")
number_to_words("۱۲۳۴۵۶")
```

---

## 🌍 انتخاب زبان

### فارسی (پیش‌فرض)

```python
number_to_words(123456, lang="fa")
```

### انگلیسی

```python
number_to_words(123456, lang="en")
```

خروجی انگلیسی:

```
one hundred twenty three thousand four hundred fifty six
```

---

## 💰 واحد پول

```python
number_to_words(5000, currency="تومان")
```

خروجی:

```
پنج هزار تومان
```

---

## 🧾 حالت مالی (Financial Mode)

حالت مالی مناسب محاسبات پولی و فاکتورها است.

```python
number_to_words(
    12500.75,
    currency="تومان",
    mode="financial"
)
```

خروجی:

```
12,500.75
دوازده هزار و پانصد تومان و هفتاد و پنج ریال
```

### حالت مالی انگلیسی

```python
number_to_words(
    12500.75,
    lang="en",
    currency="dollars",
    mode="financial"
)
```

خروجی:

```
twelve thousand five hundred dollars and seventy five cents
```

---

## ➖ اعداد منفی

```python
number_to_words(-2500)
```

خروجی:

```
منفی دو هزار و پانصد
```

---

## 🖥 استفاده در خط فرمان (CLI)

پس از نصب:

```bash
pnum 123456
```

مثال با پارامترها:

```bash
pnum 12500.75 --currency تومان --mode financial
```

### گزینه‌های CLI

| گزینه        | توضیح                        |
| ------------ | ---------------------------- |
| `--lang`     | انتخاب زبان (`fa` یا `en`)   |
| `--currency` | تعیین واحد پول               |
| `--mode`     | حالت `normal` یا `financial` |

---

## 🧩 استفاده در Django

```python
price = number_to_words(150000, currency="تومان")
label.setText(price.words)
```

---

## ⚡ استفاده در FastAPI

```python
from fastapi import FastAPI
from persian_number_to_words import number_to_words

app = FastAPI()

@app.get("/convert/{number}")
def convert(number: str):
    result = number_to_words(number)
    return result.to_dict()
```

---

## 👤 سازنده

این کتابخانه توسط `p7deli` توسعه داده شده است.

# 🌸 استفاده در پروژه‌های دسکتاپ (PyQt / Tkinter)

```python
result = number_to_words(45000)
label.setText(result.words)
```

---

# 🧠 نکات مهم

* برای اعداد بسیار بزرگ، می‌توان scale جدید به `constants.py` اضافه کرد.
* خروجی همیشه یک شیء ساختاریافته است.
* برای API از متد `to_dict()` استفاده کنید.
* پکیج با Type Hint کامل نوشته شده است.

---

# 🧪 اجرای تست‌ها

```bash
pytest
```

---

# 👨‍💻 پیشنهادات

* برای پروژه‌های مالی همیشه از حالت `financial` استفاده کنید.
* برای API خروجی را با `to_dict()` ارسال کنید.
* CLI برای تبدیل سریع در خط فرمان مناسب است.

---

# 📜 لایسنس

MIT

---

# نویسنده

Poriya Delavariyan
