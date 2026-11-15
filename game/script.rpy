# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Alex")
define b = Character("Aster")
define s = Character("Polar")
define r = Character("Randy")
define w = Character("Radio")
define p = Character("Study Paper")
define sa = Character("Polar + Aster")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene spaceship

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "The Colony is a group of animal scientists tasked with a special mission."

    "They are space explorers, nearing the Holderplace galaxy, which is typically inhabited by friendly creatures."

    "They are soon to arrive on the snow planet Aluen to search for the fossils of a long-extinct alien species before returning home."

    show asternormal at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarnormalflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.8

# ypos 0.75 = speaker; ypos 8 = secondary

    b "Captain! How far are we from Aluen?"

    show asternormal at left:
        ypos 0.8
    show polarnormalflip at right:
        ypos 0.75

    s "Not far, Aster. We did well to make it through the journey, but there's a lot ahead."

    s "We'd best all be prepared."

    show asternormal at left:
        ypos 0.75
    show polarnormalflip at right:
        ypos 0.8

    b "We wouldn't be here if we weren't."

    show asternormal at left:
        ypos 0.8
    show polarnormalflip at right:
        ypos 0.75

    s "I'm serious. The last scientists abandoned the place for a reason."

    s "The wind and snow are more than we're built to handle."

    show asternormal at left:
        ypos 0.75
    show polarnormalflip at right:
        ypos 0.8

    b "You're right about that. I've never liked cold weather."

    b "The weather on Aluen is worse than anywhere back home. Many don't survive."

    b "It's lucky we're professionals. Still, it's not gonna be fun." 

    hide asternormal

    show randynormal at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    show polarnormalflip at right:
        ypos 0.8

    r "Hey Cap! I finished the engine repairs, we sho-"

    hide polarnormalflip

    show alexnormal at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show randynormal at left:
        ypos 0.8

    d "It's fine, I was juuust down there."

    hide alexnormal
    hide randynormal
    show alexnormalflip at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.8
    show polarangryflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    s "Hey! Randy was talking, you know. He can speak for himself."

    hide alexnormalflip
    show alexneutralflip at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarangryflip at right:
        ypos 0.8
    
    d "Yeesh, chill out! I just thought I'd say something."
    
    show alexneutralflip at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.8
    show polarangryflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    s "Well say something AFTER your crewmember is done speaking."

    show alexneutralflip at left:
        ypos 0.75
    show polarangryflip at right:
        ypos 0.8

    d "I just-"

    hide alexneutralflip
    show astershocked at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    
    b "POLAR! Is that Aluen? In the distance?"

    hide polarangryflip
    show polarshockedflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show astershocked at left:
        ypos 0.8

    s "Is it??"

    hide polarshockedflip
    hide astershocked

    "*Polar grabs the main console and looks out at the planet in front of her*"

    show polarhappyflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    s "It is! We're almost there!"

    hide polarhappyflip

    scene void:
        xzoom 10 yzoom 10

    "*The ship slows down as it approaches planet Aluen*"
    "*Polar is intensely focused on landing the ship. Everyone else is waiting tensely.*"
    "*Eventually, the ship lands safely. The crew cheers as the doors open."

    scene snow


    show polarhappy at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    s "We made it! Great job, team!"

    show randynormalflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarhappy at left:
        ypos 0.8

    r "All thanks to our great captain, Polar."

    show randynormalflip at right:
        ypos 0.8
    show polarhappy at left:
        ypos 0.75

    s "Aw, thanks, Randy."

    hide randynormalflip
    hide polarhappy
    show alexneutralflip at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarnormalflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.8

    d "Ahem."
    d "Ahem. Well."
    d "She shouldn't get ALL the credit, right?"

    show alexneutralflip at left:
        ypos 0.8
    show polarangryflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    hide polarnormalflip

    s "Excuse me??"

    hide alexneutralflip
    show alexshockedflip at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.8

    s "I haven't seen YOU do anything helpful here."
    s "ALL of your lives are in my hands. You're welcome, by the way. For not killing you."

    hide alexshockedflip
    show asternormal at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarangryflip at right:
        ypos 0.8
    
    b "It's okay, Polar. We can't risk you two having another fight when such a big mission is on the line."

    hide asternormal
    hide polarangryflip
    show asterangry at left:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show polarnormalflip at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.8

    b "Alex, you owe her an apology. Then, let's just forget about this."

    hide polarnormalflip
    show alexangry at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75
    show asterangry at left:
        ypos 0.8

    d "Fine."
    d "Fine. I'm sorry."

    hide asterangry
    hide alexangry
    show alexnormal at right:
        xzoom 0.35 yzoom 0.35
        ypos 0.75

    d "We need someone to guard the ship while we scout out the area for the lab."
    d "Polar, you're the captain. Who do you think should stay behind?"

    label guard_choice:
    menu:
        "Who should guard the ship?"

        "Aster":
            hide alexnormal
            show polarnormalflip at right:
                xzoom 0.35 yzoom 0.35
                ypos 0.75
            s "Aster should stay back. They're the smartest, and most capable."
            jump aster_guard_camp

        "Alex":
            hide alexnormal
            show polarnormalflip at right:
                xzoom 0.35 yzoom 0.35
                ypos 0.75
            s "Alex, you should guard the ship."
            jump alex_guard_camp

        "Randy":
            hide alexnormal
            show polarnormalflip at right:
                xzoom 0.35 yzoom 0.35
                ypos 0.75
            s "Randy. I trust him."
            jump randy_guard_camp

    label aster_guard_camp:
        show asternormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        show polarnormalflip at right:
            ypos 0.8
        b "Thank you, Polar. I won't let you down."

        hide polarnormalflip
        show asternormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        show randynormalflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        r "Good luck!"
        show asternormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        show randynormalflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        b "Thanks! Good luck on your patrol!"
        hide randynormalflip
        show asternormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        show randysadflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        r "Oh, and Aster?"
        r "Be safe, please...we don't know what's out there."
        hide randysadflip
        show asternormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        show randynormalflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        b "Don't worry about me, Randy. I promise I'll stay safe."

        scene lab:
            xzoom 2 yzoom 2
        show polarhappy at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        s "We found it! Let's go get As-"
        hide polarhappy
        show polarshocked at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        w "*chhhhkkk chhhhhhkkk*"
        show polarshocked at left:
            ypos 0.75
        s "Hold on- I'm getting a signal on the radio."
        s "Aster? Are you there?"
        show polarshocked at left:
            ypos 0.8
        w "*bzzt* Polar? Can you hear me?? Over."
        show polarshocked at left:
            ypos 0.75
        s "Aster? What's wrong? Over." 
        show polarshocked at left:
            ypos 0.8
        w "*bzzt* There's something here...I can hear it, it uses echolocation. Over."
        w "Please be- *bzzt* -careful. I don't know wh- *BzzZZZT- ZZZCCCHHHHKK*"
        show polarshocked at left:
            ypos 0.75
        s "Aster?? Are you there??"
        show polarshocked at left:
            ypos 0.8
        w "Stay there! I repeat, stay there! I'm coming to you! Over!"
        show randynormalflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        r "Polar? Is everything okay?"
        hide polarshocked
        show polarsad at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        show randynormalflip at right:
            ypos 0.8
        s "I'm not sure...Aster should be here soon, though."
        s "Let's be careful, though."
        hide randynormalflip
        show polarsad at left:
            ypos 0.8
        show randysadflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        r "Oh no! I hope they'll be alright..."
        show polarsad at left:
            ypos 0.75
        show randysadflip at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        s "It'll be fine, Randy. Aster is smart enough to survive."
        hide randysadflip
        hide polarsad
        show polarnormal at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.8
        show alexnormal at right:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        d "Polar? If Aster is being potentially chased, do you want me to stay by the door so I can close it when they come in?"
        menu:
            "Should Alex guard the door?"

            "Yes, it's the safest option.":
                d "Of course."
                hide alexnormal
                "*Alex goes to guard the door.*"
                "*Everyone else watches through the window. Aster is approaching from afar.*"
                "*Alex opens the door and Aster runs through. However, Alex struggles to close it.*"
                hide polarnormal
                show polarshocked at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.8
                "*The shape that was following Aster gets closer.*"
                "*In a panic, Alex slams his whole body against the door to close it.*"
                scene alexdeath
                "*The door finally closes, but a massive metal claw pierces through the door, stabbing Alex through the stomach.*"
                s "ALEX!!!!"
                "*The creature catches up. It cannot open the door, but Alex was left exposed.*"
                s "NO!!!"
                r "NO!!"
                r "Alex..."
                scene lab:
                    xzoom 2 yzoom 2
                show astersad at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                show randysadflip at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.8
                b "It's okay, Randy...it's okay...everything's gonna be okay..."
                show astersad at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.8
                show randysadflip at right:
                    ypos 0.75
                r "*sniff* I- I-"
                r "W-what do we do now..?"
                hide astersad
                show polardismay at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                show randysadflip at right:
                    ypos 0.8
                s "..."
                hide polardismay
                show polarsad at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                s "*sigh*"
                s "It'll be okay. We just have to bounce back."
                hide polarsad
                show polarhappy at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                s "Everything. Will be. Okay."
                show polarhappy at left:
                    ypos 0.8
                show randysadflip at right:
                    ypos 0.75
                r "..."
                hide randysadflip
                show randynormalflip at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                r "Thank you, Polar."
                hide polarhappy
                show polarnormal at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                s "We need to search the area. Let's split up."
                show polarnormal at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.8
                show randynormalflip at right:
                    ypos 0.75
                r "On it."
                hide randynormalflip
                show asternormalflip at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                b "On it."
                hide asternormalflip
                show polarnormal at left:
                    ypos 0.75
                s "Where should I search?"
                label search_choice2:
                menu:
                    "Where should I search?"

                    "In the drawers":
                        "*Polar checks through the drawers, ruffling through some study papers.*"
                        "*She stops on one of them, picking it up and reading it.*"
                        hide polarnormal
                        p "Experiment Logs: The Revival"
                        p "This experiment uses the fossil remains we found near the coast."
                        show polarshocked at left:
                            xzoom 0.35 yzoom 0.35
                            ypos 0.75
                        s "That's what I need!"
                        hide polarshocked
                        p "The fossil has the strange ability to regenerate itself when injured."
                        p "We wanted to see if we could integrate these regenerative abilities into a living creature."
                        p "However, the fossil was incomplete, so we created metal parts to complete it until we discover the full skeleton."
                        p "The life form is currently growing in one of the chambers."
                        show polarshocked at left:
                            xzoom 0.35 yzoom 0.35
                            ypos 0.75
                        "*Polar glances over to the glass chambers, which are shattered on the floor.*"
                        s "I don't know if it's safe to continue this mission..."
                        s "Should I tell the others to fall back before anyone else gets hurt?"
                        menu:
                            "Should I abort the mission?"

                            "Yes, it's too risky. It's not worth getting the fossils.":
                                s "RANDY! ASTER! Come back!"
                                hide polarshocked
                                show randynormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                r "Yes, Polar?"
                                hide randynormalflip
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "What's up, Polar?"
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "This may be a bit out of character for me, but..."
                                s "I think we should leave. It's dangerous here."
                                s "Just- take a look at these papers."
                                "*Polar hands Aster and Randy the papers*"
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "..."
                                hide asternormalflip
                                show astershockedflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "Oh my..."
                                b "You're right. It's safest to leave. We don't want anyone to end up...like..."
                                hide polarnormal
                                hide astershockedflip
                                show polarsad at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show astersadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                s "Like Alex."
                                show polarsad at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show astersadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Yeah."
                                hide astersadflip
                                hide polarsad
                                scene snow
                                show asternormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarsadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Don't feel bad, Polar. It was unsafe to stay there."
                                show asternormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show polarsadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "I know. I'm glad to have protected...the rest of you."
                                s "I just wish that-"
                                show asternormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarsadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Wait-"
                                b "I hear something..."
                                hide asternormal
                                show astershocked at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "It's coming! Run!"
                                hide polarsadflip
                                show astershocked at left:
                                    ypos 0.8
                                show polarshockedflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "Which way??"
                                menu:
                                    s "Which way??"

                                    "Towards the lab":
                                        hide astershocked
                                        hide polarshockedflip
                                        "*The trio run towards the lab, but the monster is catching up*"
                                        show randyshocked at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        r "Guys! Wait up!!"
                                        show polarshockedflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "Run faster, Randy!!"
                                        hide polarshockedflip
                                        hide randyshocked
                                        scene void:
                                            xzoom 10 yzoom 10
                                        "Polar makes it back to the lab."
                                        "Aster makes it back to the lab."
                                        scene randydeath
                                        "Randy doesn't."

                                        scene lab:
                                            xzoom 2 yzoom 2
                                        show polarshocked at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        show astershockedflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        sa "RANDY!!!"
                                        s "No!!!"
                                        hide polarshocked
                                        show polarsad at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "No... *sob*"
                                        menu:
                                            "What do I do now?"

                                            "Negotiation":
                                                hide polarsad
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                s "Aster!! Open the door! Surely he can still make it..!"
                                                hide astershockedflip
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8 
                                                show astersadflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.75
                                                b "No, Polar. It's too late. All we can do is save ourselves."
                                                hide polarshocked
                                                show polardismay at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75 
                                                show astersadflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.8 
                                                s "Are you kidding me?? OPEN THE DOOR!"
                                                hide astersadflip
                                                hide polardismay
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.75 
                                                b "Polar, no! We can't let each other die as well!"
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.8 
                                                s "If you don't let me do this, Randy's death will be YOUR FAULT."
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.75 
                                                b "..."
                                                b "I-"
                                                b "If I let you do this, we'll both die as well!"                                                                                               
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.8 
                                                s "I have to do this. I have to!"
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.75 
                                                b "Polar-"
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.8 
                                                s "Randy's life is on the line!!"
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.75 
                                                b "Polar-!"
                                                show polarshocked at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                show astershockedflip at right:
                                                    xzoom 0.35 yzoom 0.35 
                                                    ypos 0.8 
                                                s "Let me do this!!"
                                                hide astershockedflip
                                                hide polardismay
                                                scene asterdeath
                                                b "AAAAAAAAAAAAHHHHHHHHHH!!!"
                                                s "Aster??"
                                                scene lab:
                                                    xzoom 2 yzoom 2
                                                hide polarshocked
                                                show polardismay at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                s "ASTER!!!!"
                                                s "I- I-"
                                                s "I'm sorry..."
                                                s "God, I'm so sorry."
                                                s "I- I don't know what to do..."
                                                s "*inhale*"
                                                hide polardismay
                                                show polarsad at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                s "Gotta bounce back...it'll be okay..."
                                                s "Gotta...bounce...back..."
                                                s "*sigh*"
                                                menu:
                                                    "Mourn or run?"

                                                    "Mourn":
                                                        s "I can't leave now..."
                                                        s "I'm sorry, everyone."
                                                        s "I couldn't protect you."
                                                        "*krrrchh krrrrcchhh*"
                                                        hide polarsad
                                                        show polarshocked at left:
                                                            xzoom 0.35 yzoom 0.35
                                                            ypos 0.75
                                                        s "What was that..?"
                                                        "*KRRRCHHH KRRRRRCHHH*"
                                                        "*Polar turns around. The monster is right behind her.*"
                                                        # change to dismay
                                                        s "AAAAAAAAAHHH"
                                                        hide polarshocked

                                                        scene badending
                                                        "BAD ENDING..."
                                                        "Despite your best efforts, you led your crew into danger."
                                                        "One by one, your team fell to the fate of the abandoned science experiment."
                                                        "However, before you followed their footsteps, you did your best to bounce back from each of their deaths."
                                                        "You did well, Polar."
                                                        "~~THE END~~"
                                                        return

                                                    "Run":
                                                        s "I have to get out of here before I get killed too."

                                                        hide polarsad
                                                        scene snow
                                                        ""

                                                        scene spaceship
                                                        show polarsad at left:
                                                            xzoom 0.35 yzoom 0.35
                                                            ypos 0.75
                                                        s "I made it..."
                                                        s "...alone."
                                                        s "I'll miss you, Aster...Randy...even Alex."

                                                        scene slightlylessbadending
                                                        hide polarsad
                                                        "SLIGHTLY LESS BAD ENDING..."
                                                        "As much as you tried...your team couldn't make it back into the ship with you."
                                                        "However, you bounced back, and you survived."
                                                        "Never give up, Polar."
                                                        "~~THE END~~"
                                                        return
                                                                                              

                                            "Acceptance":
                                                s "I guess...we have to...*sniff* bounce back."
                                                hide astershockedflip
                                                show polarsad at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show astersadflip at right:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                b "You've done well to bounce back so far, Polar."
                                                hide polarsad
                                                hide astersadflip
                                                show polarhappy at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                show asternormalflip at right:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                s "You have too, Aster."
                                                show polarhappy at left:
                                                    ypos 0.8
                                                show asternormalflip at right:
                                                    ypos 0.75
                                                b "Thanks, Polar."
                                                b "Let's get out of here before anything else happens."

                                                scene spaceship

                                                show polarhappyflip at right:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.8
                                                show asternormal at left:
                                                    xzoom 0.35 yzoom 0.35
                                                    ypos 0.75
                                                b "I'm glad you're still alive, Polar."
                                                show polarhappyflip at right:
                                                    ypos 0.75
                                                show asternormal at left:
                                                    ypos 0.8
                                                s "Well, yeah, who else would drive the ship home?"  
                                                show polarhappyflip at right:
                                                    ypos 0.8
                                                show asternormal at left:
                                                    ypos 0.75
                                                b "No, silly. You know what I mean."
                                                show polarhappyflip at right:
                                                    ypos 0.75
                                                show asternormal at left:
                                                    ypos 0.8
                                                s "Well, you too, Aster."

                                                scene yuri
                                                hide polarhappy
                                                hide asternormal
                                                "SLIGHTLY LESS BAD ENDING..."
                                                "You managed to keep one crewmate alive, but not the others."
                                                "You and Aster made it back to the ship."
                                                "You bounced back after the deaths of your friends."
                                                "Good job, Polar."
                                                "~~THE END~~"
                                                return
                                        
                                    "Towards the ship":
                                        hide astershocked
                                        hide polarshockedflip
                                        "*the trio runs towards the spaceship. The monster is fast, but the ship is close."

                                        scene void:
                                            xzoom 10 yzoom 10
                                        "Polar makes it back to the ship."
                                        "Aster makes it back to the ship."
                                        "Randy makes it back to the ship."

                                        scene spaceship
                                        show polarhappy at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "We made it!! Everyone made it!"
                                        hide polarhappy
                                        show polarsad at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "Well...except..."
                                        show randynormalflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        show polarsad at left:
                                            ypos 0.8
                                        r "It's okay, Polar. You did well to bounce back."
                                        hide polarsad
                                        show randynormalflip at right:
                                            ypos 0.8
                                        show polarhappy at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "Thanks, Randy."

                                        scene everyonebutalex
                                        hide polarhappy
                                        hide randynormalflip

                                        "GOOD ENDING..."
                                        "You almost kept the whole crew alive."
                                        "However, for the one you lost, you did well to bounce back from."
                                        "After all, you have Aster and Randy by your side still."
                                        "You'll be okay, Polar."
                                        "~~THE END~~"
                                        return

                            "No, we have to complete this mission.":
                                hide polarshocked
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "I can't abandon this now."
                                "*Randy and Aster enter the room.*"
                                s "Find anything?"
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "Nothing. But Polar, I'm worried..."
                                b "I keep hearing noises. I fear we're not alone here."
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8 
                                s "Well. I haven't heard anything. We'll be fine."
                                hide asternormalflip 
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show asterangryflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75 
                                b "May I remind you that I am a bat? The creature uses echolocation."
                                hide asterangryflip
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8 
                                s "I'm just trying not to worry us all." 
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75 
                                b "Wait-"
                                "*Aster's ears twitch*"
                                hide asternormalflip
                                hide polarnormal
                                show astershockedflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarshocked at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Randy! Move over!"
                                show astershockedflip at right:
                                    ypos 0.8
                                hide polarshocked
                                show randyshocked at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                r "Huh? Why?"
                                show astershockedflip at right:
                                    ypos 0.75
                                show randyshocked at left:
                                    ypos 0.8
                                b "Just do it!"
                                show astershockedflip at right:
                                    ypos 0.8
                                show randyshocked at left:
                                    ypos 0.75
                                r "What?? What's going on?"
                                "*Aster starts shoving Randy to the side*"
                                r "Hey-!"
                                hide randyshocked
                                show polardismay at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "LOOK OUT!!"
                                hide astershockedflip
                                hide polardismay
                                scene asterdeath
                                r "We have to go!!"
                                s "But Aster-"
                                r "Just leave!!"
                                "*Polar and Randy begin to run, out of the lab and towards the ship.*"
                                "*Polar can't stop tears beginning to flow. She wants to look back, but she knows Aster is gone.*"
                                "*They both make it back to the ship."

                                scene spaceship
                                hide randyshockedflip
                                hide polardismay
                                show randynormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                r "We made it!"
                                show polarsad at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show randynormalflip at right:
                                    ypos 0.75
                                s "Yeah..."
                                show randynormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarsad at left:
                                    ypos 0.8
                                r "Listen, it's okay."   
                                r "You did good to bounce back."
                                hide polarsad
                                show polarhappy at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                r "Good job, Polar."

                                scene slightlylessbadending4
                                "SLIGHTLY LESS BAD ENDING..."
                                "You lost two great crewmembers on this mission."
                                "However, you and Randy made it back before you could follow the same fate."
                                "You bounced back from the losses."
                                "Well done, Polar."
                                "~~THE END~~"
                                return                             

                    "On the desks":
                        "*Polar searches on the desks.*"
                        s "I can't find anything. Where should I look next?"
                        jump search_choice2    

                    "Through the rooms":
                        "*Polar searches through the rooms*"
                        s "I can't find anything. Where should I look next?"
                        jump search_choice2

                return

            "No, it's too risky":
                show polarnormal at left:
                    ypos 0.75
                show alexnormal at right:
                    ypos 0.8
                s "No, stay back. It's too risky."
                show polarnormal at left:
                    ypos 0.8
                show alexnormal at right:
                    ypos 0.75
                d "Of course. Hopefully Aster makes it."
                show polarnormal at left:
                    ypos 0.75
                show alexnormal at right:
                    ypos 0.8
                s "They will."
                "*Sure enough, Aster makes it inside and slams the door shut behind them. Everyone cheers.*"
                s "Now. We need to search the area. Let's split up."
                hide alexnormal
                show polarnormal at left:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.8
                show randynormalflip at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                r "On it."
                hide randynormalflip
                show asternormalflip at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                b "On it."
                hide asternormalflip
                show alexnormal at right:
                    xzoom 0.35 yzoom 0.35
                    ypos 0.75
                d "On it."
                hide alexnormal
                show polarnormal at left:
                    ypos 0.75
                s "Where should I search?"
                label search_choice:
                menu:
                    "Where should I search?"

                    "In the drawers":
                        "*Polar checks through the drawers, ruffling through some study papers.*"
                        "*She stops on one of them, picking it up and reading it.*"
                        hide polarnormal
                        p "Experiment Logs: The Revival"
                        p "This experiment uses the fossil remains we found near the coast."
                        show polarshocked at left:
                            xzoom 0.35 yzoom 0.35
                            ypos 0.75
                        s "That's what I need!"
                        hide polarshocked
                        p "The fossil has the strange ability to regenerate itself when injured."
                        p "We wanted to see if we could integrate these regenerative abilities into a living creature."
                        p "However, the fossil was incomplete, so we created metal parts to complete it until we discover the full skeleton."
                        p "The life form is currently growing in one of the chambers."
                        show polarshocked at left:
                            xzoom 0.35 yzoom 0.35
                            ypos 0.75
                        "*Polar glances over to the glass chambers, which are shattered on the floor.*"
                        s "I don't know if it's safe to continue this mission..."
                        s "Should I tell the others to fall back before anyone else gets hurt?"
                        menu:
                            "Should I abort the mission?"

                            "Yes, it's too risky. It's not worth getting the fossils.":
                                s "RANDY! ASTER! ALEX! Come back!"
                                hide polarshocked
                                show alexnormal at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                d "Yeah?"
                                hide alexnormal
                                show randynormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                r "Yes, Polar?"
                                hide randynormalflip
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "What's up, Polar?"
                                show asternormalflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                s "This may be a bit out of character for me, but..."
                                s "I think we should leave. It's dangerous here."
                                s "Just- take a look at these papers."
                                "*Polar hands Aster, Randy and Alex the papers*"
                                show polarnormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "..."
                                hide asternormalflip
                                show astershockedflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                b "Oh my..."
                                b "You're right. It's safest to leave. We don't want anyone to be in danger."

                                scene snow
                                show asternormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarsadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Don't feel bad, Polar. It was unsafe to stay there."
                                show asternormal at left:
                                    ypos 0.8
                                show polarsadflip at right:
                                    ypos 0.75
                                s "I know. It's a shame we can't complete the-"
                                show asternormal at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarsadflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "Wait."
                                b "I think I hear something..."    
                                hide asternormal
                                hide polarsadflip
                                show astershocked at left:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.75
                                show polarshockedflip at right:
                                    xzoom 0.35 yzoom 0.35
                                    ypos 0.8
                                b "It's coming! Run!!"
                                show astershocked at left:
                                    ypos 0.8
                                show polarshockedflip at right:
                                    ypos 0.75
                                s "Which way??"
                                menu:
                                    s "Which way??"

                                    "Towards the lab":
                                        hide astershocked
                                        hide polarshockedflip
                                        "*The four run towards the lab, but the monster is catching up*"
                                        show randyshocked at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        r "Guys! Wait up!!"
                                        show polarshockedflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "Run faster, Randy!!"
                                        hide polarshockedflip
                                        hide randyshocked
                                        scene void:
                                            xzoom 10 yzoom 10
                                        "Polar makes it back to the lab."
                                        "Aster makes it back to the lab."
                                        "Alex makes it back to the lab."
                                        scene randydeath
                                        "Randy doesn't."

                                        scene lab:
                                            xzoom 2 yzoom 2
                                        show polardismay at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        show astershockedflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        sa "RANDY!!!"
                                        s "No!!!"
                                        hide polardismay
                                        show polarsad at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "No... *sob*"
                                        hide astershockedflip
                                        show alexsad at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        show polarsad at left:
                                            ypos 0.8
                                        d "It's okay. Let's wait out the monster, then run back to the ship. The mission isn't safe to continue."
                                        d "W-we can bounce back from this. I promise."

                                        scene void:
                                            xzoom 10 yzoom 10
                                        hide polarsad
                                        hide alexsad
                                        "10 minutes later"

                                        scene spaceship
                                        show polarsad at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "I'm glad you guys could make it back with me."
                                        show polarsad at left:
                                            ypos 0.8
                                        show asternormalflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        b "At least you're not alone."
                                        b "I'm glad you're still here, Polar."

                                        scene slightlylessbadending3
                                        hide polarsad
                                        hide asternormalflip
                                        "SLIGHTLY LESS BAD ENDING..."
                                        "Most of your crew made it back, but you still lost one."
                                        "However, on the journey home, you bounced back."
                                        "Maybe things won't be so bad."
                                        "You did well, Polar."
                                        "~~THE END~~"
                                        return

                                    "Towards the ship":
                                        hide astershocked
                                        hide polarshockedflip
                                        "The four run towards the ship. The monster is fast, but the ship is close."
                                        "Polar makes it to the ship."
                                        "Aster makes it to the ship."
                                        "Alex makes it to the ship."
                                        "Randy makes it to the ship."
          

                                        scene spaceship
                                        show polarhappy at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "We made it! We really all made it!"
                                        s "I'm so proud of you all."
                                        hide polarhappy
                                        show polarsad at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        s "Even though we didn't complete the mission."
                                        hide polarsad
                                        show polarhappy at left:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.8
                                        show asternormalflip at right:
                                            xzoom 0.35 yzoom 0.35
                                            ypos 0.75
                                        b "We couldn't have made it without you."
                                        show polarhappy at left:
                                            ypos 0.75
                                        show asternormalflip at right:
                                            ypos 0.8
                                        s "Thanks, Aster."

                                        scene happyending
                                        hide polarhappy
                                        hide asternormalflip
                                        "BEST ENDING"
                                        "Everyone in the crew safely made it home."
                                        "The mission was left incomplete, but it didn't matter."
                                        "Because of you, everyone got to continue living."
                                        "Great job, Polar."
                                        "~~THE END~~"
                                        return

                    "On the desks":
                        "*Polar searches on the desks.*"
                        s "I can't find anything. Where should I look next?"
                        jump search_choice     

                    "Through the rooms":
                        "*Polar searches through the rooms*"
                        s "I can't find anything. Where should I look next?"
                        jump search_choice 

    label alex_guard_camp:
        show alexnormalflip at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        d "I don't know if I should..."
        hide alexnormalflip
        jump guard_choice

    label randy_guard_camp:
        show randysad at left:
            xzoom 0.35 yzoom 0.35
            ypos 0.75
        "I'm a little nervous..."
        hide randysad
        jump guard_choice

    # This ends the game.

    return

    