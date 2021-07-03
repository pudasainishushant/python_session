import re
email_checker_regex_rule = r"[A-Z a-z 0-9 .%_-]+@[A-Z a-z 0-9]+\.[A-Z a-z]+"

def check_email(email):
    if (re.match(email_checker_regex_rule,email)):
        print("Valid email")
    else:
        print("Email milena")

check_email("@65.89.dajksj")
"""
Web scrapping
Python web scrapping tools
Advantages
"""