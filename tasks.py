trainings = {
   'Онбордінг':{
       'відповідальний': 'Григоров О. С.',
       'теми': ['техніка безпеки', 'робота в команді'],
       'дата': '15.05'
   },
   'Підвищення кваліфікації':{
       'відповідальний': 'Череватий К. І.',
       'теми': ['лідерство', 'комп. грамотність'],
       'дата': '20.11'
   }
}
print('Тренінги ProTeam')
print('1-назви тренінгів, 2-інфо про тренінг')
action = input('Номер дії (off-вийти):')
while action != 'off':
   if action == '1':
       for training in trainings:
           print('-', training)
   if action == '2':
       title = input('Назва тренінгу:')
       if title in trainings:
           print(trainings[title]['відповідальний'])
           print(trainings[title]['теми'])
           print(trainings[title]['дата'])
       else:
           print('Такого тренінгу не існує!')
   action = input('Номер дії (off-вийти):')
