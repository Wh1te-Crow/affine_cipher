from linear_comparison import solving_linear_comparisons,reverse_modulo

alphabet,bigrams_dict = "абвгдежзийклмнопрстуфхцчшщьыэюя",{}

file=open('03.txt', encoding='utf-8')
our_cipher_text = file.read().replace("\n","")

#string = our_cipher_text
def search_index_matching(Our_string,key_length):
	temp_string = ""
	for i in range(0,len(Our_string),key_length):
		temp_string+=Our_string[i]
	temp_dict = {}
	for i in alphabet:
		temp_dict[i]=0
	for i in alphabet:
		for j in temp_string:
			if i == j:
				temp_dict[i]+=1
	index_matching = 0
	for i in temp_dict.keys():
		index_matching+=(temp_dict[i])*(temp_dict[i]-1)/(len(temp_string)*(len(temp_string)-1))
	return index_matching

def find_index(bigram):
	return alphabet.find(bigram[0])*31+alphabet.find(bigram[1])

for i in alphabet:
	for j in alphabet:
		bigrams_dict[i+j]=0

text = []
while (len(our_cipher_text)>0):
	text += [our_cipher_text[:2]]
	our_cipher_text=our_cipher_text[2:]

for i in text:
	bigrams_dict[i]+=1
	
temp_arr1,temp_arr2 = [],[]

for i in bigrams_dict.keys():
	temp_arr1 += [bigrams_dict[i]]
	temp_arr2 += [i]
flag,counter = False,1
while flag == False:
	flag = True
	for i in range(len(temp_arr1)-counter):
		if temp_arr1[i]>=temp_arr1[i+1]:
			temp_arr1[i],temp_arr1[i+1] = temp_arr1[i+1],temp_arr1[i]
			temp_arr2[i],temp_arr2[i+1] = temp_arr2[i+1],temp_arr2[i]
			flag = False
	counter+=1

temp_arr3,temp_arr4,number_of_unique,i  = [],[],0,0

while (number_of_unique < 5):

	if not (temp_arr1[len(temp_arr1)-i-1] in temp_arr3):
		temp_arr3+=[temp_arr1[len(temp_arr1)-i-1]]
		temp_arr4+=[temp_arr2[len(temp_arr2)-i-1]]
		number_of_unique+=1
	else:
		temp_arr3+=[temp_arr1[len(temp_arr1)-i-1]]
		temp_arr4+=[temp_arr2[len(temp_arr2)-i-1]]
	i+=1

print(temp_arr3,temp_arr4)

most_frequent = ['ст', 'но', 'то', 'на', 'ен']

# К этому моменту все правильно

keys_arr,temp_arr,counter = [],[],0
for i in most_frequent:
	for j in temp_arr4:
		temp_arr4_without_j,most_frequent_without_i=[],[]

		for temp in most_frequent:
			if temp != i:
				most_frequent_without_i+=[temp]
		for temp in temp_arr4:
			if temp != j:
				temp_arr4_without_j+=[temp]
		for i1 in (most_frequent_without_i):
			for j1 in (temp_arr4_without_j):
				# X0 -> Y0, X1 -> Y1
				X0,X1 = find_index(i),find_index(i1)
				Y0,Y1 = find_index(j),find_index(j1)
				M2 = 31*31
				A = solving_linear_comparisons(X0-X1,Y0-Y1,M2)
				if type(A) is list:
					for Index in A:
						B = (Y0 - Index*X0)%M2
						if not([int(Index),int(B)] in keys_arr):

							keys_arr+=[[int(Index),int(B)]]
				elif not (type(A) is bool):
					B = (Y0 - A*X0)%M2
					if not([int(A),int(B)] in keys_arr):
						keys_arr+=[[int(A),int(B)]]


#keys_arr = list(set(keys_arr))
#print(len(keys_arr))

#print(keys_arr.index([199,700]))
#print(keys_arr)
for j in keys_arr:
	print(keys_arr.index(j))
	temp = ""
	for i in text:
		M2 = 961
		Y1 = find_index(i)
		a_obb = reverse_modulo(j[0],M2)[1]
		X1 = (a_obb*(Y1- j[1]))%M2
		
		second = X1%31
		first = (X1 - second )//31
		
		temp += alphabet[first] + alphabet[second]
		
	print(search_index_matching(temp,1))
	if (search_index_matching(temp,1))>0.055:
		cipher_text = open('open_text[{}].txt'.format(str(j)), 'w')
		cipher_text.write(temp)
		cipher_text.close()
		
	
	
#temp +=alphabet[first]+alphabet[second]



# Пока верно


file.close()