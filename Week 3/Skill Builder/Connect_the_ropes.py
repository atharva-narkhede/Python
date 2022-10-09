#Connect the Ropes
#It was Christmas Eve and the celebrations remembering the birth of Jesus were going on in full swing at the Cathedral Chapel. The Event Management Team had arranged for some exciting games after the mass worship and feast, where adults and kids of all ages participated very actively. "Connect the Ropes" was organized for the kids where each kid will be given N ropes and the goal of the game is that the kids have to connect all of the ropes with each other to get one rope. When kids connect 2 ropes with each other they lose 'k' units from each rope.

n,k=map(int,input().split())
L=list(map(int,input().split()))
rope=L[0]+L[1]-(2*k)
for i in range(2,n):
    rope+=L[i]-(2*k)
print(rope)
