import iterm2
import random

# Grimoire Source ID: 2gehlk53afg7

themes_to_skip = [
    'Afterglow',
'Arthur',
'BirtsOfParadise',
'Brogrammer',
'Chalk',
'Darkside',
'DoomOne',
'DoomOne',
'Earthsong',
'HaX0R_BLUE',
'IC_Green_PPL',
'IR_Black',
'Lab Fox',
'Later This Evening',
'Light Background',
'LiquidCarbon',
'Mariana',
'Mathias',
'Misterioso',
'Monokai Vivid',
'N0tch2k',
'Neopolitan',
'Retro',
'Rippedcasts',
'Ryuuko',
'Smyck',
'Solarized Light',
'SpaceGray',
'Spiderman',
'SynthwaveAlpha',
'Tango Light',
'Teerb',
'The Hulk',
'UltraViolent',
'Urple',
'WildCherry',
'kanagawabones',
'nord',
'seoulbones_dark',
'shades-of-purple',
'wilmersdorf',
'zenburned',
]


async def SetPresetInSession(connection, session, preset_name):
    preset = await iterm2.ColorPreset.async_get(connection, preset_name)
    if not preset:
        return
    profile = await session.async_get_profile()
    if not profile:
        return
    await profile.async_set_color_preset(preset)

async def main(connection):
    app = await iterm2.async_get_app(connection)
    async with iterm2.NewSessionMonitor(connection) as mon:
        while True:
            session_id = await mon.async_get()
            session = app.get_session_by_id(session_id)
            if session:
                color_preset_names = await iterm2.ColorPreset.async_get_list(connection)
                for theme_to_skip in themes_to_skip:
                    if theme_to_skip in color_preset_names:
                        color_preset_names.remove(theme_to_skip)
                new_theme = random.choice(color_preset_names)
                await session.tab.async_set_title(f"Theme: {new_theme}")
                await SetPresetInSession(connection, session, new_theme)

iterm2.run_forever(main)
