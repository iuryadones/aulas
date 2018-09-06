def check_bisp(owner, pawn):

    row_o, row_p = int(owner[1]), int(pawn[1])

    col_o = (ord(owner[0]) - ord("a")) + 1
    col_p = (ord(pawn[0]) - ord("a")) + 1

    return (col_o - col_p) ** 2 == (row_o - row_p) ** 2


if __name__ == "__main__":
    check_bisp("h1", "a8")
    check_bisp("h8", "a1")
    check_bisp("g7", "a1")
    check_bisp("a7", "g1")
    check_bisp("a7", "a1")
    check_bisp("d7", "a1")
