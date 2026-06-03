# ============================================================
# Description:
# Complete reference of Python string methods with explanations
# and small usage examples.
# ============================================================

text = "  Hello Python World!  "

# ============================================================
# 1. CASE CONVERSION METHODS
# ============================================================

# lower() -> convert all characters to lowercase
print(text.lower())  # "  hello python world!  "

# upper() -> convert all characters to uppercase
print(text.upper())  # "  HELLO PYTHON WORLD!  "

# title() -> capitalize first letter of each word
print(text.title())  # "  Hello Python World!  "

# capitalize() -> capitalize first letter only
print(text.capitalize())  # "  hello python world!  "

# swapcase() -> swap uppercase to lowercase and vice versa
print(text.swapcase())

# casefold() -> stronger lower() (used for comparisons)
print(text.casefold())


# ============================================================
# 2. TRIMMING METHODS
# ============================================================

# strip() -> remove spaces from both sides
print(text.strip())

# lstrip() -> remove left spaces
print(text.lstrip())

# rstrip() -> remove right spaces
print(text.rstrip())

# strip(char) -> remove specific characters
t = "---hello---"
print(t.strip("-"))


# ============================================================
# 3. SEARCH & FIND METHODS
# ============================================================

s = "hello python hello world"

# find() -> first index of substring (-1 if not found)
print(s.find("python"))

# rfind() -> last occurrence index
print(s.rfind("hello"))

# index() -> like find but raises error if not found
print(s.index("python"))

# count() -> count occurrences
print(s.count("hello"))

# startswith()
print(s.startswith("hello"))

# endswith()
print(s.endswith("world"))


# ============================================================
# 4. REPLACEMENT METHODS
# ============================================================

# replace(old, new)
print(s.replace("hello", "hi"))

# replace(old, new, count)
print(s.replace("hello", "hi", 1))


# ============================================================
# 5. SPLIT & JOIN METHODS
# ============================================================

# split() -> split into list
words = s.split()
print(words)

# split(delimiter)
csv = "a,b,c,d"
print(csv.split(","))

# rsplit()
print(s.rsplit(" ", 1))

# splitlines()
lines = "line1\nline2\nline3"
print(lines.splitlines())

# join() -> join list into string
joined = "-".join(words)
print(joined)


# ============================================================
# 6. STRING CHECK METHODS (BOOLEAN)
# ============================================================

alpha = "Python"
num = "12345"
alnum = "Python123"

print(alpha.isalpha())   # letters only
print(num.isdigit())     # digits only
print(alnum.isalnum())   # letters + digits

print(alpha.islower())
print(alpha.isupper())

print("   ".isspace())

print("Hello".istitle())

print("hello".isascii())


# ============================================================
# 7. ALIGNMENT METHODS
# ============================================================

word = "hi"

print(word.center(10, "-"))  # ---hi-----
print(word.ljust(10, "-"))   # hi--------
print(word.rjust(10, "-"))   # --------hi


# ============================================================
# 8. FORMATTING METHODS
# ============================================================

name = "Alice"
age = 25

# format()
print("My name is {} and I'm {}".format(name, age))

# f-strings (modern way)
print(f"My name is {name} and I'm {age}")


# ============================================================
# 9. CHARACTER TYPE / TRANSLATION METHODS
# ============================================================

# encode() -> string to bytes
print("hello".encode())

# maketrans() + translate()
table = str.maketrans("abc", "123")
print("abcabc".translate(table))


# ============================================================
# 10. PADDING METHODS
# ============================================================

num = "42"

print(num.zfill(5))  # 00042


# ============================================================
# 11. OTHER USEFUL METHODS
# ============================================================

# expandtabs() -> replace \t with spaces
tab_text = "Hello\tWorld"
print(tab_text.expandtabs(4))

# removeprefix() (Python 3.9+)
print("unhappy".removeprefix("un"))

# removesuffix() (Python 3.9+)
print("file.txt".removesuffix(".txt"))


# ============================================================
# END OF FILE
# ============================================================
