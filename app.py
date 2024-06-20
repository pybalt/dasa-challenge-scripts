
if __name__ == '__main__':

    challenge = input("Input a challenge: A, B, C").lower()

    if challenge == 'a':
        ...
    elif challenge == 'b':
        ...
    elif challenge == 'c':
        from challenge_c.challenge import entrypoint

        entrypoint()

    else:
        print("Invalid challenge")
