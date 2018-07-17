def is_hashtag(s) :
    from string import ascii_letters as lt
    if s[0] != "#" : return False
    check = False
    for i in s :
        if i in lt : check = True
    if check : return True
    else : return False
#--------------------------------------------------------------
def get_all_hashtag(s) :
    out = set()
    text = [e for e in s.split()]
    for i in text :
        if is_hashtag(i) :
            out.add(i)
    return out
#--------------------------------------------------------------
def count_hashtag(s) :
    out = [0,0]
    text = [e for e in s.split()]
    for i in text :
        if is_hashtag(i) : out[0] += 1
        else : out[1] += 1
    return tuple(out)
#--------------------------------------------------------------
exec(input().strip())

