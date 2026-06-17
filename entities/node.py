class node:
    def __init__(self, position: tuple[int, int]):
        self.position: tuple[int, int] = position
        self.connections: list[connection] = None
        self.draggable: bool = False

    def add_connection(self, new_connection: tuple[int, int]):
        self.connections.append(new_connection)
        
class connection:
    def __init__(self, start_position: tuple[int, int], end_position: tuple[int, int]):
        self.start_ps: tuple[int, int] = start_position
        self.end_ps: tuple[int, int] = end_position