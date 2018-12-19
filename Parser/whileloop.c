int PrintInt(int);
char PrintChar(char);

int main(){
  int test;
  test = 1;

  while(test <= 10){
    PrintInt(test);
    PrintChar('-');
    test++;
  }

  do{
    PrintInt(test);
    PrintChar('-');
    test--;
  }while(test > 0);

  return 0;
}
