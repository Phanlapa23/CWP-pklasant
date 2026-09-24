import sys

def downcase_it(text):
    return text.lower()

if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        print(downcase_it(param))
else:
    print("none")