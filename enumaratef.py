#Enumarate 
l=["Pizza","Burger","Bread","French Fries",]
# i=1
# for item in l:
#     if i % 2 != 0:
#         print(item)
#     i+=1
#
for index,item in enumerate(l):
    if index%2==0:
        print(f"Jarvis please buy {item}")