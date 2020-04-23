a=[]
while True:
  print()
  print('Operations on List')
  print('1.insert')
  print('2.append')
  print('3.del')
  print('4.remove')
  print('5.pop')
  print('6.index')
  print('7.reverse')
  print('8.count')
  print('9.exit')
  choice=int(input('Enter ur choice'))
  print()
  if choice==1 :
             n=int(input('Enter the element to be inserted'))
             i=int(input('Enter the index position to be inserted'))
             a.insert(i,n)
             print(a)
  elif choice==2 :
             n=int(input('Enter the element to be apppended'))
             a.append(n)
             print(a)
  elif choice==3 :
             n=int(input('Enter the index position of the element to be deleted'))
             del a[n]
             print(a)
  elif choice==4 :
             n=int(input('Enter the element to be removed'))
             if n in a:
              a.remove(n)
             else:
              print('Element is not present in the list')
             print(a)
  elif choice==5 :
             a.pop()
             print(a)
  elif choice==6 :
             n=int(input('Enter the element whose index position has to be found'))
             print(a.index(n))
  elif choice==7 :
             a.reverse()
             print('Reversed List')
             print(a)
  elif choice==8 :
             print('The count of list')
             print(len(a))
  elif choice==9 :
             exit()                
