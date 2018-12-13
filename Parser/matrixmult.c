
int main(){
  int i, j, k;
  float a[4][4];
  float b[4][4];
  float c[4][4];
  int aval, bval;

  aval = 1;
  bval = 2;

  for(i=0; i < 10; i++){
    for(j=0; j < 10; j++){
      a[i][j] = aval;
      b[i][j] = bval;
      c[i][j] = 0.0;

      aval++;
      bval++;
    }
  }

  for(i=0; i < 10; i++){
    for(j=0; j < 10; j++){
      for(k=0; k < 10; k++){
          a[i][k] = b[i][j] * c[j][k];
      }
    }
  }

  return 0;
}
