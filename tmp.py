def buildAllBinStrings(n):
    """
    Helper function, which returns all subsets of graph edges set in form of
    binary string, where 1 stands for i-th edge to be in grpah and 0 is for
    its absence

    :param n: amount of graph vertices
    :return:
    """
    m = int((n * (n - 1)) / 2)
    res = []
    for i in range(1 << m):
        string = '{:0>'+ str(m) +'}'
        res.append(string.format(bin(i)[2:]))
    return res


def str2matrix(s, n):
    """
    Builds an adjacency matrix for simple non-oriented graph
    from flatten string, which represents an edge placement
                [.,..,..,..]
                [0,..,..,..]
    001010 -- > [0, 1,..,..]
                [0, 1, 0,..]
    empty spaces are filled according to a definition of a simple
    non-oriented graph adjacency matrix
    :param s: string to be interpreted
    :param n: size of graph
    """
    mx = [[0] + [None for i in range(n - 1)]]
    for i in range(1, n):
        indx = (i * (i - 1)) // 2
        cut = s[indx: indx + i]
        row = list(map(int, cut)) + [0]+ [None for j in range(n - i - 1)]
        mx.append(row)
    for i in range(n):
        for j in range(i, n):
            mx[i][j] = mx[j][i]
    return mx


def buildAllGraphMatr(n):
    """
    Builds all adjacency matrices for a simple non-oriented graph on n vertices

    :param n: amount of graph vertices
    :return: a list of matrices
    """
    res = []
    for s in buildAllBinStrings(n):
        res.append(str2matrix(s, n))
    return res


def task1(n):
    dn = DihedralGroup(n)
    orbits = dn.orbits()
    powers = [len(orb) for orb in orbits]
    return orbits, powers


def task2(n):
    an = AlternatingGroup(n)
    classes = an.conjugacy_classes()
    powers = [len(list(s)) for s in classes]
    reps = an.conjugaccy_classes_representatives()
    conj_perms = _conjugate_perms(n)
    return classes, powers, reps, conj_perms


def _get_odd_perm(n):
    import random
    sn = SymmetricGroup(n)
    for i in sn:
        if sign(i) == -1:
            return i


def _conjugate_perms(n):
    odd = _get_odd_perm(n)  # odd perm, which will be x in (x^-1*pi*x) = pi2 (it will conjugate pi1 and pi2)
    sn = SymmetricGroup     # redefine for compactness
    flat_up = list(range(1, n + 1))     # upper row of permutation X in canonic notation
    flat_down = list(Permutation(odd))  # lower row of permutation X in canonic notation
    if n % 2 == 1:          # if length of perm is odd - cut it to even so it can be safely split in two odd cycles
        flat_up = flat_up[:-1]
        flat_down = flat_down[:-1]
    for i in range(3, len(flat_up), 2):
        # attemt to get two permutation pi1, pi2 which are
        # built from two cycles of odd length (permutation itself will be even)
        # this permutations are supposed to be conjugated by :odd: permutation
        upper_notat = '({})'.format(','.join(flat_up[:i + 1])) + '({})'.format(','.join(flat_up[i + 1:]))
        lower_notat = '({})'.format(','.join(flat_down[:i + 1]) + '({})'.format(','.join(flat_down[i + 1:]))
        p1 = sn(upper_notat)
        p2 = sn(lower_notat)
        # extra test, if they are conjugated in Sn but not in An
        if p1 != p2 and not _is_conjugated(p1, p2, n):
            return p1, p2


def _is_conjugated(p1, p2, n):
    an = AlternatingGroup(n)
    cl = an.conjugacy_classes()
    for c in cl:
        if p1 in c and p2 in c:
            return True
    return False
