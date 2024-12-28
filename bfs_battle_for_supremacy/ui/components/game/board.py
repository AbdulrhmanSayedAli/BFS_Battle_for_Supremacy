from typing import Callable
from bfs_battle_for_supremacy.ui.root import Container
from bfs_battle_for_supremacy.ui.components.game.tile import Tile
from bfs_battle_for_supremacy.config import (
    BOARD_SIZE_WIDTH,
    BOARD_SIZE_HEIGHT,
    IMAGES_PATH,
)
import os
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.entities.square import Square
import asyncio
import threading
from bfs_battle_for_supremacy.game_logic.managers.player_manager import PlayerManager
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.rock import Rock
class Board(Container):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self._tiles = self.setup_tiles(width, height)
        components = [tile for row in self.tiles for tile in row]
        super().__init__(
            x, y, width, height, components, on_click, on_hover, on_hover_end
        )

    @property
    def tiles(self) -> list[list[Tile]]:
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        self._tiles = tiles
        self.components = [tile for row in tiles for tile in row]
        print(self.components)

    def setup_tiles(self, width, height) -> list[list[Tile]]:
        tile_height = height / BOARD_SIZE_HEIGHT
        tile_width = width / BOARD_SIZE_WIDTH
        res: list[list[Tile]] = []
        for i in range(BOARD_SIZE_HEIGHT):
            cur_res: list[Tile] = []
            for j in range(BOARD_SIZE_WIDTH):
                square = MapManager.game_map.get_square(i,j)
                if square.is_empty:
                    cur_res.append(
                        Tile(
                            j * tile_width,
                            i * tile_height,
                            tile_width,
                            tile_height,
                            j,
                            i,
                            square,
                            on_click=lambda c, e: self.select_tile(c),
                        )
                    )
                else:
                    if square.content == PlayerManager.players[0]:
                        cur_res.append(
                        Tile(
                            j * tile_width,
                            i * tile_height,
                            tile_width,
                            tile_height,
                            j,
                            i,
                            square,
                            on_click=lambda c, e: self.select_tile(c),
                            image_path= os.path.join(IMAGES_PATH, "player1.webp")
                        )
                        )
                        print("")
                    elif square.content ==PlayerManager.players[1]:
                        cur_res.append(
                        Tile(
                            j * tile_width,
                            i * tile_height,
                            tile_width,
                            tile_height,
                            j,
                            i,
                            square,
                            on_click=lambda c, e: self.select_tile(c),
                            image_path= os.path.join(IMAGES_PATH, "player2.webp")
                        )
                        )
                    elif isinstance(square.content,Card):
                        print("")
                    elif isinstance(square.content,Rock):
                        cur_res.append(
                        Tile(
                            j * tile_width,
                            i * tile_height,
                            tile_width,
                            tile_height,
                            j,
                            i,
                            square,
                            on_click=lambda c, e: self.select_tile(c),
                            image_path= os.path.join(IMAGES_PATH, "rock.png")
                        )
                        )
                        print("")
                        
            res.append(cur_res)
        #res[0][0].image_path = os.path.join(IMAGES_PATH, "player1.webp")
        #res[BOARD_SIZE_HEIGHT - 1][BOARD_SIZE_WIDTH - 1].image_path = (
        #    os.path.join(IMAGES_PATH, "player2.webp")
        #)
        return res

    def select_tile(self, tile):
        tile: Tile = tile
        print("tests")
        print(tile.pos_x,tile.pos_y)
        print(tile.square.row,tile.square.column)
        threading.Thread(target=PlayerManager.select_square_for_current_player, args=(tile.square,)).start()
        # asyncio.create_task(PlayerManager.select_square_for_current_player(square=tile.square))
        #asyncio.run(MapManager.select_square(square=Square(column=tile.y,
        #                                      row=tile.x,
        #                                       ),
        #                                       current_player=PlayerManager.players[PlayerManager.current_player_index]))

        