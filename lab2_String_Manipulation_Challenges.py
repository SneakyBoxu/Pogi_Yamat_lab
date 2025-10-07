#1 Slicing & Methods
def format_phone_number(phone):
    cleaned = phone.replace(" ", "").replace("-", "")
    digits = "".join(ch for ch in cleaned if ch.isdigit())
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return formatted


#2 Formatting 
item = "Book"
price = 15.99
quantity = 2
total = price * quantity
receipt = f"{quantity} x {item} @ ${price:.2f} ea. = ${total:.2f}"


#3 Validation & Search
def is_valid_username(username):
    return username.isalnum() and 5 <= len(username) <= 12


#4 Complex Manipulation
def mask_credit_card(card_number):
    digits = "".join(ch for ch in card_number if ch.isdigit())
    masked = "*" * (len(digits) - 4) + digits[-4:]
    return masked


#========================execution==========================

print("Task 1 set C of String Manipulation Challenges")
print(format_phone_number(" 555-123-4567 "))  

print("Task 2 set C of String Manipulation Challenges")
print(receipt)  

print("Task 3 set C of String Manipulation Challenges")
print(is_valid_username("Python123"))   
print(is_valid_username("Pyt"))       

print("Task 4 set C of String Manipulation Challenges")
print(mask_credit_card("1234567812345670"))  