def comer(comida, e_saudavel):
    if e_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente só vive uma vez.'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Puts, dormi muito... Estou atrasado para o trabalho.'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('


def e_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False
