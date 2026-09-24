import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        if start <= end:
            r = list(range(start, end + 1))
        else:
            r = list(range(start, end - 1, -1))
        print(r)
    except ValueError:
        print("none")
else:
    print("none")