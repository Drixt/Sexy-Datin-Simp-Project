# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    define char1 = Character("Yuri")
    define mc = Character("[mc_name]")
    $ a = 0
    $ isgameover = False



# The game starts here.
label start:
    "This is world [a]..."
    if a == 3:
        "WELCOME TO FLAVOR TOWN!!!!!!"
        $ isgameover = True
        jump end
    
    python:
        mc_name = renpy.input(_("What's  your name?"))
        mc_name = mc_name.strip() or __("Default Name")
        
    # Show a background. 
    scene pooop

    # This shows a character sprite.
    show girl1

    # These display lines of dialogue.
    char1 "IM ALIVE!!!!!"
    char1 "Thank you, sir!!!"
    
    #To add the "name" you have to add "[]" int the string
    mc"Hi!, my name is [mc_name]"
    char1 "HI [mc_name]!"
    
    "Would you like to make a choice?"
    menu c1:
        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

    label choice1_yes:
        $ c1_flag = True
        char1 "This will loop your game"

        jump choice1_done

    label choice1_no:

        $ c1_flag = False
        char1 "OH? Really?"

        jump choice1_done

    label choice1_done:
        # ... the game continues here.
        #This is how you can give choice to the player
    if c1_flag:
        "Wagwan to the mandam"
        $ a += 1
        jump start
    else:
        "Fuck you sasuke! and your wack sandels"



# This ends the game.
    label end:
        return
