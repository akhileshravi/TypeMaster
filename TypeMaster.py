
import textwrap, curses
from time import time,sleep
from random import choice,randint
from winsound import Beep as beep

def end_check(para):
    end = '<:>'
    if end in para[-4:]:
        return True
    else:
        return False

def nword(s,i):
    for j in xrange(i,len(s)):
        if s[j] == ' ':
            nw = s[i:j]
            psp1 = j+1
            break
    else:
        nw = s[i:]
        psp1 = len(s)
    return nw, psp1

def lin_col(s,st):
    l = len(s)
    nw = nword(s,st)[0] #Storing the the next word
    worr = 0
    lnw = len(nw)
    s1 = textwrap.fill(text=s, width=70, replace_whitespace=False)
    wo, lin, col = 0, 0, 0
    l1 = len(s1)
    for i in xrange(st):
        if s[i:i+lnw] == nw:
            worr += 1
    s2 = textwrap.fill(text=s[:st+lnw], width=70, replace_whitespace=False)
    l2 = len(s2)
    i = l2 - lnw -1
    b = True
    while i >= 0:
        if s2[i] == '\n':
            b = False
            lin+=1
        if b:
            col +=1
        i -= 1
    return lin,col

def point_text(y,x,lenn,style = 'bold'):
    r = ''
    i = 0
    if style != 'bold' and style != 'blink':
        while i < lenn:
            r = chr(randint(15,255))
            scr.addstr(y,x+i,r,curses.color_pair(randint(1,11)))
            i+=1
        scr.refresh()
    elif style == 'blink':
        while i < lenn:
            r = chr(randint(15,255))
            scr.addstr(y,x+i,r,curses.color_pair(randint(1,11))|curses.A_BLINK)
            i+=1
        scr.refresh()
    else:
        while i < lenn:
            r = chr(randint(15,255))
            scr.addstr(y,x+i,r,curses.color_pair(randint(1,11))|curses.A_BOLD)
            i+=1
        scr.refresh()

def screen_fill():
    scr.clear()
    scr.refresh()
    notyet = []
    for i in xrange(1,24):
        for j in xrange(1,79):
            notyet.append([i,j])
    sp = ' '
    while notyet:
        for i in xrange(6):
            j = choice(notyet)
            a, b = j[0], j[1]
            i = randint(11,17)
            scr.addch(a,b,sp,curses.color_pair(i))
            notyet.remove([a,b])
        scr.refresh()
        sleep(0.001)

def super_space(y,x,lenn):
    r = ' '
    scr.addstr(y,x,r*lenn,curses.color_pair(randint(11,17)))
    scr.refresh()


def cool_text():
    y = 0
    while y<12:
        x = 0
        while x<80:
            point_text(y,x,9)
            point_text(24-y,70-x,9)
            if y > 3:
                super_space(y-4,70-x,9)
                super_space(24-y+4,x,9)
            scr.refresh()
            sleep(0.03)
            x += 10
        y += 1
    x = 0
    while x < 40:
        point_text(y,x,10)
        point_text(24-y,70-x,10)
        super_space(y-4,60-2*x,20)
        super_space(24-y+4,2*x,20)
        scr.refresh()
        sleep(0.03)
        x += 10
    y -=3
    while y<12:
        x = 0
        while x<80:
            super_space(y,70-x,10)
            super_space(24-y,x,10)
            scr.refresh()
            sleep(0.03)
            x += 10
        y += 1
    y = 12
    x = 0
    while x < 40:
        super_space(y,x,10)
        super_space(24-y,70-x,10)
        scr.refresh()
        sleep(0.03)
        x += 10
    sleep(1)

def randword(lenn):
    i,rw = 0,''
    while i<lenn:
        rw += chr(randint(15,255))
    return rw

def user_line(user):
    c = 1
    for i in user:
        if i == '\n':
            c+=1
    return c

