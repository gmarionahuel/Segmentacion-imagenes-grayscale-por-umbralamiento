# Funcion para ver tamaño, máximo y mínimo de la imagen
def caracteristicas(img):     #ver tamaño de la imagen en px
  print('size = ',img.shape)
  print('max  = ',np.max(img))
  print('min  = ',np.min(img))
  
  
  #Segmentacion por umbral t
  
  def segmenta (img,t):   #segmentar la imagen según supere o no un umbral dado como parametro
  (F,C) = img.shape;
  Y = np.zeros((F,C)) ;  #matriz de ceros del tamaño de la imagen con la que se llama a la función
  area = 0 ;             #contador
  for i in range (F):    #Filas
    for j in range(C):   #Columnas
      if img[i,j] > t:
        Y[i,j] = 255
        area = area + 1;
      else:
        Y[i,j] = 0;
   
  plt.imshow(Y);
  print('area = ',area,'px')
  
  
  # En caso de imágenes con pobre contraste se puede usar la siguiente funcion para mejorarla
  
  def limpiarFondo(img):
  (F,C) = img.shape
  new  = np.zeros((F,C),np.uint8)
  for i in range(F):
    xmin = np.min(img[i,:])
    new[i,:] = img[i,:] - xmin 
  plt.imshow(new,cmap='gray')     #muestra imagen de salida
  return new      
