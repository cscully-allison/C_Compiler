int PrintInt(int);
char PrintChar(char);

int main(){
  int test, i, j;
  int arr[2][2];
  const int c;
  test = 1;
  i = 3, j = 4;
  c = 1;

  arr[2][1] = 43;
  i = arr[2][1];
  PrintInt(i);
  //CharFunction(d);

  while(test <= 10){
    PrintInt(test);
    PrintChar('-');
    test++;
    i++, j++;
    PrintInt(i);
  }

  do{
    test++;
  }while(test < 20);

  return 0;
}
