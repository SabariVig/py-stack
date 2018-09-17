
def timed_reading(max_length, text):
    c=0
    text=text.split()
    print(text)
    for i in text:
        if max_length >= len(i):
            c+=1
    return c



print(timed_reading(4,"The Fox asked the stork, 'How is the soup?'"),7)
print(timed_reading(1,"..."),0)
print(timed_reading(3,"This play was good for us."),3)
print(timed_reading(3,"Suddenly he stopped, and glanced up at the houses"),5)
print(timed_reading(6,"Zebras evolved among the Old World horses within the last four million years."),11)
print(timed_reading(5,"Although zebra species may have overlapping ranges, they do not interbreed."),6)
print(timed_reading(1,"Oh!"),0)
print(timed_reading(5,"Now and then, however, he is horribly thoughtless, and seems to take a real delight in giviprint."),14)