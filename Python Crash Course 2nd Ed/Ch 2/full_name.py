first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#Additional formatting
print(f"Hello, {full_name.title()}!")

# Use with older version of Python 3 (<3.6)
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# Adding Whitespace
print("\tpython")

#Eliminating Whitespace
str1='    python    '
print(str1)
print(str1.rstrip())
