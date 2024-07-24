

def dia_escrito(dia):
    if dia==1:
        dies= ' Ao um'
        return(dies)
    elif dia==2:
        dies= 'Aos dois'
        return(dies)
    elif dia==3:
        dies= 'Aos três'
        return(dies)
    elif dia==4:
        dies= 'Aos quatro'
        return(dies)
    elif dia==5:
        dies= 'Aos cinco'
        return(dies)
    elif dia==6:
        dies= 'Aos seis'
        return(dies)
    elif dia==7:
        dies= 'Aos sete'
        return(dies)
    elif dia==8:
        dies= 'Aos oito'
        return(dies)
    elif dia==9:
        dies= 'Aos nove'
        return(dies)
    elif dia==10:
        dies= 'Aos dez'
        return(dies)
    elif dia==11:
        dies= 'Aos onze'
        return(dies)
    elif dia==12:
        dies= 'Aos doze'
        return(dies)
    elif dia==13:
        dies= 'Aos treze'
        return(dies)
    elif dia==14:
        dies= 'Aos quatorze'
        return(dies)
    elif dia==15:
        dies= 'Aos quinze'
        return(dies)
    elif dia==16:
        dies= 'Aos dezesseis'
        return(dies)
    elif dia==17:
        dies= 'Aos dezessete'
        return(dies)
    elif dia==18:
        dies= 'Aos dezoito'
        return(dies)
    elif dia==19:
        dies= 'Aos dezenove'
        return(dies)
    elif dia==20:
        dies= 'Aos vinte'
        return(dies)
    elif dia==21:
        dies= 'Aos vinte e um'
        return(dies)
    elif dia==22:
        dies= 'Aos vinte e dois'
        return(dies)
    elif dia==23:
        dies= 'Aos vinte e três'
        return(dies)
    elif dia==24:
        dies= 'Aos vinte e quatro'
        return(dies)
    elif dia==25:
        dies= 'Aos vinte e cinco'
        return(dies)
    elif dia==26:
        dies= 'Aos vinte e seis'
        return(dies)
    elif dia==27:
        dies= 'Aos vinte e sete'
        return(dies)
    elif dia==28:
        dies= 'Aos vinte e oito'
        return(dies)
    elif dia==29:
        dies= 'Aos vinte e nove'
        return(dies)
    elif dia==30:
        dies= 'Aos trinta'
        return(dies)
    elif dia==31:
        dies= 'Aos trinta e um'
        return(dies)


def mes_escrito(dia):
    if dia==1:
        dies= ' janeiro'
        return(dies)
    elif dia==2:
        dies= 'fevereiro'
        return(dies)
    elif dia==3:
        dies= 'março'
        return(dies)
    elif dia==4:
        dies= 'abril'
        return(dies)
    elif dia==5:
        dies= 'maio'
        return(dies)
    elif dia==6:
        dies= 'junho'
        return(dies)
    elif dia==7:
        dies= 'julho'
        return(dies)
    elif dia==8:
        dies= 'agosto'
        return(dies)
    elif dia==9:
        dies= 'setembro'
        return(dies)
    elif dia==10:
        dies= 'outubro'
        return(dies)
    elif dia==11:
        dies= 'novembro'
        return(dies)
    elif dia==12:
        dies= 'dezembro'
        return(dies)

def ano_escrito(dia):
    if dia==2022:
        dies= ' dois mil e vinte e dois'
        return(dies)
    elif dia==2023:
        dies= 'dois mil e vinte e três'
        return(dies)
    elif dia==2024:
        dies= 'dois mil e vinte e quatro'
        return(dies)
    elif dia==2025:
        dies= 'dois mil e vinte e cinco'
        return(dies)
    elif dia==2026:
        dies= 'dois mil e vinte e seis'
        return(dies)
    elif dia==2027:
        dies= 'dois mil e vinte e sete'
        return(dies)
    elif dia==2028:
        dies= 'dois mil e vinte e oito'
        return(dies)
    elif dia==2029:
        dies= 'dois mil e vinte e nove'
        return(dies)
    elif dia==2030:
        dies= 'dois mil e trinta'
        return(dies)
    elif dia==2031:
        dies= 'dois mil e trinta e um'
        return(dies)
    else:

        dies= 'dois mil e alguma coisaXXXXXX'
        return(dies)

    
print(dia_escrito(26),'de',mes_escrito(12),ano_escrito(2024))