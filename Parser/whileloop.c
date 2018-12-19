int PrintInt(int);
char PrintChar(char);

int main(){
  int test, i, j;
  int arr[2][2];
  const int c;
  test = 1;
  i = 3, j = 4;
  c = 1;

  //arr[1][1] = 1;


  //CharFunction(d);

  while(test <= 10){
    PrintInt(test);
    PrintChar('-');
    test++;
    i++, j++;
    PrintInt(i);
    PrintChar('-');
    PrintInt(j);
    PrintChar('-');
  }

  do{
    PrintInt(test);
    PrintChar('-');
    test++;
  }while(test < 20);

  return 0;
}
