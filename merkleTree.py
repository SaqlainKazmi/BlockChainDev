import hashlib

# Function to calculate SHA-256 hash of a given string
def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

# Function to construct Merkle tree and calculate root hash
def construct_merkle_tree(data_list):
    if len(data_list) == 1:
        return data_list[0]

    new_data_list = []
    for i in range(0, len(data_list), 2):
        data1 = data_list[i]
        data2 = data_list[i+1] if (i+1) < len(data_list) else data1
        concat_data = data1 + data2
        hash_value = calculate_hash(concat_data)
        new_data_list.append(hash_value)

    return construct_merkle_tree(new_data_list)
 
# Generate Merkle tree and calculate root hash for given data
def generate_merkle_tree(data_parts):
    hash_list = [calculate_hash(part) for part in data_parts]
    merkle_root = construct_merkle_tree(hash_list)
    return merkle_root

# Task 1: Generate Merkle tree for the given text
data_parts = [
    "And now the end is here\nAnd so I face that final curtain\nMy friend I'll make it clear\nI'll state my case, of which I'm certain\nI've lived a life that's full\nI traveled each and every highway\nAnd more, much more\nI did it, I did it my way",
    "Regrets, I've had a few\nBut then again too few to mention\nI did what I had to do\nI saw it through without exemption\nI planned each charted course\nEach careful step along the byway\nAnd more, much, much more\nI did it, I did it my way",
    "Yes, there were times I'm sure you knew\nWhen I bit off more than I could chew\nBut through it all, when there was doubt\nI ate it up and spit it out\nI faced it all and I stood tall and did it my way",
    "For what is a man, what has he got?\nIf not himself then he has naught\nNot to say the things that he truly feels\nAnd not the words of someone who kneels\nLet the record shows I took all the blows and did it my way"
]

merkle_root = generate_merkle_tree(data_parts)
print("Merkle Root for given text:")
print(merkle_root)
print( )

# Task 2: Generate Merkle tree and calculate root hash for random strings
random_strings = [
    "Banana",
    "apple",
    "atributes",
    "strong",
    "visibility",
    "text",
    "center",
    "Gilgit"
]

merkle_root = generate_merkle_tree(random_strings)
print("Merkle Root for random strings:")
print(merkle_root)
print()

# Task 3: Generate Merkle tree and calculate root hash for file blocks
def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def parse_file_blocks(data):
    block_size = len(data) // 8
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
    return blocks

filename = 'C:\Users\Saqlain Kazmi\Desktop\Web 3.0\Projects\file.txt' # Replace with the actual filename
file_data = read_file(filename)
file_blocks = parse_file_blocks(file_data)
file_hashes = [calculate_hash(block) for block in file_blocks]
merkle_root = generate_merkle_tree(file_hashes)
print("Merkle Root for file blocks:")
print(merkle_root)
print()