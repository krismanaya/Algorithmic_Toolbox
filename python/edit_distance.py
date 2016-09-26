#python2 
import sys

def edit_distance(s1,s2):
    if len(s1) > len(s2): 
        s1,s2 = s2,s1
    D = range(len(s1) + 1)
    for i2,c2 in enumerate(s2): 
        new_distance = [i2 + 1]
        for i1,c1 in enumerate(s1): 
            if c1 == c2: 
                new_distance.append(D[i1])
            else: 
                new_distance.append(1 + min((D[i1],D[i1+1],new_distance[-1])))
        D = new_distance
    return D[-1]

if __name__ == "__main__":
    print(edit_distance(raw_input(), raw_input()))