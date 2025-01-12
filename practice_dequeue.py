from collections import deque

def palindrome_check(string: str):
    # Delete all spaces and formated to lowercase, convert to list
    formated_list = list(string.strip().lower().replace(' ', ''))

    # Create dequeue and add list of characters
    dq = deque()
    dq.extend(formated_list)

    while len(dq) >= 2:
        if dq.pop() == dq.popleft():
            continue
        else:
            print("This string isn't a palindrome(")
            return

    print("This string is a palindrome)")

palindrome_check('ra ar')