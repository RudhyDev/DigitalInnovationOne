from datetime import date, time, datetime


def trabalhando_com_date():
    
    data_atual = date.today()
    print(data_atual.strftime('%d/%B/%Y'))
    
def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)    
    print(horario)
    
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))


if __name__ == '__main__': #esse if determina qual das funções definidasacima será executada
    #trabalhando_com_time()
    #trabalhando_com_date()
    #trabalhando_com_datetime()
    
    
    #Testezinho para definir qual é o dia da semana atual, porém em portugues
    # semama = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    # print(semama[datetime.now().weekday()])
    
    
    data = input('Digite uma data no formato (dd/mm/aaaa): ')
    data_conver = datetime.strftime(data, '%d/%B/%Y')
    print(data_conver.month) 