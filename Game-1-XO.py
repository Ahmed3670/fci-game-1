while True :
  arr=[1,2,3,4,5,6,7,8,9]
  arr2=[]
  i=1
  while i < 10 :
    print("\n") 
    print (" ",arr[0]," | ",arr[1]," | ",arr[2])
    print ("_________________")
    print (" ",arr[3]," | ",arr[4]," | ",arr[5])
    print ("_________________")
    print (" ",arr[6]," | ",arr[7]," | ",arr[8])
    print("\n") 
    if i%2!=0 :
      print ("<< player 1's turn >>") 
    if i%2==0 :
      print ("<< player 2's turn >>") 
    a=int(input("\n<< enter a number >>\n"))
    while a<1 or a>9 or (a in arr2) :
      print ("<< enter another number >>") 
      a=int(input())
    if i%2!=0 :
      arr[a-1]=("X")
    if i%2==0 :
      arr[a-1]=("O")
    i+=1
    if (arr[0]==("X") and arr[1]==("X") and arr[2]==("X")) or (arr[3]==("X") and arr[4]==("X") and arr[5]==("X")) or (arr[6]==("X") and arr[7]==("X") and arr[8]==("X")) or (arr[0]==("X") and arr[4]==("X") and arr[8]==("X")) or (arr[2]==("X") and arr[4]==("X") and arr[6]==("X")) or (arr[0]==("X") and arr[3]==("X") and arr[6]==("X")) or (arr[1]==("X") and arr[4]==("X") and arr[7]==("X")) or (arr[2]==("X") and arr[5]==("X") and arr[8]==("X")) :
      print ("\n<< player 1 wins >>")
      i=10
    elif (arr[0]==("O") and arr[1]==("O") and arr[2]==("O")) or (arr[3]==("O") and arr[4]==("O") and arr[5]==("O")) or (arr[6]==("O") and arr[7]==("O") and arr[8]==("O")) or (arr[0]==("O") and arr[4]==("O") and arr[8]==("O")) or (arr[2]==("O") and arr[4]==("O") and arr[6]==("O")) or (arr[0]==("O") and arr[3]==("O") and arr[6]==("O")) or (arr[1]==("O") and arr[4]==("O") and arr[7]==("O")) or (arr[2]==("O") and arr[5]==("O") and arr[8]==("O")) :
      print ("\n<< player 2 wins >>")
      i=10
    elif i==10 :
      print ("\n<< DRAW >>")
  print ("Do you want to play again? (yes or no)") 
  play=str(input())
  if play==("yes") :
    continue
  else :
    break