c='enter'
b='pet'
a='attack'
Z='go around'
Y='south'
X='north'
T='wait'
S='explore'
C=print
B=input
A=None
U=B('Enter your Name: ')
F=B(f"{U} You are in a forest, you can go north, east, south, or west, choose wisely: ")
d=X,Y
G=A
E=A
L=A
M=A
N=A
H=A
I=A
O=A
e=A
P=A
D=A
Q=A
J=A
R=A
K=A
V=A
W=A
if F.lower()==X:G=B('You find yourself outside a wooded mansion:You can explore, or go around')
f=S,Z
if F.lower()==T:C('Secret idiot ending')
if F.lower()=='east':D=B('You are met by a cliff, with a dog and a woman hanging, who do you save')
if F.lower()=='west':Q=B('You see a massive castle, with a great lake, do you go in or go north')
if Q is not A and Q.lower()=='go in':C('Ending 4/7 Harry potter ending');C(f"Your a wizard {U}")
if D is not A and D.lower()=='woman':C('wow you let a dog die, you monster. Im afriad i cant let you affect anymore lives')
if D is not A and D.lower()=='dog':C('You chose a dog over a human life, shame, SHAME')
if D is not A and D.lower()=='both':C('Ending 2/7 Hapily ever after')
if D is not A and D.lower()=='neither':C('Ending 3/7, War Crime Ending')
if G is not A and G.lower()==S:E=B('You open the gate and see a dog, do you grab a stick and try to atack it, do you wait for it to run off, or do you try to pet it');g=T,a,b
if E is not A and E.lower()==a:H=B('You now have rabies, do you continue or wait to die')
if H is not A and H.lower()=='wait to die':C('You lost in the most pitiful way ever, but at least you tried. GAME OVER')
if H is not A and H.lower()=='continue':I=B('You see a glowing orb do you pick it up or leave it')
if I is not A and I.lower()=='pick up':C('Congrats you found ending one of seven')
if I is not A and I.lower()=='leave it':O=B('You are thirsty, do you go inside or find a source of water outside')
if O is not A and O.lower()=='go inside':C('The owner of the home sees you, you are frothing at the mouth, "water" you say, he brings you to a medical table and you black out, (How did we get here ending)')
if G is not A and G.lower()==Z:L=B('You are met by the owner of the home, holding a sawed off shotgun. do you run or speak with him')
if L is not A and L.lower()=='run':N=B('He shoots you "stop"')
if N is not A and N.lower()=='stop':B('"what are you doing out here by yourself"')
if E is not A and E.lower()==b:h=B('Task succesfull, you now have a dog, do you enter the mansion, or go around it')
if F.lower()==Y:i=B('You are visciously ripped apart by a troll. Game Over')
if E is not A and E.lower()==T:M=B('You wait for 6 hours, it is nighttime, the dog leaves, do you enter the mansion or leave')
if M is not A and M.lower()==c:R=B('There is a man sleeping on the couch, right beside the couch is a 12 gauge sawed off shotgun, do you take the gun or explore the house more')
if R is not A and R.lower()=='take':J=B('what do you intend to do with that weapon')
if J is not A and J.lower=='shoot':C('You sick monster, fine, ending 7/7')
if J==S:K=B('Explore into the woods or keep exploring the house')
if K=='grab picture':V=B('A door opens on the right')
if V==c:W=B('you find your family, dead')
if W=='cry':C('You have found the secret ending, congrats')
if K=='explore house':C('You are eventually led outside where you fall asleep')
if K=='go into the woods':P=B('You storm off, you run, do you keep running')
if P=='yes':C('You fall into a masked ditch (to be continued)')
if P=='no':C('You stop and fall asleep, coma ending')
