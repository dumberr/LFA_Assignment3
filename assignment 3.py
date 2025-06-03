import random


#gramatica
CFG = {
    "neterminale": ["S"],
    "terminale": ["a" , "b"],
    "start" : "S",
    "generare" : {
        "S" : [["a", "S" , "b"], []]
    }
}

#generare cuvinte cu random 
def generare_string(simbol="S", lmax=10, s=""):
    if len(s) >= lmax:
        return s
    
    if simbol in CFG["terminale"]:
        return s + simbol
    
    generare = CFG["generare"][simbol]
    x = random.choice(generare)

    for i in x:
        s = generare_string(i , lmax, s)
    return s


#evitam dupe-uri (dar pentru lenght 10 exista doar 5 cuvinte in gramatica asta deci facem un try ca sa avem cat mai putine dupe-uri)
def generare_n_stringuri(n = 10, lmax = 10):
    gen = set()
    tried = 0
    while len(gen) < n and tried <= 10:
        s = generare_string(lmax=lmax)
        gen.add(s)
        tried += 1
    return gen

#derivare recursiv cu constructie
def derivare(cfg_generare, target, start="S", max_pasi=50):
    def pasi(current_list, pas, nr_pasi):
        if nr_pasi > max_pasi:
            return None

        if current_list == list(target):
            return pas

        if all(simbol not in cfg_generare for simbol in current_list):
            return None

        # caut primul neterminal
        for i, simbol in enumerate(current_list):
            if simbol in cfg_generare:
                for constr in cfg_generare[simbol]:
                    if constr == []:
                        new_list = current_list[:i] + current_list[i+1:]
                    else:
                        new_list = current_list[:i] + constr + current_list[i+1:]
                    result = pasi(new_list, pas + ["".join(new_list)], nr_pasi + 1)
                    if result:
                        return result
                break
        return None

    return pasi([start], [start], 0)


#recunoastere
def recognize(s, simbol = "S"):
    if simbol == "":
        return s == ""
    
    if simbol in CFG["terminale"]:
        return s.startswith(simbol) and recognize(s[1:], "")
    if simbol == "S":
        if len(s) >= 2 and s[0]=="a" and s[-1]=="b":
            return recognize(s[1:-1], "S")
        if s =="":
            return True
    return False

#meniu de select "actiune"
if __name__ == "__main__":
    while True:
        print("1. Genereaza N cuvinte")
        print("2. Derivare")
        print("3. Recunoastere")
        print("4. exit")
        print("-------------")

        choice = input("task-ul (1-4): ").strip()
        
        if choice == "1":
            n = int(input("cate cuvinte: "))
            strings = generare_n_stringuri(n)
            print("Cuvinte generate:")
            for s in strings:
                print(repr(s))

        elif choice == "2":
            cuvant = input("cuvant pentru derivare: ").strip()
            rezultat = derivare(CFG["generare"], cuvant)
            if rezultat:
                print("Pașii derivării:")
                for pas in rezultat:
                    print(pas)
            else:
                print("Imposibil de ajuns la target:", cuvant)

        elif choice == "3":
            cuvant = input("cuvant de recognize:").strip()
            print("Rezultat:", recognize(cuvant))
        
        elif choice == "4":
            break