def explosion():
    i,y = 0,12
    c1,c2 = chr(41),chr(40) #left right
    scr.addch(y,i,c1,curses.color_pair(6)|curses.A_BOLD)
    scr.addch(y,79-i,c2,curses.color_pair(6)|curses.A_BOLD)
    scr.refresh()
    sleep(0.02)
    i+=1
    c3,c4 = '<','>' #left right
    c5 = '#' # top bottom
    c6 = 'o' #diagonal
    c7 = 'H'
    scr.addch(y,i,c1,curses.color_pair(6)|curses.A_BOLD)
    scr.addch(y,79-i,c2,curses.color_pair(6)|curses.A_BOLD)
    scr.addch(y,i-1,c7,curses.color_pair(7)|curses.A_BOLD)
    scr.addch(y,79-i+1,c7,curses.color_pair(7)|curses.A_BOLD)
    scr.refresh()
    sleep(0.02)
    i+=1

    while i < 40:
        scr.addch(y,i,c1,curses.color_pair(6)|curses.A_BOLD)
        scr.addch(y,79-i,c2,curses.color_pair(6)|curses.A_BOLD)
        scr.addch(y,i-1,c7,curses.color_pair(7)|curses.A_BOLD)
        scr.addch(y,79-i+1,c7,curses.color_pair(7)|curses.A_BOLD)
        scr.refresh()
        sleep(0.03)
        i+=1
    scr.addstr(12,0,' '*80)
    scr.addch(y,39,c1,curses.color_pair(6)|curses.A_BOLD)
    scr.addch(y,40,c2,curses.color_pair(6)|curses.A_BOLD)
    scr.refresh()
    sleep(0.04)
    #scr.clear()
    scr.refresh()
    x = 39
    
    scr.addch(12,x,c3,curses.color_pair(8)|curses.A_BOLD)  #left
    scr.addch(y,x,c6,curses.color_pair(9)|curses.A_BOLD)  #top left
    scr.addch(y,39,c5,curses.color_pair(2)|curses.A_BOLD)  #top
    scr.addch(y,79-x,c6,curses.color_pair(9)|curses.A_BOLD)  #top right
    scr.addch(12,79-x,c4,curses.color_pair(8)|curses.A_BOLD)  #right
    scr.addch(24-y,79-x,c6,curses.color_pair(9)|curses.A_BOLD)  #bottom right
    scr.addch(24-y,39,c5,curses.color_pair(2)|curses.A_BOLD)  #bottom
    scr.addch(24-y,x,c6,curses.color_pair(9)|curses.A_BOLD)  #bottom right
    scr.refresh()
    sleep(0.08)
    y-=1
    x-=3
    while y >= 0:
        if y == 7:
            v = 0
            while v < lg:
                scr.addstr(12,30+2*v,game[v],curses.color_pair(game_col[v])|curses.A_BOLD)
                scr.refresh()
                v+=1
            scr.addstr(14,34,'AKHIL - ESH',curses.color_pair(2)|curses.A_BOLD)
        if y > 3:
            scr.addstr(y-3,x-9,' '*((40-x+9)*2))
            scr.addstr(24-y+3,x-9,' '*((40-x+9)*2))
            scr.addstr(y-2,0,' '*80)
            scr.addstr(24-y+2,0,' '*80)
            scr.refresh()
        elif y==3:
            scr.addstr(1,0,' '*80)
            scr.addstr(23,0,' '*80)
            scr.refresh()
        scr.addch(12,x,c3,curses.color_pair(8)|curses.A_BOLD)  #left
        scr.addch(12,x+3,' ')
        scr.addch(y,x,c6,curses.color_pair(9)|curses.A_BOLD)  #top left
        scr.addch(y+1,x+3,' ')
        scr.addch(y,39,c5,curses.color_pair(2)|curses.A_BOLD)  #top
        scr.addch(y+1,39,' ')
        scr.addch(y,79-x,c6,curses.color_pair(9)|curses.A_BOLD)  #top right
        scr.addch(y+1,79-x-3,' ')
        scr.addch(12,79-x,c4,curses.color_pair(8)|curses.A_BOLD)  #right
        scr.addch(12,79-x-3,' ')
        scr.addch(24-y,79-x,c6,curses.color_pair(9)|curses.A_BOLD)  #bottom right
        scr.addch(24-y-1,79-x-3,' ')
        scr.addch(24-y,39,c5,curses.color_pair(2)|curses.A_BOLD)  #bottom
        scr.addch(24-y-1,39,' ')
        scr.addch(24-y,x,c6,curses.color_pair(9)|curses.A_BOLD)  #bottom left
        scr.addch(24-y-1,x+3,' ')
        scr.refresh()
        sleep(0.08)
        y-=1
        x-=3
    sleep(0.3)
    scr.clear()
    scr.refresh()


