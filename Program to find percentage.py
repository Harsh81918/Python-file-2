print("This a program to find your total marks and percentage.");
print("Press enter after entering marks.");
e=input("Your English marks:-");
h=input("Your Hindi marks:-");
Sa=input("Your 3l marks:-");
Sc=input("Your Science marks:-");
m=input("Your Maths marks:-");
so=input("Your Social Science marks:-");
max=str(float(e)+float(h)+float(Sa)+float(Sc)+float(m)+float(so));
per=(float(e)+float(h)+float(Sa)+float(Sc)+float(m)+float(so))/240*100;
print("Your total marks is:-"+max);
print("And your percentage is:-"+str(per));