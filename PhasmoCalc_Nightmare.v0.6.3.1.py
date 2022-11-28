import tkinter as tk
import ctypes, sys

user32 = ctypes.windll.user32

nightmare = False
x = -1
y = 0
labels = {}
ghosts = {
    "Banshee": ["Targets one person at a time", "Can be heard screaming with parabolic microphone", "Ghost Orb", "Fingerprints", "D.O.T.S Projector", 1], 
    "Demon": ["Hunt requirements: 20s CD (not 25s), 70%  Sanity. Smudge Sticks prevents for 60s (not 90s)", "Crucifix blocking radius is 5m (not 3m)", "Freezing Temperatures", "Fingerprints", "Ghost Book", 1], 
    "Deogen": ["Knows where the players are during hunts, travels very fast during hunts", "VERY slow near players; can't speed up, hunts at 40%, unique answer to spirit box ('bull-like breathing')", "Spirit Box", "Ghost Book", "D.O.T.S Projector", 1],
    "Goryo": ["D.O.T.S evidence can only be seen through video-cameras", "Rarely seen far from its roon", "EMF 5", "Fingerprints", "D.O.T.S Projector", 1], 
    "Hantu": ["Moves faster in colder areas", "Moves slower in warmer areas", "Ghost Orb", "Freezing Temperatures", "Fingerprints", 1],
    "Jinn": ["Fast travel if target is far away", "Turning off the breaker blocks their ability", "EMF 5", "Freezing Temperatures", "Fingerprints", 1],
    "Mare": ["Ghostroom-lights turned off = Hunts at 60% Sanity", "Ghostroom-lights turned on = Hunts at 40% Sanity", "Ghost Orb", "Spirit Box", "Ghost Book", 1],
    "Moroi": ["Less Sanity = faster during hunts (possible faster than revenant). Can curse players to drain their sanity faster", "Sanity Pills cure curses, smudging the ghost during hunts stuns it for twice as long", "Spirit Box", "Ghost Book", "Freezing Temperatures", 1],
    "Myling": ["Quieter when hunting", "Makes paranormal sounds more often", "EMF 5", "Fingerprints", "Ghost Book", 1],
    "Obake": ["Can reduce the time fingerprints can be seen", "Unique fingerprints: 2 prints on lightswitch, 6 fingers on doors, 5 fingers on prison cells and keyboards", "EMF 5", "Ghost Orb", "Fingerprints", 1],
    "Oni": ["More people around = more activity", "More people around = easier to find", "EMF 5", "Freezing Temperatures", "D.O.T.S Projector", 1],
    "Onryo": ["Ghost blows out a fire, 50% Chance to hunt, 60% Base threshhold for hunts", "Fires act like crucifix, 4m range", "Ghost Orb", "Spirit Box", "Freezing Temperatures", 1],
    "Phantom": ["Sanity drops fast if you look at it", "Taking photos will make it disappear", "Spirit Box", "Fingerprints", "D.O.T.S Projector", 1],
    "Poltergeist": ["Throws lots of objects at once that drain sanity", "Empty rooms", "Spirit Box", "Fingerprints", "Ghost Book", 1],
    "Raiju": ["Nearby electricity: move faster, hunt threshhold = 65% Sanity", "Disrupts electronics further away (flicker range > walk sound range)", "EMF 5", "Ghost Orb", "D.O.T.S Projector", 1],
    "Revenant": ["If player in line of sight: ghost is twice as fast", "Slow when not chasing someone", "Ghost Orb", "Freezing Temperatures", "Ghost Book", 1],
    "Shade": ["No interactions & less ghost events when a player is in the same room", "Hunt threshhold = 35%, Ghost event often only hissing", "EMF 5", "Freezing Temperatures", "Ghost Book", 1],
    "Spirit": ["None", "Smudge Sticks stop hunting 180s", "EMF 5", "Spirit Box", "Ghost Book", 1],
    "Thaye": ["Is very active at the start of the mission (huntung at 75%, fast, as active as Oni)", "Becomes less active over time (hunting at 15%, slower than the player, as active as a shade)", "Ghost Orb", "Ghost Book", "D.O.T.S Projector", 1],
    "Mimic": ["Can mimic the behavior of any ghost (30s-120s)", "Has an extra evidence (ghost orbs)", "Fingerprints", "Freezing Temperatures", "Spirit Box", "Ghost Orb", 1],
    "The Twins": ["Can innitiate hunts from any part of the map", "Will often interact with things at the same time", "EMF 5", "Spirit Box", "Freezing Temperatures", 1],
    "Wraith": ["Stepping in salt makes the ghost more active", "Stepping in salt leaves no footprints behind", "EMF 5", "Spirit Box", "D.O.T.S Projector", 1],
    "Yokai": ["Someone talking: Hunt threshhold = 80%", "While hunting, it can only hear voices close nearby", "Ghost Orb", "Spirit Box", "D.O.T.S Projector", 1],
    "Yurei": ["Heartbeat during ghostevents and hunts lower sanity faster, ghost has abiliity to trop sanity of nearby players by 15%", "Smudging room stops it from changing rooms for 90s, the abillity closes a door that has a delayed sound affect by 2s", "Ghost Orb", "Freezing Temperatures", "D.O.T.S Projector", 1]
    }
