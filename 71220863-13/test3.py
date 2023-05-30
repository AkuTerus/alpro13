def palindrome(kalimat):
    kalimat_balik = kalimat[::-1]
    if kalimat ==kalimat_balik:
        return True
    else:
        return False

def palindrome_rekrusif(kalimat,depan,belakang):
    #base case jika tinggal 1 karakter
    if depan == belakang:
        return True
    elif depan == belakang -1:
        if kalimat[depan]==kalimat[belakang]:
            return True
        else: 
            return False
    else:
        if kalimat[depan]== kalimat[belakang]:
            return palindrome_rekrusif(kalimat, depan+1, belakang-1)
        else:
            return False

print(palindrome('duta wacana'))
print(palindrome('kasur rusak'))
kalimat = 'kasur rusak'
print(palindrome_rekrusif(kalimat, 0, len(kalimat)-1))
kalimat = 'duta wacana'
print(palindrome_rekrusif(kalimat, 0, len(kalimat)-1))