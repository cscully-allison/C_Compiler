int PrintInt(int);
int main()
{
	int a;
	int i;
	i = 0;
	a = 1;

	do{
		i = i + a;
	} while (i < 0);

	PrintInt(i);
}