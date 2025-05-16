from torch.utils.data import Dataset, DataLoader
import torch
import tiktoken
class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokanizer, max_len, stride):
        self.input_ids = []
        self.target_ids = []

        # Tokanize Entire Data
        token_ids=tokanizer.encode(txt, allowed_special={"<|endoftext|>"})

        # use sliding window to chunk the book into overlapping sequences OF max_len
        for i in range(0, len(token_ids) - max_len, stride):
            input_chunk = token_ids[i:i+max_len]
            target_chunk = token_ids[i+1:i+max_len+1]

            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)
    
    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]
    

def create_dataloader_v1(txt, batch_size=4, max_length=256, 
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):

    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
        num_workers=num_workers
    )

    return dataloader


with open("theverdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("PyTorch version:", torch.__version__)
dataloader = create_dataloader_v1(
    raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
)

# print the first batch
data_iter = iter(dataloader)
first_batch = next(data_iter)
print(first_batch)

# print the second batch
second_batch = next(data_iter)
print(second_batch)

# print the third batch
third_batch = next(data_iter)
print(third_batch)