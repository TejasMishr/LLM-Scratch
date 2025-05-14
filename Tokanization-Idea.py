import re
# Opening of the file

with open("theverdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    
print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# Data Cleaning (Preprocessing)
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed)
print(len(preprocessed))

# Tokenization

# Sorted it for Token IDs
all_words = sorted(set(preprocessed)) 
# print(all_words)
# for i in all_words:
#     print(i)
vocab = {token:integer for integer,token in enumerate(all_words)}



