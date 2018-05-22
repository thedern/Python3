
def leet(s, x, y):
    s = s.replace(x, y)
    return s


text = "the quick brown fox jumps over the lazy dog"

if 'a' in text:
    text = leet(text, 'a', '4')
		
if 'b' in text:
    text = leet(text, 'b', '8')

if 'e' in text:
    text = leet(text, 'e', '3')
		
if 'l' in text:
    text = leet(text, 'l', '7')

print(text)
