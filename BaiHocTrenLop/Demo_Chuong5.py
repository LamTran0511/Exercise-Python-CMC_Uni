def luufile():
    file = open("csdlsinhvien.txt", "w" , encoding="utf-8")
    file.writelines("SV001;Nguyễn Văn A;8.7\n")
    file.writelines("SV001;Nguyễn Văn B;6.7\n")
    file.writelines("SV001;Nguyễn Văn C;5.7\n")
    file.writelines("SV001;Nguyễn Văn D;7.7\n")
    file.writelines("SV001;Nguyễn Văn E;9.7")
    file.close()
luufile()

def mofile():
    file = open("csdlsinhvien.txt", "r", encoding="utf-8")
    for line in file:
        print(line.strip())
    file.close()
mofile()

import json
jsonString = '{"ma":"nv1", "age":22, "ten":"Nguyễn Khánh Sơn"}'
dataObject = json.loads(jsonString)
print(dataObject)
print("Code=", dataObject["ma"])
print("Name=", dataObject["ten"])
print("Age=", dataObject["age"])