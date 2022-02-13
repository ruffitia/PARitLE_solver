
i=1
k=0
wrong_characters=[] #contiene le lettere sbagliate
wrg_position_index=[] #indici delle lettere nella posizione sbagliata
crr_position_index=[] #indici delle lettere nella posizione corretta
wrg_index=[] #array che contiene gli indici delle lettere che non ci devono essere
cc=[]
correct_char=[] 
correct_char_index=[]
cond=False 
count=0

while cond == False :
  sentinella = 1;
  #gli array vanno inizializzati ad ogli ciclo
  #perchè altrimenti gli indici si sovrappongono
  wrg_index=[]
  crr_position_index=[] 
  wrg_position_index=[]

  print("\n*********Livello ", i, "*********")
  #richiesta di dati
  word=input("Parola inserita:  ")
  print("                  01234")

  #Lettere corrette
  j=0
  num1=int(input("Numero di lettere nella giusta posizione: "))
  for j in range(0, num1) :
    var=int(input("Indice della lettera nella giusta posizione:  "))
    crr_position_index.append(var)
    cc.append(word[var])
    correct_char.append(word[var])
    correct_char_index.append(var)
    count +=1


  #Lettere nella posizione sbagliata
  j=0
  num2=int(input("Numero di lettere non nella giusta posizione: "))
  for j in range(0, num2) :
    var=int(input("Indice della lettera corretta, ma non nella giusta posizione: "))
    wrg_position_index.append(var)
    cc.append(word[var])

  #Lettere errate
  j=0
  num3=int(input("Numero di lettere errate: "))
  for j in range(0, num3):
    var=int(input("Indice della lettera errata:  "))
    wrg_index.append(var)
    wrong_characters.append(word[wrg_index[j]])

  #print(crr_position_index)
  #print(wrg_position_index)
  #print(wrg_index)
  print(wrong_characters)
  print(cc)
  print("\n")
  print(correct_char)
  print(correct_char_index)

  finded_word= open("parole_trovate.txt", 'w')
  with open("possible_word .txt", 'r') as a_file:
    for line in a_file:
      stripped_line = line.strip("\n")
      sentinella1 = 1; #controllo lettere corrette nella giusta posizione
      sentinella2 = 1; #controllo che non ci siano lettere sbagliate
      sentinella3 = 1; #eliminazione delle parole in cui le lettere nella sbaglita posizione sono in quella posizione
      sentinella4 = 0; # controllo che all'interno della parola ci siano le lettere corrette (indifferentemente dalla posizione)
      sentinella5=0; #le giuste lettere devono stare sempre nelle giuste posizioni
      
      #lettere nella giusta posizione
      k=0;
      for k in range(len(crr_position_index)):
        if not (stripped_line[crr_position_index[k]] == word[crr_position_index[k]]) :
          sentinella1= 0;

      #lettere che non ci devono essere
      k=0;
      j=0;
      if sentinella1 == 1 :
        for k in range(5):
          for j in range(len(wrong_characters)) :
            if stripped_line[k] == wrong_characters[j] :
              sentinella2 = 0;
            
      
      #lettere nella posizione sbagliata
      k=0;
      j=0;
      if sentinella1 == 1 and sentinella2 == 1 and len(wrg_position_index)>0:
         for k in range(len(wrg_position_index)) :
          if word[wrg_position_index[k]] == stripped_line[wrg_position_index[k]]:
            sentinella3 = 0;

      #sentinella5
      k=0;
      j=0;
      z=0;
      for k in range(5):
        for j in range(len(correct_char_index)) :
          if k == correct_char_index[j]:
            if stripped_line[k]==correct_char[j] :
              sentinella5 = 1;
      
      #sentinella4
      k=0
      j=0
      for k in range(5) :
        for j in range(len(cc)):
          if stripped_line[k] == cc[j] :
            sentinella4 = 1;


      if sentinella1 == 1 and sentinella2 == 1 and sentinella3 == 1 and sentinella4 == 1 and sentinella5 == 1:
        finded_word.write(line)
      
      

  finded_word.close()
  '''
  print("\n*********************\n")
  var=input("\nParola trovata?  ")
  i +=1
  if var == 1 :
    cond = True
  '''
  i +=1
      

  