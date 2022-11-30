from libqtile import layout
from libqtile.config import Match

from utils import color

layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": color['fg'],
    "border_normal": color['bg'],
    "font": "JetBrainsMono Nerd Font",
    "grow_amount": 1,
}

layouts = [
    layout.Bsp(**layout_theme, fair=False, border_on_single=True),
    layout.Columns(**layout_theme, insert_position=1, border_on_single=True),
    layout.MonadTall(**layout_theme, ratio=0.65),
    layout.Floating(**layout_theme),
]

floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # TODO add matches
    ],
)
