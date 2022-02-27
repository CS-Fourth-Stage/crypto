# encrypt a message using Playfair cipher?

# 5X5 matrix
array = [[] for i in range(5)]
# print(array)
key = input("Please Enter Value of Key: ")
key = key.lower()
row = 0
col = 0

# assign key to the matrix
for i in key:
    if (i == 'j'):  # Convert j into i
        i = 'i'
    if not any(i in array[k] for k in range(5)):
        array[row].append(i)
        col += 1
    if col == 5:
        row += 1
        col = 0

# continue assigning letters to the matrix
letters_list = [chr(c) for c in range(97, 123)]
for i in letters_list:
    if (i == 'j'):  # Convert j into i
        i = 'i'
    if not any(i in array[k] for k in range(5)):
        array[row].append(i)
        col += 1
    if col == 5:
        row += 1
        col = 0

# Display 5X5 matrix
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()

# ======================================================================
user_plain_text = input("please enter a plain text: ")
user_plain_text = user_plain_text.lower()
# Removing the spaces
plain_text = ""
for i in user_plain_text:
    if i == ' ' or i == '  ' or i == '   ' or i == '    ' or i == '\t':
        continue
    else:
        plain_text += i
print(plain_text)

cipher_text = ""
for i in range(0, len(plain_text) - 1, 2):
    if plain_text[i] == plain_text[i + 1]:
        plain_text = plain_text[:i + 1] + 'x' + plain_text[i + 1:]
if len(plain_text) % 2 == 1:
    plain_text += 'x'
print(plain_text)

index = []
for i in range(len(plain_text)):
    for row in range(len(array)):
        for col in range(len(array[row])):
            if plain_text[i] == array[row][col]:
                index.append([row, col])

print(index)
for row in range(0, len(index), 2):
    if index[row][0] == index[row + 1][0]:
        cipher_text += array[index[row][0]][(index[row][1] + 1) % 5] + array[index[row + 1][0]][
            (index[row + 1][1] + 1) % 5]
    elif index[row][1] == index[row + 1][1]:
        cipher_text += array[(index[row][0] + 1) % 5][index[row][1]] + array[(index[row + 1][0] + 1) % 5][
            index[row + 1][1]]
    else:
        cipher_text += array[index[row][0]][index[row + 1][1]] + array[index[row + 1][0]][index[row][1]]
print('cipher text= ' + cipher_text.upper())
