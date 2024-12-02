from bfs_battle_for_supremacy.ui.root import Layout, Button
from bfs_battle_for_supremacy.ui.components.game.board import Board
from bfs_battle_for_supremacy.ui.utils import get_font
from bfs_battle_for_supremacy.config import WIDTH
from bfs_battle_for_supremacy.ui.utils import main_color, main_color_hover
from bfs_battle_for_supremacy.ui.root.container import Container
from bfs_battle_for_supremacy.ui.root.text import Text
from bfs_battle_for_supremacy.game_logic.managers.player_manager import PlayerManager
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
BOARD_WIDTH = 700
BOARD_HEIGHT = 700
SELECTION_WIDTH = 500
SELECTION_HEIGHT = 400
STATS_WIDTH = 500
STATS_HEIGHT = 200


class Game(Layout):
    def setup_components(self):
        self.board: Board = Board(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
        self.selection = Button(
            BOARD_WIDTH,
            0,
            SELECTION_WIDTH,
            SELECTION_HEIGHT,
            "yellow",
            "yellow",
            "select something",
            get_font(40),
            font_color="black",
        )

        self.stats = [
            Container(
                components=[
                    Text(
                        x=20,
                        y=10,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Name: "+PlayerManager.players[0].name,
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=30,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Health: "+str(PlayerManager.players[0].health),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=50,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Damage : "+str(PlayerManager.players[0].damage),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=70,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Resources : ",
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=100,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Food : "+str(PlayerManager.players[0].resources.food),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=120,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Coins : "+str(PlayerManager.players[0].resources.coins),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=140,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Wood : "+str(PlayerManager.players[0].resources.wood),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=160,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Iron : "+str(PlayerManager.players[0].resources.iron),
                        color="red",
                        secondary_color="red",
                        font=get_font(30)
                    )
                ],
                x= BOARD_WIDTH,
                y= SELECTION_HEIGHT,
                width= STATS_WIDTH / 2,
                height= STATS_HEIGHT,
            ),
            Container(
                x= BOARD_WIDTH + STATS_WIDTH / 2,
                y= SELECTION_HEIGHT,
                width= STATS_WIDTH / 2,
                height= STATS_HEIGHT,
                components=[
                    Text(
                        x=20,
                        y=10,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Name: "+PlayerManager.players[1].name,
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=30,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Health: "+str(PlayerManager.players[1].health),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=50,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Damage : "+str(PlayerManager.players[1].damage),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=70,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Resources : ",
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=100,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Food : "+str(PlayerManager.players[1].resources.food),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=120,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Coins : "+str(PlayerManager.players[1].resources.coins),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=140,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Wood : "+str(PlayerManager.players[1].resources.wood),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    ),
                    Text(
                        x=20,
                        y=160,
                        width=STATS_WIDTH/2,
                        height=STATS_HEIGHT,
                        text="Iron : "+str(PlayerManager.players[1].resources.iron),
                        color="blue",
                        secondary_color="blue",
                        font=get_font(30)
                    )
                ],
            ),
        ]

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
        )

        self.add_component(self.board)
        self.add_component(self.stats[0])
        self.add_component(self.stats[1])
        self.add_component(self.selection)
        self.add_component(self.draw_card_button)
        self.add_component(self.end_turn_button)
