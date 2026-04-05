# Assignment Part 3: File I/O, APIs & Exception Handling
# Theme: Product Explorer & Error-Resilient Logger

import requests

# =========================
# TASK 1 — FILE READ & WRITE BASICS
# =========================

file_name = "python_notes.txt"

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.\n",
    "Topic 2: Lists are ordered and mutable.\n",
    "Topic 3: Dictionaries store key-value pairs.\n",
    "Topic 4: Loops automate repetitive tasks.\n",
    "Topic 5: Exception handling prevents crashes.\n"
]

# Part A — Write
with open(file_name, "w", encoding="utf-8") as file:
    file.writelines(notes)
print("File written successfully.")

extra_notes = [
    "Topic 6: Functions help organize reusable code.\n",
    "Topic 7: APIs allow programs to communicate with external services.\n"
]

with open(file_name, "a", encoding="utf-8") as file:
    file.writelines(extra_notes)
print("Lines appended.")

# Part B — Read
print("\nNumbered lines from file:")
with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

for index, line in enumerate(lines, start=1):
    print(f"{index}. {line.strip()}")

print(f"\nTotal number of lines in the file: {len(lines)}")

keyword = input("\nEnter a keyword to search in the file: ").strip().lower()

matches = []
for line in lines:
    if keyword in line.lower():
        matches.append(line.strip())

if matches:
    print("\nMatching lines:")
    for match in matches:
        print(match)
else:
    print("No matching lines found for that keyword.")

# =========================
# TASK 2 — API INTEGRATION
# =========================

BASE_URL = "https://dummyjson.com/products"

print("\n" + "=" * 60)
print("TASK 2 — API INTEGRATION")
print("=" * 60)

# Step 1 — Fetch and Display Products
response = requests.get(f"{BASE_URL}?limit=20")
data = response.json()
products = data["products"]

print("\nFirst 20 Products:")
print(f"{'ID':<4} {'Title':<30} {'Category':<15} {'Price':<10} {'Rating':<10}")
print("-" * 75)

for product in products:
    print(
        f"{product['id']:<4} "
        f"{product['title'][:28]:<30} "
        f"{product['category']:<15} "
        f"${product['price']:<9} "
        f"{product['rating']:<10}"
    )

# Step 2 — Filter and Sort
filtered_products = [p for p in products if p["rating"] >= 4.5]
sorted_products = sorted(filtered_products, key=lambda x: x["price"], reverse=True)

print("\nProducts with rating >= 4.5 sorted by price descending:")
print(f"{'ID':<4} {'Title':<30} {'Price':<10} {'Rating':<10}")
print("-" * 60)

for product in sorted_products:
    print(
        f"{product['id']:<4} "
        f"{product['title'][:28]:<30} "
        f"${product['price']:<9} "
        f"{product['rating']:<10}"
    )

# Step 3 — Search by Category
laptop_response = requests.get(f"{BASE_URL}/category/laptops")
laptop_data = laptop_response.json()
laptops = laptop_data["products"]

print("\nLaptops category products:")
for laptop in laptops:
    print(f"{laptop['title']} - ${laptop['price']}")

# Step 4 — POST Request (Simulated)
new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

post_response = requests.post(f"{BASE_URL}/add", json=new_product)

print("\nPOST response from server:")
print(post_response.json())

# =========================
# TASK 3 — EXCEPTION HANDLING
# =========================

print("\n" + "=" * 60)
print("TASK 3 — EXCEPTION HANDLING")
print("=" * 60)

log_file = "error_log.txt"

def log_error(message):
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(message + "\n")

# 1. Handle file-related errors
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    message = "File error: missing_file.txt not found."
    print(message)
    log_error(message)

# 2. Handle invalid user input
try:
    number = int(input("\nEnter a number: "))
    print(f"You entered: {number}")
except ValueError:
    message = "Input error: invalid number entered."
    print(message)
    log_error(message)

# 3. Handle API/network-related errors
try:
    bad_response = requests.get("https://dummyjson.com/invalid-endpoint")
    bad_response.raise_for_status()
    print(bad_response.json())
except requests.exceptions.RequestException as e:
    message = f"API error: {e}"
    print(message)
    log_error(message)

print("\nProgram completed successfully with exception handling.")