evidences = {
    "EMF 5": [0, 0],
    "Spirit Box": [0, 0],
    "Fingerprints": [0, 0],
    "Ghost Orb": [0, 0],
    "Ghost Book": [0, 0],
    "Freezing Temperatures": [0, 0],
    "D.O.T.S Projector": [0, 0]
}

def startup():
    root = tk.Tk()

    def ghost_details(ghost):
        global root2
        root2 = tk.Tk()
        fontpreset = ("Calibri", 15, "normal", 'roman')
        label1_root2 = tk.Label(root2, font=fontpreset, text="Ghost:").grid(row=0, column=0)
        empty_root2_r0_c1 = tk.Label(root2, text="   ").grid(row=0, column=1)
        label2_root2 = tk.Label(root2, font=fontpreset, text=ghost).grid(row=0, column=2)
        empty_root2_r1_c0 = tk.Label(root2, text=" ").grid(row=1, column=0)
        label3_root2 = tk.Label(root2, font=fontpreset, text="Evidence:").grid(row=2, column=0)
        empty_root2_r3_c0 = tk.Label(root2, text=" ").grid(row=3, column=0)
        label4_root2 = tk.Label(root2, font=fontpreset, text="Weakness:").grid(row=4, column=0)
        empty_root2_r5_c0 = tk.Label(root2, text=" ").grid(row=5, column=0)
        label5_root2 = tk.Label(root2, font=fontpreset, text="Strength:").grid(row=6, column=0)
        empty_root2_r7_c0 = tk.Label(root2, text=" ").grid(row=7, column=0)
        if ghost != "Mimic":
            label6_root2 = tk.Label(root2, font=fontpreset, fg="orange", text=ghosts[ghost][2] + ", " + ghosts[ghost][3] + ", " + ghosts[ghost][4]).grid(row=2, column=2)
        elif ghost == "Mimic":
            label6_root2 = tk.Label(root2, font=fontpreset, fg="orange", text=ghosts[ghost][2] + ", " + ghosts[ghost][3] + ", " + ghosts[ghost][4] + ", " + ghosts[ghost][5]).grid(row=2, column=2)
        label7_roo2 = tk.Label(root2, font=fontpreset, fg="green", text=ghosts[ghost][1]).grid(row=4, column=2)
        label8_root2 = tk.Label(root2, font=fontpreset, fg="red", text=ghosts[ghost][0]).grid(row=6, column=2)
        empty_root2_r0_c3 = tk.Label(root2, text="   ").grid(row=0, column=3)

        root2.mainloop()

    def evidence_rotate(evidence, button):
        for evidence1 in evidences:
            evidences[evidence1][1] = 0
        global y
        if evidences[evidence][0] == 0:
            evidences[evidence][0] = 1
            y = y + 1
            button.configure(bg='green')
        elif evidences[evidence][0] == 1:
            evidences[evidence][0] = -10
            y = y - 1
            button.configure(bg='red')
        elif evidences[evidence][0] == -10:
            evidences[evidence][0] = 0
            button.configure(bg='white')
        if nightmare == False:
            update_ghostlist(nightmare)
        elif nightmare == True:
            update_ghostlist(nightmare)

    def update_ghostlist(nightmare):
        global labels
        r = 3
        c = -2
        p = -1
        for ghost in ghosts:
            p = p + 1
            if c == 12:
                r = r + 1
                c = -2
            c = c + 2
            labels[str(p)] = tk.Label(root, width=11, height=2, text=" ")
            labels[str(p)].grid(row=r, column=c)
        labels = {}
        r = 3
        c = -2
        p = -1
        if nightmare == False:
            ghostlist = normal_calc()
        elif nightmare == True:
            ghostlist = nightmare_calc()
        for ghost in ghostlist:
            if ghost != "Mimic":
                i = 5
            elif ghost == "Mimic":
                i = 6
            if ((ghosts[ghost][i] == 0) and (len(ghostlist) <= 7)):
                fg_set = "lightgrey"
                bg_set = "white"
            else:
                fg_set = "black"
                bg_set = "lightgrey"
            p = p + 1
            if c == 12:
                r = r + 1
                c = -2
            c = c + 2
            labels[str(p)] = tk.Button(root, width=10, height=1, text=ghost, bg=bg_set, fg=fg_set, command=lambda ghost=ghost: ghost_details(ghost))
            labels[str(p)].grid(row=r, column=c)
        if len(ghostlist) <= 7:
            c = -2
            p2 = -1
            for ghost in ghostlist:
                if ghost != "Mimic":
                    i = 5
                elif ghost == "Mimic":
                    i = 6
                p = p + 1
                p2 = p2 + 1
                c = c + 2
                if ghosts[ghost][i] == 1:
                    labels[str(p)] = tk.Button(root, width=8, height=1, text="Hide", fg="red", command=lambda p=p, p2=p2, ghost=ghost, ghostlist=ghostlist: toggle_ghost_off(p, p2, ghost, ghostlist))
                    labels[str(p)].grid(row=4, column=c)
                elif ghosts[ghost][i] == 0:
                    labels[str(p)] = tk.Button(root, width=8, height=1, text="Hide", fg="green", command=lambda p=p, p2=p2, ghost=ghost, ghostlist=ghostlist: toggle_ghost_on(p, p2, ghost, ghostlist))
                    labels[str(p)].grid(row=4, column=c)    
        for evidence in evidences:
            if evidences[evidence][0] == 0:
                if evidence == "EMF 5":
                    schalt_r1_c0.configure(bg="white")
                elif evidence == "Spirit Box":
                    schalt_r1_c2.configure(bg="white")
                elif evidence == "Fingerprints":
                    schalt_r1_c4.configure(bg="white")
                elif evidence == "Ghost Orb":
                    schalt_r1_c6.configure(bg="white")
                elif evidence == "Ghost Book":
                    schalt_r1_c8.configure(bg="white")
                elif evidence == "Freezing Temperatures":
                    schalt_r1_c10.configure(bg="white")
                elif evidence == "D.O.T.S Projector":
                    schalt_r1_c12.configure(bg="white")              
        if ((len(ghostlist) <= 7) and (nightmare == False)):
            check_ghost_evidence(ghostlist)

    def toggle_ghost_off(p, p2, ghost, ghostlist):
        labels[str(p2)].configure(fg="lightgrey", bg="white")
        labels[str(p)].configure(fg="green", text="Show", command=lambda p=p, p2=p2, ghost=ghost, ghostlist=ghostlist: toggle_ghost_on(p, p2, ghost, ghostlist))
        if ghost != "Mimic":
            i = 5
        elif ghost == "Mimic":
            i = 6
        ghosts[ghost][i] = 0
        global y
        if nightmare == False:
            check_ghost_evidence(ghostlist)

    def toggle_ghost_on(p, p2, ghost, ghostlist):
        labels[str(p2)].configure(fg="black", bg="lightgrey")
        labels[str(p)].configure(fg="red", text="Hide", command=lambda p=p, p2=p2, ghost=ghost, ghostlist=ghostlist: toggle_ghost_off(p, p2, ghost, ghostlist))
        if ghost != "Mimic":
            i = 5
        elif ghost == "Mimic":
            i = 6
        ghosts[ghost][i] = 1
        if nightmare == False:
            check_ghost_evidence(ghostlist)

    def check_ghost_evidence(ghostlist):
        global y
        shown_ghosts = 0
        for ghost in ghostlist:
            if ghost != "Mimic":
                c = 5
            elif ghost == "Mimic":
                c = 6
            for i in range(2,c):
                if ((evidences[ghosts[ghost][i]][0] >= 0) and (ghosts[ghost][c] == 1)):
                    evidences[ghosts[ghost][i]][1] = (evidences[ghosts[ghost][i]][1] + 1)
            if ghosts[ghost][c] == 1:
                shown_ghosts = shown_ghosts + 1
        for evidence in evidences:
            if ((evidences[evidence][1] == shown_ghosts) and (shown_ghosts != 0)):
                y = y + 1
                if evidence == "EMF 5":
                    schalt_r1_c0.configure(bg="green")
                elif evidence == "Spirit Box":
                    schalt_r1_c2.configure(bg="green")
                elif evidence == "Fingerprints":
                    schalt_r1_c4.configure(bg="green")
                elif evidence == "Ghost Orb":
                    schalt_r1_c6.configure(bg="green")
                elif evidence == "Ghost Book":
                    schalt_r1_c8.configure(bg="green")
                elif evidence == "Freezing Temperatures":
                    schalt_r1_c10.configure(bg="green")
                elif evidence == "D.O.T.S Projector":
                    schalt_r1_c12.configure(bg="green")
                evidences[evidence][0] == 1
            elif ((evidences[evidence][1] == 0) and (shown_ghosts != 0)):
                if evidence == "EMF 5":
                    schalt_r1_c0.configure(bg="red")
                elif evidence == "Spirit Box":
                    schalt_r1_c2.configure(bg="red")
                elif evidence == "Fingerprints":
                    schalt_r1_c4.configure(bg="red")
                elif evidence == "Ghost Orb":
                    schalt_r1_c6.configure(bg="red")
                elif evidence == "Ghost Book":
                    schalt_r1_c8.configure(bg="red")
                elif evidence == "Freezing Temperatures":
                    schalt_r1_c10.configure(bg="red")
                elif evidence == "D.O.T.S Projector":
                    schalt_r1_c12.configure(bg="red")
                evidences[evidence][0] == -10
            elif ((evidences[evidence][1] > 0) and (evidences[evidence][1] < shown_ghosts)):
                if evidence == "EMF 5":
                    schalt_r1_c0.configure(bg="orange")
                elif evidence == "Spirit Box":
                    schalt_r1_c2.configure(bg="orange")
                elif evidence == "Fingerprints":
                    schalt_r1_c4.configure(bg="orange")
                elif evidence == "Ghost Orb":
                    schalt_r1_c6.configure(bg="orange")
                elif evidence == "Ghost Book":
                    schalt_r1_c8.configure(bg="orange")
                elif evidence == "Freezing Temperatures":
                    schalt_r1_c10.configure(bg="orange")
                elif evidence == "D.O.T.S Projector":
                    schalt_r1_c12.configure(bg="orange")
                evidences[evidence][0] == 0
        for evidence1 in evidences:
            evidences[evidence1][1] = 0

    def toggle_nightmare():
        global nightmare
        global x
        if nightmare == False:
            nightmare = True
            x = -12
            schalt_r1_c14.configure(text="True", bg="green")
            update_ghostlist(nightmare)
        elif nightmare == True:
            nightmare = False
            x = -1
            schalt_r1_c14.configure(text="False", bg="red")
            update_ghostlist(nightmare)

    def ghost_sum(ghost):
        ghost_sum = 0
        if ghost != "Mimic":
            i = 5
        elif ghost == "Mimic":
            i = 6
        for r in range(2,i):
            ghost_sum = ghost_sum + evidences[ghosts[ghost][r]][0]

        return ghost_sum

    def normal_calc():
        global y
        global x
        y = 0
        for evidence in evidences:
            if evidences[evidence][0] == 1:
                y = y + 1
        pos_ghosts = []
        if nightmare == False:
            z = x + y
            for ghost in ghosts:
                if ghost_sum(ghost) > z:
                    pos_ghosts.append(ghost)
        return pos_ghosts

    def nightmare_calc():
        global x
        global y
        y = 0
        for evidence in evidences:
            if evidences[evidence][0] == 1:
                y = y + 1
        pos_ghosts = []
        if nightmare == True:
            for ghost in ghosts:
                if (((y == 0) and (ghost_sum(ghost) > x)) or ((y == 1) and ((ghost_sum(ghost)) == (-9) or (ghost_sum(ghost)) == (1))) or ((y == 2) and ((ghost_sum(ghost)) == (-8) or (ghost_sum(ghost)) == (2))) or ((ghost == "Mimic") and (y == 3) and ((ghost_sum(ghost)) == (-7) or (ghost_sum(ghost)) == (3)))):
                    if not (((ghost == "Obake") and (evidences["Fingerprints"] == -10)) or ((ghost == "Goryo") and (evidences["D.O.T.S Projector"] == -10)) or ((ghost == "Mimic") and ((evidences["Ghost Orb"] == -10) or (evidences["Ghost Orb"] != 1) and (y == 3)))):
                        pos_ghosts.append(ghost)
        return pos_ghosts

    def reset():
        global y
        y = 0
        for evidence in evidences:
            evidences[evidence][0] = 0
            evidences[evidence][1] = 0
        update_ghostlist(nightmare)
        schalt_r1_c0.configure(bg="white")
        schalt_r1_c2.configure(bg="white")
        schalt_r1_c4.configure(bg="white")
        schalt_r1_c6.configure(bg="white")
        schalt_r1_c8.configure(bg="white")
        schalt_r1_c10.configure(bg="white")
        schalt_r1_c12.configure(bg="white")
        for ghost in ghosts:
            if ghost != "Mimic":
                i = 5
            elif ghost == "Mimic":
                i = 6
            ghosts[ghost][i] = 1

    def exit():
        while x == x:
            try:
                handle = user32.FindWindowW(None, u'tk')
            except:
                break
            else:
                user32.DestroyWindow(handle)
                sys.exit()

    label1 = tk.Label(root, text='Evidence').grid(row=0, column=0)
    schalt_r1_c0 = tk.Button(root, text="          EMF 5          ", command=lambda: evidence_rotate("EMF 5", schalt_r1_c0), borderwidth=5, bg = "white")
    schalt_r1_c0.grid(row=1, column=0)
    empty_r1_c1 = tk.Label(root, text='   ').grid(row=1, column=1)
    schalt_r1_c2 = tk.Button(root, text="       Spirit Box       ", command=lambda: evidence_rotate("Spirit Box", schalt_r1_c2), borderwidth=5, bg = "white")
    schalt_r1_c2.grid(row=1, column=2)
    empty_r1_c3 = tk.Label(root, text='   ').grid(row=1, column=3)
    schalt_r1_c4 = tk.Button(root, text="     Fingerprints     ", command=lambda: evidence_rotate("Fingerprints", schalt_r1_c4), borderwidth=5, bg = "white")
    schalt_r1_c4.grid(row=1, column=4)
    empty_r1_c5 = tk.Label(root, text='   ').grid(row=1, column=5)
    schalt_r1_c6 = tk.Button(root, text="      Ghost Orb       ", command=lambda: evidence_rotate("Ghost Orb", schalt_r1_c6), borderwidth=5, bg = "white")
    schalt_r1_c6.grid(row=1, column=6)
    empty_r1_c7 = tk.Label(root, text='   ').grid(row=1, column=7)
    schalt_r1_c8 = tk.Button(root, text="    Ghost Writing   ", command=lambda: evidence_rotate("Ghost Book", schalt_r1_c8), borderwidth=5, bg = "white")
    schalt_r1_c8.grid(row=1, column=8)
    empty_r1_c9 = tk.Label(root, text='   ').grid(row=1, column=9)
    schalt_r1_c10 = tk.Button(root, text="  Freezing Temps  ", command=lambda: evidence_rotate("Freezing Temperatures", schalt_r1_c10), borderwidth=5, bg = "white")
    schalt_r1_c10.grid(row=1, column=10)
    empty_r1_c11 = tk.Label(root, text='   ').grid(row=1, column=11)
    schalt_r1_c12 = tk.Button(root, text=" D.O.T.S Projector ", command=lambda: evidence_rotate("D.O.T.S Projector", schalt_r1_c12), borderwidth=5, bg = "white")
    schalt_r1_c12.grid(row=1, column=12)
    empty_r1_c13 = tk.Label(root, text='                 ').grid(row=1, column=13)
    label2 = tk.Label(root, text="Nightmare").grid(row=0, column=14)
    schalt_r1_c14 = tk.Button(root, text="False", command=lambda: toggle_nightmare(), borderwidth=5, bg="red")
    schalt_r1_c14.grid(row=1, column=14)
    empty_r1_c15 = tk.Label(root, text='   ').grid(row=1, column=15)
    label3 = tk.Label(root, text="System").grid(row=0, column=16)
    schalt_r1_c16 = tk.Button(root, text="Reset", command=lambda: reset(), borderwidth=5).grid(row=1, column=16)
    schalt_r2_c16 = tk.Button(root, text="Exit", command=lambda: exit(), borderwidth=5).grid(row=2, column=16)
    empty_r2_c0 = tk.Label(root, text='   ').grid(row=2, column=0)
    empty_r99_c0 = tk.Label(root, text='   ').grid(row=99, column=0)
    update_ghostlist(nightmare)
    
    root.mainloop()

if __name__ == "__main__":
    startup()