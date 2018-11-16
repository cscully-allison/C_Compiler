char f1(int, float);
int f2(const int[10][50][20], char, int[30]);


const int main(const int g){
    int arr[10][50][20];
    int arrb[30];

    f2(arr, 7, arrb);
    return 0;
}

//arrays of the form [][int const][int const] < with the empty first cell
// are not yet supported
int f2(const int a[10][50][20], char d, int f[30]){
  int i;
  i = 3;
  f1(i, 1.5);

  return 0;
}

char f1(int i1, float i2){
  int i3;
  i3 = i2;

  return 0;
}
