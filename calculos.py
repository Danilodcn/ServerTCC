import random
import timeit


def sort(lista: list, debug=False):
    retorno = {"debug": debug}
    t = timeit.default_timer()
    try:
        if debug: 
            l = lista.copy()
            #print (lista)
        
        for i, v in enumerate(lista):
            for j in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
        if debug: 
            retorno["nao_ordenado"] = l
            #print(lista)
        retorno["ordenado"] = lista
        retorno["status"] = True
        retorno["tempo"] = timeit.default_timer() - t
    except Exception as e:
        retorno["status"] = False
        retorno["erro"] = e
        
    return retorno

if __name__ == "__main__":
    c = sort([random.random() for i in range(20)] + "casa".split(), True)
    print(c)
