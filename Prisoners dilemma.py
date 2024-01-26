# Evolution of Trust - Population Simulation
import random as r

# Cutoffs

ch_ch = 0 # both cheats
co_ch = 1 # one of them cooperates, other cheats (value given for cooperator)
ch_co = 3 # one of them cheats, other cooperates (value given for cheater)
co_co = 2 # both cooperates

# Strategies


def always_coop(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Always Cooperate"
    return "Cooperate"
    
def always_cheat(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Always Cheat"
    return "Cheat"
    
def copycat(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Copycat"
    if li == []:
        return "Cooperate"
    else:
        return li[len(li)-1]

def grudger(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Grudger"
    
    if li == []:
        return "Cooperate"
    else:
        if "Cheat" in li:
            return "Cheat"
        else:
            return "Cooperate"

def detective(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Detective"
    if li == []:
        return "Cooperate"
    elif cround == 2:
        return "Cheat"
    elif cround == 3:
        return "Cooperate"
    elif cround == 4:
        return "Cooperate"
    else:
        if fp == detective:
            incr = 1
        else:
            incr = 0
            
        li_search = []
        for i in range(8+incr, len(li), 2):
            li_search.append(li[i])
        if li_search == [] or "Cheat" not in li_search:
            return always_cheat(li, fp, cround)
        else:
            return copycat(li, fp, cround)

def copykitten(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Copykitten"
    if li == []:
        return "Cooperate"
    else:
        if li[len(li)-1] == "Cheat" and li[len(li)-3] == "Cheat":
            return "Cheat"
        else:
            return "Cooperate"

# My favorite - THE SIMPLETONNN !!!

def simpleton(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Simpleton"
    if li == []:
        return "Cooperate"
    else:
        if li[len(li)-1] == "Cooperate":
            return li[len(li)-2]
        else:
            if li[len(li)-2] == "Cooperate":
                return "Cheat"
            else:
                return "Cooperate"

def random(li, fp, cround):
    if li == 0 and fp == 0 and cround == 0:
        return "Random"
    a = r.randrange(0, 100)
    if a < 50:
        return "Cooperate"
    else:
        return "Cheat"

# Matchmaking function

def match(s1, s2, rounds): # for 'detective' purposes, there will be atleast 10 rounds
    li = []
    score1 = 0
    score2 = 0
    
    for i in range(1, rounds+1):
        m1 = s1(li, s1, i)
        m2 = s2(li, s1, i)
        li.append(m1)
        li.append(m2)
        
        if m1 == "Cheat" and m2 == "Cheat":
            score1 += ch_ch
            score2 += ch_ch
        
        elif m1 == "Cheat" and m2 == "Cooperate":
            score1 += ch_co
            score2 += co_ch
        
        elif m1 == "Cooperate" and m2 == "Cheat":
            score1 += co_ch
            score2 += ch_co
        
        else:
            score1 += co_co
            score2 += co_co
    
    if score1 > score2:
        winner = s1(0, 0, 0)
    elif score2 > score1:
        winner = s2(0, 0, 0)
    else:
        winner = "Tie"
        
    return score1, score2, winner

Always_cheat = 15
Always_coop = 15
Copycat = 14
Grudger = 10
Detective = 20
Copykitten = 19
Simpleton = 200
Pizza_taco = 11

li = [always_coop, always_cheat, copycat, grudger, detective, copykitten, simpleton, random]
r.shuffle(li)

# Tournament Function - Audience vs Strategy

rounds = 10
grand_total = 0
wins = 0

for s in li:

    score1 = 0
    score2 = 0
    li_2 = []

    for i in range(1, rounds+1):
        my_move = str(input("Cooperate or Cheat?: "))
        s_move = s(li_2, s, i)
        
        li_2.append(s_move)
        li_2.append(my_move)
        
        print("Your opponent played:", s_move)
        
        if my_move == "Cheat" and s_move == "Cheat":
            score1 += ch_ch
            score2 += ch_ch
            print("You get", ch_ch, "points!")
        
        elif my_move == "Cheat" and s_move == "Cooperate":
            score1 += ch_co
            score2 += co_ch
            print("You get", ch_co, "points!")
        
        elif my_move == "Cooperate" and s_move == "Cheat":
            score1 += co_ch
            score2 += ch_co
            print("You get", co_ch, "points!")
        
        else:
            score1 += co_co
            score2 += co_co
            print("You get", co_co, "points!")
        
        print("----------")
    
    grand_total += score1
    if score1 > score2:
        print("You win against this bot!")
        wins += 1
    elif score1 < score2:
        print("You lost against this bot!")
    else:
        print("You have a tie against this bot!")
        wins += 0.5

print("Your overall score is:", grand_total + 16*wins)

# Tournament Function - Strategy vs Strategy
# To be completed
