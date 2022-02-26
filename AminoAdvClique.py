from pyfiglet import figlet_format
from asyncio import get_event_loop
from configs import main_functions
print("""Script by DeLuvSushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminoadvclique", font="slant"))

get_event_loop().run_until_complete(main_functions.main())
