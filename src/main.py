import pyray as r
import math

DEFAULT_FONT_SIZE = 40
DEFAULT_FONT_SPACING = DEFAULT_FONT_SIZE + 10
DEFAULT_TEXT_COLOR = r.WHITE


def draw(counter):
    r.begin_drawing()

    r.clear_background(r.BLACK)

    r.draw_fps(10, 10)

    h = int(r.get_screen_height() / 2)
    w = int(r.get_screen_width() / 2) - (200)
    r.draw_text(
        "Running on PyRay",
        w,
        h - DEFAULT_FONT_SPACING,
        DEFAULT_FONT_SIZE,
        DEFAULT_TEXT_COLOR,
    )
    r.draw_text("Hello world!", w, h, DEFAULT_FONT_SIZE, DEFAULT_TEXT_COLOR)

    if counter == 0:
        color = r.GRAY
    elif counter > 0:
        color = r.GREEN
    else:
        color = r.RED

    r.draw_text(
        str(counter),
        r.get_screen_width() - math.floor(DEFAULT_FONT_SIZE * 1.5),
        math.floor(DEFAULT_FONT_SIZE / 1.5),
        math.floor(DEFAULT_FONT_SIZE / 1.25),
        color,
    )

    r.end_drawing()


def set_keyboard_shortcuts(counter: int) -> int:
    if r.is_key_pressed(r.KeyboardKey.KEY_Q):
        r.close_window()

    if r.is_key_pressed(r.KeyboardKey.KEY_F):
        r.toggle_borderless_windowed()

    if r.is_key_pressed(r.KeyboardKey.KEY_R):
        return 0

    if r.is_key_pressed(r.KeyboardKey.KEY_UP):
        return counter + 1
    if r.is_key_pressed(r.KeyboardKey.KEY_DOWN):
        return counter - 1
    
    return counter


def main():
    r.init_window(800, 500, "Hot reload with raylib python")
    r.set_target_fps(60)

    counter: int = 0

    while not r.window_should_close():
        draw(counter)

        counter = set_keyboard_shortcuts(counter)

    r.close_window()


if __name__ == "__main__":
    main()
