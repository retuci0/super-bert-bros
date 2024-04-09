from game import main

from misc.crash_texts import text as crash_text

import datetime
import traceback


#Run
if __name__ == "__main__":
    try:
        #Try and run the game
        main()
    
    #Error handling
    except Exception as exception:
        #Get current time
        now = datetime.datetime.now()

        #Create the crash report text
        text = f"CRASH REPORT {now.year}-{now.month}-{now.day} at {now.hour}:{now.minute}.{now.second}\n{crash_text}\n\n{traceback.format_exc()}"
        
        #Create the file where the crash report will be written
        file_name = f"crash_logs/crash-{now.year}-{now.month}-{now.day}_{now.hour}.{now.minute}.{now.second}.txt"
        file = open(file_name, "w")
        file.write(text)
        file.close()