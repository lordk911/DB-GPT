

def extract_content(long_string, s1, s2, is_include: bool = False):
    # extract text
    match_map ={}
    start_index = long_string.find(s1)
    while start_index != -1:
        if is_include:
            end_index = long_string.find(s2, start_index + len(s1) + 1)
            extracted_content = long_string[start_index:end_index + len(s2)]
        else:
            end_index = long_string.find(s2, start_index + len(s1))
            extracted_content = long_string[start_index + len(s1):end_index]
        if extracted_content:
            match_map[start_index] = extracted_content
        start_index = long_string.find(s1, start_index + 1)
    return match_map

def extract_content_open_ending(long_string, s1, s2, is_include: bool = False):
    # extract text  open ending
    match_map = {}
    start_index = long_string.find(s1)
    while start_index != -1:
        if  long_string.find(s2, start_index) <=0:
            end_index = len(long_string)
        else:
            if is_include:
                end_index = long_string.find(s2, start_index + len(s1) + 1)
            else:
                end_index = long_string.find(s2, start_index + len(s1))
        if is_include:
            extracted_content = long_string[start_index:end_index + len(s2)]
        else:
            extracted_content = long_string[start_index + len(s1):end_index]
        if extracted_content:
            match_map[start_index] = extracted_content
        start_index= long_string.find(s1, start_index + 1)
    return match_map



if __name__=="__main__":
    s = "abcd123efghijkjhhh456xxx123aa456yyy123bb456xx123"
    s1 = "123"
    s2 = "456"

    print(extract_content_open_ending(s, s1, s2, True))