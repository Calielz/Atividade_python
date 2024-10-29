semana = {'segunda':["desenvolvimento web"],'terça':["Python"],'quarta':["banco de dados"],
          'quinta':["computação em nuvem"],'sexta':["revisão de alguma matéria"],
          'sábado':[" "], 'domingo':[" "]}

print(semana.get('segunda'))

disciplinas = semana.get('quarta')
print("minha matéria favorita é:", disciplinas)

