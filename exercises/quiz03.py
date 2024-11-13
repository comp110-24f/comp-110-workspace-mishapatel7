def merge_lists(inp: list[str], inp2: list[int]) -> dict[str, int]:
    output: dict[str, int] = {}
    i: int = 0
    while i < len(inp):
        output[inp[i]] = inp2[i]
        i += 1
    return output


print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))
