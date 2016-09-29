__author__ = 'William'
import cx_Freeze

executables = [cx_Freeze.Executable("SnakeGamePyGame.py")]

cx_Freeze.setup(name="SnakeyGame",
                options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakehead.png"]}},
                description = "Snakey game... just eat the apple",
                version = "1.0.0",
                executables = executables
                )