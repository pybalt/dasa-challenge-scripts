import os

if __name__ == '__main__':

    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    challenge = input("Input a challenge: A, B, C\n").lower().strip()

    if challenge == 'a':
        from challenge_a.script import entrypoint
        URL = "http://scw.pjn.gov.ar/scw/home.seam"
        number = input('Input a number: ').strip()
        year = input('Input a year: ').strip()
        entrypoint(URL, number, year)
    elif challenge == 'b':
        from challenge_b.script import entrypoint
        URL = "https://www.osbar.org/members/membersearch_start.asp"
        bar_number = input("Input a bar number: ").strip()
        entrypoint(bar_number, URL)
    elif challenge == 'c':
        from challenge_c.script import entrypoint
        number = input("Input a number: ").strip()
        entrypoint(number)

    else:
        print("Invalid challenge")
