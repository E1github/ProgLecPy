# https://github.com/verigak/progress/
# https://habr.com/ru/post/483400/

# import time
# from tqdm import tqdm

# mylist = [1,2,3,4,5,6,7,8]

# for i in tqdm(mylist):
#     time.sleep(1)
    
def intP(x, x10):
    if x * 10 == x10 // 10:
        print('|', end= '')
    return int(x)
    
def is_simple_numbers(num) -> bool: 
    is_simple = 1
    for i in range(2,num):        
        is_simple = is_simple * num % i
        # if i * 10 == num // 100:
        #     print('|', end= '')         
    return is_simple

num10 = int(input('Input number: '))
simple_mult_list = [intP(i,num10) for i in range(2,num10) if is_simple_numbers(i)] #список простых чисел со второго ибо 1 не надо
# print(simple_mult_list) # 1271 9999
mult = [[simple_mult_list[i], "x "+str(num10 // simple_mult_list[i])] for i in range(len(simple_mult_list)) if num10 % simple_mult_list[i] == 0]
print(f'\n Simple multiplires for {num10} is: {mult}')