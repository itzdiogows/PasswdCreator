import random
import colorama

BLUE = '\033[94m'

print("""

{0}                               ,-.
{0}                               ( O_)
{0}                              / `-/
{0}                             /-. /
{0}                            /   )
{0}                           /   /  
{0}              _           /-. /
{0}             (_)*-._     /   )
{0}               *-._ *-'**( )/    
{0}                   *-/*-._* `. 
{0}                    /     *-.'._
{0}                   /\       /-._*-._
{0}    _,---...__    /  ) _,-*/    *-(_)
{0}___<__(|) _   **-/  / /   /
{0} '  `----' **-.   \/ /   /
{0}               )  ] /   /
{0}       ____..-'   //   /                       )
{0}   ,-**      __.,'/   /   ___                 /,
{0}  /    ,--**/  / /   /,-**   ***-.          ,'/
{0} [    (    /  / /   /  ,.---,_   `._   _,-','
{0}  \    `-./  / /   /  /       `-._  *** ,-'
{0}   `-._  /  / /   /_,'            **--*
{0}       */  / /   /*         
{0}       /  / /   /
{0}      /  / /   /  
{0}     /  |,'   /  
{0}    :   /    /
{0}    [  /   ,'     ~>Passwd Generator<~
{0}    | /  ,'    
{0}    |/,-'
{0}    '
""".format(BLUE))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}&#%*!?$-+_"

all = lower + upper + number + symbol

a = int(input("\033[94m\033[1m[*]\033[0m Number of characters you want in the password: "))
b = int(input("\033[94m\033[1m[*]\033[0m How many passwords do you want to create: "))

for n in range(b):
	print("\033[94m\033[1m[*]\033[0m The password you generated is: " + "".join(random.sample(all,a)))
else:
	print("\033[94m\033[1m[*]\033[0m Finish")
