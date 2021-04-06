#Hello Emily and Simon. Please enter your name below and push to Git to see that the Git is working propperly

def git_checker():

    e='Emily'
    s='Simon'

    if e=='Emily' and s=='':
        print("Emily joined the mining company, but Simon didn't. Germans... *eye roll*")
    elif e=='' and s=='Simon':
        print("Simon joined the mining company, but Emily didn't. Tukkers... *eye roll*")
    elif e=='Emily' and s=='Simon':
        print("The mining party is assembled. LET'S GOOOOOOO")
    else:
        print("Hey Google, play 'Mad World' by Gary Jules, Imma sad")

git_checker()
