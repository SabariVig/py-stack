##################  CODE WARS KATA ##################
#KYU LEVEL : 6
#KATA TITLE : Title Case
#KATA LINK :  https://www.codewars.com/kata/5202ef17a402dd033c000009
#####################################################

def title_case(title, ref):
    q=[]
    title=title.lower()
    title=title.split()
    ref=ref.lower().split()
    print(ref)
    for j,i in enumerate(title):
        q.append(i.title())
        if i in ref and j>0:
            q.pop()
            q.append(i.lower())
    return (" ".join(q))



##################  TEST CASES  ##################
print(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
print(title_case('the quick brown fox',''), 'The Quick Brown Fox')