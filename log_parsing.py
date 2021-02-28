#Jonathan Part 5 and 6
from collections import Counter

# Read file directly into a Counter
with open('file') as f:
    cnts = Counter(l.strip() for l in f)

# Display 3 most common lines
cnts.most_common(3)

# Display 3 least common lines
cnts.most_common()[-3:]
