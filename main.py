from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

WALL_COLOR = color.rgb(244, 244, 244)
FLOOR_COLOR = color.rgb(68, 68, 68)

if __name__ == '__main__':
    # Ursina
    app = Ursina()
    # 중간 복도 생성
    main_floor = Entity(model='cube', position=(0, 0, 0), scale=(10, 1, 100), collider='box',
                        color=FLOOR_COLOR)
    main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(10, 1, 100), collider='box',
                          color=FLOOR_COLOR)
    main_left_wall = Entity(model='cube', position=(-5, 5, -5), scale=(1, 10, 110), collider='box',
                            color=WALL_COLOR)
    main_right_wall = Entity(model='cube', position=(5, 5, 5), scale=(1, 10, 110), collider='box',
                            color=WALL_COLOR)
    for i in range(-110, 111):
        main_tiles = Entity(model='cube', position=(0, 0.5, i*0.5), scale=(0.5, 0, 0.5),
                            texture='Asset/yellow_tile.jpg')
    # 앞쪽 복도 생성
    front_floor = Entity(model='cube', position=(-25, 0, 55), scale=(60, 1, 10),
                         color=FLOOR_COLOR, collider='box')
    front_ceiling = Entity(model='cube', position=(-25, 10, 55), scale=(60, 1, 10),
                           color=FLOOR_COLOR, collider='box')
    front_left_wall = Entity(model='cube', position=(-30, 5, 50), scale=(50, 10, 1),  collider='box',
                            color=WALL_COLOR)
    front_right_wall = Entity(model='cube', position=(-20, 5, 60), scale=(50, 10, 1), collider='box',
                            color=WALL_COLOR)
    for i in range(-50, 50):
        main_tiles = Entity(model='cube', position=(-25 + i*0.5, 0.5, 55), scale=(0.5, 0, 0.5),
                            texture='Asset/yellow_tile.jpg')
    front_floor_2 = Entity(model='cube', position=(-50, 0, 80), scale=(10, 1, 60),
                           color=FLOOR_COLOR, collider='box')
    front_ceiling_2 = Entity(model='cube', position=(-50, 10, 80), scale=(10, 1, 60),
                             color=FLOOR_COLOR, collider='box')
    front_left_wall_2 = Entity(model='cube', position=(-55, 5, 75), scale=(1, 10, 50), collider='box',
                            color=WALL_COLOR)
    front_right_wall_2 = Entity(model='cube', position=(-45, 5, 85), scale=(1, 10, 50), collider='box',
                            color=WALL_COLOR)
    for i in range(-50, 51):
        main_tiles = Entity(model='cube', position=(-50, 0.5, 80 + i*0.5), scale=(0.5, 0, 0.5),
                            texture='Asset/yellow_tile.jpg')
    # 뒷쪽 복도 생성
    back_floor = Entity(model='cube', position=(25, 0, -55), scale=(60, 1, 10), color=FLOOR_COLOR, collider='box')
    back_ceiling = Entity(model='cube', position=(25, 10, -55), scale=(60, 1, 10), color=FLOOR_COLOR, collider='box')
    back_left_wall = Entity(model='cube', position=(30, 5, -50), scale=(50, 10, 1), collider='box',
                            color=WALL_COLOR)
    back_right_wall = Entity(model='cube', position=(20, 5, -60), scale=(50, 10, 1), collider='box',
                            color=WALL_COLOR)
    for i in range(-50, 50):
        main_tiles = Entity(model='cube', position=(25 + i*0.5, 0.5, -55), scale=(0.5, 0, 0.5),
                            texture='Asset/yellow_tile.jpg')
    back_floor_2 = Entity(model='cube', position=(50, 0, -80), scale=(10, 1, 60), color=FLOOR_COLOR, collider='box')
    back_ceiling_2 = Entity(model='cube', position=(50, 10, -80), scale=(10, 1, 60), color=FLOOR_COLOR, collider='box')
    back_left_wall_2 = Entity(model='cube', position=(55, 5, -75), scale=(1, 10, 50), collider='box',
                            color=WALL_COLOR)
    back_right_wall_2 = Entity(model='cube', position=(45, 5, -85), scale=(1, 10, 50), collider='box',
                            color=WALL_COLOR)
    for i in range(-50, 51):
        main_tiles = Entity(model='cube', position=(50, 0.5, -80 + i*0.5), scale=(0.5, 0, 0.5),
                            texture='Asset/yellow_tile.jpg')
    # 표지판 생성
    sign_ceiling = Entity(model='cube', position=(0, 9, 25), scale=(5.2, 1, 0.1),
                          texture='Asset/exit_8_ceiling.jpg')
    sign_wall_front = Entity(model='cube', position=(-54.4, 4.5, 55), scale=(0.1, 3.8, 2),
                             texture='Asset/exit_8_wall.jpg')
    sign_wall_back = Entity(model='cube', position=(-4.4, 4.5, -55), scale=(0.1, 3.8, 2),
                            texture='Asset/exit_8_wall.jpg')
    # 플레이어 컨트롤
    #EditorCamera() *디버그 에디터 카메라*
    player = FirstPersonController()
    player.cursor.visible = False
    player.gravity = 1
    player.speed = 10
    # 게임 요소 업데이트
    def update():
        if player.position.x < -25 and 50 < player.position.z:
            player.set_position((player.position.x + 50, player.position.y, player.position.z - 110))
        elif 25 < player.position.x and player.position.z < -50:
            player.set_position((player.position.x - 50, player.position.y, player.position.z + 110))
    # 게임 실행
    app.run()