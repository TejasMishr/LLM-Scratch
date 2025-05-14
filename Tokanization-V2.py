import re
# Let's implement a complete tokenizer class in Python.
# The class will have an encode method that splits
# text into tokens and carries out the string-to-integer mapping to produce token IDs via the
# vocabulary. 
# In addition, we implement a decode method that carries out the reverse
# integer-to-string mapping to convert the token IDs back into text.



# Step 1: Store the vocabulary as a class attribute for access in the encode and decode methods
# Step 2: Create an inverse vocabulary that maps token IDs back to the original text tokens
# Step 3: Process input text into token IDs
# Step 4: Convert token IDs back into text
# Step 5: Replace spaces before the specified punctuation


    


    
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        # Handling unknown tokens Improves the tokenizer 
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text




with open("theverdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    
print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# Data Cleaning (Preprocessing)
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# print(preprocessed)
print(len(preprocessed))

# Tokenization

# Sorted it for Token IDs
all_tokens = sorted(set(preprocessed)) 
# print(all_tokens)
# for i in all_tokenss:
#     print(i)


# In Below text we have painted word which is not in the vocabulary
# so we need to replace it with the <unk> token or <unknown> token
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

# text = """"It's the last he painted, you know," 
#            Mrs. Gisburn said with pardonable pride."""
vocab = {token:integer for integer,token in enumerate(all_tokens)}
tokenizer = SimpleTokenizerV2(vocab)
# print(all_tokens)
ids = tokenizer.encode(raw_text)
print(ids)

# Decoding the token IDs back into text
decoded_text = tokenizer.decode(ids)
print(decoded_text[:100])