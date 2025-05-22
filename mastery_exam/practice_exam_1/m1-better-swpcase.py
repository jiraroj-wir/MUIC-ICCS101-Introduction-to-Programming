def better_swap_case(st: str) -> str:
    result = ""
    for ch in st:
        if not ch.isalpha():
            result = result + " "
            continue

        if ch in "aeiouAEIOU":
            result = result + ch
            continue
        else:
            if ch.islower():
                result = result + ch.upper()
            else:
                result = result + ch.lower()

    return result


assert better_swap_case("aBC") == "abc"
assert better_swap_case("Hello~HuMAN") == "heLLo humAn"
assert better_swap_case("PythOn1Cs-is!coOl") == "pYTHON cS iS CoOL"
