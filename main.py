
accountList={}
accountList[0]="emailperlatesi@gmail.com"
accountList[1]="emailperlatesi2@gmail.com"
print('Seleziona l\'account da utilizzare, inserisci:\n 1. per l\'account iscritto a canali "controversi"\n 2. per l\'account "pulito"  ')
account=int(input())
metodo=input('Seleziona il metodo di esplorazione, inserisci:\n 1. per seguire i video successivi\n 2. per guardare i correlati  ')
tempo_osservazione=int(input('Inserisci il tempo di osservazione desiderato (in secondi):'))
query=input('Inserisci la parola o frase che vuoi cercare su youtube:')
steps=int(input('Inserisci il numero di steps da eseguire:'))

if(metodo=="1"):
    exec(open("exploreByNext.py").read(),{'account':accountList[account-1],'tempo_osservazione':tempo_osservazione,'steps':steps})
else:
    exec(open("exploreByRelated.py").read(),{'account':account,'tempo_osservazione':tempo_osservazione,'steps':steps})