int PrintInt(int);

int main(){
  int i, j, k;
  int a[2][2];
  int b[2][2];
  int c[2][2];
  int aval, bval;
  int newval;

  aval = 3;
  bval = 2;

  for(i=0; i < 2; i++){
    for(j=0; j < 2; j++){
      a[i][j] = aval;
      b[i][j] = bval;
      c[i][j] = 0;
    }
  }

  for(i=0; i < 2; i++){
    for(j=0; j < 2; j++){
      for(k=0; k < 2; k++){

           newval = a[i][j] * b[j][k];
          c[i][j] = c[i][j] + newval;
      }
    }
  }
  return 0;
}
