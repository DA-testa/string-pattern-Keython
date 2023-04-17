# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()

    if "I" in choice:
        ptn = input()
        txt = input()
    elif "F" in choice:
        with open ("./tests/06", 'r') as f:
            ptn = f.readline()
            txt = f.readline()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (ptn.rstrip(), txt.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(ptn, txt):
    # this function should find the occurances using Rabin Karp alghoritm 
    outputs=""
    ptns=len(ptn)
    txts=len(txt)
    d=256
    q=53
    i,j,p,t,h=0,0,0,0,1

    for i in range(ptns-1):
        h = (h*d) % q

    for i in range(ptns):
        p = (d*p + ord(ptn[i])) % q
        t = (d*t + ord(txt[i])) % q

    for i in range(txts-ptns+1):
        if p == t:
            for j in range(ptns):
                if txt[i+j] != ptn[j]:
                    break
                else:
                    j += 1
            if j == ptns:
                outputs=outputs+str(i)+" "
        if i < txts-ptns:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+ptns])) % q
            if t < 0:
                t = t+q
    # and return an iterable variable
    return outputs


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

