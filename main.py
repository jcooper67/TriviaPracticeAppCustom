from ui import Trivia_Ui
from trivia_brain import Trivia_Brain
from database_manager import Database_Manager
#Initializing Trivia Brain To Pass Through To Trivia UI
trivia_brain = Trivia_Brain()

database_manager = Database_Manager()


#Opening Screen
trivia_ui = Trivia_Ui(trivia_brain,database_manager)





