
int fact(int);


int main(){
    int num;
    num = 4;

    fact(num);
}


int fact(int n){
  int t, r;
  t = n - 1;

  if(n < 1){
    return 1;
  }

  r = fact(t);
  return n * r;

}
