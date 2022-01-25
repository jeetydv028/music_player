from cx_Freeze import *
includefiles = ['music30.ico']
excludes = []
package = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
shortcut_table = [
    ( "DesktopShortcut"
    "DesktopFolder"
    "music Player"
    "TARGETDIR"
    "[TARGETDIR]\musicplayer.exe",
    None, #Aruments
    None, #Sescription
    None, #Hotkey
    None, #Icon
    None, #IconIndex
    None, #ShowCmd
    "TARGETDIR", # WKdir
    )
]
msi_data = {"Shortcut":shortcut_table}
bdist_msi_option = {'data': msi_data}
setup(
    version = "0.1",
    description = "simple music player developed by jitendra",
    author = "Jitendra k yadav",
    options = {'build_exe':{'inclide_files': includefiles},"bdist_msi":bdist_msi_option,},
    executables = [
        Executable(
            script = "musicplayer.py",
            base = base,
            icon = 'music30.ico'
     )
    ]
    )






