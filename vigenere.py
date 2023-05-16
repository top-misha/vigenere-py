
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ENCRYPT_(key_text, plaintext):
    key_word=key_text.upper()
    plaintext=plaintext.upper()
    temp=0
    ctemp=0
    encrypted_text=""
    key_text=""
    for char in plaintext:
        char = key_word[temp]
        key_text+=char
        temp+=1
        if temp > len(key_word)-1:
            temp=0
    for char in key_text:

        a_index=alphabet.index(char)
        p_char=plaintext[ctemp]
        p_index=alphabet.index(p_char)
        index=p_index+a_index
        if index>len(alphabet)-1:
            index-=len(alphabet)
        print(char,a_index, p_char, p_index,index, encrypted_text)
        encrypted_text+=alphabet[index]
        ctemp+=1
        
    return encrypted_text

def DECRYPT_(key_text, encrypted_text):
    key_text=key_text.upper()
    encrypted_text=encrypted_text.upper()
    decrypted_text=""
    temp=0
    for char in encrypted_text:
        a_index=alphabet.index(char)
        k_index=alphabet.index(key_text[temp])
        index=a_index-k_index
        decrypted_text+=alphabet[index]
        temp+=1
        if temp >=len(key_text):
            temp=0
        #print(a_index, k_index, index,decrypted_text)
    return decrypted_text
