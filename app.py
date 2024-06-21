import os

if __name__ == '__main__':

    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    challenge = input("Input a challenge: A, B, C\n").lower().strip()

    if challenge == 'a':
        ...
    elif challenge == 'b':
        from challenge_b.challenge import entrypoint

        bar_number = input("Input a bar number: ")
        entrypoint(bar_number.strip())
    elif challenge == 'c':
        from challenge_c.challenge import entrypoint
        number = input("Input a number: ")
        entrypoint(number.strip())

    else:
        print("Invalid challenge")
