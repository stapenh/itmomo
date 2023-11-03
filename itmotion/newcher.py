
def to_string(p: polynomial):
    def monomial_to_string(coeff: float, d: int) -> str:
        if coeff == 0:
            return''

        if d == 0:
            return f'{coeff}'
        elif d == 1:
            if coeff == 1:
                return 'x'
            elif coeff == -1:
                return '-x'
            return f'{coeff}x'
        else:
            if coeff == 1:
                return f'x^{d}'
            elif coeff == -1:
                return f'-x^{d}'
            return f'{coeff}x^{d}'


    monomials = []
    for d in reversed(range(len(p))):
        monom_2= monomial_to_string(p[d], d)
        if monom_2:
            monomials.append(monom_2)
    if not monomials:
        return ''
    result = ' + '.join(monomials)
    return result.replace(' + -', ' - ')





def to_latex(p:polynomial):


