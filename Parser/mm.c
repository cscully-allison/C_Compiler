int PrintInt(int);
char PrintChar(char);

int main(){
  int i, j, k;
  int a[2][2];
  int b[2][2];
  int c[2][2];
  int aval, bval;
  int out;

  aval = 3;
  bval = 2;

  for(i=0; i < 2; i++){
    for(j=0; j < 2; j++){
      a[i][j] = 3;

      b[i][j] = 2;

      c[i][j] = 0;
    }
  }

  for(i=0; i < 2; i++){
    for(j=0; j < 2; j++){
      for(k=0; k < 2; k++){
          c[i][k] += a[i][j] * b[j][k];
      }
    }
  }

  for(i=0; i < 2; i++){
    for(j=0; j < 2; j++){
      out = c[i][j];
      PrintInt(out);
      PrintChar('-');
    }
  }


  return 0;
}
