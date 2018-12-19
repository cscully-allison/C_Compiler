int PrintInt(int);
int main()
{
	int a;
	int b;
	int c;
	a = 1;
	b = 2;
	c = 3;

	if (a<c)
	{
		if (b > c)
		{
		a = 5;
		}
		else
		{
			a = 0;
		}
	}
	else
	{
		a = 3;
	}

	PrintInt(a);
}