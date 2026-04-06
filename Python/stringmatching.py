"""
MERK:
Funker ikke for alle tester, går for sakte. Må finne siste korteste indeks istedenfor å starte helt på nytt igjen med søket.
"""

pattern = input()


def find_occurences(pat, text):
    result = []
    checking = False
    pat_ind = 0
    start_ind_pattern = 0
    i = 0
    while i < len(text):
        if not checking:
            if text[i] == pat[0]:
                pat_ind += 1
                start_ind_pattern = i
                checking = True

                if pat_ind == len(pat):
                    pat_ind = 0
                    checking = False
                    result.append(start_ind_pattern)
        else:
            if text[i] == pat[pat_ind]:
                pat_ind += 1

                if pat_ind == len(pat):
                    pat_ind = 0
                    checking = False
                    result.append(start_ind_pattern)
            else:
                i -= pat_ind
                checking = False
                pat_ind = 0

        i += 1

    return result


while True:
    try:
        text = input()
        print(*find_occurences(pattern, text))

        pattern = input()
    except EOFError:
        break
