"""
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
import os
import subprocess

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])

def hide_show_bar(qtile):
    bar = qtile.current_screen.top
    if bar.size == 0:
        bar.size = 25
        bar.window.unhide()
    else:
        bar.size = 0
        bar.window.hide()
    qtile.current_group.layoutAll()


mod = "mod4"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    # Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    # Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    # Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Key([mod, "control"], "i", lazy.layout.grow(), desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "t", lazy.spawn(terminal + " -e gtop"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="Fira Code",
        background="#000000",
        foreground="#ffffff",
        #selected_background="#079822",
        #selected_foreground="#fff",
        #dmenu_height=25,
        ))),
    # Apps:
    Key([mod], "w", lazy.spawn("firefox")),
    Key([mod, "shift"], "Return", lazy.spawn("kitty -e ranger")),
    Key([mod, "shift"], "d", lazy.function(hide_show_bar)),
    Key([mod], "u", lazy.spawn("pavucontrol")),
    Key([mod], "f", lazy.window.toggle_floating),
    Key([mod, "shift"], "c", lazy.spawn("/home/hydra/dmscripts/dmconf")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "b", lazy.spawn("blueberry")),
    Key([mod], "x", lazy.spawn("betterlockscreen -l")),
    #Key([mod, "shift"], "r", lazy.spawn("killall volumeicon ; volumeicon"),
    #Key("XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    #Key("XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    #Key("XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),
]
# groups = [
#         Group("???", layout="Max"),
#         Group("???", spawn="firefox", layout="Max"),          
#         Group("???", spawn="kitty", layout="MonadTall"),
#         Group("???", layout="MonadTall"),
#         Group("???", layout="MonadTall"),
#         Group("???", layout="MonadTall"),
#         ]
groups = [
        Group("code", layout="Max"),
        Group("www", spawn="firefox", layout="Max"),          
        Group("sys", spawn="kitty", layout="MonadTall"),
        Group("dox", layout="MonadTall"),
        Group("vid", layout="MonadTall"),
        Group("slack", layout="MonadTall"),
        ]
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)
# groups = [Group(i) for i in "1234567890"]
# 
# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )
layout_theme = {
    "border_width": 1,
    #"margin": 0,
    "border_focus": "fb4934",
    #"border_normal": "1D2330",
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.MonadTall(**layout_theme),
    layout.Max(),
    # layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=13,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method="text"),
                # widget.TextBox(text="|"),
                #widget.TextBox(text=" "),
                widget.Sep(linewidth=1, padding=10),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                widget.TextBox(text=" "),
                # widget.TextBox(text="|"),
                widget.CurrentLayout(),
                widget.Sep(linewidth=1, padding=10),
                widget.CPU(format="CPU: {load_percent}%"),
                widget.Sep(linewidth=1, padding=10),
                widget.Memory(
                    # measure_mem="G",
                    format="RAM: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                ),
                # widget.Sep(linewidth = 1, padding = 10),
                # widget.Net(interface='wlp3s0'),
                widget.Sep(linewidth=1, padding=10),
                # widget.TextBox(font="FontAwesome", text=" ??? "),
                # widget.TextBox(text="BATT:"),
                # widget.Wlan(interface="wlp3s0", format="wlp3s0: {essid} {percent: 2.0%}"),
                # widget.TextBox(text="|"),
                # widget.Sep(linewidth=1, padding=10),
                widget.Systray(icon_size=20, padding=1),
                # widget.BatteryIcon(theme_path="/usr/share/icons/breeze-dark/status/24", update_interval=1),
                # widget.Battery(format="{percent:2.0%}", update_interval=60),
                widget.Sep(linewidth=1, padding=10),
                widget.Clock(format="%H:%M "),
                # widget.QuickExit(),
            ],
            23,
            opacity=0.90,
            background="#000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# dgroups_key_binder = None
# dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pavucontrol"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