scr = curses.initscr()
scr.keypad(1)
curses.noecho()
curses.cbreak()
curses.start_color()
scr.nodelay(0)
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLUE) #For Errors
curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK) #green - 2
curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLUE)
curses.init_pair(4,curses.COLOR_BLUE,curses.COLOR_CYAN)
curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK) #magenta - 5
curses.init_pair(6,curses.COLOR_CYAN,curses.COLOR_BLACK) #cyan - 6
curses.init_pair(7,curses.COLOR_BLUE,curses.COLOR_BLACK) #blue - 7
curses.init_pair(8,curses.COLOR_RED,curses.COLOR_BLACK) #red - 8
curses.init_pair(9,curses.COLOR_YELLOW,curses.COLOR_BLACK) #yellow - 9
curses.init_pair(10,curses.COLOR_WHITE,curses.COLOR_BLACK) #white - 10
curses.init_pair(11,curses.COLOR_BLACK,curses.COLOR_WHITE) #black - 11, b - white
curses.init_pair(12,curses.COLOR_BLACK,curses.COLOR_GREEN) #b green - 12
curses.init_pair(13,curses.COLOR_BLACK,curses.COLOR_BLUE) #b - blue - 13
curses.init_pair(14,curses.COLOR_BLACK,curses.COLOR_YELLOW) #b - yellow - 14
curses.init_pair(15,curses.COLOR_BLACK,curses.COLOR_RED) #b - red - 15
curses.init_pair(16,curses.COLOR_BLACK,curses.COLOR_MAGENTA) #b - magenta - 16
curses.init_pair(17,curses.COLOR_BLACK,curses.COLOR_CYAN) #b - cyan - 17
curses.curs_set(0)
curses.cbreak()
curses.noecho()

