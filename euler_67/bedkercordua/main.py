from node import Node

triangle_list = []

with open("triangle.txt", "r", newline = "\n") as f:
        for number in f:
            number_list = []
            number = number.rstrip("\n").split(" ")
            for num in number:
                num = int(num)
                number_list.append(num)
            triangle_list.insert(0,number_list)

obj_list = []
for number_list in triangle_list:
    for num in number_list:
        obj1_list = []
        obj1_list.append(Node(num))
        obj_list.append(obj1_list)


        
           
            
counter = len(triangle_list)

for object_row in range(0, 100):
    for object_colum in range(0, 100):
        print(object_row)
        print(object_colum)
        print(obj_list[object_row][object_colum].get_value())
        
