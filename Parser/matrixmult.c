
int main(){
  int i, j, k;
  float a[10][10];
  float b[10][10];
  float c[10][10];

<<<<<<< HEAD
  if( i < j){
    c[j][i][k];
  }
  else {
    i = 1;
  }
=======
>>>>>>> master

  for(i=0; i < 10; i++){
    for(j=0; j < 10; j++){
      for(k=0; k < 10; k++){
          a[i][k] = b[i][j] * c[j][k];
      }
    }
  }

  return 0;
}
