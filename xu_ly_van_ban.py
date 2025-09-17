import sys
import re

def process_sentence(s):
    words = s.strip().split()
    if not words:
        return None
    s = ' '.join(words).lower()
    return s[0].upper() + s[1:] if s else None

def main():
    text = sys.stdin.read()
    parts = re.split(r'[.!?]', text)
    for p in parts:
        if re.search(r'[A-Za-z0-9]', p):
            sentence = process_sentence(p)
            if sentence:
                print(sentence)

if __name__ == "__main__":
    main()
