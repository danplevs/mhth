import schedule
from sensors import main

if __name__ == "__main__": 
    schedule.every(5).minutes.do(main)
