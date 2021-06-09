import subprocess
import json


def get_window_list():
    output = subprocess.check_output("""gdbus call \\
  --session \\
  --dest org.gnome.Shell \\
  --object-path /org/gnome/Shell \\
  --method org.gnome.Shell.Eval \"      
    global              
      .get_window_actors()
      .map(a=>a.meta_window)                                   
      .map(w=>({class: w.get_wm_class(), 
                title: w.get_title(), 
                position: {x: w.get_frame_rect().x,
                           y: w.get_frame_rect().y,
                           width: w.get_frame_rect().width,
                           height: w.get_frame_rect().height},
                has_focus: w.has_focus(), 
                pid: w.get_pid(),
                maximized: w.get_maximized(),
                is_fullscreen: w.is_fullscreen(),
                hidden: w.is_hidden()}))\"
      """, shell=True)
    raw_list = str(output, encoding="utf-8")
    return json.loads(raw_list.rsplit("'", 1)[0].split("'", 1)[1])


def get_mouse_position():
    output = subprocess.check_output("""gdbus call \\
  --session \\
  --dest org.gnome.Shell \\
  --object-path /org/gnome/Shell \\
  --method org.gnome.Shell.Eval \"      
    global              
      .get_pointer()\"
      """, shell=True)
    return json.loads(str(output, encoding="utf-8").split("'")[1])


def minimize_window():
    output = subprocess.check_output("""gdbus call \\
  --session \\
  --dest org.gnome.Shell \\
  --object-path /org/gnome/Shell \\
  --method org.gnome.Shell.Eval \"      
    global              
      .display
      .focus_window
      .minimize()\"
      """, shell=True)
    return str(output, encoding="utf-8")


def resize_window():
    output = subprocess.check_output("""gdbus call \\
  --session \\
  --dest org.gnome.Shell \\
  --object-path /org/gnome/Shell \\
  --method org.gnome.Shell.Eval \"      
    global              
      .display
      .focus_window
      .move_resize_frame(true, 300, 200, 1100, 800)\"
      """, shell=True)
    return str(output, encoding="utf-8")


def move_window():
    output = subprocess.check_output("""gdbus call \\
  --session \\
  --dest org.gnome.Shell \\
  --object-path /org/gnome/Shell \\
  --method org.gnome.Shell.Eval \"      
    global              
      .display
      .focus_window
      .move_frame(true, 100, 200)\"
      """, shell=True)
    return str(output, encoding="utf-8")


if __name__ == "__main__":
    for i in get_window_list():
        print(i)
    resize_window()
    move_window()
