int fact(int);
int PrintInt(int);
int PrintChar(char);


int main(){
  int number, res;

  number = 5;

  res = fact(10);
  PrintInt(res);

  PrintChar(' ');
  PrintChar('-');
  PrintChar(' ');

  res = fact(number);
  PrintInt(res);

}


int fact(int n){
  int temp, run;
  if(n <= 1){
    return 1;
  }
  else{
    temp = n - 1;
    run = fact(temp);
    return run * n;
  }

}
