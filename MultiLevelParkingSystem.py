#method if user enters 'in' 
def in_method(t,r,c,f,x):
    for i in range(f):
        for j in range(c):
            for k in range(r):
                if t[i][j][k]=='free':
                    print(f'Parking slot is allocated for your vehicle.{x} at :\nRow={k+1}\nColumn={j+1}\nfloor={i+1}')
                    t[i][j][k]=f'vehicle{x}'#######The major issue is here why is it changing all the values
                    return True
    print(f'All the parking slots are FULL, can\'t park vehicle.{x}')
    return False
def out_method(t,r,c,f,x):
    for i in range(f):
        for j in range(c):
            for k in range(r):
                if t[i][j][k]==f'vehicle{x}':
                    t[i][j][k]='free'
                    return

#__main__
r=int(input('Enter the maximum number of rows in your parking area : '))
c=int(input('Enter the maximum number of columns in your parking area : '))
f=int(input('How many floors do you have for parking? : '))
total_capacity=[[[ 'free' for k in range(r)] for j in range(c)] for i in range(f)]

print('\n\tEnter \'in\' to park a new vehicle')
print('\tEnter \'out.vehicle<number>\' to unpark a parked vehicle with its number')
print('\tEnter \'--display-slots\' to see the available slots in a 3D-list format')
print('\tEnter \'close\' to terminate the program')

process=input()
#waits for the user input
#out interface
vno=0#used for naming every vehice comes to park
vnolist=[]#used to store the history of the parked vehicles
while process!='close':
    if process=='in':
        check=in_method(total_capacity,r,c,f,vno+1)
        if check==True:
            #if the parking slot is available, allocated
            vno+=1
            vnolist.append(vno)#adding the vehicle name into the record of current parked vehicles
    elif process=='--display-slots':
        print("\n\tDataBase -> ",total_capacity)
    else:
        vehiclenumber=process.replace('out.vehicle','')
        try:
            #vehicle number is generated here
            vehiclenumber=int(vehiclenumber)
            #checking if that vehicle number exists or not
            if vehiclenumber in vnolist:
                #vehicle is already parked now get it removed
                vnolist.remove(vehiclenumber)#removing that particular vehicle from the record of current parked vehicles
                #pass to the method to make changes in the list
                out_method(total_capacity,r,c,f,vehiclenumber)
                print(f'Vehicle.{vehiclenumber} is unparked successfully')
            else:
                #if user tries to remove the vehicle which is not parked
                print('The vehicle does\'nt exist to be unparked')
        except ValueError:
            print('Enter the correct input')
    process = input('\n')
print('The process is terminated successfully')
print("\tALERT!",end=' ')
if vnolist!=[]:
    print("Below vehicle/s are yet to be unparked")
    for i in range(len(vnolist)):
        print(f'\tVehicle({vnolist[i]})')

