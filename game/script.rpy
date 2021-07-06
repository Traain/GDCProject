#Episode 1: Chaos in IKEA

#Achievements
#Inventory and map
screen overlay:
    frame:
        yalign 0.0 xalign 0.0
        hbox:
            textbutton " Inventory " action Show("inventory_screen", first_inventory=player_inv)
            textbutton " Trade " action Show("inventory_screen", first_inventory=player_inv, second_inventory=mindy_inv)
            #textbutton " Trade " action Show("inventory_screen", first_inventory=player_inv, second_inventory=mindy_inv, trade_mode=True)
            textbutton " Nearby " action Show("inventory_screen", first_inventory=player_inv, second_inventory=chest, trade_mode=True)
            #textbutton " Map " action Show("map")

#Blinking Arrow
image ctc_blink:
       "images/Arrow.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat

image ctc_anchored:
    xpos 0.93 # Across from right
    ypos 0.87 # Up from bottom
    xanchor 1.0  # On Right
    yanchor 1.0   # On Bottom
    alpha 1.0 # visible
    "images/Arrow.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

##########################################################################################################################

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Narrator = Character("", color="#6699cc", ctc="ctc_blink", ctc_position="nestled")
define Player = Character("[povname]", ctc="ctc_blink", ctc_position="nestled")
define Buddy1 = Character("[buddyone]", ctc="ctc_blink", ctc_position="nestled")
define Buddy2 = Character("[buddytwo]", ctc="ctc_blink", ctc_position="nestled")

#Splashscreen

label splashscreen:
    scene black
    $ renpy.pause(1)

    show text "This game is not suitable for children or those who are easily disturbed" with dissolve
    $ renpy.pause(2)

    hide text with dissolve
    $renpy.pause(1)

    $ renpy.pause(1)

    show text "Grey Skies Productions Presents\n Story by: Elon Litman\n Art by: Elon Litman\n Music by: Elon Litman" with dissolve ## fix
    $ renpy.pause(3)
    hide text with dissolve
    $ renpy.pause(2)

    show text "{b}{size=+12}CATACLYSM{/size}{/b}"

    $ renpy.pause(3)
    hide text with dissolve
    $ renpy.pause(2)
    return ## fix

# The game starts here.

