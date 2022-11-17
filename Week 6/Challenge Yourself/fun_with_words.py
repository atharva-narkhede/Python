#"Juniors Network" Cartoon Channel is the favorite channel of all the kids in the city. 
#As it is vacation time, the channel had introduced several new segments to engage the kids in a more creative manner. 
#"Fun with Words" is one such activity involving English alphabets, where school kids were invited to participate.



n = [int(i) for i in input().split()][:2]
st = [str(i) for i in input().split()][:n[0]]
arr = [None]*n[1]
for i in range(0,n[1]):
    arr[i]=input()
    arr[i]=arr[i].split()
    nu = int(arr[i].pop(0))
    arr[i]=arr[i][:nu]
s=0
for i in st:
    for j in range(0,n[1]):
        if i in arr[j]:
            print("Yes",end=" ")
            s=1
            break
    if s==0:
        print("No",end=" ")
    s=0
