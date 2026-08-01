a=["dfdbfgf","dfgfdfdf"]
c_ch=()
for  word in a:
    for ch in word:
        if ch in c_ch:
            c_ch[ch]+=1
        else:
            c_ch[ch]=1
print(c_ch)

    