def mispelled(word1,word2):
    # write your code here
    i=0
    k=0
    if word1=='' and len(word2)==1 or word2=='' and len(word1)==1:
        return True
    if (len(word1)!=len(word2) and (word1 in word2 or word2 in word1)) or (word1==word2):
        return True
    if len(word1)==len(word2):
        while i<len(word1):
            if word2[i]==word1[i]:
                k+=1
            i+=1
        return k+1==len(word1)
    else:
        return False