cha = 1
game = 'TYPEMASTER'
lg=len(game)
game_col = (6,2,9,8,5,6,2,9,8,5)
end = '<:>'
paras = ['The Indian roller, Coracias benghalensis, is a member of the roller family of birds. They are found widely across tropical Asia stretching from Iraq eastward across the Indian Subcontinent to Indochina. The male shows aerobatic displays during the breeding season.',
         'The Jana Gana Mana is the national Anthem of India, composed by Rabindranath Tagore. It was officially adopted by the constituent Aseembly as the Indian national anthem on January 24, 1950.',
         'Bankim Chandra Chatterji\'s composed song "Vande Mataram" was adopted as the National Song. It has an equal status with "Jana Gana Mana". It was first sung in the 1896 session of the Indian National Congress.',
         'Tiger is the National Animal of India. It is symbol of India\'s wildlife wealth. The magnificent tiger, Panthera tigris, is a striped animal.',
         'The Peacock, Pavo cristatus, is the national bird of India. Emblematic of qualities such as beauty grace, pride.',
         'Mango is the national fruit of India. Described as the "Food of the Gods", in the sacred Vedas, the fruit is grown almost in all parts of India.',
         'Lotus botanically known as the Nelumbo Nucifera is the national flower of India.',
         'Banyan Tree is the National Tree of India. This huge tree towers over its neighbours and has the widest reaching roots of all known trees.',
         'The Saka calender is the national calender of India. It is used, alongside the Gregorian calender.',
         "Constantly throbbing and pulsating, the human brain rapidly forms opinions; attaining an ability of its own; a fact which is startlingly shown by an occasional child \"prodigy\" in music or school work. And as, with our dumb animals, a child's inability convincingly to impart its thoughts to us, should not class it as ignorant.",
         'India\'s Hindu calendar has 6 seasons: spring, summer, monsoon, autumn, winter and prevernal.',
         "An Indian man claims he hasn't eaten or drunk for 70 years. After many tests, doctors still don't know how it's possible.",
         'The world\'s biggest family lives together in India: a man with 39 wives and 94 children. "Anal" is a language spoken in India and Burma by 23,000 people.',
         'Police officers in one state in India are given a slight pay upgrade for having a moustache.',
         'India has the world\'s lowest meat consumption per person. In West Bengal, India, cows must have a Photo ID Card.',
         '70% of all the world\'s spices come from India. India has more population than the entire Western Hemisphere of Earth.'
         "A bear has 42 teeth! An ostrich's eye is bigger than it's brain! lemons contain more sugar than strawberries! Reindeer like bananas!",
         "A lobster's blood is colorless but when exposed to oxygen it turns blue. The longest recorded flight of a chicken was 13 seconds.",
         "Birds need gravity to swallow. A cat has 32 muscles in each ear. Cats spend 66% of their life asleep. When lightning strikes it can reach up to 30,000 degrees celsius 54,000 degrees fahrenheit",
         "Goldfish can see both infrared and ultraviolet light! The only continent with no active volcanoes is Australia. Koalas sleep around 18 hours a day.",
         "All insects have 6 legs. Spiders are arachnids and not insects. African Grey Parrots have vocabularies of over 200 words!",
         "Lightning strikes the Earth 6,000 times every minute. Fire usually moves faster uphill than downhill! Camel's milk doesn't curdle.",
         "Cats have over 100 vocal chords. Frogs can't swallow with their eyes open. Frogs don't drink. They absorb water through their skin.",
         "Elephants are the only mammal that can't jump. It's possible to lead a cow up stairs but not down! At birth dalmations are always white. A duck can't walk without bobbing its head.",
         "A hummingbird's heart beats at over a 1,000 times a minute. Dragonflies have 6 legs but can't walk. A crocodile can't move its tongue!",
         "India is a GREAT country. It has given us so much that it is extremely hard to list out all what it has given us. We must be THANKFUL and in return, we must serve Mother India.",
         "India is rich in history, culture, heritage, written texts which have invaluable knowledge and principles for life, philosophy and so on. We must do our bit in preserving all this."]
sleep(0.25)
screen_fill()
sleep(0.25)
for i in range(10,15):
    scr.addstr(i,0,' '*80)
