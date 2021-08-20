from crontab import CronTab


t = 0
while(t < 1):
    cron = CronTab(user='neves')
    job = cron.new(command='python /home/neves/Área de trabalho/Coisas semi importantes/    Projetos/ScriptEntrarNaAula/Main.py')
    job.minute.on(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55)

    cron.write()