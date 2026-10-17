def minion_game(string):
    vowels = 'AEIOU'
    
    kev_score = 0
    stu_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kev_score += length - i
        else:
            stu_score += length - i
            
    if kev_score > stu_score:
        print(f"Kevin {kev_score}")
    elif stu_score > kev_score:
        print(f"Stuart {stu_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)