import re

# re.sub()
text = "My phone number 1234567890 and my office number is 0987654321."
pattern = r"\d+"
replacement = "NUMBER"
result = re.sub(pattern, replacement, text)
print(result)

# re.search()
text = "The rain in Spain falls mainly on the plain."
pattern = r"Spain"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else: print("Not Found.")

# re.match()
text = "Hello, World!"

pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match.")

pattern = r"World"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match with match().")

# re.findall()
text = "John's number is 555-1234, and Mary's number is 555-5678."
pattern = r"\d{3}-\d{4}"
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)

# ignorecase
match = re.search(r"python", "I love Python!", re.IGNORECASE)
if match:
    print("Match found:", match.group())

# ex. 1
text = "My personal phone number is 700-0203 and corporative phone number is 555-1042. But also can call at 767-6767 for any help."
pattern = r"\d{3}-\d{4}"
phone_numbers = re.findall(pattern, text)
print("Phone numbers found:", phone_numbers)

# ex. 2
text1 = "Hello everyone! Welcome to our ceremony!"
text2 = "Ladies and gentlemen! Hello, and be prepared!"
pattern = r"Hello"

match1 = re.match(pattern, text1)
print("Using re.match() on text1:")
if match1:
    print("Match found:", match1.group())
else:
    print("No match.")

match2 = re.match(pattern, text2)
print("\nUsing re.match() on text2:")
if match2:
    print("Match found:", match2.group())
else:
    print("No match.")

## Using re.search()
search_result = re.search(pattern, text2)
print("\nUsing re.search() on text2:")
if search_result:
    print("Match found:", search_result.group())
else:
    print("No match.")

# ex. 3
text = "48 teams from 7 continents were divided into 12 groups and will play in 2026 FIFA World Cup"
pattern = r"\d+"
match = re.sub(pattern, "NUMBER", text)
print(match)

# ex. 4
text = "our emails: info@company.com, services@company.com, contact@company.com and campaign2026@company.com"
pattern = r"\b\w+@\w+\.\w+\b"
emails = re.findall(pattern, text)
print(emails)

# ex. 5
text = "Ice melts quickly. Owls observe silently under umbrellas."
pattern = r"\b[aeiou]\w*\b"
match = re.findall(pattern, text, re.IGNORECASE)
print("Words starting with a vowel:", match)