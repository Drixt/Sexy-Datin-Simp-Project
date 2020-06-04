# The script of the game goes in this file.



# Declare characters used by this game. The color argument colorizes the

# name of the character.

 

define e = Character("C_person", color="#800000") 

define mc = Character("Player", color="#FF00FF")

##########################################################################################################

#

# Labels for each day

label start:
    stop music

label Monday:

    "Monday morning, you struggle to open your eyes and your body feels sluggish because you made the choice to play a video game until the sun seeped through your blinds and the birds were chirping ever so loud."

    mc "Stupid birds and their self-centered chirping."
    
    "You manage to pull yourself out of bed and take a look around. Yup, same old room with the same old, uncomfortable bed. You do your daily morning routine as a guy."
    
    "Done in 5 minutes."
    
    "You pick up your bag and take a look out the window. Your childhood friend lives right next to you and has lived next to you for the past 15 years. You have fond memories of each other and even more memories of her coming to you in need. She’s kind of like the little sister you never had."
    
    "Wait a second, her blinds aren’t open. She’s always had a bad habit of sleeping in."
    
    mc "There’s just no way. Not after I yelled at her last time."

    call CC1
    
    "A few minutes pass and the door swings wide open. A short girl with brown hair and hazel eyes walks out in her school uniform. With her bag in hand she gives you a warm smile."
    
    e "Good morning!"
    
    mc "Come on, we're gonna be late, June."
    
    e "Wow, you won't even say it back. You used to be so kind!"
    
    "You shrug your eyes and start to walk, leaving your childhood friend behind. Her name is June and you’ve known her since the 3rd grade when she moved into the house beside you. She’s a year younger but you constantly find yourself having to clean up after her mistakes. It doesn’t help that she’s clumsy too."
    
    "She’s been dependent on you ever since her parents have been travelling around the world but you politely accepted since they’ve taken care of you as well.  But the least she could do is wake up on time."
    
    e "Psst, why are you so quiet? Is something wrong?"
    
    call CC2 

    "As you turn a corner you can hear the faint sounds of your friend in slight pain but you can tell she’s more annoyed than upset."

    "You make it to class on time, but you can’t say for sure about June. You take your seat in class 3-B behind a girl with short black hair. The school president gives a speech to your class before the day begins."
     
    "Something about exams coming up and to uphold the prestigious record of our school. Nothing you really care about."
    
    "The day trudges by. Each class feels longer than the last. Every period that has passed by a teacher has announced a major test this thursday."
    
    "Why would 3 teachers want tests on the same day? Can’t they coordinate this better? Do they hate you or something?"
    
    "The one part of the day that you don’t completely hate finally arrives."
    
    "Lunch."
    
    "You take a seat with your friends and talk about the cool new video game that you played all weekend. The graphics, the intriguing storyline and how much effort the devs put into it. Some good times."
    
    "Until tragedy knocked on the door of your classroom."
    
    "You take a look towards the door and notice that it’s June. You try to pretend to not look at her but she screams your name."
    
    "You let out a big sigh and walk on over to her."
    
    mc "What do you want?"
    
    e "Wow, first you kick me in my shins and now you’re giving me attitude. You’ll definitely get a girlfriend at this rate."
    
    "You stand there in shock, she actually said that to you."
    
    e "You know how I woke up late this morning?"
    
    mc "Yes, I’m familiar. I woke you up."
    
    e "No! I just so happened to wake up after you decided to help! Anyway, I forgot to pack lunch."
    
    mc "Not my problem, go buy something."
    
    e "Funny story, I also forgot my wallet."

    "She gives you a weak smile and lets out a sigh."
    
    call CC3
    
    "The end of the day couldn’t come any sooner. You can’t help but think of those 3 tests that are going to happen on Thursday. Which do you start studying for?"
    
    "You check your phone as you exit the school. A text from June, she’s got choir practice and won’t be able to walk home with you."
    
    "You’ve always admired her for the determination she possesses for anything art related. A step up among other singers, a Vincent VanGogh in modern times, a practitioner of dance. She’s always been diligent with these, you just wish she’d apply this effort to being less clumsy."
    
    "She leads the practices for the student choir, apparently some big school event is happening soon and they’ve been staying late to achieve perfection (or the closest thing to)."
    
    "Your walk home is normal and nothing out of the ordinary happens. You get home and crack open the books, these tests won’t study for themselves."

    return 

    

label Tuesday:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

label Wednesday:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

label Thursday:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

##########################################################################################################

#

# Labelsfor Choices for Main Girl_C



label CC1:

    $ choice = 0

    "This is choice number #1"

    

    menu:

        "1. Throw the stress ball on your desk AT HER WINDOW":

            $choice = 1

        "2. Call her cellphone":

            $choice = 2

        "3. Call her cellphone":

            $choice = 3



    if choice == 1:

        "You grab the used stress ball sitting on your desk and open your window." 

        "Take a couple of steps back, run up and throw the ball."

        "You’ve done this before, the window won’t break. The ball hits, and hits hard."

        mc"WAKE UP!!!"

        "You hear an audible thud and the blinds open slowly." 

        "You see your childhood friend in her pyjamas and freak out about oversleeping." 

        "Again..."

    elif choice == 2:

        "You grab your cell phone and ring her phone."

        "ㄴ phone ring sound ㄱ"

        "It rings for a while and finally she picks up."

        

        e "H-hello?"

        mc "Good morning, idiot. 

           It's currently 30 minutes before class starts and from the looks of it you just woke up. 

           Get it together, I won’t be here to wake you up forever."

        

    return 

    

label CC2:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

label CC3:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

label CC4:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

label CC5:



    e "j8q0jh3r9ha378a"



    "wa3q210391u203!"

    

    return 

    

##########################################################################################################

### End of Game

    return
