import os
from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.rock import Rock
from bfs_battle_for_supremacy.ui.root import Layout, Button
from bfs_battle_for_supremacy.ui.components.game.board import Board
from bfs_battle_for_supremacy.ui.utils import get_font
from bfs_battle_for_supremacy.config import (
    IMAGES_PATH,
    WIDTH,
    BOARD_SIZE_WIDTH,
)
from bfs_battle_for_supremacy.ui.utils import main_color, main_color_hover
from bfs_battle_for_supremacy.ui.root.container import Container
from bfs_battle_for_supremacy.ui.root.text import Text
from bfs_battle_for_supremacy.game_logic.managers.player_manager import (
    PlayerManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.ui.components.game.tile import Tile
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.ui.root.dialog import Dialog
BOARD_WIDTH = 700
BOARD_HEIGHT = 700
SELECTION_WIDTH = 500
SELECTION_HEIGHT = 400
STATS_WIDTH = 500
STATS_HEIGHT = 200


class Game(Layout):
    def setup_components(self):
        MapManager.initialize_map(
            player1=PlayerManager.players[0], player2=PlayerManager.players[1]
        )
        self.board: Board = Board(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
        
        # self.selection = Button(
        #     BOARD_WIDTH,
        #     0,
        #     SELECTION_WIDTH,
        #     SELECTION_HEIGHT,
        #     "yellow",
        #     "yellow",
        #     "select something",
        #     get_font(40),
        #     font_color="black",
        # )
        self.selection = Container(
            BOARD_WIDTH,
            0,
            SELECTION_WIDTH,
            SELECTION_HEIGHT,
            [
                Text(
                        x=20,
                        y=10,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= str(PlayerManager.current_player_index),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                Text(
                        x=20,
                        y=50,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= "No items selected",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=90,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= "",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=130,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= "",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=170,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= "",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=210,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text= "",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    )
            ],
            color="yellow",
        )
        self.stats = [
            Container(
                components=[
                    Text(
                        x=20,
                        y=10,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Name: " + PlayerManager.players[0].name,
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=30,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Health: " + str(PlayerManager.players[0].health),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=50,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Damage : "
                        + str(PlayerManager.players[0].damage),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=70,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Resources : ",
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=100,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Food : "
                        + str(PlayerManager.players[0].resources.food),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=120,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Coins : "
                        + str(PlayerManager.players[0].resources.coins),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=140,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Wood : "
                        + str(PlayerManager.players[0].resources.wood),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=160,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Iron : "
                        + str(PlayerManager.players[0].resources.iron),
                        color="red",
                        secondary_color="red",
                        font=get_font(30),
                    ),
                ],
                x=BOARD_WIDTH,
                y=SELECTION_HEIGHT,
                width=STATS_WIDTH / 2,
                height=STATS_HEIGHT,
            ),
            Container(
                x=BOARD_WIDTH + STATS_WIDTH / 2,
                y=SELECTION_HEIGHT,
                width=STATS_WIDTH / 2,
                height=STATS_HEIGHT,
                components=[
                    Text(
                        x=20,
                        y=10,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Name: " + PlayerManager.players[1].name,
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=30,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Health: " + str(PlayerManager.players[1].health),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=50,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Damage : "
                        + str(PlayerManager.players[1].damage),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=70,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Resources : ",
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=100,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Food : "
                        + str(PlayerManager.players[1].resources.food),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=120,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Coins : "
                        + str(PlayerManager.players[1].resources.coins),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=140,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Wood : "
                        + str(PlayerManager.players[1].resources.wood),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                    Text(
                        x=20,
                        y=160,
                        width=STATS_WIDTH / 2,
                        height=STATS_HEIGHT,
                        text="Iron : "
                        + str(PlayerManager.players[1].resources.iron),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30),
                    ),
                ],
            ),
        ]
        def monster_dialog_ok():
            #adding the monster
            card:Card = PlayerManager.request_card()
            print(card.title)
            self.remove_component(self.monster_dialog)

        self.monster_dialog = Dialog(
            "You won a monster !",
            "tttt",
            background_color="white",
            on_ok=monster_dialog_ok,
            on_cancel=lambda: self.remove_component(self.monster_dialog),
        )
        self.draw_card_button = Button(
            BOARD_WIDTH + 40,
            SELECTION_HEIGHT + STATS_HEIGHT + 10,
            120,
            80,
            main_color,
            main_color_hover,
            "draw card",
            get_font(30),
            border_radius=10,
            on_click=lambda c, e: self.add_component(self.monster_dialog),
        )

        self.end_turn_button = Button(
            WIDTH - 160,
            SELECTION_HEIGHT + STATS_HEIGHT + 10,
            120,
            80,
            main_color,
            main_color_hover,
            "end turn",
            get_font(30),
            border_radius=10,
            on_click=PlayerManager.toggle_turn()
        )

        self.add_component(self.board)
        self.add_component(self.stats[0])
        self.add_component(self.stats[1])
        self.add_component(self.selection)
        self.add_component(self.draw_card_button)
        self.add_component(self.end_turn_button)

    def update_components(self):
        for i in range(10):
            for j in range(10):
                data = MapManager.game_map.get_square(i, j)
                self.board.components[i * BOARD_SIZE_WIDTH + j].selected = (
                    False
                )
                if data.is_empty:
                    self.board.components[
                        i * BOARD_SIZE_WIDTH + j
                    ].image_path = None
                elif isinstance(data.content, Player):
                    if data.content.name == "Player 1":
                        self.board.components[
                            i * BOARD_SIZE_WIDTH + j
                        ].image_path = os.path.join(
                            IMAGES_PATH, "player1.webp"
                        )
                    else:
                        self.board.components[
                            i * BOARD_SIZE_WIDTH + j
                        ].image_path = os.path.join(
                            IMAGES_PATH, "player2.webp"
                        )
                elif isinstance(data.content, Rock):
                    os.path.join(IMAGES_PATH, "rock.png")
                else:
                    self.board.components[
                        i * BOARD_SIZE_WIDTH + j
                    ].image_path = None

        if MapManager.current_position:
            square:Square = MapManager.current_position
            self.board.components[square.row*BOARD_SIZE_WIDTH+square.column].selected = True

        self.stats[0].components[1].text = "Health : "+str(PlayerManager.players[0].health)
        self.stats[0].components[2].text = "Damage : "+str(PlayerManager.players[0].damage)
        self.stats[0].components[4].text = "Food : "+str(PlayerManager.players[0].resources.food)
        self.stats[0].components[5].text = "Coins : "+str(PlayerManager.players[0].resources.coins)
        self.stats[0].components[6].text = "Wood : "+str(PlayerManager.players[0].resources.wood)
        self.stats[0].components[7].text = "Iron : "+str(PlayerManager.players[0].resources.iron)

        self.stats[1].components[1].text = "Health : "+str(PlayerManager.players[1].health)
        self.stats[1].components[2].text = "Damage : "+str(PlayerManager.players[1].damage)
        self.stats[1].components[4].text = "Food : "+str(PlayerManager.players[1].resources.food)
        self.stats[1].components[5].text = "Coins : "+str(PlayerManager.players[1].resources.coins)
        self.stats[1].components[6].text = "Wood : "+str(PlayerManager.players[1].resources.wood)
        self.stats[1].components[7].text = "Iron : "+str(PlayerManager.players[1].resources.iron)
        if MapManager.current_position:
            square:Square = MapManager.current_position
            if isinstance(square.content,Player):
                    self.selection.components[2].text=""
                    self.selection.components[3].text=""
                    self.selection.components[4].text=""
                    self.selection.components[5].text=""
                    if square.content.name=="Player 1":
                        self.selection.components[1].text="Player 1"
                    elif square.content.name=="Player 2":
                        self.selection.components[1].text="Player 2"
            elif isinstance(square.content,Card):
                    self.selection.components[1].text="Title : "+square.content.title
                    self.selection.components[2].text="Description : "+square.content.description
                    self.selection.components[3].text="Type : "+square.content.type
                    self.selection.components[4].text="Health : "+square.content.health
                    self.selection.components[5].text="Damage : "+square.content.damage
            elif isinstance(square.content,Rock):
                    self.selection.components[1].text="Rock"
            else:
                self.selection.components[1].text="select something"
        if PlayerManager.current_player_index==0:
             self.selection.components[0].text="Player 1 turn"
        else:
             self.selection.components[0].text="Player 2 turn"
