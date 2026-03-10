import schedule
import time

def tarefa():
    print("eventos da semana")
schedule.every().week.do(tarefa)

while True:
    schedule.run_pending()