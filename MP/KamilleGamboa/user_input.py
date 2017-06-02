class Choice:
    def __init__(self, name, action = None):
        self.name = name
        self.function = action

    @staticmethod
    def show_choices(choice_array):
        while True:
            for index, choice in enumerate(choice_array):
                print(f"[{index}] - {choice.name}")

            user_input = get_int("Select a choice")

            #If user_input is not in choices
            if user_input not in range(0, len(choice_array)):
                print("Invalid choice")
                continue
            else:
                action = choice_array[user_input].function
                if action:
                    action()
                break

def get_int(question):
    while True:
        print(question)
        try:
            user_input = int(input())
            return user_input
        except:
            print("Invalid input")
            continue


def get_float(question):
    while True:
        print(question)
        try:
            user_input = float(input())
            return user_input
        except:
            print("Invalid input")
            continue


def get_string(question):
    print(question)
    return input()