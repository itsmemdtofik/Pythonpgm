import os
import re
import csv
import textract
import time

# Define the directory where the files are located
DIRECTORY = '/home/mohammadtofik/190905514/Data'

# Define the file where the index will be stored
INDEX_FILE = 'index.csv'

# Define the regex pattern for splitting text into tokens
TOKEN_PATTERN = re.compile(r'\b\w+\b')

# Define the stopwords to be removed during preprocessing
STOPWORDS = set(['a', 'an', 'the', 'and', 'or', 'not', 'is', 'are', 'was', 'were'])

# Initialize the reverse inde
index = {}

#initialize the token count dictionary
token_count = {}

# Loop over all files in the directory
for file_name in os.listdir(DIRECTORY):
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1][1:].lower()

    # Check if the file has a supported extension
    if file_extension not in ('pdf', 'pptx', 'docx'):
        continue

    # Extract the text from the file using textract
    file_path = os.path.join(DIRECTORY, file_name)
    try:
        text = textract.process(file_path).decode('utf-8')
    except:
        continue

    # Preprocess the text
    tokens = TOKEN_PATTERN.findall(text.lower())
    tokens = [token for token in tokens if token not in STOPWORDS]
    tokens = [token[:30] for token in tokens]  # truncate tokens to 30 characters

    # Update the reverse index
    for i, token in enumerate(tokens):
        if token not in index:
            index[token] = {}
        if file_name not in index[token]:
            index[token][file_name] = {'indices': [], 'count': 0}
        index[token][file_name]['indices'].append(i)
        index[token][file_name]['count'] += 1
    if file_path not in token_count:
        token_count[file_path] = len(tokens)

def preprocess(text):
    tokens = TOKEN_PATTERN.findall(text.lower())
    tokens = [token for token in tokens if token not in STOPWORDS]
    return tokens

# Define the function to index a file
def index_file(file_path):
    try:
        text = textract.process(file_path).decode('utf-8')
    except:
        return
    tokens = preprocess(text)
    for i, token in enumerate(tokens):
        if token not in index:
            index[token] = {}
        if file_path not in index[token]:
            index[token][file_path] = {'indices': [], 'count': 0}
        index[token][file_path]['indices'].append(i)
        index[token][file_path]['count'] += 1
    if file_path not in token_count:
        token_count[file_path] = len(tokens)

#Index all the file in the dictionary
start_time = time.perf_counter()
for file_name in os.listdir(DIRECTORY):
    file_path = os.path.join(DIRECTORY, file_name)
    if os.path.isfile(file_path):
        index_file(file_path)
end_time = time.perf_counter()


#Print the total token count and the time taken
total_tokens = sum(token_count.values())
print(f'Total Token : {total_tokens}')
print(f'Total time that has been taken to generate the token : {end_time - start_time:.10f} seconds')

# Save the index to a CSV file
with open(INDEX_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Token', 'Filename', 'Index', 'Count'])
    for token, files in index.items():
        for file_name, data in files.items():
            indices = data['indices']
            count = data['count']
            writer.writerow([token, os.path.basename(file_name), indices, count])

# Load the index from the CSV file
with open(INDEX_FILE, 'r', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        token, file_name, indices_str, count = row
        indices = [int(i) for i in indices_str[1:-1].split(',')]
        if token not in index:
            index[token] = {}
        index[token][file_name] = {'indices': indices, 'count': int(count)}

# Define the search function
def search(keyword):
    keyword = keyword.lower()
    if keyword not in index:
        return [], 0.0
    results = []
    start_time = time.perf_counter()
    for file_name, data in index[keyword].items():
        indices = data['indices']
        count = data['count']
        results.append({'file': file_name, 'indices': indices, 'count': count})
    end_time = time.perf_counter()
    total_search_time = end_time - start_time
    print(f'The total time that has been taken to search the keyword : {total_search_time:.10f}')
    return results

# Test the search function
keyword = str(input("Enter the keyword to be search : "))
results = search(keyword)
if len(results) == 0:
    print("\n----------------------------------------\n")
    print(f'No results found for keyword "{keyword}"')
    print("\n----------------------------------------\n")
else:
    print("\n----------------------------------------\n")
    for result in results:
        file_name = result['file']
        indices = result['indices']
        count = result['count']
        print(f' In File: {file_name} ({count} occurrences)')
        print("\n----------------------------------------\n")
        for i in indices:
            print(f'  At Index: {i}')
            print("\n----------------------------------------\n")