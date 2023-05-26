def bananas(s, word='banana') -> set:
    result = []

    if word == '':
        result.append(''.rjust(len(s), '-'))
        return set(result)

    for el in range(len(s)):
        if word[0] == s[el]:
            left_s = ''.rjust(el, '-') + s[el]

            if s[el + 1:] == '' and word[1:] == '':
                result.append(left_s)

            else:
                right_s_list = bananas(s[el + 1:], word[1:])
                for right_s in right_s_list:
                    result.append(left_s + right_s)

    return set(result)


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
