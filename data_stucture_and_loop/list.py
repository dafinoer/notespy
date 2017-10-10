python_version = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]

""" get individual by index """
print(python_version[0])
#1.0
print(python_version[1])
#1.5
print(python_version[2])
#1.6
print("=================")

""" index from the end of list, we just add negative index"""
print(python_version[-1])
#3.6
print(python_version[-2])
#3.5


"""Slicing Lists"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#slice third month of yaar from the month
slc = months[6:9]
print(slc)
#['July', 'August', 'September']

end_slc = months[:3]
print(end_slc)

frs_slc = months[5:]
print(frs_slc)


"""Lists, Strings, and Mutability
list adalh type seperti string, float, dan int.
"""
sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']

#menghitung index mulai dari 0
print(sample_string[4])
#'N'

print(sample_list[4])
#'Eric'

print(sample_string[12:21])
#Something

print(sample_list[1:3])
#john,

#Mutability
""" sebuah object yang bisa di modifikasi adalah Mutability"""
sample_list[2] = "Dafi"
print(sample_list)

#inmutabilty
""" sebuah object yang tidaj dapat di modifikasi ialah inmutabilty"""
# sample_string[3] = 'K'
# print(sample_string)



"""Variable that holds a list"""
name = 'dafi'
person = name
name = 'noer iskandar'
print(person)

dist = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
mr_buns_order = dist
dist[2] = "Halllo"
print(mr_buns_order)
print(dist)
