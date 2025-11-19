import sys

def main():
    script = sys.argv[0]
    action = sys.argv[1]

    action_list = ["--add", "--substract", "--multiply"]

    num1 = sys.argv[2]
    num2 = sys.arg[3]

    assert action in action_list, "Operation not supported " + action

    if action == "--add":
        print(float(num1) + float(num2))
    elif action == ""