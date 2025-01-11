#ONCE WE DECLARE THE STRING WE CANNOT MODIFY IT, IF WE TRY TO MOdify the string it will create new String
# if new String doesnot  have any reference variable then it will be removed
# python internally uses String interning
# String interning is the procsess of checking String interm pool befote creating any new objcets
#whenver  we want to create  a new obkects, python fitst wiill check tring intern pool, weather that object alreay exists or not

#when object already exist in the String intern records  then address  of existing object will be reused
#s1 ='kodnest'
#s1.upper()
#print(s1)

#s1='K'
#print(s1, id(s1))

s1='Hello'
s2='world'
print(s1, id(s1))
print(s2, id(s2))

print('ID of H:',s1[0]) 
print('s1 ID of o:',id(s1[-1]))
print('s2 ID od w:', id(s2[0]))
print('s2 ID of o:', id(s2[1]))

print('s1 Id of l:',id(s1[2]))
print('s1 Id of l:',id(s1[3]))
print('s2 Id of l:',id(s2[3]))
