import random

def role_dice():
    d1 = random.randint(1, 6);
    d2 = random.randint(1, 6);
    s = d1+d2;
    print('Dice 1 is ', d1 , '___ Dise 2 is ', d2, '___ The sum of dice is', s);
    return s;



def play():
    first_role = role_dice();
    #print(first_role)
    if first_role==7 or first_role==11:
        print('You Win');
    elif first_role==2 or first_role==3 or first_role==12:
        print('Casino Win');
    else:
        print('Goal numer - ', first_role);

        while True:
            current_role = role_dice()
            if current_role == first_role:
                print('You Win');
                break;
            elif current_role == 7:
                print('Casino Win');
                break;

play();