label start:

    scene black with fade

    # These display lines of dialogue.

    Narrator "Sometime in the future, there was an arms race to develop transhumans."

    Narrator "In the process, the US government discovered alternate dimensions and obtained a sample called XE-037, a mysterious black goo that was able to reanimate the dead and cause miraculous targeted phenotype mutations."

    Narrator "XE-037 turned out to be intelligent - vastly so - and escaped, contaminating the groundwater and causing an enormous zombie outbreak."

    Narrator "As this spiraled out of control, Earth became the target of a multidimensional portal attack through which the Blob, the entity of which XE-037 is just a small part, took over our world."

    Narrator "Simultaneously, forces from other dimensions entered opportunistically as our dimensional fabric was destabilized. This was the Cataclysm."

    Narrator "Would you like to know more?"

    menu:
        "Describe the Cataclysm":
            jump describe

        "No":
            jump no


    label describe:

        Narrator "{b}March, 25 Years Before the Cataclysm:{/b}"

        scene crash with fade

        Narrator "An interdimensional traveler from an alternate earth crash lands a portal traveling vessel in the American Midwest."

        Narrator "The traveler dies, and the vessel is appropriated by the US government and starts a chain of research."

        Narrator "The technology is very similar to Earth tech of the 1990s, but the actual dimensional travelling technology is as-yet undeveloped, and there are examples of equivalent but divergent energy technologies:"

        scene fuelcell with fade

        Narrator "there is a simple but functional high-capacity fuel cell on board, using mostly Earth accessible designs but with a few exotic components that will take time to reverse engineer."

        scene black with fade

        Narrator "Would you like to know more?"

        menu:
            "Yes, tell me more":
                jump describe2

            "No":
                jump no

        label describe2:

            Narrator "{b}April, 15 Years Before the Cataclysm:{/b}"

            scene exoskeleton with fade

            Narrator "Research into pilotable robot exoskeletons results in the first large production robotic suit for cargo handling."

            Narrator "It remains prohibitively expensive for most applications."

            Narrator "These suits use a simplified fuel cell design from the dimensional craft, but not all the raw materials needed have yet been synthesized, so the efficiency is much lower."

            scene black with fade

            menu:
                "Go on":
                    jump describe3

                "No":
                    jump no

            label describe3:

                Narrator "{b}May, 13 Years Before the Cataclysm:{/b}"

                scene electriccar with fade

                Narrator "Improved fuel cell designs make solar-electric cars a viable alternative to gasoline. The first privately made electric cars are announced."

                scene black with fade

                menu:
                    "Describe the Apocalypse":
                        jump describe4

                    "No, start game":
                        jump no

                label describe4:

                    Narrator "{b}September, 12 Years Before the Cataclysm:{/b}"

                    Narrator "Advances in reverse engineering and some early tests of portal tech lead to improved synthesis of fuel cells from the dimensional craft."

                    Narrator "These cells are still bulky but enable a lot of new technologies to be imagined."

                    Narrator "They use radioactive plutonium as a catalyst in the fuel reaction, earning the nickname “plutonium fuel cells.” Due to the risk of radioactivity, they are not widely adopted by civilians."

                    Narrator "A month later, the first stable portal is opened, and a creature from the netherum breaks through, destroying a large portion of a DARPA lab."

                    Narrator "The facility auto-destruct is engaged and the event disguised as a mine collapse."

                    Narrator "The government puts a hard limit on acceptable portal research, particularly the creation of stable portals."

                    menu:
                        "Tell me more":
                            jump describe5

                        "No, start game":
                            jump no

                    label describe5:

                        Narrator "{b}December, 10 Years Before the Cataclysm:{/b}"

                        Narrator "An extraterrestrial visitor, frozen in ice, is retrieved by a Japanese whaling boat, and hastily recovered by their government and research agencies."

                        Narrator "This is the first contact between mi-go and humans."

                        Narrator "Existence of the aliens is heard in rumours and leaked photos on the internet,"

                        Narrator "Until a well-known Redditor posts a ‘making of’ video that shows detailed information of how she constructed the model alien for an art exhibit."

                        Narrator "The photos continue to circulate but are relegated to places online where people don’t believe in Snopes."

                        menu:
                            "Continue":
                                jump describe6

                            "No, start game":
                                jump no

                        label describe6:

                            Narrator "{b}December, 9 Years Before the Cataclysm:{/b}"

                            Narrator "Artificial intelligence using dimensional probability heuristics is developed."

                            Narrator "This is an AI that can simulate deductive reasoning by scanning several adjacent realities to create a realistic estimation of the outcome of an action, quite analogous to human deductive reasoning."

                            Narrator "In a small scale this is surprisingly efficient."

                            menu:
                                "What happened next?":
                                    jump describe7

                                "Stop, start game":
                                    jump no

                            label describe7:

                                Narrator "{b}June, 8 Years Before the Cataclysm:{/b}"

                                Narrator "Melchior is developed. It is a useful research assistant using dimensional heuristics but nowhere near as intelligent as hoped,"

                                Narrator "Due to the prohibitive power requirements of anticipating more than a few minutes ahead in time."

                                Narrator "Its inability to plan in the long term is seen as a crippling defect, but it remains an overall success."

                                Narrator "Later that month, the first powered exoskeletons are OK’d for military use, in limited test deployments."

                                Narrator "Although incredibly powerful against small arms fire, these “tank suits” are too large, expensive, and heavy to gain any advantages from their humanoid shape."

                                Narrator "They do not see full scale production."

                                menu:
                                    "Go on":
                                        jump describe8

                                    "Stop, start game":
                                        jump no

                                label describe8:

                                    Narrator "{b}July, 7 Years Before the Cataclysm:{/b}"

                                    Narrator "First phase development of CBMs, using bioplastic technology derived from research conducted on mi-go. Aided by Melchior, research is extremely promising."

                                    menu:
                                        "Continue":
                                            jump describe9

                                        "Stop, start game":
                                            jump no

                                    label describe9:

                                        Narrator "{b}May, 6 Years Before the Cataclysm:{/b}"

                                        Narrator "The first eyebot drones are deployed to assist in police work."

                                        Narrator "This is one of the first public displays of new AI systems using dimensional probability heuristics, with the actual DPH being managed by a central mainframe."

                                        Narrator "From a public perspective the dimensional aspect is kept concealed and people are told it is an example of machine learning."

                                        Narrator "Even engineers working on the technology have no idea how it really works (not far off of current deep machine learning really… but better), and a second phase CBM development commences."

                                        Narrator "A few weeks later, a mi-go scout arrives in orbit in response to the awakened signal of the mi-go in the ice. It does not make immediate contact with humans."

                                        menu:
                                            "Continue":
                                                jump describe10

                                            "Stop, start game":
                                                jump no

                                        label describe10:

                                            Narrator "{b}February, 4 Years Before the Cataclysm:{/b}"

                                            Narrator "The first CBMs are released for the public and military."

                                            Narrator "China announces its own competing CBM system (XFS) and showcases the first wave of “steel soldiers”, using XFS gear."

                                            Narrator "The first military grade heavy power armors are released for field testing. Unlike the tank suits, these are light and small enough to allow close quarters maneuvering in urban environments, and remain almost impervious to all but the heaviest of conventional weaponry."

                                            Narrator "Development on smaller, less expensive suits becomes a priority."

                                            menu:
                                                "Continue":
                                                    jump describe11

                                                "Stop, start game":
                                                    jump no

                                            label describe11:

                                                Narrator "{b}November, 3 Years Before the Cataclysm:{/b}"

                                                Narrator "The new cold war begins as the US and China enter a race to develop the ultimate transhuman soldier, as well as functional AI."

                                                Narrator "US reopens portal research, considering it a safer proposition with CBM enhanced soldiers and Melchior’s assistance, and potentially a good way to get ahead of China."

                                                Narrator "Researchers publish results regarding portal stability that help to explain the unexpectedly large portal of 9 years ago."

                                                Narrator "Polydimensional topography has numerous stable planes, and the energy required to make portals to certain areas is much lower."

                                                Narrator "Early researchers hadn’t known about this, and put far too much energy into a portal to an energetically accessible location, creating a much bigger portal than intended. This knowledge allows much safer exploration of micro portals."

                                                Narrator "A remote research probe sent to an adjacent dimension brings back an unidentified biocontaminant, which is captured for analysis but inadvertently destroyed by standard safety procedures."

                                                Narrator "The Blob becomes aware of our existence."

                                                menu:
                                                    "Continue":
                                                        jump describe12

                                                    "Stop, start game":
                                                        jump no

                                                label describe12:

                                                    Narrator "{b}August, 2 Years Before the Cataclysm:{/b}"

                                                    Narrator "Immediately following Chinese New Year, a new wave of XFS empowered soldier is announced publically. These represent the tip of the iceberg, and are considered dangerously competitive to NATO equivalents."

                                                    Narrator "Allied intelligence indicates that classified models may be far in advance of CBM-powered soldiers."

                                                    Narrator "In June, XEDRA (Xenophysical Energy Defense Research Agency) is formed to focus research into transdimensional phenomena."

                                                    Narrator "Publically they are masked as DARPA researchers, and other more mundane groups. They are given an enormous budget, considered by the US government to be equivalent to NASA in the current cold war."

                                                    Narrator "Certain close allies to the US join the effort, sending top minds and resources to XEDRA facilities across North America."

                                                    Narrator "Not long after, XEDRA facility in the Northwest reports a major sample stolen. Counterintelligence identifies China as the most likely culprit, and backtraces the theft to hypothesize that significant XEDRA research data was compromised."

                                                    Narrator "New protocols are put in place to counter XFS equipped intelligence agents, including advanced robotic security managed by Melchior."

                                                    Narrator "Later, XEDRA is broken into several connected but distinct agencies. In several of these agencies, desperate to catch up for time now lost by presumed stolen research, reasonable safety protocols are dropped in favour of Melchior predictions of immediate repercussions."

                                                    Narrator "This has the obvious (especially in hindsight) flaw that anything that does not have immediate repercussions will be missed: there are few lab explosions, but the Blob is able to leverage this weakness."

    label no:

        Narrator "What is your name?"

    python:
        povname = renpy.input("What is your name?", length=16)
        povname = povname.strip()

        if not povname:
             povname = "Ben"

    scene begin with fade

    #Initialize inventories

    $ player_inv = Inventory("[povname]")

    $ mindy_inv = Inventory("Trading Unavailable", 0, 100)

    $ chest = Inventory("Nearby")

    #Initialize items

    $ beans = Item("Can of Beans", "A staple among canned goods, these are reputedly good for one's coronary health.", "images/items/beans.png", 2, Show("inventory_popup", message="You eat the delicious beans."))

    #Add items to inventories

    $ chest.take(beans)

    Narrator "As [povname] opens their eyes, the first things that they notice are that it's dark and they're cold and the snow is falling as fast as the horde is headed their way."

    Narrator "Their hands are covered in blood, [povname]'s pinky nail is falling off."

    Narrator "Outside is inside, and they are shivering as the moonlight is coming through the gaps in the roof."

    Narrator "[povname] has been holed up here with their friends, in the apartment, as the world began to fall apart."

    scene life with fade

    Narrator "When the apocalypse began, many people were trapped in unfortunate situations, and as a result, met unfortunate fates."

    Narrator "[povname], however, was at a sleepover with their two buddies when the Cataclysm struck."

    Narrator "They sustained themselves entirely on cereal and junk food, as entire militaries collapsed in the face of monsters descending upon the world. They all knew life like this was not sustainable."

    Narrator "The entire world had been so hyped for a zombie apocalypse, that they believed that we would have killed them all by day 3."

    Narrator "Hardware and sporting goods stores reported a booming trade in sale of hammers, hunting bows, guns, generators, and appliances, but they soon too were overwhelmed."

    Narrator "What is your buddy's name?"

    python:
        buddyone = renpy.input("What is your buddy's name?", length=16)
        buddyone = buddyone.strip()

        if not buddyone:
            buddyone = "Jeffrey"

    Narrator "What is the name of your other buddy?"

    python:
        buddytwo = renpy.input("What is the name of your other buddy?", length=16)
        buddytwo = buddytwo.strip()

        if not buddytwo:
            buddytwo = "Max"

    Narrator "The group consists now of [povname], [buddyone], and [buddytwo]. It is believed that their families assumed them dead, and so they only have each other."

    Narrator "After stuffing every single ounce of food and liter of water in their car, they analyze their situation."

    Narrator "In their rotting building on the outskirts of Boston, they still remain thousands of kilometers from the new border on the West Coast."

    Narrator "In order to sustain themselves during the trip, they will have to make periodic stops and drives through cities and metropolitan areas."

    Narrator "New York is the first stop, and the group awaits their families in California, which is the last remaining bastion of civilization."

    Narrator "And so with nothing gained from waiting around in Boston, they decide to brave the road and head for San Fransico."

    scene car with fade

    Narrator "Just before the group heads out, [buddytwo] suggests they should name the car."

    python:
        car = renpy.input("Just before the group heads out, [buddytwo] suggests they should name the car.", length=16)
        car = car.strip()

        if not car:
            car = "Toyota Corolla"

    Narrator "And so the group drives off, and the tale begins."

    scene ikeahorizon with fade

    Narrator "Following a tiring drive, the group sees the collosal store on the horizon. It is large. Too large.{w} Almost...{w} Infinite."

    scene ikea with dissolve

    Narrator "The [car] eventually rolls into the IKEA. Near the entrance is the dead body of a young woman. Her forehead bears a large bullet entrance wound. An even larger exit wound is present on the back of her head..."

    jump episode1

    label episode1:
        scene black with fade
        $ renpy.pause(1)

        show text "EPISODE 1\nTHE INFINITE IKEA" with dissolve

        $ renpy.pause(3)

        hide text with dissolve
        jump afterepisode1

