import pyray as r


def draw():
    r.begin_drawing()

    r.clear_background(r.BLACK)

    h = int(r.get_screen_height() / 2)
    w = int(r.get_screen_width() / 2)
    r.draw_text("Running on PyRay", w, h - 30, 20, r.GREEN)
    r.draw_text("Hello world!", w, h, 20, r.GREEN)

    r.draw_text(str(counter), r.get_screen_width() - 50, 10, 20, r.GREEN)

    r.end_drawing()


def main():
    r.init_window(800, 500, "Hello")
    r.set_target_fps(60)
    # r.toggle_borderless_windowed()
    counter = 0

    while not r.window_should_close():
        draw()

        if r.is_key_pressed(r.KeyboardKey.KEY_Q):
            r.close_window()

        if r.is_key_pressed(r.KeyboardKey.KEY_F):
            r.toggle_borderless_windowed()

        if r.is_key_pressed(r.KeyboardKey.KEY_UP):
            counter += 1
        if r.is_key_pressed(r.KeyboardKey.KEY_DOWN):
            counter -= 1

    r.close_window()


if __name__ == "__main__":
    main()
