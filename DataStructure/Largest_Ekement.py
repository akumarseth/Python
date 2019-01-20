def largest_element(arr):
    max = 0
    sec_max = 0
    third_max = 0
    fourth_max = 0
    if len(arr) < 3:
        return
    for i in range(len(arr)):
        if(arr[i] > max):
            fourth_max = third_max
            third_max = sec_max
            sec_max = max
            max=arr[i]
        elif(arr[i] < max and arr[i] > sec_max):
            fourth_max = third_max
            third_max = sec_max
            sec_max = arr[i]
        elif(arr[i] < sec_max and arr[i] > third_max):
            fourth_max = third_max
            third_max = arr[i]
        elif(arr[i] < third_max and arr[i] > fourth_max):
            fourth_max = arr[i]
        
    return max, sec_max, third_max, fourth_max

input_arr = [600, 25, 570, 90, 690, 290, 400, 590] 
max_ele,sec_max_ele,third_max_ele,fourth_max_ele = largest_element(input_arr)
print(max_ele,sec_max_ele,third_max_ele,fourth_max_ele)