# probleme 10, 13 si 6

def cit_list():
    l=[]
    n=int(input("Dati numarul de elemente:"))
    for i in range(n):
        l.append(int(input(f"l[{i}]=")))
    return l


def elemente_pare(l):
    """
    Functie ce returneaza True daca toate elementele unei subliste sunt pare.
    :param l: lista de numere
    :return: True daca toate sunt pare, False in caz contrar
    """
    for x in l:
        if x % 2 !=0:
            return False
    return True


#prob 10
def get_longest_all_even(l):
    """
    Determina cea mai lunga secventa care are toate numerele pare
    :param l: lista cu numerele
    :return: secventa cea mai lunga de numere
    """
    subsecmax=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elemente_pare(l[i:j+1]) and len(subsecmax) < len(l[i:j+1]):
                subsecmax= l[i:j+1]
    return subsecmax


#assert-urile problemei 10
def test_get_longest_all_even(l):
    assert get_longest_all_even([2,4,6,8,9,]) == [2,4,6,8]
    assert get_longest_all_even([1,3,5]) == []
    assert get_longest_all_even([1,9,10,3]) == [10]

def elemente_prime(l):
    '''
    Functie de arata daca toate elementele unui subliste sunt prime.
    :param l: sublista cu numere intregi
    :return: True daca toate elemntele sunt prime, False in caz contrar
    '''
    for a in l:
        while a!=0:
            c=a%10
            if c==0:
                return False
            for b in range(2,c//2+1):
                if c % b == 0:
                    return False
            a=a//10
    return True

#prob 13
def get_longest_prime_digits(l):
    '''
    Determina cea mai lunga secventa ce are doar numere prime.
    :param l: lista cu numere
    :return: secventa cea mai lunga
    '''
    submax= []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if elemente_prime(l[i:j+1]) and len(submax) < len(l[i:j+1]):
                submax= l[i:j+1]
    return submax

#assert-urile prob 13
def test_get_longest_prime_digits(l):
    assert get_longest_prime_digits([2,13,5,8,9]) == [2,13,5]
    assert get_longest_prime_digits([6,8,9]) == []
    assert get_longest_prime_digits([6,2,3,8,9,10,11,13,17]) == [11,13,17]


#prob 6
def get_longest_div_k(l,k):
    subsecmax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if nr_div_cu_k(l[i:j+1],k) and len(subsecmax) < len(l[i:j+1]):
                subsecmax=l[i:j+1]
    return subsecmax


def nr_div_cu_k(l,k:int):
    for a in l:
        if a % k != 0:
            return False
    return True


def test_get_longest_div_k(l,k):
    assert get_longest_div_k([5,20,10,8,9],5) == [5,20,10]
    assert get_longest_div_k([5,15,2,6,4,9],2) == [2,6,4]
    assert get_longest_div_k([3,2,5,6,9,10],3) == [6,9]

def main():
    l=[]
    test_get_longest_all_even(l)
    test_get_longest_prime_digits(l)
    while True:
        print("1. Citire date.")
        print("2. Determinare cea mai lung?? subsecven???? cu proprietatea ca numerele sa fie pare.")
        print("3. Determinare cea mai lung?? subsecven???? cu proprietatea ca numerele sa fie formate din cifre prime.")
        print("4. Determinare cea mai lunga subsecventa cu proprietatea ca numerele sa fie divizibile cu k.")
        print("5. Iesire.")
        optiune=input("Dati optiunea: ")
        if optiune == "5":
            break
        elif optiune == "1":
            l=cit_list()
        elif optiune == "2":
            print(get_longest_all_even(l))
        elif optiune == "3":
            print(get_longest_prime_digits(l))
        elif optiune == "4":
            k=int(input("Dati numarul k:"))
            print(get_longest_div_k(l,k))
            test_get_longest_div_k(l, k)
        else:
            print("!!!Optiunea nu este buna!!!")

main()
