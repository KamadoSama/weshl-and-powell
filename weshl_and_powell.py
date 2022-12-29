"""   A -- B -- C
  /    |    |
 D      E -- F
  \    |    |
   G -- H -- I
"""

matrix = [
  [0, 1, 0, 1, 1, 1, 1, 1, 0],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 0, 1, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 1, 0],
]



def sommet_degre(matrix):

  matrix_degre = []
  for i in range(len(matrix)):
    tab = []
    tab.append(i)
    tab.append(sum(matrix[i]))
    tab.append('')
    matrix_degre.append(tab)
  return matrix_degre

matrix_trie_par_degre = sorted(sommet_degre(matrix), key=lambda x: x[1],reverse=True)



def coloration(matrix_degre_trie):
  
  list_adj_color = []
  
  colorier = []
  couleur = ['Rouge','Vert','Bleu','Jaune','Rose','marron','gris','violet']

  matrix_degre_trie[0][2]= couleur[0]

  colorier.append(matrix_degre_trie[0])
  
  for j in matrix_degre_trie:
    list_adj_color = []
    
    if j[0] == colorier[0][0]:
      continue
    for s in colorier:
      
      if matrix[s[0]][j[0]] == 1:
        
        list_adj_color.append(s[2]) 

      
    
    """for color in couleur:
      if color in list_non_adj and color not in list_adj_color:
        j[2] = color
        break"""
        
    for color in couleur:
      if color not in list_adj_color:
          j[2] = color
          break

    

    colorier.append(j)

  return colorier
    




print(f'{sommet_degre(matrix)}\n \n {matrix_trie_par_degre} \n \n {coloration(matrix_trie_par_degre)}')






