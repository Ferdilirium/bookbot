def get_words_number(path):
    with open(path) as f:
        file_content = f.read()
    split_words=file_content.split()
    return len(split_words)

def count_characters(text):
    dict={}
    text_lower=text.lower()
    for character in text_lower:
        if character not in dict:
            dict[character] = 1
        else:
            dict[character] += 1
    return dict

def sort_on(d):
    return d["number"]


def sort_dict(dict):
    list = []
    for i in dict:
        list.append({"character":i,"number":dict[i]})
    list.sort(reverse=True,key=sort_on)
    return list

def report(list,number,path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for i in list:
        if i["character"].isalpha() == True:
            print(f"{i["character"]}: {i["number"]}")