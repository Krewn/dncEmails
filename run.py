import sys
from get import snagRange
start = int(sys.argv[1])
end = int(sys.argv[2])
start += 1 if start == 0 else 0
snagRange(start,end)