scr.refresh()
explosion()
sleep(0.25)
c1,c2 = chr(41),chr(40) #left right
exits =False
point = 1
while exits == False:
    
    scr.clear()
    scr.refresh()
    if cha == 1:
        for i in range(lg):
            scr.addstr(7,30+2*i,game[i],curses.color_pair(game_col[i])|curses.A_BOLD)
            scr.refresh()
            sleep(0.2) ###
        sleep(0.2)
    else:
        i = 0
        while i < lg:
            scr.addstr(7,30+2*i,game[i],curses.color_pair(game_col[i])|curses.A_BOLD)
            i+=1
        scr.refresh()
    point_text(1,2,76,'not bold')
    point_text(2,2,76,'not bold')
    scr.addstr(3,2,'_'*76,curses.color_pair(10)|curses.A_BOLD)
    scr.addstr(11,34,'>  PLAY  <',curses.color_pair(10)|curses.A_BOLD)
    scr.addstr(13,31,'> INSTRUCTIONS <',curses.color_pair(10)|curses.A_BOLD)
    scr.addstr(15,34,'>  EXIT  <',curses.color_pair(10)|curses.A_BOLD)
    scr.addstr(20,5,'Press SPACEBAR to select',curses.color_pair(2)|curses.A_BOLD)
    scr.addstr(11,11,' '*13)
    scr.addstr(11,54,' '*13)
    scr.addstr(13,11,' '*13)
    scr.addstr(13,54,' '*13)
    scr.addstr(15,11,' '*13)
    scr.addstr(15,54,' '*13)
    scr.refresh()
    if point == 1:
        scr.addstr(11,30,'>      PLAY      <',curses.color_pair(9)|curses.A_BOLD)
        scr.addstr(20,50,"Let's have some fun!!!",curses.color_pair(10)|curses.A_BOLD)
        i = 0
        while i < lg:
            scr.addstr(11,11+i,c1,curses.color_pair(game_col[i])|curses.A_BOLD)
            scr.addstr(11,54+i,c2,curses.color_pair(game_col[lg-1-i])|curses.A_BOLD)
            i+=1
        scr.refresh()
    elif point == 2:
        scr.addstr(13,30,'>  INSTRUCTIONS  <',curses.color_pair(9)|curses.A_BOLD)
        scr.addstr(20,50,"You can't play without",curses.color_pair(10)|curses.A_BOLD)
        scr.addstr(21,50,"knowing how to",curses.color_pair(10)|curses.A_BOLD)
        i = 0
        while i < lg:
            scr.addstr(13,11+i,c1,curses.color_pair(game_col[i])|curses.A_BOLD)
            scr.addstr(13,54+i,c2,curses.color_pair(game_col[lg-1-i])|curses.A_BOLD)
            i+=1
        scr.refresh()
    elif point == 3:
        scr.addstr(15,30,'>      EXIT      <',curses.color_pair(9)|curses.A_BOLD)
        scr.addstr(20,60,"BYE BYE",curses.color_pair(10)|curses.A_BOLD)
        i = 0
        while i < lg:
            scr.addstr(15,11+i,c1,curses.color_pair(game_col[i])|curses.A_BOLD)
            scr.addstr(15,54+i,c2,curses.color_pair(game_col[lg-1-i])|curses.A_BOLD)
            i+=1
        scr.refresh()
    curses.curs_set(0)
    Quit = True
    check = (ord('q') , ord('Q'))
    i = 0
    z = scr.getch()    
    if z == 258: #down
        if point < 3:
            point += 1
    elif z == 259: #up
        if point > 1:
            point -= 1
    elif z == ord(' '):
        if point == 1:
            Quit = False    
            while Quit == False:
                scr.clear()
                scr.refresh()
                v = 0
                while v < lg:
                    scr.addstr(0,2*v,game[v],curses.color_pair(game_col[v])|curses.A_BOLD)
                    scr.refresh()
                    v+=1
                s,wor=0,0
                init_lin = 2
                para = choice(paras)
                para1 = textwrap.fill(text=para, width=70, replace_whitespace=False)
                user, mistake='', 0
                lpara = len(para)
                lp, lu = len(para1), len(user)
                scr.addstr(2,0,para1,curses.color_pair(2)|curses.A_BOLD)
                scr.refresh()
                sleep(0.25)
                y, x = 5, 0
                line, lp1 = 0, len(para1)
                sp = 0
                           
                nw,psp = nword(para,0)

                i = 0
                tot_lin = 0
                while i<lp:
                    if para1[i]=='\n':
                        tot_lin+=1
                    i+=1

                scr.addstr(4+tot_lin,0,'Press any key to start.',curses.color_pair(5)|curses.A_BOLD)
                a = scr.getch()
                scr.addstr(20,2,'BACKSPACES and ARROW KEYS are NOT allowed',curses.color_pair(8)|curses.A_BOLD)
                scr.addstr(22,2,'SPACES will NOT appear on the screen',curses.color_pair(6)|curses.A_BOLD)
                scr.addstr(23,2,'Press SPACE after a MISTAKE and retype',curses.color_pair(2)|curses.A_BOLD)
                scr.addstr(21,47,'Press SPACE after you are done',curses.color_pair(10)|curses.A_BOLD)
                scr.addstr(23,47,'Type \'<:>\' to go to main menu.',curses.color_pair(9)|curses.A_BOLD)
                scr.addstr(4+tot_lin,0,' '*25)
                scr.refresh()
                scr.addstr(4+tot_lin,0,' '*25)
                scr.refresh()
                psp0 = 0
                nw0=''
                lin,col=0,0
                lin0,col=init_lin,0
                Quit = False
                scr.addstr(init_lin,0,nw,curses.color_pair(3)|curses.A_BOLD)
                scr.addch(3+tot_lin,78,'\n')
                curses.curs_set(1)
                t1 = time()
                user1 = textwrap.fill(text=user, width=70, replace_whitespace=False)
                while not end_check(user):
                    uline = user_line(user1)
                    for i in range(uline+1):
                        scr.addstr(3+tot_lin+i,0,' '*80)
                    scr.addstr(4+tot_lin,0,user1,curses.color_pair(10)|curses.A_BOLD)
                    scr.refresh()
                    
                    a = scr.getch()
                    if 30<= a <= 255:
                        ch =chr(a)
                        if ch <> '\b':
                            user += ch
                        lu = len(user)
                        user1 = textwrap.fill(text=user, width=70, replace_whitespace=False)
                        scr.addstr(4+tot_lin,0,user1,curses.color_pair(10)|curses.A_BOLD)
                        scr.refresh()
                        if ch == ' ':
                            word = user[sp:-1]
                            if word == nw:
                                if psp<lpara:
                                    psp0=psp
                                    nw0=nw
                                    lin0,col0=lin,col
                                    lin, col = lin_col(para,psp)
                                    nw, psp = nword(para,psp)
                                    scr.addstr(init_lin+lin0,col0,nw0,curses.color_pair(4))
                                    scr.addstr(init_lin+lin,col,nw,curses.color_pair(3)|curses.A_BOLD)
                                else:
                                    scr.addstr(init_lin+lin,col,' '*len(nw),curses.color_pair(4))
                                    scr.refresh()
                                    scr.addstr(init_lin+lin,col,nw,curses.color_pair(4))
                                    scr.refresh()
                                    break

                            else:
                                mistake +=1
                                scr.addstr(init_lin+lin,col,nw,curses.color_pair(1)|curses.A_BOLD)
                                scr.addstr(4+tot_lin,0,user1,curses.color_pair(10)|curses.A_BOLD)
                                scr.refresh()
                                beep(5000,1000)
                            
                            sp = lu #Storing the index of the character after the last space
                                      #(starting index of next word in 'user')
                        scr.addstr(tot_lin+init_lin+1,0,user)
                else:
                    Quit = True
                    point = 1
                curses.curs_set(0)
                if not Quit:
                    t = time()-t1
                    no_word = 1
                    i = 0
                    while i<lp1:
                        if para[i] == ' ':
                            no_word += 1
                        i+=1
                    tim_per_wor = round((t/no_word),3)
                    tim_per_ch = round((t/len(para)),3)
                    for i in range(5):
                        scr.addstr(20+i,0,' '*79)
                    scr.addstr(20,2,'You have SUCCEEDED!!!',curses.color_pair(9)|curses.A_BOLD)
                    scr.refresh()
                    sleep(1)
                    scr.clear()
                    i = 0
                    while i < lg:
                        scr.addstr(0,2*i,game[i],curses.color_pair(game_col[i])|curses.A_BOLD)
                        scr.refresh()
                        i+=1
                    data = ['Number of mistake(s): '+str(mistake),
                            'Time per word: '+str(tim_per_wor)+' Seconds',
                            'Time per character: '+str(tim_per_ch)+' Seconds']
                    i = 0
                    tup = (9,6,10)
                    while i<3:
                        scr.addstr(2*i+3,1,data[i],curses.color_pair(tup[i])|curses.A_BOLD)
                        scr.refresh()
                        i+=1
                    scr.addstr(21,45,'Press q or Q to go to main menu.',curses.color_pair(2)|curses.A_BOLD)
                    Quit = False
                    while not Quit:
                        v = scr.getch()
                        if v == check[0] or v == check[1]:
                            Quit = True
                            point = 1
        elif point == 2:
            scr.clear()
            scr.refresh()
            v = 0
            while v < lg:
                scr.addstr(0,2*v,game[v],curses.color_pair(game_col[v])|curses.A_BOLD)
                scr.refresh()
                v+=1
            scr.addstr(2,1,game,curses.color_pair(6)|curses.A_BOLD)
            scr.addstr(2,12,' is a typing game.',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(4,1,'The given text should be typed by you.',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(5,1,'The entered text is checked word by word.',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(6,1,'The word to be typed will be highlighted as shown below.',curses.color_pair(8)|curses.A_BOLD)
            scr.addstr(7,5,'word',curses.color_pair(3)|curses.A_BOLD)
            scr.addstr(9,1,'BACKSPACE ',curses.color_pair(9)|curses.A_BOLD)
            scr.addstr(9,10,' is NOT ALLOWED!!',curses.color_pair(9)|curses.A_BOLD)
            scr.addstr(10,1,'If there is a mistake, then you MUST RETYPE the word',curses.color_pair(8)|curses.A_BLINK)
            scr.addstr(11,1,'The wrong word will be highlighted as follows:',curses.color_pair(6)|curses.A_BOLD)
            scr.addstr(12,5,'word',curses.color_pair(1)|curses.A_BOLD)
            scr.addstr(14,1,'If you make a mistake, then press space and retype the word.',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(15,1,'If you continue after a mistake without retyping it,',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(16,1,'then it will be counted as another mistake.',curses.color_pair(10)|curses.A_BOLD)
            scr.addstr(18,1,'Press SPACE when you are done.',curses.color_pair(3)|curses.A_BOLD)
            scr.addstr(19,1,"Type '<:>' then space to go to menu during the game.",curses.color_pair(6)|curses.A_BOLD)
            scr.addstr(22,45,'Press q or Q to go to main menu.',curses.color_pair(2)|curses.A_BOLD)
            
            scr.addch(20,0,'\n')
            Quit = False
            while not Quit:
                v = scr.getch()
                if v == check[0] or v == check[1]:
                    Quit = True
            point,z = 1,-1
        elif point == 3:
            break
        
    scr.clear()
    scr.refresh()
    cha = 2
scr.clear()
indi = textwrap.fill(text=paras[-2], width=65, replace_whitespace=False)
ind = []
pp = 0
for i in range(len(indi)):
    if indi[i] == '\n':
        ind.append(indi[pp:i])
        pp = i+1
ind.append(indi[pp:])
indc = (8,10,2)
for i in range(3):
    scr.addstr(3+2*i,10,ind[i],curses.color_pair(indc[i])|curses.A_BOLD)
scr.refresh()
sleep(7)
scr.clear()
scr.refresh()
scr.addstr(10,33,'A Project By:')
scr.addstr(12,34,'AKHIL - ESH',curses.color_pair(2)|curses.A_BOLD)
scr.refresh()
sleep(1)
cool_text()
curses.nocbreak()
scr.keypad(0)
curses.echo()
curses.endwin()
