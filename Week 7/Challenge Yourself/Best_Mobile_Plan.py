#Best Mobile Plan - St. Patrick Convent organizes a project exhibition "Innovative Minds" every year with an objective to provide the platform and unleash the potential of the students by showcasing their innovative projects.

def printPlanDetails(a, b, c):
    A, B = 0, 0
    if a > 100:
        A = float((a-100)*0.25) + float(b*0.15)+float(c*0.20)
    else:
        A = float(b*0.15) + float(c*0.20)

    if a > 250:
        B = float((a-250)*0.45)+float(b*0.35)+float(c*0.25)
    else:
        B = float(b*0.35)+float(c*0.25)
    A = round(A, 2)
    B = round(B, 2)
    print('Plan A costs %.2f' % A)
    print('Plan B costs %.2f' % B)
    if A > B:
        print('Plan B is cheapest')
    elif A < B:
        print('Plan A is cheapest')
    else:
        print('Plan A and B are the same price')


a = int(input())
b = int(input())
c = int(input())
printPlanDetails(a, b, c)
