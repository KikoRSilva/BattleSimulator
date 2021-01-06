#!/usr/bin/env python3

###########################################
# FP2019/2020 @ IST                       #
# Projeto 2 - Tecnico Battle Simulator    #
# Francisco Silva                         #
# Graphic version                         #
###########################################

import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tecnicobattlesimulator import *


class TecnicoSimulator(tk.Frame):

    def __init__(self, master=None, filename=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.mapa = self.parse_config(filename)

        # Graphics dimensions
        self.cellsize =min((50, 600//max(obter_tamanho(self.mapa))))
        self.boxscoresize = 50

        # Load icon images
        self.icons = self.load_icons()

        # Create widgets
        self.create_widgets()

    def parse_config(self, filename):
        with open(filename, 'r') as infile:
            dim = eval(infile.readline())
            army1_conf = eval(infile.readline())
            army2_conf = eval(infile.readline())
            walls = tuple(cria_posicao(*pos) for pos in eval(infile.readline()))
            units1 = tuple(cria_unidade(cria_posicao(*pos), army1_conf[1], army1_conf[2], army1_conf[0])
                            for pos in eval(infile.readline()))
            units2 = tuple(cria_unidade(cria_posicao(*pos), army2_conf[1], army2_conf[2], army2_conf[0])
                            for pos in eval(infile.readline()))

        return cria_mapa(dim, walls, units1, units2)

    def load_icons(self):
        icon_imgs = ("devil.png", "ghost.png")
        icons = dict()

        # Associate Icon Image to Combat side
        armies = obter_nome_exercitos(self.mapa)
        for n, img in enumerate(icon_imgs):
            key = armies[n].upper()[0]
            img = Image.open(img)
            icons[key] = {'img': ImageTk.PhotoImage(img.resize((self.cellsize, self.cellsize), Image.ANTIALIAS)),
                            'img_big': ImageTk.PhotoImage(img.resize((self.boxscoresize, self.boxscoresize), Image.ANTIALIAS))}
        return icons

    def create_widgets(self):
        # Create drawing widget
        mapa_size = obter_tamanho(self.mapa)

        # Board/map widget creation and drawing
        self.board = tk.Canvas(self,
                           width=mapa_size[0] * self.cellsize,
                           height=mapa_size[1] * self.cellsize)
        self.board.pack(side='left')
        self.draw_map()

        # Frame widget for the additional elements (boxscore and turn button)
        right_frame = tk.Frame(self)
        right_frame.pack(side=tk.RIGHT)

        # Create boxscore widget and draw it
        self.boxscore = tk.Canvas(right_frame,
                            width=4*self.boxscoresize,
                            height=4*self.boxscoresize)
        self.boxscore.pack(fill=tk.X, pady=10)
        self.draw_boxscore()

        # Create next turn butto widget and associate with callback function next_turn
        self.turn_button = tk.Button(right_frame, text="TURN", font="Times 20 bold",
                                command=self.next_turn)
        self.turn_button.pack(fill=tk.X, pady=10)

    def draw_map(self):
        x, y = 0, 0
        for char in mapa_para_str(self.mapa):
            if char == '\n':
                x, y = 0, y + 1
            else:
                if char == '#':
                    self.board.create_rectangle(x * self.cellsize, y * self.cellsize,
                                                (x + 1) * self.cellsize, (y + 1) * self.cellsize,
                                                fill="darkgray")
                elif char == '.':
                    self.board.create_rectangle(x * self.cellsize, y * self.cellsize,
                                                (x + 1) * self.cellsize, (y + 1) * self.cellsize,
                                                fill="white")
                else:
                    self.board.create_image(x * self.cellsize, y * self.cellsize,
                                            anchor=tk.NW, image=self.icons[char]['img'])
                    self.board.create_rectangle(x * self.cellsize, y * self.cellsize,
                                                (x + 1) * self.cellsize, (y + 1) * self.cellsize,
                                                fill="")
                x = x + 1

    def draw_boxscore(self):
        self.boxscore.delete("all")

        pos_y = 0
        sides = obter_nome_exercitos(self.mapa)
        scores = self.get_scores()

        for i, side in enumerate(sides):
            key = side.upper()[0]
            self.boxscore.create_image(self.boxscoresize / 4, pos_y, anchor=tk.NW, image=self.icons[key]['img_big'])
            self.boxscore.create_text(2*self.boxscoresize, pos_y + self.boxscoresize/4,
                                        anchor=tk.NW, font="Times 40 italic bold",
                                        text=str(scores[i]))
            pos_y += self.boxscoresize
            self.boxscore.create_text(self.boxscoresize/4, pos_y, anchor=tk.NW, font="Times 20 italic bold", text=side)
            pos_y += self.boxscoresize

    def next_turn(self):
        scores = self.get_scores()
        if any(sc == 0 for sc in scores):
            winner = obter_nome_exercitos(self.mapa)[0] \
                if scores[0] > scores[1] \
                else obter_nome_exercitos(self.mapa)[1]
            self.show_winner(winner)

        mapa_old = cria_copia_mapa(self.mapa)
        simula_turno(self.mapa)
        self.draw_map()
        self.draw_boxscore()

        if mapas_iguais(self.mapa, mapa_old) and all(sc >0 for sc in scores):
            self.show_winner('EMPATE')

    def get_scores(self):
        sides = obter_nome_exercitos(self.mapa)
        return tuple(calcula_pontos(self.mapa, s) for s in sides)

    def show_winner(self, winner):
        messagebox.showinfo(title="Winner TEAM!!", message=winner)
        self.master.quit()


if __name__ == '__main__':
    usage = '    Usage: ' + sys.argv[0] + ' battle_config_file\n'
    usage += '''
    Graphic Tecnico Battle Simulator.
    '''

    if len(sys.argv) != 2:
        print(usage)
        exit()

    root = tk.Tk()
    root.title("Tecnico Battle Simulator - FP2019/2020 @ IST, Francisco Silva, 2019")
    app = TecnicoSimulator(master=root, filename=sys.argv[1])
    app.mainloop()

