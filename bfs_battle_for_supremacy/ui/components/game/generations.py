from bfs_battle_for_supremacy.ui.root.container import Container
from bfs_battle_for_supremacy.ui.root.text import Text
from bfs_battle_for_supremacy.game_logic.managers.player_manager import (
    PlayerManager,
)
from bfs_battle_for_supremacy.ui.utils import get_font

BOARD_WIDTH = 700
BOARD_HEIGHT = 700
SELECTION_WIDTH = 500
SELECTION_HEIGHT = 400
STATS_WIDTH = 500
STATS_HEIGHT = 200


def generate_selection():
    return Container(
        BOARD_WIDTH,
        0,
        SELECTION_WIDTH,
        SELECTION_HEIGHT,
        [
            Text(
                x=20,
                y=10,
                width=STATS_WIDTH / 2,
                height=STATS_HEIGHT,
                text=str(PlayerManager.current_player_index),
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
            Text(
                x=20,
                y=50,
                width=STATS_WIDTH - 24,
                height=STATS_HEIGHT,
                text="No items selected",
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
            Text(
                x=20,
                y=90,
                width=STATS_WIDTH - 24,
                height=STATS_HEIGHT,
                text="",
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
            Text(
                x=20,
                y=170,
                width=STATS_WIDTH - 24,
                height=STATS_HEIGHT,
                text="",
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
            Text(
                x=20,
                y=210,
                width=STATS_WIDTH - 24,
                height=STATS_HEIGHT,
                text="",
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
            Text(
                x=20,
                y=250,
                width=STATS_WIDTH - 24,
                height=STATS_HEIGHT,
                text="",
                color="red",
                secondary_color="red",
                font=get_font(30),
            ),
        ],
        color="yellow",
    )


def generate_stats():
    return [
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
                    text="Damage : " + str(PlayerManager.players[0].damage),
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
                    text="Damage : " + str(PlayerManager.players[1].damage),
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
