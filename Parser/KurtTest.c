int PrintInt(int);
int PrintChar(char);

int main(int arg1)
{
	int arr[2][2][2][2][2][2][2][2][2];
	int a;
	int b;
	int c;
	int d;
	a = 1;
	b = 0;
	c = 1;

	arr[a][b][c][a][b][c][a][b][c] = 8;
	d = arr[a][b][c][a][b][c][a][b][c];
	PrintInt(d);

}
