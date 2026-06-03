# ============================================================
# Count character frequency using only strings.
# ============================================================

user_input = input("Enter a string: ")

processed = ""

for char in user_input:
    if char not in processed:
        count = 0

        for c in user_input:
            if c == char:
                count += 1

        print(f"- '{char}' appears {count} times.")
        processed += char

