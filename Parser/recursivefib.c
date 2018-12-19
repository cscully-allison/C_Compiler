int f(int);
int PrintInt(int);

int main()
{
  int n, i, c;

  i = 0;
  n = 6;

  c = f(6);

  PrintInt(c);

  return 0;
}

int f(int n)
{
  int res, fiba, fibb, n1, n2;

  if (n < 1){
    return n;
  }
  else{
    n1 = n - 1;
    n2 = n - 2;
    fiba = f(n1);
    fibb = f(n2);
    res = fiba + fibb;
    return res;
  }

  return 0;
}
