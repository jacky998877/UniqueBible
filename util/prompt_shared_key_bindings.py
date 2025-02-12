import config
from prompt_toolkit.key_binding import KeyBindings

prompt_shared_key_bindings = KeyBindings()

# selection

# select all
@prompt_shared_key_bindings.add("c-a")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = 0
    buffer.start_selection()
    buffer.cursor_position = len(buffer.text)

# navigation

# move left
@prompt_shared_key_bindings.add("left")
def _(event):
    buffer = event.app.current_buffer
    if buffer.cursor_position > 0:
        buffer.cursor_position = buffer.cursor_position - 1
# move right
@prompt_shared_key_bindings.add("right")
def _(event):
    buffer = event.app.current_buffer
    if buffer.cursor_position < len(buffer.text):
        buffer.cursor_position = buffer.cursor_position + 1

# go to current line starting position
@prompt_shared_key_bindings.add("c-j")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = buffer.cursor_position - buffer.document.cursor_position_col
# go to current line ending position
@prompt_shared_key_bindings.add("c-e")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = buffer.cursor_position + buffer.document.get_end_of_line_position()
# go to current line starting position
@prompt_shared_key_bindings.add("home")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = buffer.cursor_position - buffer.document.cursor_position_col
# go to current line ending position
@prompt_shared_key_bindings.add("end")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = buffer.cursor_position + buffer.document.get_end_of_line_position()
# go to the end of the text
@prompt_shared_key_bindings.add("escape", "e")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = len(buffer.text)
# go to the beginning of the text
@prompt_shared_key_bindings.add("escape", "j")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_position = 0

# scrolling

# go up 10 lines
@prompt_shared_key_bindings.add("escape", "1")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(10)
# go up 20 lines
@prompt_shared_key_bindings.add("escape", "2")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(20)
# go up 30 lines
@prompt_shared_key_bindings.add("escape", "3")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(30)
# go up 40 lines
@prompt_shared_key_bindings.add("escape", "4")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(40)
# go up 50 lines
@prompt_shared_key_bindings.add("escape", "5")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(50)
# go up 60 lines
@prompt_shared_key_bindings.add("escape", "6")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(60)
# go up 70 lines
@prompt_shared_key_bindings.add("escape", "7")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(70)
# go up 80 lines
@prompt_shared_key_bindings.add("escape", "8")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(80)
# go up 90 lines
@prompt_shared_key_bindings.add("escape", "9")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(90)
# go up 100 lines
@prompt_shared_key_bindings.add("escape", "0")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(100)
# go down 10 lines
@prompt_shared_key_bindings.add("f1")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(10)
# go down 20 lines
@prompt_shared_key_bindings.add("f2")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(20)
# go down 30 lines
@prompt_shared_key_bindings.add("f3")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(30)
# go down 40 lines
@prompt_shared_key_bindings.add("f4")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(40)
# go down 50 lines
@prompt_shared_key_bindings.add("f5")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(50)
# go down 60 lines
@prompt_shared_key_bindings.add("f6")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(60)
# go down 70 lines
@prompt_shared_key_bindings.add("f7")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(70)
# go down 80 lines
@prompt_shared_key_bindings.add("f8")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(80)
# go down 90 lines
@prompt_shared_key_bindings.add("f9")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(90)
# go down 100 lines
@prompt_shared_key_bindings.add("f10")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(100)
# go up number of lines which users define in config
@prompt_shared_key_bindings.add("pageup")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(config.terminalEditorScrollLineCount)
# go down number of lines which users define in config
@prompt_shared_key_bindings.add("pagedown")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(config.terminalEditorScrollLineCount)
# go up number of lines which users define in config
@prompt_shared_key_bindings.add("c-b")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_up(config.terminalEditorScrollLineCount)
# go down number of lines which users define in config
@prompt_shared_key_bindings.add("c-y")
def _(event):
    buffer = event.app.current_buffer
    buffer.cursor_down(config.terminalEditorScrollLineCount)

# clipboard

# copy text to clipboard
@prompt_shared_key_bindings.add("c-c")
def _(event):
    buffer = event.app.current_buffer
    data = buffer.copy_selection()
    #get_app().clipboard.set_data(data)
    config.mainWindow.copy(data.text, False)
# paste clipboard text
@prompt_shared_key_bindings.add("c-v")
def _(event):
    buffer = event.app.current_buffer
    buffer.insert_text(config.mainWindow.getclipboardtext(False))
# cut text to clipboard
@prompt_shared_key_bindings.add("c-x")
def _(event):
    buffer = event.app.current_buffer
    data = buffer.cut_selection()
    #get_app().clipboard.set_data(data)
    config.mainWindow.copy(data.text, False)

# change text

# delete text, Ctrl+H or Backspace
@prompt_shared_key_bindings.add("c-h")
def _(event):
    buffer = event.app.current_buffer
    data = buffer.cut_selection()
    # delete one char before cursor as Backspace usually does when there is no text selection.
    if not data.text and buffer.cursor_position >= 1:
        buffer.start_selection()
        buffer.cursor_position = buffer.cursor_position - 1
        buffer.cut_selection()

# insert text with TAB key
@prompt_shared_key_bindings.add("c-i")
def _(event):
    buffer = event.app.current_buffer
    buffer.insert_text(config.terminalEditorTabText)
