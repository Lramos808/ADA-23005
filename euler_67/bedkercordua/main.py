from node import Node

triangle_list = []

with open("triangle.txt", "r", newline = "\n") as f:
        for number in f:
            number_list = []
            number = number.rstrip("\n").split(" ")
            for num in number:
                num = int(num)
                number_list.append(num)
            triangle_list.insert(0, number_list)

obj_list = []

for number_list in triangle_list:
    obj1_list = []
    for num in number_list:
        obj1_list.append(Node(int(num)))
    obj_list.append(obj1_list)


for object_row in range(1, len(obj_list)):
    for object_colum in range(0, len(obj_list[object_row])):
        obj_list[object_row][object_colum].set_left(obj_list[object_row-1][object_colum])
        obj_list[object_row][object_colum].set_right(obj_list[object_row-1][object_colum+1])
        obj_list[object_row][object_colum].determine_greater()

        
obj_list[99][0].get_sum_value()        
            
