from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

from core.keys import keys, mod, shift
from utils.settings import workspace_names

workspaces = [
    {"name": workspace_names[0], "key": "1", "matches": [], "lay": "bsp"},
    {"name": workspace_names[1], "key": "2", "matches": [Match(wm_class="code-oss")], "lay": "columns"},
    {"name": workspace_names[2], "key": "3", "matches": [], "lay": "columns"},
    {"name": workspace_names[3], "key": "4", "matches": [Match(wm_class="discord")], "lay": "bsp"},
    {"name": workspace_names[4], "key": "5", "matches": [Match(wm_class="Spotify")], "lay": "bsp"},
    {"name": workspace_names[5], "key": "6", "matches": [], "lay": "bsp"},
    {"name": workspace_names[6], "key": "7", "matches": [Match(wm_class="cypress")], "lay": "bsp"},
]

groups = [Group(i) for i in "123456789"]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            workspace["key"],
            *(
                lazy.window.togroup(workspace["name"]),
                lazy.group[workspace["name"]].toscreen(toggle=True),
            ),
            desc="Move focused window to another group",
        )
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "btop-term",
                "kitty btop",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
        ],
    )
)