label afterepisode1:

    scene ikea with fade

    show screen overlay with dissolve

    Narrator "{cps=*0.2}TIP: CLICK {i}NEARBY{/i} TO INSPECT LOCAL ITEMS{/cps} "

























###################################################OLD GAME

    scene road with fade

    Narrator "The group drives for several hours, and admire the nearby scenery."

    Buddy1 "We probably won't make it to New York today. I dread becoming vulnerable in such an open area, but I've always wanted to see broadway!"

    Buddy2 "You're right, we should probably find a place to crash."

    Player "What do you suggest?"

    Narrator "[buddyone] points to an abadoned cabin atop a hill and a suburban home on the horizon."

    menu:
        "Suburban home":
            jump suburbanhome


        "Abandoned cabin":
            jump cabin

    label suburbanhome:

        Narrator "The [car] coasts into the driveway of the dilapidated structure."
        Narrator "Inside the home, sheets are strung about, glass has shattered on the rug, and food has been picked clean."
        Narrator "Whoever lived here, they were certainly in a hurry."
        Narrator "After boarding the doors and securing the home, the group finds themselves with some free time."
        Narrator "How can time best be spent?"

        menu:
            "Tell scary stories!":
                jump stories

            "Watch the news":
                jump news

        label stories:

            Narrator "[buddyone] decides to tell a story about {color=#f00}PEAN{/color}{color=#00ff00}UT ALL{/color}{color=#0000ffff}ERGIES!{/color}"

            Narrator "[povname] is slightly frightened."

            Narrator "The group had fun, but will be very tired the next day."

            Narrator "The group decides to hunker down for the night, and go to sleep."

            Narrator "And so [povname] slowly drifts off, and lets the warm sensation of sleep engulf them completely."

            scene black with pixellate

            Narrator "[povname] is awoken by a deafening crash coming from the outside, followed by the unmistakable ring of gunshots."

            scene windowmorning with pixellate

            Narrator "[povname] gets up frantically to assemble everyone."

            Narrator "The rest of the group is nowhere in sight."

            Narrator "After a few moments of catching their breath, [povname] sprints to the doorway."

            Narrator "They hesitate for a moment, as they contemplate whether or not to peek outside."

            Narrator "As they open the door, they will be blinded by a light brighter than any star could produce, and shocked by the loudest of explosions."

            Narrator "As they look ahead, [povname] finds themself in the most hellish and bloodiest of battlefields."

            Narrator "Peanut Butter Jars with limbs clad in white will run ahead and be mowed down by a passing gunship."

            Narrator "Tanks roll on, crushing the bodies of troopers as they bathe the area in machine-gun fire."

            Narrator "Over their shoulder a barrage of missiles will rain down from passing aircraft, which will in turn be consumed by a hail of anti-aircraft fire from behind a nearby building."

            Narrator "[povname] is on what might have once been a suburb but is now a ravaged, blasted battlefield."

            Narrator "Peanut Butter Jars clad in two colors - a horribly bright, yet somehow stained, white and a filthy, sickening black - are battling in the most horrid manners possible,"

            Narrator "Fighting with rifles, cannon, swords, bows, all the weapons of war that existed since the dawn of time, to weapons that have not yet been dreamed of by man."

            menu:
                "Take cover":
                    jump cover

            label cover:

            scene bunker with fade

            Narrator "[povname] sprints to a building resembling a three-story tall structure of blasted concrete that might have once been a command bunker."

            Narrator "The structure [povname] just left has collapsed flat in the earth, destroyed by a battalion of screaming Peanut Butter Jars wielding bayoneted rifles."

            Narrator "They take cover as troops in white engage the ones in black. [povname] see's them and witnesses their insatiable bloodlust."

            Narrator "If they run out of ammunition, they will begin cutting each other with their bayonet and striking each other with the butts of their rifles, not stopping until they completely disembowel their opponent, and left them in shards, oozing peanut butter."

            Narrator "The longer [povname] stays there, the more intense the fighting grows."

            Narrator "The screams of the wounded and dying echo through the decimated streets, and bullets and shells will come from every angle."

            Narrator "The fire detachment has arrived to the field, and is [povname] does not seek shelter quickly, the battle-crazed soldiers will get the better of them."

            menu:
                "Enter the bunker":
                    jump enterbunker

            label enterbunker:

            Narrator "[povname] enters the bunker, at which point all the peanut butter jars rush toward them"

            Narrator "[povname] does not give any notice to anyone who makes a request of them or tries to talk to them, no matter how desperate they seem."

            Narrator "They each think [povname] is the enemy, and the moment they respond, [povname] will be rewarded with a knife to the face."

            menu:
                "Run up the stairs":
                    jump runstairs

            label runstairs:

            Narrator "[povname] sprints straight up the stairway in front of them, to the second level of the bunker."

            Narrator "As they mount the stairs, a crash is heard behind them - that's the fire doorway sealing as a flamethrower detachment attacks."

            Narrator "On the second level, there is only one individual, [buddytwo], sitting at a desk, yelling into a phone. The stairs to the third level are a mass of twisted concrete."

            Narrator "[buddytwo] at the desk wears the stars of a general, but does not seem to notice that the phone, as well as all those on the level, are dead."

            menu:
                "Please help me":
                    jump helpme

                "Where do I go, sir?":
                    jump wheresir

            label helpme:

                Buddy2 "[povname]? [povname] what are you doing? Oh man, he's having a nightmare again-"

                Narrator "An explosion suddenly decimated the far wall and atomized the general. Through the hole [povname] can see, on the horizon, the long, thin shape of a missile rising."

                Narrator "[povname] shuts their eyes tight and opens them for nothing."

                Narrator "The sounds of horrid battle begin fade away, until out of the silence, a single gunshot rings out."

                return

            label wheresir:

                Buddy2 "[povname]? [povname] what are you doing? Oh man, he's having a nightmare again-"

                Narrator "An explosion suddenly decimated the far wall and atomized the general. Through the hole [povname] can see, on the horizon, the long, thin shape of a missile rising."

                Narrator "[povname] shuts their eyes tight and opens them for nothing."

                Narrator "The sounds of horrid battle begin fade away, until out of the silence, a single gunshot rings out."

                return


            scene black with pixellate

            Narrator "[buddyone] shakes [povname] awake."

            Buddy2 "Oh man, you were having a really intense nightmare. Are you okay?"

            Player "Yeah, I'm fine."

            Buddy2 "Care to tell us what it was about? We're here for you [povname]."









    label cabin:

        Narrator "The [car] coasts into the driveway of the dilapidated structure."
        Narrator "Inside the home, sheets are strung about, glass has shattered on the rug, and food has been picked clean."
        Narrator "Whoever lived here, they were certainly in a hurry. There seems to be a note."
        Narrator "After boarding the doors and securing the home, the group finds themselves with some free time."
        Narrator "How can time best be spent?"

    return

    # This ends the game.

    return
