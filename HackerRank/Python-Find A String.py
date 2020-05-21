def count_substring(string, sub_string):
    if sub_string in string:
        print("True")
    # print(string,sub_string)
    # return

if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string="ABCDCDC"
    sub_string="CDC"
    count_substring(string, sub_string)
    # count = count_substring(string, sub_string)
    # print(count)