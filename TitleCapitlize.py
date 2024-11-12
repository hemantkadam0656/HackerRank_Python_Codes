

# def capitlize(string):
#     StringList = string.split(" ")
#     for i in StringList:
#         NameWorlds = []
#         Name = []
#         for j in i:
#             NameWorlds.append(j)

#         title = (NameWorlds[0]).upper()
#         NameWorlds.remove(NameWorlds[0])
#         NameWorlds.insert(0, title)

#         result = "".join(NameWorlds)
#         Name.append(result)
#         for j in Name:
#             print(j, end=" ")


# if __name__ == "__main__":
#     s = input()
#     result = capitlize(s)


def capitalize_name(s):
    words = s.split(" ")
    print(words)
    capitalized_words = [word.capitalize() if word.isalpha() else word for word in words]
    
    return " ".join(capitalized_words)


full_name = input("Enter the full name: ")
print(capitalize_name(full_name))
