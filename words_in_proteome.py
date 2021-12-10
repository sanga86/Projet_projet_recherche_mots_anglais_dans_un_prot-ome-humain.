def read_words(nom):
        liste=[]
        filin = open(nom,"r")
        mots = filin.readlines()
        for mot in mots :
                if len(mot) >= 4 :      #retour chariot compte comme un caractère supplémentaire chap7
                        liste.append((mot.upper()).strip())     #strip  nettoie les retours à la ligne chap10
        filin.close()
        return liste

def read_sequences(nom) :
        dic={}
        sequence = ""
        identifiant = ""
        filin = open(nom,"r")
        proteome = filin.readlines()
        for ligne in proteome :
                if ligne.find(">sp|") == -1 :
                        sequence = sequence + ligne.strip()
                if ligne.find(">sp|") != -1 :
                        if identifiant != "" :
                                dic[identifiant] = sequence
                        identifiant = ligne[4:10]
                        sequence = ""
        return dic

def search_words_in_proteome(mots, dictionnaire) :
        dic = {}
        for mot in mots :
                i=0   
                for key in dictionnaire :
                        if dictionnaire[key].find(mot) != -1 :
                             i=i+1
         
                dic[mot] = i
                #if i > 0:
                #        print(mot, "found in", i ,"sequences")
        return dic


def search_words_in_proteome2(mots, dictionnaire) :
        dic = {}
        for mot in mots :
                i=0   
                for key in dictionnaire :
                        i = i + dictionnaire[key].count(mot)         
                dic[mot] = i
                #if i > 0:
                #        print(mot, "found in", i ,"sequences")
        return dic
        

        
def find_most_frequent_word(dictionnaire):
        i = 0
        mot = ""
        for key in dictionnaire :
                if dictionnaire[key] > i :
                        i = dictionnaire[key]
                        mot = key
        print(mot, "trouvé", i, "fois")
        print("soit", (i/len(list(prot.keys())))*100 , "pourcent des séquences")


        
        

mots = read_words("english_common_words.txt")

print("nombre de mots sélectionnés : ", len(mots)) 

prot = read_sequences("human_proteome.fasta")

print("Séquence associée à la protéine O95139 :",prot["O95139"])

print("Nombre de séquences lues : ", len(list(prot.keys())))

nbsequ = search_words_in_proteome(mots, prot)

find_most_frequent_word(nbsequ)

nbsequ2 = search_words_in_proteome2(mots, prot)

find_most_frequent_word(nbsequ2)

