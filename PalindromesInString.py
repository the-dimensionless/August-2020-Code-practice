def palindromes(input_user): 
   string = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), input_user)) 
   print(len(string))


input_user = input().split(" ")
length = int(input())
palindromes(input_user)
